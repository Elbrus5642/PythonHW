import text_fields

def main_menu() -> None:
    print(text_fields.main_menu)
     

def choice_menu() -> int:
    menu_lenght = len(text_fields.main_menu.split('\n')) - 1
    while True:
        number =  input('Выберите пункт меню: ')
        if number.isdigit()  and 0 < int(number) <= menu_lenght:
            return int(number)
        print(f'Выберите число от 1 до {menu_lenght}')

def show_contacts(phone_book: list[dict], index: int):
    if not phone_book: # если тк не пустая или не открыта
        print(text_fields.error_message)
        return False
    else:
        for index, contact  in enumerate(phone_book, 1):  
            print(f"{index}.{contact.get('name'):<20}"
                f"{contact.get('phone'):<20}"
                f"{contact.get('comment'):<20}")
        return True

def add_contact() -> dict:
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Запишите комментарий к номеру: ')
    return {'name': name, 'phone': phone,'comment':comment}

def input_index(message: str):
    return int(input(message))

def input_search(message):
    return  input(message)

def input_number_for_remove(message):
    return int(input(message))

def change_contact(phone_book: list[dict], index):
    print('Введите новые данные или оставьте пустое поле, если изменений нет')
    contact  = add_contact()
    return {'name': contact.get('name') if contact.get('name') else  phone_book[index -1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else  phone_book[index -1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else  phone_book[index -1].get('comment')}


        
def show_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))
