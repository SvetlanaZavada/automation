month = int(input("Введите номер месяца"))


def month_to_season(month):
    if month < 3 or month > 11:
        return "Зима"
    if 2 < month < 6:
        return "Весна"
    if 6 <= month < 9:
        return "Лето"
    if 9 <= month < 12:
        return "Осень"


print(month_to_season(month))
