# coding:utf-8
num = 1
string = '1'
num2 = int(string)
print(num+num2)
word = "a loooooong word"
num = 12
string = 'bang'
total = string * (len(word)-num)
print(len(word))
print(total)
phone_number = "18566666666"
hidden_number = phone_number.replace(phone_number[3:7],'*'*4)
print(hidden_number)
searchCondition = '137'
num_a = '13766666666'
num_b = '18113723333'
searchResult = searchCondition + 'is at ' + str(num_a.find(searchCondition))
searchResult += ' to ' + str(num_a.find(searchCondition) + len(searchCondition)) + ' of num_a '
searchResult += '\n' + searchCondition + 'is at ' + str(num_b.find(searchCondition))
searchResult += ' to ' + str(num_b.find(searchCondition) + len(searchCondition)) + ' of num_b '
print(searchResult)

