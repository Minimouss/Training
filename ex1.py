
table = [9, 4, 18, 37, 35, 99, 74, 56, 12, 24, 47, 29, 40, 68, 44, 30, 63, 32, 83, 52, 91]

# table = [9, 4, 91, 8]


def isintable():

    while True:
        try:
            x = int(input('Entrez une nombre entier : '))

            for value in table:
                if x == value:
                    print(True)
                    break

            else:
                print(False)
        except:
            print('Erreur : Attention ! Entrez un nombre entier puis validez avec la touche entrée.')


def sort_table(*sorting_methods):
    for sorting_method in sorting_methods:
        sorting_method()


def asc_bot():

    temp_tab = table.copy()
    print(table, ": Tableau original")

    for i in range(len(temp_tab)):
        try:
            for index, value in enumerate(temp_tab):
                next_value = temp_tab[index + 1]
                prev_value = temp_tab[index - 1]
                if index == 0:
                    continue
                elif value < prev_value:
                    temp_tab[index - 1] = value
                    temp_tab[index] = prev_value
                elif value > next_value:
                    temp_tab[index] = next_value
                    temp_tab[index + 1] = value
                elif index == len(temp_tab):
                    pass
        except:
            pass
    print(temp_tab, ": Tableau trié par le début par ordre croissant")


def desc_bot():

    temp_tab = table.copy()
    print(temp_tab, ": Tableau original")

    for i in range(len(temp_tab)):
        try:
            for index, value in enumerate(temp_tab):
                next_value = temp_tab[index + 1]
                prev_value = temp_tab[index - 1]
                if index == 0:
                    continue
                elif value > prev_value:
                    temp_tab[index - 1] = value
                    temp_tab[index] = prev_value
                elif value < next_value:
                    temp_tab[index] = next_value
                    temp_tab[index + 1] = value
                elif index == len(temp_tab):
                    pass
        except:
            pass
    print(temp_tab, ": Tableau trié par le début par ordre décroissant")


def desc_top():

    temp_tab = table.copy()
    print(temp_tab, ": Tableau original")

    for i in range(len(temp_tab), 0, -1):
        try:
            for index, value in reversed(list(enumerate(temp_tab))):
                next_value = temp_tab[index - 1]
                prev_value = temp_tab[index + 1]
                if index == 0:
                    pass
                elif value > prev_value:
                    temp_tab[len(temp_tab) - index] = value
                    temp_tab[len(temp_tab)] = prev_value
                elif value < next_value:
                    temp_tab[len(temp_tab)] = next_value
                    temp_tab[len(temp_tab) + index] = value
                elif index == len(temp_tab):
                    continue
        except:
            pass
    print(temp_tab, ": Tableau trié par la fin par ordre décroissant")


# isintable()

# asc()
# sort_table(asc_bot)
# sort_table(desc_bot)
sort_table(desc_top)
