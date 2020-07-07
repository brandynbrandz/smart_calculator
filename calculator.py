import math
import time

while True:
    try:
        option = int(input('what type of calculation do you want to do: 1. Basic Arithmetic'
                           + '\n' + ' ' * len('what type of calculation do you want to do: ') +
                           '2.Trigonometric'
                           + '\n' + ' ' * len('what type of calculation do you want to do: ') +
                           '3. Exit -->'))
    except:
        print('\nERROR: Please enter a serial number\n')
        continue
    else:
        break

if option == 1:
    while True:
        try:
            option = int(input('select one: 1. Sum' + '\n' + ' ' * len('select one: ') +
                               '2. Difference' + '\n' + ' ' * len('select one: ') +
                               '3. Multiplication' + '\n' + ' ' * len('select one: ') +
                               '4. Division' + '\n' + ' ' * len('select one: ') +
                               '5. Exit -->'))
        except:
            print('\nERROR: Please enter a serial number\n')
            continue
        else:
            break

    if option == 1:
            i = 1
            added = []
            print('\nKeep entering number and enter any non numerical value to get the result\n')
            while True:
                try:
                    a = int(input("Enter the number " + str(i) + ': '))
                    added.append(a)
                    i += 1
                except:
                    added = sum(added)
                    print(f"\nResult is: {added}\n")
                    break
                else:
                    continue

    elif option == 2:
            while True:
                try:
                    a = int(input("Enter the number 2: "))
                    b = int(input("Enter the number 1: "))
                except:
                    print(f"\nResult is: {added}\n")
                    continue
                else:
                    print("\nThe difference is{}".format(a - b))
                    break

    elif option == 3:
            print('\nKeep entering number and enter any non numerical value to get the result\n')
            while True:
                try:
                    mul = int(input("Enter the number " + str(i) + ': '))
                    mul = mul * mul
                    i += 1
                except:
                    print("Result is: {0:.4f}" / format(a))
                    print(f"Rounded value is {round(mul, 2)}")
                    break
                else:
                    continue

    elif option == 4:
            while True:
                try:
                    a = int(input("Enter the number 2: "))
                    b = int(input("Enter the number 1: "))
                except:
                    print("\nThere is some error please try again")
                    continue
                else:
                    try:
                        print(f"The division is {a / b}")
                    except:
                        print("The division is infinite")
                    finally:
                        break
    else:
            exit(0)

elif option == 2:
    while True:
        option = input("Enter trigonometric function").lower()
        if option in ["cos", "sin", "tan", "cosec", "cot", "sec"]:
            pass
        else:
            print(
                f"\nERROR: No such trigonometric function found.\nExample:\n{' ' * len('Example')}Enter trigonometric function function: cos, (or sin,cosec,cot,tan,sec)")
            continue

        while True:
            try:
                value = int(input("Enter the angle: "))
            except:
                print("ERROR: There is some error, please try again.")
                continue
            else:
                break
        break

    if option in ['cos', 'sec']:
        cos = math.cos(value)
        if option == 'cos':
            print(f"cos({value}) ={cos}")
        else:
            sec = 1 / cos
            print(f"sec({value}) = {sec}")

    if option in ['tan', 'cot']:
        tan = math.tan(value)
        if option == 'tan':
            print("tan({}) = {}".format(value, tan))
        else:
            sec = 1 / tan
            print("cot({angle}) = {result}".format(result=cot, angle=value))

    if option in ['sin', 'cosec']:
        sin = math.sin(value)
        if option == 'sin':
            print(f"sin({value}) ={sin}")
        else:
            sec = 1 / cos
            print(f"cosec({value}) = {cosec}")


elif option == 3:
    exit(0)

else:
    print('ERROR: Entered operation not found')

if option != 3:
    time.sleep(30)
