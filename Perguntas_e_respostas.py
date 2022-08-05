perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas':{'a':5, 'b':8, 'c':4},
        'resposta_correta': 'c'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 7*5?',
        'respostas':{'a':35, 'b':88, 'c':4},
         'resposta_correta': 'a'
    }
}
resp = 0
for pk, pv in perguntas.items():
    print(f'{pk}: \n {pv["pergunta"]}')
    for rk, rv in pv["respostas"].items():
        print(f'{rk} = {rv}')
    alt = str(input("Digite a alternativa: "))
    if alt == pv['resposta_correta']:
        print("Parabens! voce acertou")
        resp += 1
    else:
        print("Seu animal! vc errou")
print(f"total de acertos {resp}")