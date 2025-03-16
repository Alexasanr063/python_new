import pytest
from decimal import Decimal
import datetime as dt
from inventory import add, add_by_note, find, get_amount, get_expired, goods

def test_add_new_item():
    items = {}
    add(items, 'Яблоки', Decimal('5'), '2025-12-31')
    assert items['Яблоки'] == [{'amount': Decimal('5'), 'expiration_date': dt.date(2025, 12, 31)}]

def test_add_existing_item():
    items = {'Яблоки': [{'amount': Decimal('5'), 'expiration_date': dt.date(2025, 12, 31)}]}
    add(items, 'Яблоки', Decimal('3'), '2025-12-31')
    assert items['Яблоки'] == [{'amount': Decimal('5'), 'expiration_date': dt.date(2025, 12, 31)},
                                {'amount': Decimal('3'), 'expiration_date': dt.date(2025, 12, 31)}]

def test_add_by_note_with_expiration():
    items = {}
    add_by_note(items, 'Яблоки 5 2025-12-31')
    assert items['Яблоки'] == [{'amount': Decimal('5'), 'expiration_date': dt.date(2025, 12, 31)}]

def test_add_by_note_without_expiration():
    items = {}
    add_by_note(items, 'Яблоки 5')
    assert items['Яблоки'] == [{'amount': Decimal('5'), 'expiration_date': None}]

def test_find_existing_item():
    result = find(goods, 'яйца')
    assert 'Яйца Фабрики №1' in result
    assert 'Фабрика №2: яйца' in result

def test_find_case_insensitive():
    result = find(goods, 'яЙца')
    assert 'Яйца Фабрики №1' in result
    assert 'Фабрика №2: яйца' in result

def test_find_non_existing_item():
    result = find(goods, 'хлеб')
    assert result == []

def test_get_amount_existing_item():
    amount = get_amount(goods, 'яйца')
    assert amount == Decimal('5')

def test_get_amount_non_existing_item():
    amount = get_amount(goods, 'хлеб')
    assert amount == Decimal('0')

def test_get_expired_no_expiration():
    expired_items = get_expired(goods)
    assert expired_items == []

def test_get_expired_with_advance_days():
    expired_items = get_expired(goods, in_advance_days=1)
    assert expired_items == []

def test_get_expired_with_no_items():
    empty_goods = {}
    expired_items = get_expired(empty_goods)
    assert expired_items == []

def test_get_expired_with_future_expiration():
    items = {
        'Яблоки': [{'amount': Decimal('5'), 'expiration_date': dt.date(2025, 12, 31)}]
    }
    expired_items = get_expired(items, in_advance_days=30)
    assert expired_items == []

def test_get_expired_with_multiple_expirations():
    items = {
        'Молоко': [{'amount': Decimal('2'), 'expiration_date': dt.date(2023, 10, 1)}],
        'Яйца': [{'amount': Decimal('3'), 'expiration_date': dt.date(2023, 10, 5)}],
    }
    expired_items = get_expired(items, in_advance_days=0)
    assert expired_items == [('Молоко', Decimal('2')), ('Яйца', Decimal('3'))]

def test_get_expired_advanced_days():
    items = {
        'Молоко': [{'amount': Decimal('2'), 'expiration_date': dt.date(2023, 10, 1)}],
        'Яйца': [{'amount': Decimal('3'), 'expiration_date': dt.date(2023, 10, 5)}],
    }
    expired_items = get_expired(items, in_advance_days=5)
    assert expired_items == [('Яйца', Decimal('3'))]


