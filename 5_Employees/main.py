import json

def load_data(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не найден. Создан новый список.")
        return []

def save_data(employees, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(employees, f, ensure_ascii=False, indent=4)
    print(f"Данные сохранены в {filename}")

def add_employee(employees):
    surname = input("Фамилия: ")
    name = input("Имя: ")
    age = int(input("Возраст: "))
    position = input("Должность: ")
    employees.append({
        "surname": surname,
        "name": name,
        "age": age,
        "position": position
    })
    print("Сотрудник добавлен.")

def find_employees_by_surname(employees, surname):
    return [e for e in employees if e["surname"].lower() == surname.lower()]

def edit_employee(employees):
    surname = input("Фамилия для редактирования: ")
    found = find_employees_by_surname(employees, surname)
    if not found:
        print("Сотрудник не найден.")
        return
    if len(found) > 1:
        for i, e in enumerate(found):
            print(f"{i+1}. {e}")
        idx = int(input("Выберите номер: ")) - 1
        if idx < 0 or idx >= len(found):
            print("Неверный выбор.")
            return
        emp = found[idx]
    else:
        emp = found[0]

    new_surname = input(f"Фамилия [{emp['surname']}]: ") or emp['surname']
    new_name = input(f"Имя [{emp['name']}]: ") or emp['name']
    new_age = input(f"Возраст [{emp['age']}]: ") or emp['age']
    new_position = input(f"Должность [{emp['position']}]: ") or emp['position']

    emp.update({
        "surname": new_surname,
        "name": new_name,
        "age": int(new_age),
        "position": new_position
    })
    print("Сотрудник обновлён.")

def delete_employee(employees):
    surname = input("Фамилия для удаления: ")
    found = find_employees_by_surname(employees, surname)
    if not found:
        print("Сотрудник не найден.")
        return
    if len(found) > 1:
        for i, e in enumerate(found):
            print(f"{i+1}. {e}")
        idx = int(input("Выберите номер: ")) - 1
        if idx < 0 or idx >= len(found):
            print("Неверный выбор.")
            return
        emp = found[idx]
    else:
        emp = found[0]
    employees.remove(emp)
    print("Сотрудник удалён.")

def search_by_surname(employees):
    surname = input("Фамилия для поиска: ")
    found = find_employees_by_surname(employees, surname)
    if not found:
        print("Сотрудники не найдены.")
    else:
        for e in found:
            print_employee(e)
    return found

def list_by_age(employees):
    age = int(input("Возраст: "))
    result = [e for e in employees if e["age"] == age]
    if not result:
        print("Сотрудники не найдены.")
    else:
        for e in result:
            print_employee(e)
    return result

def list_by_surname_letter(employees):
    letter = input("Первая буква фамилии: ").lower()
    result = [e for e in employees if e["surname"].lower().startswith(letter)]
    if not result:
        print("Сотрудники не найдены.")
    else:
        for e in result:
            print_employee(e)
    return result

def print_employee(e):
    print(f"{e['surname']} {e['name']}, {e['age']} лет, {e['position']}")

def save_found(found):
    filename = input("Имя файла для сохранения найденных данных: ")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(found, f, ensure_ascii=False, indent=4)
    print("Найденные данные сохранены.")

def main():
    filename = input("Введите имя JSON-файла для загрузки данных (например, employees.json): ")
    employees = load_data(filename)

    while True:
        print("\n--- Меню ---")
        print("1. Добавить сотрудника")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск по фамилии")
        print("5. Фильтр по возрасту")
        print("6. Фильтр по первой букве фамилии")
        print("7. Сохранить найденные данные в файл")
        print("8. Сохранить все данные")
        print("9. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            edit_employee(employees)
        elif choice == "3":
            delete_employee(employees)
        elif choice == "4":
            found = search_by_surname(employees)
        elif choice == "5":
            found = list_by_age(employees)
        elif choice == "6":
            found = list_by_surname_letter(employees)
        elif choice == "7":
            if 'found' in locals() and found:
                save_found(found)
            else:
                print("Сначала выполните поиск или фильтрацию.")
        elif choice == "8":
            save_data(employees, filename)
        elif choice == "9":
            save_data(employees, filename)
            print("Выход. Данные сохранены.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
