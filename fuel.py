def main():
    girdi = check_fraction()
    if 99 <= girdi <= 100:
        print("F")
    elif 0 <= girdi <= 10:
        print("E")
    elif girdi <= 100:
        print((f"{girdi}%"))

def check_fraction():

    while True:

        try:
            fraction = convert("Дробь: ")
            if fraction <= 100:
                return int(fraction)
        except (ValueError, ZeroDivisionError):
            pass

def convert(a):
    b = input(a).split('/')
    x = b[0]
    y = b[1]
    x = int(x)
    y = int(y)
    converted = float(x/y * 100)
    converted = round(converted, 0)
    return int(converted)
main()
