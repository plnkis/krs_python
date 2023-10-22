
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
excess = spend - salary
while money_capital > excess:
    spend *= (1 + increase)
    excess = spend - salary
    money_capital -= excess
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)