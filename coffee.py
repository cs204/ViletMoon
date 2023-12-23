def coffee_machine():
    amount_due = 50
    total_amount = 0

    while total_amount < amount_due:
        print(f"Нужная сумма: {amount_due - total_amount}")
        coin = int(input("Вставьте монету: "))
        total_amount += coin


    change_owed = total_amount - amount_due
    print(f"Ваша сдача: {change_owed}")


coffee_machine()
