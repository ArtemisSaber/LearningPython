import random


def generate_points():
    i = 3
    points = []
    while i > 0:
        point = random.randrange(1, 7)
        points.append(point)
        i -= 1
    return points


def calc_total(points):
    i = len(points)
    total = 0
    while i > 0:
        point = points[i-1]
        total += point
        i -= 1
    return total


def get_input():
    print("<<<<GAME START!>>>>")
    input_data = input("Big or small: ")
    if input_data == "Big":
        is_big = True
    elif input_data == "Small":
        is_big = False
    else:
        print("Invalid Data!")
        return None
    print("<<<<Roll the dice!>>>>")
    pts = generate_points()
    totals = calc_total(pts)
    print("The points are "+str(pts))
    if 11 <= totals <= 18:
        is_Big = True
    else:
        is_Big = False
    if is_big == is_Big:
        print("You won")
        return True
    else:
        print("You lose")
        return False


def gamble_start(rate=1, start_money=10000):
    money = start_money
    while money > 0:
        print("<<<<You have $" + str(money) + " Now>>>>")
        debit_money = int(input("How much do u want to bet : "))
        if 0 < debit_money <= money:
            is_won = get_input()
            if is_won:
                money += debit_money*rate
                print("<<<<You won $" + str(debit_money*rate) + " >>>>")
            elif is_won is None:
                get_input()
            else:
                money -= debit_money*rate
                print("<<<<You lost $" + str(debit_money*rate) + " >>>>")
        elif debit_money > money:
            print("<<<<You can't bet more than you have>>>>")
        else:
            print("<<<You can't bet less than zero")
    print("<<<<You lost all money!>>>>")
    return None

gamble_start()

