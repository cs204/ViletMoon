меню = {
"кофе": 20.00,
"чай": 10.00,
"булочка": 5.00,
"салат": 30.40,
"пирожное": 45.50
}
total_cost = 0.0
try:
    while True:
        user_input = input("Блюдо: ")
        if user_input in меню:
            total_cost += меню[user_input]
except EOFError:
    print("\nСумма: {:.2f}".format(total_cost))
