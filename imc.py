def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Baixo peso"
    elif 18.5 <= imc < 24.9:
        classificacao = "Peso adequado"
    elif 25.0 <= imc < 29.9:
        classificacao = "Sobrepeso"
    elif 30.0 <= imc < 34.9:
        classificacao = "Obesidade grau I"
    elif 35.0 <= imc < 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
    return imc, classificacao

def obter_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

if __name__ == "__main__":
    print("Olá, iremos calcular o seu Índice de Massa Corporal (IMC), mas para isso, preciso que você me informe o seu peso "
          "(em kg) e sua altura (em metros). Bora lá?")
    input("Aperte ENTER para continuar...")
    
    peso = obter_numero("Digite seu peso: ")
    altura = obter_numero("Digite sua altura: ")
    
    imc, classificacao = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")
