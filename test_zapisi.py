all_date = []
def in_file_data(data_user):
    data_users = open("data.csv", "a+t")
    for i in range(len(data_user)):
        data_users.writelines(data_user[i])
        if i < (len(data_user) - 1):
            data_users.write(', ')
    data_users.write('\n')
    data_users.close()
name = input('введите имя :')
all_date.append(name)
female = input('Введите фамилию :')
all_date.append(female)
in_file_data(all_date)
