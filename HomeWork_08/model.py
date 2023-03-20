phone_book =[]

def open_file():
    with open('phone.txt', 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
        for row in data: # Парсинг
            contact = row.strip().split(';')
            contact = {'name':contact[0],
                       'phone': contact[1] , 
                       'comment':contact[2]}
            phone_book.append(contact)
        print(data)

def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open('path', 'w', encoding='utf-8') as file:
            file.write(data)


def get_phone_book():
    return phone_book

def add_contact(contact:dict):
    phone_book.append(contact)

def remove_contact(index: int):
    phone_book.pop(index-1)

def change_contact(contact:dict, index:int):
    phone_book.pop(index - 1)
    phone_book.insert(index - 1, contact)

def find_contact(search:str) -> list[dict]:
    result = []
    for contact in phone_book:
        for field in contact.values():
            if search.lower() in field.lower():
                result.append(contact)
    return result

    