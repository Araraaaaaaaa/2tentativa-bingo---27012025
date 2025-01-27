import random
permanencia = True
Joga1 = {(50,70,80,90),
         (51,72,82,91)}
falta1= 8
Joga2 = {(53,65,83,92),
         (50,78,82,95)}
falta2= 8
ganhadores = 0

def cartelas(J1, J2):
    #________________________________________________________Sorteio
    for Indic, List1 in enumerate(J1):
        for Indice, Number in enumerate(List1):
            if Indice == 0:
                J1[Indic][0] = random.randint(1,10)
                J2[Indic][0] = random.randint(1,10)
            elif Indice == 1:
                J1[Indic][1] = random.randint(11,20)
                J2[Indic][1] = random.randint(11,20)
            elif Indice == 2:
                J1[Indic][2] = random.randint(21,30)
                J2[Indic][2] = random.randint(21,30)
            elif Indice == 3:
                J1[Indic][3] = random.randint(31,40)
                J2[Indic][3] = random.randint(31,40)
    #_____________________________________________________________________________________Correção 
    for Indicelin, Linha in enumerate(J1):
        for Indi, Number in enumerate(Linha):
            if J1[0][Indi] == J1[1][Indi]: # verifica se tem algum igual
                if Indi == 0: # separa pelos parâmetros
                    if J1[0][Indi] < 9: #verifica se é um número difícil de alterar
                        J1[0][Indi] += 2
                    else:
                        J1[1][Indi] -= 2
                elif Indi == 1:
                    if J1[0][Indi] < 19: 
                        J1[0][Indi] += 2
                    else:
                        J1[1][Indi] -= 2
                elif Indi == 2:
                    if J1[0][Indi] < 29: 
                        J1[0][Indi] += 2
                    else:
                        J1[1][Indi] -= 2
                elif Indi == 3:
                    if J1[0][Indi] < 39: 
                        J1[0][Indi] += 2
                    else:
                        J1[1][Indi] -= 2
    for Indicelin, Linh in enumerate(J2):
        for Ind, Number in enumerate(Linh):
            if J2[0][Ind] == J2[1][Ind]: # verifica se tem algum igual
                if Ind == 0: # separa pelos parâmetros
                    if J2[0][Ind] < 9: #verifica se é um número difícil de alterar
                        J2[0][Ind] += 2
                    else:
                        J2[1][Ind] -= 2
                elif Indi == 1:
                    if J2[0][Ind] < 19: 
                        J2[0][Ind] += 2
                    else:
                        J2[1][Ind] -= 2
                elif Indi == 2:
                    if J2[0][Ind] < 29: 
                        J2[0][Ind] += 2
                    else:
                        J2[1][Ind] -= 2
                elif Indi == 3:
                    if J2[0][Ind] < 39: 
                        J2[0][Ind] += 2
                    else:
                        J2[1][Ind] -= 2
    return J1, J2 

def Jogin(dificuldade, Homem1, Homem2): 
    while ganhadores == 0:
    
        # _______________________________#
        print("         Jogador 1")
        print(f"{Homem1[0][0]}  {Homem1[0][1]}   {Homem1[0][2]}")
        print(f"{Homem1[1][0]}  {Homem1[1][1]}   {Homem1[1][2]}")
        print(f"{Homem1[2][0]}  {Homem1[2][1]}   {Homem1[2][2]}")
        # _______________________________#
        print("         Jogador 2")
        print(f"{Homem2[0][0]}  {Homem2[0][1]}   {Homem2[0][2]}")
        print(f"{Homem2[1][0]}  {Homem2[1][1]}   {Homem2[1][2]}")
        print(f"{Homem2[2][0]}  {Homem2[2][1]}   {Homem2[2][2]}")
 
def Jogo(dificuldade, Homem1, Homem2):
    print("Hello Word")

# ______________________________________________________________________Código Principal

while permanencia == True:
    print("Qual o nível de dificuldade?")
    print("Rápido = 1   |   Longo  = 2")
    D = int(input())
    Impar, Par = cartelas(Joga1,Joga2)
    if D == 1:
        Jogin(D,Impar,Par)
    else:
        Jogo(D,Impar,Par)

