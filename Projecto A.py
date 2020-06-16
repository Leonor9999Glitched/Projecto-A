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

    print("Escolheste ver a imersão num fluido")
    while(sair  != "2"):
        print("Por favor, diga quais os valores do seguintes parametros")
        gravity = input("Gravidade > ")
        densidade1 = input("Densidade do fluído > ")
        densidade2 = input("Densidade do objecto > ")
        volume = input("Volume do cubo > ")
        
        f = float(densidade1) * float(gravity) * float(volume)
        
        massa_do_objecto = float(densidade2) * float(volume)

        fg = float(massa_do_objecto) * float(gravity)

        if(fg > f):
            print("Força do objecto é " + str(f))
            print("Força da gravidade é = " + str(fg))
            print("Força do objecto é maior do que " + str(f) + "logo o objecto afundu-se")
            print("Repetir?")
            print("1 - Repetir")
            print("2 - Sair")
            sair = input()

        if(fg < f):
            print("O objecto está flutauar.")
            print("Repetir?")
            print("1 - Repetir")
            print("2 - Sair")
            sair = input()

if(escolha == 2):

    print("Escolheste ver os calculos relacionados com as molas")
    while(sair  != "2"):
        gravity = input("Gravity > ")
        massa = input("Massa > ")
        repouso = input("Repouso > ")
        const_mola = input("Constante da mola > ")

        fg = float(massa) * float(gravity)

        l = (fg + (float(const_mola) * float(repouso))) / float(const_mola)

        print("Este é o comprimento da mola > " + str(l))

        print("Repetir?")
        print("1 - Repetir")
        print("2 - Sair")
        sair = input()



if(escolha >= 3):

    print("Escolha inválida")
    
