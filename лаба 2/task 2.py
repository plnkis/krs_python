# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
count = 1
money_capital = 0
while count <= 10:
    excess = spend - salary
    money_capital += excess
    spend *= (1 + increase)
    count += 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", f"{money_capital:.2f}")




