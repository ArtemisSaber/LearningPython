import os
path = os.path.dirname(__file__)
validate_file_path = os.path.join(path, 'validate.txt')


def validate_input(input_data, validate_file_pos=validate_file_path, input_length=11):
    validate_file = open(validate_file_pos)
    validate_list = validate_file.readlines()
    is_valid = False
    if len(input_data) >= input_length:
        for string in validate_list:
            string = string.split('=')
            operator = string[0]
            number_list = string[1].replace('[', '').replace(']', '').split(',')
            for number in number_list:
                number = number.strip('\n')
                index = input_data.find(number, 0, 3)
                if index != -1:
                    print(operator)
                    print('Sending SMS to your cell phone : ' + input_data)
                    is_valid = True
        if not is_valid:
            print('No such operator')
    else:
        print('invalid input')
    return is_valid

is_not_valid = True
while is_not_valid:
    input_data_0 = input('Enter your number: ')
    is_not_valid = not validate_input(input_data_0)
