def filter_short_strings(arr):
    result = []
    for string in arr:
        if len(string) <= 3:
            result.append(string)
    return result

def main():
    # Ввод строки пользователя
    input_str = input("Введите строки через пробел: ")

    # Если строка пустая, выведем сообщение об ошибке
    if not input_str:
        print("Ошибка: ничего не введено.")
        return

    # Разбиваем введенные строки на массив
    input_arr = input_str.split()
    # Вызываем функцию для фильтрации строк
    result = filter_short_strings(input_arr)

    # Проверяем, были ли введены строки
    if not result:
        print("[]")
    else:
        # Выводим результат
        print("Отфильтрованный массив строк:", result)

if __name__ == "__main__":
    main()