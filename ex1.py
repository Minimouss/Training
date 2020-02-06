
table = [9, 4, 18, 37, 35, 99, 74, 56, 12, 24, 47, 29, 40, 68, 44, 30, 63, 32, 83, 52, 91]
# table = [9, 4, 18, 37, 35, 99, 74, 56, 12]

# table = [9, 4, 8]


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


# def sort_table(*sorting_methods, **sorting_modes):
#     for sorting_method in sorting_methods:
#         for sorting_mode in sorting_modes:
#             sorting_method(sorting_mode)

def sort_table(*sorting_methods):
    for sorting_method in sorting_methods:
        sorting_method()


class FromTop:
    @staticmethod
    def asc():

        temp_tab = table.copy()
        print(table, ": Tableau original")

        for i in range(len(temp_tab)):
            try:
                for index, value in enumerate(temp_tab):
                    down = temp_tab[index - 1]
                    up = temp_tab[index + 1]
                    if index == 0:
                        continue
                    elif value < down:
                        temp_tab[index - 1] = value
                        temp_tab[index] = down
                    elif value > up:
                        temp_tab[index] = up
                        temp_tab[index + 1] = value
                    elif index == len(temp_tab):
                        pass
            except:
                pass
        print(temp_tab, ": Tableau trié par le début par ordre croissant")

    @staticmethod
    def sort(mode):

        temp_tab = table.copy()
        print(temp_tab, ": Tableau original")

        if mode == 'asc':
            for i in range(len(temp_tab), 0, -1):
                for value in list(temp_tab[::-1]):
                    index = temp_tab.index(value)
                    if index == 0:
                        for n in temp_tab:
                            idx = temp_tab.index(n)
                            if idx == len(temp_tab) - 1:
                                continue
                            elif temp_tab[idx] < temp_tab[idx + 1]:
                                continue
                    elif index == len(temp_tab) - 1 and i > 0:
                        continue
                    elif index == len(temp_tab) - 1:
                        pass

                    up = temp_tab[index + 1]
                    down = temp_tab[index - 1]
                    if value > up:
                        temp_tab[index + 1] = value
                        temp_tab[index] = up
                    elif value < down:
                        temp_tab[index] = down
                        temp_tab[index - 1] = value
            print(temp_tab, ": FromTop('asc')")

        if mode == 'desc':
            for n in range(1, len(temp_tab) - 1):
                for i in range(len(temp_tab), 0, -1):
                    for value in list(temp_tab[::-1]):
                        if temp_tab[n] > temp_tab[n + 1]:
                            break

                        index = temp_tab.index(value)
                        if index == len(temp_tab) - 1 and i > 0:
                            continue
                        elif index == len(temp_tab) - 1:
                            pass

                        up = temp_tab[index + 1]
                        down = temp_tab[index - 1]
                        if value < up:
                            temp_tab[index + 1] = value
                            temp_tab[index] = up
                        elif value > down:
                            temp_tab[index] = down
                            temp_tab[index - 1] = value
            print(temp_tab, ": FromTop('desc')")

    @staticmethod
    def desc():

        temp_tab = table.copy()
        print(temp_tab, ": Tableau original")

        for i in range(len(temp_tab)):
            try:
                for index, value in enumerate(temp_tab):
                    down = temp_tab[index - 1]
                    up = temp_tab[index + 1]
                    if index == 0:
                        continue
                    elif value > down:
                        temp_tab[index - 1] = value
                        temp_tab[index] = down
                    elif value < up:
                        temp_tab[index] = up
                        temp_tab[index + 1] = value
                    elif index == len(temp_tab):
                        pass
            except:
                pass
        print(temp_tab, ": Tableau trié par le début par ordre décroissant")


class FromBot:
    @staticmethod
    def asc():

        temp_tab = table.copy()
        print(temp_tab, ": Tableau original")

        for i in range(len(temp_tab), 0, -1):
            try:
                for value in list(temp_tab[::-1]):
                    index = temp_tab.index(value)

                    if index == 0:
                        continue
                    elif index == len(temp_tab) - 1:
                        pass
                    else:
                        up = temp_tab[index + 1]
                        down = temp_tab[index - 1]
                        if value > up:
                            temp_tab[index + 1] = value
                            temp_tab[index] = up
                        elif value < down:
                            temp_tab[index] = down
                            temp_tab[index - 1] = value
                        elif index == len(temp_tab):
                            pass
            except:
                pass
        print(temp_tab, ": Tableau trié par la fin par ordre croissant")

    @staticmethod
    def sort(mode):

        temp_tab = table.copy()
        print(temp_tab, ": Tableau original")

        if mode == 'asc':
            for i in range(len(temp_tab), 0, -1):
                for value in list(temp_tab[::-1]):

                    index = temp_tab.index(value)
                    if index == 0:
                        for n in temp_tab:
                            idx = temp_tab.index(n)
                            if idx == len(temp_tab) - 1:
                                continue
                            elif temp_tab[idx] < temp_tab[idx + 1]:
                                break
                    elif index == len(temp_tab) - 1 and i > 0:
                        continue
                    elif index == len(temp_tab) - 1:
                        pass

                    up = temp_tab[index + 1]
                    down = temp_tab[index - 1]
                    if value > up:
                        temp_tab[index + 1] = value
                        temp_tab[index] = up
                    elif value < down:
                        temp_tab[index] = down
                        temp_tab[index - 1] = value
                        continue

            print(temp_tab, ": FromBot('asc')")

        if mode == 'desc':
            for i in range(len(temp_tab), 0, -1):
                for value in list(temp_tab[::-1]):

                    index = temp_tab.index(value)
                    if index == 0:
                        for n in temp_tab:
                            idx = temp_tab.index(n)
                            if idx == len(temp_tab) - 1:
                                continue
                            elif temp_tab[idx] > temp_tab[idx + 1]:
                                break
                        continue
                    if index == len(temp_tab) - 1 and i > 0:
                        continue
                    elif index == len(temp_tab) - 1:
                        pass

                    up = temp_tab[index + 1]
                    down = temp_tab[index - 1]
                    if value < up:
                        temp_tab[index + 1] = value
                        temp_tab[index] = up
                    elif value > down:
                        temp_tab[index] = down
                        temp_tab[index - 1] = value
            print(temp_tab, ": FromBot('desc')")

    @staticmethod
    def desc():

        temp_tab = table.copy()
        print(temp_tab, ": Tableau original")

        for i in range(len(temp_tab), 0, -1):
            try:
                for value in list(temp_tab[::-1]):
                    index = temp_tab.index(value)

                    if index == 0:
                        continue
                    elif index == len(temp_tab) - 1:
                        pass
                    elif index == len(temp_tab):
                        pass
                    else:
                        up = temp_tab[index + 1]
                        down = temp_tab[index - 1]
                        if value < up:
                            temp_tab[index + 1] = value
                            temp_tab[index] = up
                        elif value > down:
                            temp_tab[index] = down
                            temp_tab[index - 1] = value
            except:
                pass
        print(temp_tab, ": Tableau trié par la fin par ordre décroissant")


class Dichotomie:
    @staticmethod
    def asc():
        pass

    @staticmethod
    def desc():
        pass

# isintable()

# sort_table(asc_bot)
# sort_table(desc_bot)
# sort_table(asc_top)
# sort_table(desc_top)
# FromBot.asc()
# FromBot.desc()
# FromTop.desc()
FromBot.sort('asc')
FromBot.sort('desc')
FromTop.sort('asc')
FromTop.sort('desc')
