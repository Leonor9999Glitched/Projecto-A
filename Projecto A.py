print("")
print("Bem-vindo.")
print("Este programa tem duas opcções.")
print("Poderá a imersão de um fluido ou o comprimento final de uma mola depois do sistema entrar em equilibrio.")
print("Por favor escolha a opcção que quer.")

print("1 - Inersão de um fluido")
print("2 - Molas")

escolha = ""
sair = ""

escolha = int(input("Sua escolha > "))

if(escolha == 1):

    print("Escolheste ver a imersão num fluido.")
    print("O objectivo desta opcção é ver qual o volume que fica submerso no liquido quando sistema entrar em equilibrio.")
    print("Para tal a força gravitica é igual à força de buoyancy.")
    while(sair  != "2"):
        print("")
        print("Por favor, diga quais os valores do seguintes parametros.")
        gravity = input("Gravidade > ")
        densidade1 = input("Densidade do fluído > ")
        densidade2 = input("Densidade do objecto > ")
        volume = input("Volume do cubo > ")

        massa_do_objecto = float(densidade2) * float(volume) #Massa do objecto

        fg = float(massa_do_objecto) * float(gravity) #Força gravitica

        print("A força gravitica é > " + str(fg))
        print("A massa do objecto é > " + str(massa_do_objecto))
        print("")
        print("Para o objecto ficar a flutuar, a força gravitica tem que ser igual à força de buoyancy.")
        print("Para isso temos que descobrir o volume da formula da força bouyancy.")
        print("")

        volume_buoyancy = float(fg) / (float(densidade1) * float(gravity))  #Calcular o calado ou o que fica por debaixo do liquid

        print("Este é o volume de buoyancy > " + str(volume_buoyancy))
        print("Ou seja, o objecto fica a submerso > " + str(volume_buoyancy) + " metros.")
        print("")

        print("Deseja continuar?")
        print("1 - Repetir")
        print("2 - Sair")
        sair = input()

        if(sair == "2"):
            print("Escolheste sair.")
            print("Adeus!")


if(escolha == 2):

    print("Escolheste ver os calculos relacionados com as molas")
    print("")
    print("O objectivo desta opcção é ver o comprimento da mola, após o sistema estar em equilibrio")
    print("A força gravitica é igual à força da mola.")
    while(sair  != "2"):
        print("Por favor, diga quais os valores do seguintes parametros.")
        gravity = input("Gravity > ")
        massa = input("Massa > ")
        repouso = input("Repouso > ")
        const_mola = input("Constante da mola > ")

        fg = float(massa) * float(gravity)

        l = (-fg - (float(const_mola) * float(repouso))) / -float(const_mola)

        print("Este é o comprimento da mola > " + str(l))

        print("Repetir?")
        print("1 - Repetir")
        print("2 - Sair")
        sair = input()

        if(sair == "2"):
            print("Escolheste sair.")
            print("Adeus!")



if(escolha >= 3):

    print("Escolha inválida")
    
