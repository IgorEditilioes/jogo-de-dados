from random import randint
from time import sleep
grupo = []
for j in range(0,4):
    jogador = {}
    jogador['Nome'] = str(input("Nome: "))
    jogador['Jogada'] = randint(0,6)
    grupo.append(jogador.copy())
    jogador.clear()
vencedor = ''
for j in grupo:
    sleep(1)
    print(f"Jogador {j['Nome']} tirou {j['Jogada']}")
    for i in range(0,4):
        if grupo[i] == 0:
            vencedor = grupo[0]['Nome']
        elif grupo[i]["Jogada"] > grupo[i - 1]["Jogada"]:
            vencedor = grupo[i]["Nome"]

print("="*15)
print(f"O vencedor foi {vencedor}")
