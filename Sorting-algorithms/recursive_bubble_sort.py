def bubble_sort(listres):
    for i, num in enumerate(listres):
        try:
            if listres[i + 1] < num:
                listres[i] = listres[i + 1]
                listres[i + 1] = num
                bubble_sort(listres)
        except IndexError:
            pass
    return listres
