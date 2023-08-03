def menu():
    menu = """
    ===== MENU =====
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuário
    [c] Criar Conta Corrente
    [l] Listar Contas
    [q] Sair
    ================
    => """
    return input(menu)


def depositar(saldo, list_dep, /):
    dep = float(input("Digite quanto deseja depositar: "))
    while dep <= 0:
        dep = float(input(f"Operação Inválida. Digite quanto deseja depositar: "))
    saldo += dep
    list_dep.append(dep)
    
    return saldo, list_dep


def sacar(*, saldo, limite, numero_saques, LIMITE_SAQUES, list_saq):
    if numero_saques == LIMITE_SAQUES:
        print("Limite de saques diários atingido")
    else:
        saq = float(input("Digite quanto deseja sacar: "))
        while (saq <= 0 or saq > saldo or saq > limite):
            if saq > saldo:
                saq = float(input("Saldo insuficiente. Digite novo valor: "))
            elif saq > limite:
                saq = float(input(f"Valor acima do máximo de R${limite}.00 permitido por saque. Digite novo valor: "))
            else:
                saq = float(input("Operação Inválida. Digite quanto deseja sacar: "))
        saldo -= saq
        numero_saques += 1
        list_saq.append(saq)

    return saldo, numero_saques, list_saq


def extrato(saldo, /, *, list_dep, list_saq):
    print("\n===== EXTRATO =====\n")
    
    if len(list_dep) == 0 and len(list_saq) == 0:
        print("Não foram realizadas movimentações")
    else:
        print("Depósitos: ")
        for i in range(len(list_dep)):
            print(f"R${list_dep[i]:.2f}")
        
        print("\nSaques: ")
        for j in range(len(list_saq)):
            print(f"R${list_saq[j]:.2f}")
    
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("================")


def criar_usuario(usuario):
    print("\n========== CRIAR USUÁRIO ==========\n")
    nome = input("Nome: ").title()
    data_nasc = input("Data de Nascimento (DD/MM/AAAA): ").replace("-", "/")
    cpf = str(input("CPF: ")).replace(".", "").replace("-", "")
    while cpf in usuario:
        print("CPF Inválido. Digite novamente\n")
        cpf = str(input("CPF: ")).replace(".", "").replace("-", "")
    #Endereço
    logradouro = input("\n========== Endereço ==========\n\nLogradouro, nº: ").title()
    bairro = input("Bairro: ").title()
    cidade = input("Cidade: ").title()
    estado = input("Estado (sigla): ").upper()
    while estado not in sigla_estados:
        print("Estado Inválido. Digite novamente\n")
        estado = input("Estado (sigla): ").upper()
    print("\n==============================\n")
    endereco = (f"{logradouro} - {bairro} - {cidade}/{estado}")
    
    usuario[cpf] = [nome, data_nasc, endereco]
    
    return usuario


def conta_corrente(usuario, agencia, nro_conta, dic_contas):
    cpf = str(input("Digite CPF do usuário a ser vinculado a uma conta corrente: ")).replace(".", "").replace("-", "")
    while cpf not in usuario:
        print("CPF Inválido. Digite novamente\n")
        cpf = str(input("CPF: ")).replace(".", "").replace("-", "")
    conta = [agencia, nro_conta, usuario[cpf][0]]
    dic_contas[nro_conta] = conta
    nro_conta += 1

    return nro_conta, dic_contas


def listar_contas(dic_contas):
    print("=" * 50)
    for conta, conta_values in dic_contas.items():
        print(f"\nAgência: {conta_values[0]}\nConta Corrente: {conta_values[1]}\nCliente: {conta_values[2]}\n")
        print("=" * 50)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001" #mesma agência para todos os usuários

    nro_conta = 1 #número da conta corrente é sequencial e começa em "1"
    saldo = 0
    limite = 500
    numero_saques = 0
    opcao = ""
    list_dep = [] #lista onde será armazenado todos os depósitos realizados
    list_saq = [] #lista onde será armazenado todos os saques realizados
    usuario = {} #dicionário onde será armazenado {CPF: [nome, data de nascimento, endereço]}
    dic_contas = {} #dicionário onde será armazenado {CPF: [agência, número da conta, [nome, data de nascimento, endereço]]}
    global sigla_estados
    sigla_estados = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", 
            "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
    
    while opcao != "q":

        opcao = menu()
        while opcao not in "dseuclq":
            opcao = input(f"Operação inválida. Por favor selecione novamente a operação desejada.\n{menu()}").lower()

        if opcao == "d":
            saldo, list_dep = depositar(saldo, list_dep)

        elif opcao == "s":
            saldo, numero_saques, list_saq = sacar(saldo=saldo, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES, list_saq=list_saq)

        elif opcao == "e":
            extrato(saldo, list_dep=list_dep, list_saq=list_saq)
        
        elif opcao == "u":
            usuario = criar_usuario(usuario)

        elif opcao == "c":
            nro_conta, dic_contas = conta_corrente(usuario, AGENCIA, nro_conta, dic_contas)

        elif opcao == "l":
            listar_contas(dic_contas)

        else:
            break


main()