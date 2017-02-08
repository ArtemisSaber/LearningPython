# import os
# path = os.path.dirname(__file__)
# for i in range(1, 11):
#     full_path = os.path.join(path, str(i) + '.txt')
#     file = open(full_path, 'w')
#     file.write('This is number '+str(i))


def compound_interest(amount, rate, time):
    if time >= 1:
        cur_time = 0
        full_amount = amount
        while time >= 1:
            full_amount *= 1 + rate
            time -= 1
            cur_time += 1
            print('year ' + str(cur_time) + ': $' + str(full_amount))
    return None

invest_amount = input('Amount: ')
invest_rate = input('Annual Rate: ')
invest_time = input('Investment During: ')
compound_interest(float(invest_amount), float(invest_rate), float(invest_time))

