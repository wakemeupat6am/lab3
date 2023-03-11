def is_divisible_by_3(number: int):
    return number % 3 == 0


def divide_100_by(number):
    try:
        return 100 / float(number)
    except ValueError:
        print("Нужно передать число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except Exception as e:
        print("Ошибка: ", e)



def is_magic_date(date: str):
    try:
        date = date.split(".")
        day = int(date[0])
        month = int(date[1])
        year = int(date[2][2:])
        return day * month == year
    except Exception:
        print("Функия принимает строку с датой в формате dd.mm.yyyy")


def is_lucky_ticket(ticket: str):
    if len(ticket) % 2 != 0:
        raise ValueError("Нужно ввести четное кол-во чисел")

    middle = int(len(ticket) / 2)

    right = ticket[middle:]
    left = ticket[:middle]

    left_int_array = [int(x) for x in list(left)]
    right_int_array = [int(x) for x in list(right)]

    return sum(left_int_array) == sum(right_int_array)


if __name__ == "__main__":
    print("Деление на 3")
    print(is_divisible_by_3(30))
    print(is_divisible_by_3(2))

    print("\nДеление числа на 100")
    print(divide_100_by(200))
    print(divide_100_by(0))
    print(divide_100_by("a"))

    print("\nПроверка магической даты")
    print(is_magic_date("22.01.2022"))
    print(is_magic_date("21.01.2022"))

    print("\nСчастливый билет")
    result1 = is_lucky_ticket("385916")
    print("385916: {}".format(result1))
    result2 = is_lucky_ticket("231002")
    print("231002: {}".format(result2))