import  view
import model

def start():
    while True: # Для  работы  с повторениями  при запросах пунктов меню
        pb = model.get_phone_book()
        view.main_menu()
        choice = view.choice_menu()    
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт!')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранён!')
            case 3:
                view.show_contacts(pb,'Телефонный спарвочник пустой или закрыт')
            case 4:
                model.add_contact(view.add_contact())
                view.show_message("Контакт успешно сохранён в справочнике!")
            case 5:
                if view.show_contacts(pb,'Телефонный спарвочник пустой или закрыт'):
                    index =view.input_index('Введите номер изменяемого контакта: ')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Контакт {(model.get_phone_book())[index-1].get("name")} успешно сохранён!')
            case 6:
                search = view.input_search('Введите элемент поиска:')
                result = model.find_contact(search)
                view.show_contacts(result, 'Контакты с такими параметрами не найдены')
            case 7: 
                view.show_contacts(pb,'Телефонный спарвочник пустой или закрыт')
                number_for_remove = view.input_number_for_remove('Введите номер контакта, который необходимо удалить: ')
                model.remove_contact(number_for_remove)
                view.show_message("Контакт удалён из справочника")
            case 8:                
                return
    


