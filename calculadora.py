vit = int(input("Digite a quantidade de vitórias do herói: "))
der = int(input("Digite a quantidade de derrotas do herói: "))

saldo = vit - der

if saldo <= 10:
    print(f"O Herói tem saldo de {saldo} está no nível de Ferro")
elif saldo <= 20:
    print(f"O Herói tem saldo de {saldo} está no nível de Bronze")
elif saldo <= 50:
    print(f"O Herói tem saldo de {saldo} está no nível de Prata")
elif saldo <= 80:
    print(f"O Herói tem saldo de {saldo} está no nível de Ouro")
elif saldo <= 90:
    print(f"O Herói tem saldo de {saldo} está no nível de Diamante")
elif saldo <= 100:
    print(f"O Herói tem saldo de {saldo} está no nível de Lendário")
elif saldo > 100:
    print(f"O Herói tem saldo de {saldo} está no nível de Imortal")