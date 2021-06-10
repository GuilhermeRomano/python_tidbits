def validar_nota(nota: float):
    if nota < 0 or nota > 100:
        nova_nota = float(input("Insira uma nova nota válida\n"))
        nota = validar_nota(nova_nota)
    return nota


def inserir_notas():
    contagem = 1
    total_notas = int(input("Quantas notas serão inseridas?\n"))
    lista_notas = []
    while contagem <= total_notas:
        nota_inserida = float(input("Insira a {0} ª nota \n".format(contagem)))
        lista_notas.append(validar_nota(nota_inserida))
        contagem += 1
    return lista_notas


def avaliacao(media: float):
    if media >= 70 and media <= 100:
        status = "aprovado"
    else:
        status = "reprovado"
    return status


aluno = input("Insira o nome do aluno:\n")
resultado_notas = inserir_notas()
media_aluno = sum(resultado_notas)/len(resultado_notas)
avaliacao_final = avaliacao(media_aluno)


print("O aluno {0} está {1} com nota igual a {2}".format(
    aluno, avaliacao_final, media))
