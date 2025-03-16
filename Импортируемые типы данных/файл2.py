import sys
import io

# Устанавливаем кодировку вывода
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# Пропишите нужные импорты.
# Импортируйте всё необходимое:
from decimal import Decimal, getcontext

# Установите требуемую точность вычислений:
getcontext().prec = 3


# Допишите код функции.
def get_monthly_payment(total_sum, months_count, percents):
    # Подсчитайте основную сумму ежемесячного платежа, без учёта процентов:
    monthly_raw =  Decimal(total_sum) / Decimal(months_count)

    # Подсчитайте ежемесячный платёж по процентам банка,
    # исходя из ежемесячной части основной суммы и процентной ставки:
    monthly_addition = (monthly_raw * Decimal(percents/100))

    # Подсчитайте общую сумму ежемесячного платежа:
    total_per_month = monthly_raw + monthly_addition
    # Верните общую сумму ежемесячного платежа:
    return total_per_month


payment_value = get_monthly_payment(54, 24, 9)
print('Ежемесячный платёж:', payment_value, 'ВтК.')