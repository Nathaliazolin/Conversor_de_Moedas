VALOR_REAIS = float (input(f" Digite o valor em Reais: "))
print("1 - Conversão para Euro")
print ("2 - Conversão para Dolares")
OPCAODESEJADA = input ("Digite a opção desejada: ")
TAXADECAMBIO = float(input ("Digite a taxa de cambio para conversão: "))

if OPCAODESEJADA == "1":
    VALOR_EURO: float = (VALOR_REAIS/TAXADECAMBIO)
    print(f"Valor convertido para Euro: {VALOR_EURO}")

else:
    VALOR_DOLAR: float = (VALOR_REAIS/TAXADECAMBIO)
    print(f"Valor convertido para Dolares: {VALOR_DOLAR}")
