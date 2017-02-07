import math


def search(search_condition, search_target):
    search_result = search_condition + ' is at ' + str(search_target.find(search_condition))
    search_result += ' to ' + str(search_target.find(search_condition)+len(search_condition)) + ' in '\
                     + str(search_target)
    search_result += '\n'
    return search_result
key = '189'
target1 = '18923333333'
target2 = '13781892333'
result = search(key, target1)
result += search(key, target2)
print(result)


def temp_convert(temp, temp_type):
    if temp_type == 'C':
        con_temp = temp * 9/5 + 32
        return str(con_temp) + ' °F'
    elif temp_type == 'F':
        con_temp = (temp - 32) * 5 / 9
        return str(con_temp) + '°C'
    else:
        return 'Invalid Type'


temp_1 = 35
temp_2 = 89.6
print(temp_convert(temp_1, 'C'))
print(temp_convert(temp_2, 'F'))


def weight_convert(weight, weight_type):
    if weight_type == 'KG':
        con_weight = weight*1000
        return str(con_weight) + 'G'
    elif weight_type == 'G':
        con_weight = weight/1000
        return str(con_weight) + 'KG'
    else:
        return 'Invalid Type'

weight1 = 1500
weight2 = 2.7
print(weight_convert(weight1, 'G'))
print(weight_convert(weight2, 'KG'))


def triangle_calc(length0, length1):
    length = math.sqrt(length0*length0 + length1*length1)
    prefix = 'The right triangle third side\'s length is '
    return prefix + str(length)

length_0 = 3
length_1 = 4
print(triangle_calc(length_0, length_1))


def trapezoid_area_calc(base_up, base_down, height):
    area = (base_up+base_down) * height / 2
    return area

up_base = 3
down_base = 4
height0 = 5
trapezoid_area = trapezoid_area_calc(up_base, down_base, height0)
print(str(trapezoid_area))
print(str(trapezoid_area_calc(1, 2, 3)))
print(str(trapezoid_area_calc(base_up=1, height=3, base_down=2)))
print(str(trapezoid_area_calc(1, height=3, base_down=2)))


