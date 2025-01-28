import random
permanencia = "ficar"
while permanencia != "NAO":
    Joga1 = [[0,0,0,0],
            [0,0,0,0]]
    Joga2 = [[0,0,0,0],
            [0,0,0,0]]
    Joga3 = [[0,0,0,0],
            [0,0,0,0]]
    Joga4 = [[0,0,0,0],
            [0,0,0,0]]
    conjunto = []
    casa = [1]
    ganhadores = 0
    numerosinit = [ 1, 11, 21, 31]
    numerosfini = [10, 20, 30, 40]
    espaco=" "

    def cartelas(J1, J2, J3, J4):
        #________________________________________________________Sorteio na cartela
        for Indic, List1 in enumerate(J1):
            for Indice, Number in enumerate(List1):
                a = random.randint(numerosinit[Indice], numerosfini[Indice])
                b = random.randint(numerosinit[Indice], numerosfini[Indice])
                J1[Indic][Indice] = a
                J2[Indic][Indice] = b
                J3[Indic][Indice] = a
                J4[Indic][Indice] = b
        #_____________________________________________________________________________________Correção da cartela
        for Linha in (J1):
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
        for Linh in (J2):
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
        for Linh in (J3):
            for Ind, Number in enumerate(Linh):
                if J3[0][Ind] == J3[1][Ind]: # verifica se tem algum igual
                    if Ind == 0: # separa pelos parâmetros
                        if J3[0][Ind] < 9: #verifica se é um número difícil de alterar
                            J3[0][Ind] += 2
                        else:
                            J3[1][Ind] -= 2
                    elif Indi == 1:
                        if J3[0][Ind] < 19: 
                            J3[0][Ind] += 2
                        else:
                            J3[1][Ind] -= 2
                    elif Indi == 2:
                        if J3[0][Ind] < 29: 
                            J3[0][Ind] += 2
                        else:
                            J3[1][Ind] -= 2
                    elif Indi == 3:
                        if J3[0][Ind] < 39: 
                            J3[0][Ind] += 2
                        else:
                            J3[1][Ind] -= 2
        for Linh in (J4):
            for Ind, Number in enumerate(Linh):
                if J4[0][Ind] == J4[1][Ind]: # verifica se tem algum igual
                    if Ind == 0: # separa pelos parâmetros
                        if J4[0][Ind] < 9: #verifica se é um número difícil de alterar
                            J4[0][Ind] += 2
                        else:
                            J4[1][Ind] -= 2
                    elif Indi == 1:
                        if J4[0][Ind] < 19: 
                            J4[0][Ind] += 2
                        else:
                            J4[1][Ind] -= 2
                    elif Indi == 2:
                        if J4[0][Ind] < 29: 
                            J4[0][Ind] += 2
                        else:
                            J4[1][Ind] -= 2
                    elif Indi == 3:
                        if J4[0][Ind] < 39: 
                            J4[0][Ind] += 2
                        else:
                            J4[1][Ind] -= 2
        return J1, J2 , J3, J4

    def Jogin(Homem1, Homem2): 
        print("Nome de usuário:")
        Jogador1 = input("jogador 1: ")
        Jogador2 = input("jogador 2: ")
        possibilidadesF = [1,2,3,4,5,6,7,8,9,10
                    ,11,12,13,14,15,16,17,18,19,20
                    ,21,22,23,24,25,26,27,28,29,30] #!

        falta1, falta2 , fim= 6, 6 , 0#!
        # _______________________________#
        print("")
        print(" Jogador 1")
        print(f"{Homem1[0][0]}  {Homem1[0][1]}   {Homem1[0][2]}")#!
        print(f"{Homem1[1][0]}  {Homem1[1][1]}   {Homem1[1][2]}")#!
        print(" Jogador 2")
        print(f"{Homem2[0][0]}  {Homem2[0][1]}   {Homem2[0][2]}")#!
        print(f"{Homem2[1][0]}  {Homem2[1][1]}   {Homem2[1][2]}")#!
        # _______________________________#
        while fim == 0:
            fim = 0     
            # _____________________________________Sorteio dos números

            sorteio = possibilidadesF[random.randint(0,len(possibilidadesF)-1)]
            possibilidadesF.remove(sorteio) #retira o item X da lista
            conjunto.append(sorteio)

            # ______________________________________________________________________________Marca os sorteados
            for i,N1 in enumerate(Homem1):
                for v,NN1 in enumerate(N1):
                    if sorteio == NN1:      #se algum número de Homem1 for sorteado
                        Homem1[i][v] = f"<{NN1}>"
                        falta1 -= 1
            for i,N2 in enumerate(Homem2):
                for v,NN2 in enumerate(N2):
                    if sorteio == NN2:      #se algum número de Homem1 for sorteado
                        Homem2[i][v] = f"<{NN2}>"
                        falta2 -= 1

            conjunto.sort()#___________sort=deixa em ordem
            print("")
            print(f"Sorteio = {sorteio}", end='    ')
            print(f"Sorteados = {conjunto}")
            print("")
            print(f"{Jogador1}  {falta1}              {Jogador2}  {falta2}")
            print(f"{Homem1[0][0]} {Homem1[0][1]} {Homem1[0][2]}                 {Homem2[0][0]} {Homem2[0][1]} {Homem2[0][2]}")
            print(f"{Homem1[1][0]} {Homem1[1][1]} {Homem1[1][2]}                 {Homem2[1][0]} {Homem2[1][1]} {Homem2[1][2]}")
            print("")
        
            #_____________________________________________________Relação dos ganhadores
            if falta2 == 0 or falta1 == 0:
                fim = 5
                if falta1 == 0 and falta2 == 0:
                    print("Bingo! Ambos jogadores ganharam \o/")
                elif falta1 == 0:
                    print(f"Bingo! {Jogador1} ganhou \o/")
                else:
                    print(f"Bingo! {Jogador2} ganhou \o/")
            print("")
            input("Continue?")

    def Jogo(Homem1, Homem2, Homem3, Homem4):
        print("Nome de usuário:")
        Jogador1 = input("jogador 1: ")
        Jogador2 = input("jogador 2: ")
        Jogador3 = input("jogador 3: ")
        Jogador4 = input("jogador 4: ")
        possibilidadesF = [1,2,3,4,5,6,7,8,9,10,
                    11,12,13,14,15,16,17,18,19,20,
                    21,22,23,24,25,26,27,28,29,30,
                    31,32,33,34,35,36,37,38,39,40] #!
        
        falta1, falta2, falta3, falta4 = 8, 8, 8, 8#!
        fim, acima1, acima2, acima3,acima4, = 0, 4,4,4,4

        # _______________________________#
        print("")
        print(" Jogador 1")
        print(f"{Homem1[0][0]}  {Homem1[0][1]}   {Homem1[0][2]}   {Homem1[0][3]}")#!
        print(f"{Homem1[1][0]}  {Homem1[1][1]}   {Homem1[1][2]}   {Homem1[1][3]}")#!
        print(" Jogador 2")
        print(f"{Homem2[0][0]}  {Homem2[0][1]}   {Homem2[0][2]}   {Homem2[0][3]}")#!
        print(f"{Homem2[1][0]}  {Homem2[1][1]}   {Homem2[1][2]}   {Homem2[1][3]}")#!
        print(" Jogador 3")
        print(f"{Homem3[0][0]}  {Homem3[0][1]}   {Homem3[0][2]}   {Homem3[0][3]}")
        print(f"{Homem3[1][0]}  {Homem3[1][1]}   {Homem3[1][2]}   {Homem3[1][3]}")
        print(" Jogador 4")
        print(f"{Homem4[0][0]}  {Homem4[0][1]}   {Homem4[0][2]}   {Homem4[0][3]}")
        print(f"{Homem4[1][0]}  {Homem4[1][1]}   {Homem4[1][2]}   {Homem4[1][3]}")
        # _______________________________#
        while fim == 0:
            fim = 0     
            # _____________________________________Sorteio dos números

            sorteio = possibilidadesF[random.randint(0,len(possibilidadesF)-1)]
            possibilidadesF.remove(sorteio) #retira o item X da lista
            conjunto.append(sorteio)

            # ______________________________________________________________________________Marca os sorteados
            for i,N1 in enumerate(Homem1):
                for v,NN1 in enumerate(N1):
                    if sorteio == NN1:      #se algum número de Homem1 for sorteado
                        Homem1[i][v] = f"<{NN1}>"
                        falta1 -= 1
                        acima1 += 1
            for i,N2 in enumerate(Homem2):
                for v,NN2 in enumerate(N2):
                    if sorteio == NN2:      #se algum número de Homem2 for sorteado
                        Homem2[i][v] = f"<{NN2}>"
                        falta2 -= 1
                        acima2 += 1
            for i,N3 in enumerate(Homem3):
                for v,NN3 in enumerate(N3):
                    if sorteio == NN3:      #se algum número de Homem3 for sorteado
                        Homem3[i][v] = f"<{NN3}>"
                        falta3 -= 1
                        acima3 += 1
            for i,N4 in enumerate(Homem4):
                for v,NN4 in enumerate(N4):
                    if sorteio == NN4:      #se algum número de Homem4 for sorteado
                        Homem4[i][v] = f"<{NN4}>"
                        falta4 -= 1
                        acima4 += 1

            conjunto.sort()#___________sort=deixa em ordem
            print("")
            print(f"Sorteio = {sorteio}", end='    ')
            print(f"Sorteados = {conjunto}")
            print("")
            print(f"{Jogador1}  {falta1}            {Jogador2}  {falta2}")
            print("")
            print(f"{Homem1[0][0]} {Homem1[0][1]} {Homem1[0][2]} {Homem1[0][3]}{espaco*(acima1)}{Homem2[0][0]} {Homem2[0][1]} {Homem2[0][2]} {Homem2[0][3]}")
            print(f"{Homem1[1][0]} {Homem1[1][1]} {Homem1[1][2]} {Homem1[1][3]}{espaco*(acima1)}{Homem2[1][0]} {Homem2[1][1]} {Homem2[1][2]} {Homem2[1][3]}")
            print("")
            print(f"{Jogador3}  {falta3}         {Jogador4}  {falta4}")
            print(f"{Homem3[0][0]} {Homem3[0][1]} {Homem3[0][2]} {Homem3[0][3]}{espaco*(acima3)}{Homem4[0][0]} {Homem4[0][1]} {Homem4[0][2]} {Homem4[0][3]}")
            print(f"{Homem3[1][0]} {Homem3[1][1]} {Homem3[1][2]} {Homem3[1][3]}{espaco*(acima3)}{Homem4[1][0]} {Homem4[1][1]} {Homem4[1][2]} {Homem4[1][3]}")
        
            #_____________________________________________________Relação dos ganhadores....refarer
            if falta1 == 0 or falta2 == 0 or falta3 == 0 or falta4 == 0:
                fim = 5
                if falta1 == 0 and falta2 == 0 and falta3 == 0 and falta4 == 0: #Todos
                    print("Bingo! Ambos jogadores ganharam \o/")          
                    # ___________________________________________________________Vitórias solo
                elif falta1 == 0 and falta2 > 0 and falta3 > 0 and falta4 > 0:
                    print(f"Bingo! {Jogador1} ganhou \o/")
                elif falta1 > 0 and falta2 == 0 and falta3 > 0 and falta4 > 0:
                    print(f"Bingo! {Jogador2} ganhou \o/")
                elif falta1 > 0 and falta2 > 0 and falta3 == 0 and falta4 > 0:
                    print(f"Bingo! {Jogador3} ganhou \o/")
                elif falta1 > 0 and falta2 > 0 and falta3 > 0 and falta4 == 0:
                    print(f"Bingo! {Jogador4} ganhou \o/")
                    # ___________________________________________________________Vitórias duplas
                elif falta1 == 0 and falta2 == 0 and falta3 > 0 and falta4 > 0:
                    print(f"Bingo! os jogadores {Jogador1} e {Jogador2} ganharam \o/")
                elif falta1 == 0 and falta2 > 0 and falta3 == 0 and falta4 > 0:
                    print(f"Bingo! os jogadores {Jogador1} e {Jogador3} ganharam \o/")
                elif falta1 == 0 and falta2 > 0 and falta3 > 0 and falta4 == 0:
                    print(f"Bingo! os jogadores {Jogador1} e {Jogador4} ganharam \o/")
                elif falta1 > 0 and falta2 == 0 and falta3 == 0 and falta4 > 0:
                    print(f"Bingo! os jogadores {Jogador2} e {Jogador3} ganharam \o/")
                elif falta1 > 0 and falta2 == 0 and falta3 > 0 and falta4 == 0:
                    print(f"Bingo! os jogadores {Jogador2} e {Jogador4} ganharam \o/")
                elif falta1 > 0 and falta2 > 0 and falta3 == 0 and falta4 == 0:
                    print(f"Bingo! os jogadores {Jogador3} e {Jogador4} ganharam \o/")
                # ________________________________________________________________Vitórias triplas
                elif falta1 == 0 and falta2 == 0 and falta3 == 0 and falta4 > 0:
                    print(f"Bingo! os jogadores {Jogador1}, {Jogador2} e {Jogador3} ganharam \o/")
                elif falta1 > 0 and falta2 == 0 and falta3 == 0 and falta4 == 0:
                    print(f"Bingo! os jogadores {Jogador2}, {Jogador3} e {Jogador4} ganharam \o/")
                elif falta1 == 0 and falta2 > 0 and falta3 == 0 and falta4 == 0:
                    print(f"Bingo! os jogadores {Jogador1}, {Jogador3} e {Jogador4} ganharam \o/")
                elif falta1 == 0 and falta2 == 0 and falta3 > 0 and falta4 == 0:
                    print(f"Bingo! os jogadores {Jogador1}, {Jogador2} e {Jogador4} ganharam \o/")

            print("")
            input("Continue?")


    # ______________________________________________________________________Código Principal

    print("Rápido = 1   |   Longo  = 2")
    print("Qual o nível de dificuldade?", end=" ")
    D = int(input())

    Impar, Par, hoje, depois = cartelas(Joga1,Joga2,Joga3,Joga4)
    if D == 1:
        Jogin(Impar,Par)
    else:
        Jogo(Impar,Par, hoje, depois)


print(" ")
print("The End")