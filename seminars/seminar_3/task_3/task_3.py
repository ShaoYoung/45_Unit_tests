# Задание №3
# Создайте тесты, обеспечивающие полное покрытие кода метода calculatingDiscount, который принимает сумму
# покупки и размер скидки, затем вычисляет и возвращает сумму с учетом скидки. Метод должен обрабатывать
# исключения, связанные с некорректным размером скидки или отрицательной суммой покупки.

def calculating_discount(purchase_amount: float, discount_amount: int) -> float:
    if purchase_amount < 0:
        raise ValueError('Сумма не может быть меньше нуля')
    if not 0 <= discount_amount <= 100:
        raise ValueError('Размер скидки должен быть от 0 до 100')
    return purchase_amount - purchase_amount * discount_amount / 100

