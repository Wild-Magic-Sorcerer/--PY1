salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

increment = 1
for i in range(months):
    need_money += (spend * increment) - salary
    increment *= (increase + 1)

print(round(need_money))
