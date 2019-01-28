Base_pay = 32
Base_pay25 = 40
Base_pay50 = 48
Hour = Base_pay

while True:
    print(': ')
    user_input = input(': ')
    if user_input == 'quit':
        break
    elif user_input == "start":
        num1 = float(input('חישוב שכר בסיסי: '))
        result = str(num1 * Base_pay)
        num2 = float(input('חישוב שכר 25% תוספת:'))
        result2 = str(num2 * Base_pay25)
        num3 = float(input('חישוב שכר 50% תוספת'))
        result3 = str(num3 * Base_pay50)
        print(str(result, result2, result3))
    else:
        print("Error Ocourd!")
        break
def Tax():
    print(result.format(n))
    