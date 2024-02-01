# Calculadora de Operações Básicas

continuar_usando = 'SIM'

while continuar_usando == 'SIM':
    # Criando um menu de opções
    print("SELECIONE A OPÇÃO DESEJADA")
    print("+ para Adição")
    print("- para subtração")
    print("* para Multiplicação")
    print("/ para Divisão")

    # Interação com o usuário
    operacao = input("\nQual operação você deseja realizar? ")

    # Criando as operações e as apresentações de respotas

    # Adição
    if operacao == '+':
        a1 = int(input("\nDigite o primeiro valor: "))
        a2 = int(input("Digite o segundo valor: "))
        adicao = a1 + a2
        print("\nA soma entre", a1, "e", a2, "é:", adicao,"\n")
        print("*"*33,"\n")
        continuar_usando = input("Gostaria de fazer outra operação? ").upper()
        print("*"*33,"\n")

    # Subtração
    if operacao == '-':
        s1 = int(input("\nDigite o primeiro valor: "))
        s2 = int(input("Digite o segundo valor: "))
        adicao = s1 - s2
        print("\nA soma entre", s1, "e", s2, "é:", adicao,"\n")
        print("*"*33,"\n")
        continuar_usando = input("Gostaria de fazer outra operação? ").upper()
        print("*"*33,"\n")

    # Multiplicação
    if operacao == '*':
        m1 = int(input("\nDigite o primeiro valor: "))
        m2 = int(input("Digite o segundo valor: "))
        adicao = m1 * m2
        print("\nA soma entre", m1, "e", m2, "é:", adicao,"\n")
        print("*"*33,"\n")
        continuar_usando = input("Gostaria de fazer outra operação? ").upper()
        print("*"*33,"\n")

    # Divisão
    if operacao == '/':
        d1 = float(input("\nDigite o primeiro valor: "))
        d2 = float(input("Digite o segundo valor: "))
        adicao = d1 / d2
        print("\nA soma entre", d1, "e", d2, "é:", adicao,"\n")
        print("*"*33,"\n")
        continuar_usando = input("Gostaria de fazer outra operação? ").upper()
        print("*"*33,"\n")
