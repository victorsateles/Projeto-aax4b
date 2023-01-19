#usando if, elif e else

fases_da_vida = 2

if fases_da_vida <= 14:
    print("Crianca")
elif fases_da_vida <= 17:
    print ("Adolescente")
elif fases_da_vida <= 59:
    print("Adulto")
elif fases_da_vida <=100:
    print ("Idoso")
else:
    print("Imortal?")

# utilizando o match case

#fase da vida 1 = criança
#fase da vida 2 = adolescente
#fase da vida 3 = adulto
#fase da vida 4 = idoso

fases_da_vida = 2

match fases_da_vida:
    case 1:
        print("Criança")
match fases_da_vida:
    case 2:
        print("Adolescente")
match fases_da_vida:
    case 3:
        print("Adulto")
match fases_da_vida:
    case 4:
        print("idoso")

# Usando and, or, not ( não consegui aplicar o is no meu codigo)

Sou_adulto = False
Tenho_barba = False
sou_alto = False

if Sou_adulto and Tenho_barba:
    print("Esse sou eu")
elif Sou_adulto and not Tenho_barba:
    print ("Não sou eu")
elif Tenho_barba or sou_alto or Sou_adulto:
    print("Eu tbm sou assim")
else:
    print(" <3 ")


