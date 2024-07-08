from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)


# # TODO 1: выполните пункты 1-3 ДЗ
# задание 1: Помещаем Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно
for person in contacts_list:
    name_lastname = person[0].split(" ")
    name_firstname = person[1].split(" ")
    name_surname = person[2].split(" ")
    name = (" ".join(name_lastname + name_firstname + name_surname)).split()
    for i in range(len(name)):
        person[i] = name[i]


# задание 2: Приводим все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999
phone_pattern = re.compile(r"(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?")
phone_subst = r"+7(\2)\3-\4-\5\6\7\8"
for person in contacts_list:
    person[-2] = phone_pattern.sub(phone_subst, person[-2])


# задание 3: Объединяем все дублирующиеся записи о человеке в одну
contacts_dict = {}
for person in contacts_list:
    dict_key = tuple(person[0:2])
    if dict_key not in contacts_dict:
        contacts_dict[dict_key] = person
    else:
        contact = contacts_dict[dict_key]
        for i in range(2, len(person)):
            if not contact[i]:
                contact[i] = person[i]
contacts_list = list(contacts_dict.values())
pprint(contacts_list)


# # # TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
