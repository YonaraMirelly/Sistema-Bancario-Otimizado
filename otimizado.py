from time import sleep

def menu():
    menu = '''
    ----------MENU----------
    [D] Depositar
    [S] Sacar 
    [E] Extrato
    [NC] Nova Conta
    [LC] Listar Contas
    [NU] Novo Usuário
    [SAIR] Para Sair
    ------------------------
-> '''
    return input(menu)

def bonitinho():
    print('='*50)

def Depositar(saldo, valor, extrato, /):
    if valor>0:
        saldo+=valor
        extrato += f'depósito: R${valor:.2f}'
        bonitinho()
        print(f'R${valor} depositado com sucesso!!!')
        bonitinho()
    else:
        print('Falha na operação! informe valores válidos, por favor!')

    return saldo, extrato

def Saque(*, saldo, valor, extrato, limite, numero_saque, limite_saque):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque >= limite_saque

    
    if excedeu_saldo:
        print('\033[1;31mVocê não tem saldo o suficiente!\033[m')
    elif excedeu_limite:
        print("\033[1;31mO valor do saque excede o limite de R$500!\033[m")
    elif excedeu_saques:
        print('\033[1;31mNúmero máximo de saque (3) excedido!\033[m')

    elif valor >0:
        saldo-=valor
        extrato += f"Saque: R${valor:.2f}.\n"
        numero_saque +=1
        bonitinho()
        print(f'Saque de R${valor} retirado com sucesso!')
        bonitinho()
    else:
        print('\033[1;31mOperação falhou!\033[m O valor informado é inválido!')

    return saldo, extrato

def Extrato(saldo, /, *, extrato):
    print('==========EXTRATO==========')
    print(f'SAlDO -> R$ {saldo:.2f}')
    print('===========================')

def usuario(usuarios):
    cpf = input("Digite o seu cpf [APENAS NÚMEROS]: ")
    usuario = analisar_usuario(cpf, usuarios)

    if usuario:
        bonitinho()
        print(f"O cpf{cpf} já está registrado!")
        bonitinho()
        return
    
    nome = input('Diga seu nome completo: ')
    data = input('Diga sua data de nascimento [00/00/0000]: ')
    endereço = input('Diga o seu endereço: [logradouro, nro - bairro - cidade/silga estado]: ')
    usuarios.append({'nome': nome, 'data': data, 'endereço': endereço, 'cpf': cpf})
    bonitinho()
    print('Você foi cadastrado(a) com sucesso!')
    bonitinho()

def analisar_usuario(cpf, usuarios):
    usuarios_analisados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_analisados[0] if usuarios_analisados else None 

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o cpf do usuário: ')
    usuario = analisar_usuario(cpf, usuarios)

    if usuario:
        bonitinho()
        print('Conta criada com sucesso!!!')
        bonitinho()
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('Esse usuário NÃO existe.')

def lista_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            Conta: {conta['numero_conta']}
            Títular: {conta['usuario']['nome']}
"""
        bonitinho()
        print(linha)

def principal():
    Agencia = '0001'
    Limites_Saques = 3
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []

    while True:
        opçao = menu()

        if opçao == 'D':
            valor = float(input("Diga o valor do depósito: "))
            saldo, extrato  = Depositar(saldo, valor, extrato)

        elif opçao == 'S':
            valor = float(input("Diga o valor do saque: "))
            
            saldo, extrato  = Saque (
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saque = numero_saque,
                limite_saque = Limites_Saques,
            ) 
        
        elif opçao == "E":
            Extrato(saldo, extrato=extrato)
        
        elif opçao == 'NU':
            usuario(usuarios)

        elif opçao == 'NC':
            numero_conta = len(contas)+1
            conta = criar_conta(Agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opçao == 'LC':
            lista_contas(contas)
        
        elif opçao == "SAIR":
            bonitinho()
            print('Encerrando...')
            sleep(1.5)
            print('Até a próxima!')
            break
            
principal()