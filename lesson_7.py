from datetime import datetime as dt
from time import time

fio = None
number_phone = None


def add_model_phonebook(user_data):
    global fio
    global number_phone
    fio = user_data[0]
    number_phone = user_data[1]
    log_data_user(fio, number_phone)


def search_phone_in_phonebook(user_data_search):
    all_data_user = give_the_data_user(user_data_search)
    if all_data_user.find(user_data_search) == -1:
        return 'No person found with these parametrs.'
    else:
        all_data_user = all_data_user.split(f'\n')
        answer = -1
        answer_new = []
        for i in range(0, len(all_data_user)):
            answer = all_data_user[i].find(user_data_search)
            if answer != -1:
                answer_new.append(all_data_user[i])
        return answer_new


def delete_user(user):
    all_data_user = give_the_data_user(user)
    if all_data_user.find(user) == -1:
        return 'No person found with these parametrs.'
    else:
        all_data_user = all_data_user.split(f'\n')
        answer = -1
        answer_new = []
        for i in range(0, len(all_data_user)):
            answer = all_data_user[i].find(user)
            if answer != -1:
                answer_new.append(all_data_user[i])
        if len(answer_new) != 1:
            return 'To delete, enter more complete data or phone number!'
        else:
            log_delete_user(user)
            return 'Removal was successful!'


def get_view_model():
    fio = input('Enter FIO: ')
    while True:
        number_phone = input('Enter number phone: ')
        if number_phone.isdigit():
            break
    return fio, number_phone


def get_user_search():
    data_user = input('Enter FIO or numberphone: ')
    return data_user


def get_user_delete():
    delete_user = input('Enter who you want to delete: ')
    print('Are you sure you want to delete?')
    return delete_user


def Button_click():
    user_data = get_view_model()
    add_model_phonebook(user_data)


def Button_click_search():
    user_data_search = get_user_search()
    all_user_data = search_phone_in_phonebook(user_data_search)
    return all_user_data


def Button_click_delete():
    user_data_search = get_user_delete()
    answer = delete_user(user_data_search)
    return answer


def log_data_user(fio, phone_number):
    file_log_user_data = 'phonebook.txt'
    time = dt.now().strftime("%d/%m/%Y Time %H:%M")
    with open(file_log_user_data, 'a') as file:
        file.write(f'{time} \nFIO: {fio} - NumberPhone: {phone_number}\n')


def give_the_data_user(user_data_search):
    file_log_user_data = 'phonebook.txt'
    with open(file_log_user_data, 'r') as file:
        all_data_user = file.read()
        return all_data_user


def log_delete_user(user):
    file_log_user_data = 'phonebook.txt'
    with open(file_log_user_data, 'r') as file:
        all_data_user = file.read().split(f'\n')
        wh = len(all_data_user)
        for i in range(0, wh):
            ind = all_data_user[i].find(user)
            if ind != -1:
                tmp = i
                break
        all_data_user.pop(tmp)
        all_data_user.pop(tmp - 1)
        for i in range(0, len(all_data_user)):
            if len(all_data_user[i]) == 0:
                all_data_user.pop(i)
                break
        with open(file_log_user_data, 'w') as file_new:
            for i in range(0, len(all_data_user)):
                file_new.write(f'{all_data_user[i]}\n')


while True:
    result = int(input('\n\nВведите число для выбора действия\n 0 - выход, 1 - добавление контакта,'
                       ' 2 - поиск контакта, 3 - удаление контакта\n'))
    if result == 0:
        print('Программа завершена')
        break
    elif result == 1:
        Button_click()
        print('\nКонтакт добавлен\n')
    elif result == 2:
        all_user_data = Button_click_search()
        if all_user_data == 'No person found with these parametrs.':
            print(all_user_data)
        else:
            print('\nКонтакт найден\n')
            for i in range(0, len(all_user_data)):
                print(all_user_data[i])
    elif result == 3:
        answer = Button_click_delete()
        print(answer)
        print('\nКонтакт удалён\n')
    else:
        print('Некорректный ввод. Повторите ещё раз')
