import json

SPRAVOCHNIK_FILE = "spravochnik.json"


def load_spravochnik():

    # Загрузка данных справочника из файла.

    try:
        with open(SPRAVOCHNIK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_spravochnik(spravochnik):

    # Сохранение данных справочника в файл.

    with open(SPRAVOCHNIK_FILE, "w") as file:
        json.dump(spravochnik, file)


def display_records(records):

    # Вывод записей на экран постранично.

    page_size = 5
    num_pages = len(records) // page_size + (1 if len(records) % page_size != 0 else 0)
    for page in range(num_pages):
        print("=== Страница", page + 1, "из", num_pages, "===")
        for i in range(page * page_size, min((page + 1) * page_size, len(records))):
            print(records[i])
        input("Нажмите Enter для продолжения...")


def add_record(spravochnik, record):

    # Добавление новой записи в справочник.

    spravochnik.append(record)
    save_spravochnik(spravochnik)
    print("Запись добавлена успешно.")


def search_records(spravochnik, **kwargs):

    # Поиск записей по заданным характеристикам.

    results = []
    for record in spravochnik:
        match = True
        for key, value in kwargs.items():
            if key not in record or record[key] != value:
                match = False
                break
        if match:
            results.append(record)
    return results


def edit_record(spravochnik, phone_number, new_record):

    # Редактирование записи в справочнике по номеру телефона.

    for record in spravochnik:
        if record.get("телефон рабочий") == phone_number or record.get("телефон личный") == phone_number:
            record.update(new_record)
            save_spravochnik(spravochnik)
            print("Запись отредактирована успешно.")
            return
    print("Запись с указанным номером телефона не найдена.")


def main():
    spravochnik = load_spravochnik()

    while True:
        print("\nТелефонный справочник")
        print("1. Вывести записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_records(spravochnik)
        elif choice == "2":
            record = {
                "порядковый номер": len(spravochnik) + 1,
                "фамилия": input("Введите фамилию: "),
                "имя": input("Введите имя: "),
                "отчество": input("Введите отчество: "),
                "название организации": input("Введите название организации: "),
                "телефон рабочий": input("Введите рабочий телефон: "),
                "телефон личный": input("Введите личный телефон: ")
            }
            add_record(spravochnik, record)
        elif choice == "3":
            phone_number = input("Введите номер телефона для редактирования: ")
            new_record = {
                "фамилия": input("Введите новую фамилию: "),
                "имя": input("Введите новое имя: "),
                "отчество": input("Введите новое отчество: "),
                "название организации": input("Введите новое название организации: "),
                "телефон рабочий": input("Введите новый рабочий телефон: "),
                "телефон личный": input("Введите новый личный телефон: ")
            }
            edit_record(spravochnik, phone_number, new_record)
        elif choice == "4":
            query = input("Введите характеристики для поиска (например, фамилия=Иванов): ")
            search_params = dict(item.split("=") for item in query.split(","))
            results = search_records(spravochnik, **search_params)
            print("Результаты поиска:")
            for i, result in enumerate(results, 1):
                print(i, result)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
