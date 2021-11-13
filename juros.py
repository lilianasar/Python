#JUROS SIMPLES
valor_inicial = float(input("Qual o valor do produto? "))
juros = float(input("Qual o valor de juros em %? "))
meses = int(input("A quantos meses? "))
juros = juros * 0.01
cont = 1
valor_juros = valor_inicial * juros
valor_final = 0
print("")
print("VALOR COM JUROS")
while cont <= meses:
    valor_final = valor_inicial + valor_juros
    valor_inicial = valor_final
    print("Mês " +str(cont) + ': '+ str(valor_inicial) +"€")
    cont += 1

