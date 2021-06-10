def cantiga():
    """Testando newline e tabs"""
    print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


def info_sys():
    """Apresenta a versão de python do sistema e a info relacionada"""
    import sys
    print("Python version")
    print(sys.version)
    print("Version info.")
    print(sys.version_info)


def current_time():
    """Mostra a hora atual aqui e em tokyo, pode ser mudada pra mostrar em outros lugares"""
    import datetime
    import pytz
    now = datetime.datetime.now()
    now_tokyo = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    print("Current date and time: " + now.strftime("%Y-%m-%d %H:%M:%S"))
    print("Current date and time in Tokyo: " +
          now_tokyo.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_area(radius: float()):
    import math
    return math.pi * radius**2


def reverse_name():
    first_name = str(input("Insert First Name: "))
    last_name = str(input("Insert Last Name: "))
    return print(last_name + " " + first_name)


def number_sequence():
    numbers = input("Insert number list: ")
    list_order = numbers.split(",")
    tuple_order = tuple(list_order)
    return print("List: ", list_order, "\n Tuple: ", tuple_order)


def extension_separator():
    filename = input("Insert filename here: ")
    file_extension = filename.split(".")
    return print("The extension of the file is: ", repr(file_extension[-1]))


def first_last_list():
    color_list = ["Red", "Green", "White", "Black"]
    return print("%s and %s" % (color_list[0], color_list[-1]))


def date_from_list():
    exam_st_date = (11, 12, 2014)
    return print("The examination will start from : %i/%i/%i" % exam_st_date)


def dumb_sum():
    """Is a function to make a dumb sum"""
    number_to_sum = input("Enter a number to make a dumb sum: ")
    n1 = int("%s" % (number_to_sum))
    n2 = int("%s%s" % (number_to_sum, number_to_sum))
    n3 = int("%s%s%s" % (number_to_sum, number_to_sum, number_to_sum))
    sum_of_dumb = n1 + n2 + n3
    return print("Your dumb sum is: ", sum_of_dumb)


def function_info(python_function):
    return print(python_function.__doc__)


def show_calendar(year, month):
    import calendar
    return print(calendar.month(year, month))


def heredoc_sample():
    return print("""
    a string that you "don't" have to escape
    This
    is a  ....... multi-line
    heredoc string --------> example
    """)


def date_diff(FirstYear, FirstMonth, FirstDay, LastYear, LastMonth, LastDay):
    from datetime import date
    first_date = date(FirstYear, FirstMonth, FirstDay)
    last_date = date(LastYear, LastMonth, LastDay)
    delta = last_date - first_date
    return print(delta.days)


def absolute_difference(FirstNumber, SecondNumber):
    if FirstNumber >= SecondNumber:
        difference = 2 * abs(FirstNumber-SecondNumber)
    else:
        difference = abs(FirstNumber-SecondNumber)
    return print(difference)


def string_with_is(string):
    if len(string) >= 2 and string[:2] == "Is":
        return string
    else:
        return "Is" + string


def multiply_string(string, repetitions):
    result = ""
    for i in range(repetitions):
        result = result + string
    return result


def even_or_odd(number: int):
    mod = int(number) % 2
    if mod > 0:
        return print("It's even")
    else:
        return print("It's odd")


def count_repeated_element():
    wanted_element = input("Search for: ")
    record = input("In this comma separated list:")
    listed_record = record.split(",")
    return print("{} occurs {} time(s)".format(wanted_element, listed_record.count(wanted_element)))


def substring_copy(str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]

    result = ""
    for i in range(n):
        result = result + substr
    return result


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels


def is_group_member(n, group_data):
    for value in group_data:
        if n == value:
            return True
    return False


def histogram(data, char):
    for i in data:
        print(i * char)
    return


def concatenate_list_data(list):
    result = ''
    for element in list:
        result += str(element)
    return result


def check_and_stop():
    numbers = [
        386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
        399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
        815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
        958, 743, 527
    ]

    for x in numbers:
        if x == 237:
            print(x)
            break
        elif x % 2 == 0:
            print(x)
    return


def difference_between_lists(list1, list2):
    Set1 = set(list1)
    Set2 = set(list2)
    return (Set1 - Set2)


def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    return a + b


def distance_between_points(Coordinates1, Coordinates2):
    import math
    distance = math.sqrt(
        ((Coordinates1[0]-Coordinates2[0])**2)+((Coordinates1[1]-Coordinates2[1])**2))

    return distance


def open_file():
    import os.path
    open('abc.txt', 'w')
    print(os.path.isfile('abc.txt'))


def comma_code(lista_nome: list):
    frase = ""
    for nome in range(len(lista_nome)):
        if nome == len(lista_nome)-1:
            frase += lista_nome[nome] + "."
        elif nome == len(lista_nome)-2:
            frase += lista_nome[nome] + " and "
        else:
            frase += lista_nome[nome] + ", "
    return frase
