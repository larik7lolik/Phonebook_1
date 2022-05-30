import record_tel
import search_tel
import user_interface
import logger

def run():
    temp = user_interface.choice()
    if temp == 1:
        print('Вами выбрана операция внесения в справочник нового контакта')

        entry = record_tel.record()   # Запись в справочник
        logger.log_to_file(entry)
        run()
    if temp == 2:
        print('\nВами выбрана операция поиска контакта в справочнике\n')
        entry = search_tel.search()   # Поиск в справочнике
        logger.reading_file(entry)
        run()

    if temp == 3:
        print('\nВами выбрана операция вывода на печать всех контактов справочника\n\n\=== КОНТАКТЫ ТЕЛЕФОННОГО СПРАВОЧНИКА ===\n') 
        logger.read_all_file()
        run()

    if temp == 4:
        print('\nРабота телефонного справочника окончена. Всего доброго.\n')
        exit


        
