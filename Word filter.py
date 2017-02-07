import os


def create_text(msg, name='my_file'):
    root_path = os.path.dirname(__file__)
    full_path = os.path.join(root_path, name+'.txt')
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done \n'+'Wrote file '+full_path)
    return None
# create_text(msg='This is message')


def text_filter(word, censor_file, changed_word='***'):
    censor_list = censor_file.readlines()
    print(censor_list)
    for censor_word in censor_list:
        censor_word = censor_word.strip('\n')
        word = word.replace(censor_word, changed_word)
    return word
# censor_path = os.path.dirname(__file__)
# censor_file_path = os.path.join(censor_path, 'censorship.txt')
# censor_files = open(censor_file_path)
# print(text_filter('This is horrible fuck u python', censor_files, 'Awesome'))


def text_create_censored(msg, name='censored_file.txt'):
    censorship_path = os.path.dirname(__file__)
    censorship_file = open(os.path.join(censorship_path, 'censorship.txt'))
    msg = text_filter(msg, censorship_file, '根据相关法律法规部分文字没有显示')
    create_text(msg, name)
    print('Done')
    return None
text_create_censored('fuck u python')
