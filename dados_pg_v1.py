from random import randint

quantidade = int(input("Digite a quantidade de dados123: "))
tipo_dado = int(input("Digite o tipo dee dado: "))
repeticao = int(input("Digite quantas repetições: "))

tentativa = 1 
valores = []

while tentativa <= repeticao:
    quantidade_temp = 1
    while quantidade_temp <= quantidade:
        valor = randint(1, tipo_dado)
        print(valor)
        quantidade_temp = quantidade_temp + 1
    print("------Fim da Repetição------")
    tentativa = tentativa + 1 
print("FIM DO PROGRAMA!")