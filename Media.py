nome = input("Insira seu nome:")


def nota_1ee():
    nota = float(input("Insira a primeira nota \n"))
    if nota > 100:
        print("Insira uma nota válida")
        nota = nota_1ee()
    return nota


def nota_2ee():
    nota = float(input("Insira a segunda nota \n"))
    if nota > 100:
        print("Insira uma nota válida")
        nota = nota_2ee()
    return nota


nota_1 = nota_1ee()
nota_2 = nota_2ee()

media = (nota_1 + nota_2)/2

if media > 70:
    print("aprovado")
else:
    print("reprovado")
