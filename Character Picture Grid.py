def print_grid(list_of_lists: list):
    for i in range(len(list_of_lists[1])):
        print("\n", end="")
        for j in range(len(list_of_lists)):
            lista_atual = list_of_lists[j]
            print(lista_atual[i], end=" ")
    return


grid = [
    [' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
    [' . ', ' O ', ' O ', ' . ', ' . ', ' . '],
    [' O ', ' O ', ' O ', ' O ', ' . ', ' . '],
    [' O ', ' O ', ' O ', ' O ', ' O ', ' . '],
    [' . ', ' O ', ' O ', ' O ', ' O ', ' O '],
    [' O ', ' O ', ' O ', ' O ', ' O ', ' . '],
    [' O ', ' O ', ' O ', ' O ', ' . ', ' . '],
    [' . ', ' O ', ' O ', ' . ', ' . ', ' . '],
    [' . ', ' . ', ' . ', ' . ', ' . ', ' . ']
]

print_grid(grid)
