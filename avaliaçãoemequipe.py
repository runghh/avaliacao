
Produtos = []
def cadastrar_produtos(Produtos,nome,valor,qnt,lucro,valordecusto,valordevenda,imp1,imp2,imp3):
    produto ={
        'Nome' : nome,
        'Valorinicial' : valor,
        'Valorcusto' : valordecusto,
        'Lucro' : lucro,
        'Valorvenda': valordevenda,
        'qnt' : qnt,
        'imp1' : imp1,
        'imp2' : imp2,
        'imp3' : imp3
    }

    Produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def imprimir_produtos(Produtos):
    for i,produto in enumerate(Produtos):
        print(f"ID: {i}")
        print(f"Produto: {produto['Nome']}")
        print(f"Valor inicial: R${produto['Valorinicial']}")
        print(f"Valor com imposto e frete:R$ {produto['Valorcusto']:.2f}")
        print(f"Taxa de lucro:{produto['Lucro']*100}%")
        print(f"Preço de venda: R${produto['Valorvenda']}")
        print(f"Quantidade:{produto['qnt']}")
        print("\n")  

def atualizar_produto(Produtos,id,nome,valor,qnt,lucro,valordecusto,valordevenda,imp1,imp2,imp3):
        if id <= len(Produtos) and id < len(Produtos):
            Produtos[id]['Nome'] = nome
            Produtos[id]['Valorinicial'] = valor
            Produtos[id]['Valorcusto'] = valordecusto
            Produtos[id]['Lucro'] = lucro
            Produtos[id]['imp1'] = imp1
            Produtos[id]['imp2'] = imp2
            Produtos[id]['imp3'] = imp3
            Produtos[id]['Valorvenda'] = valordevenda
            Produtos[id]['qnt'] = qnt
        else:
            print("ID INVALIDO")

def deletar_produto(clientes,id):
    if 0<= id < len(clientes):
        del clientes[id]
        print("Produto apagado")
    else:
        print("ID inválido")

while True: 
    print("-------------------------------")
    print(" 1= CADASTRAR PRODUTO ")
    print(" 2= IMPRIMIR ESTOQUE ")
    print(" 3= ATUALIZAR PRODUTO ")
    print(" 4= DELETAR PRODUTO")
    print(" 5= FECHAR ")
    print("-------------------------------")
    escolha = int(input("Escolha uma opção:"))
    
    if escolha == 1:
        nome = input("Digite o nome do produto: ")
        valor= int(input("Digite o valor do produto: "))
        qnt = int(input("Digite a quantidade de produtos: "))
        imp1 = int(input("Digite a taxa de imposto 1 :"))
        imp2 = int(input("Digite a taxa de imposto 2 :"))       
        imp3 = int(input("Digite a taxa de imposto 3 :"))
        lucro = int(input("Digite a taxa de lucro:"))
        lucro = lucro/100
        imp1 = imp1/100
        imp2 = imp2/100
        imp3 = imp3/100 
        valordecusto = valor+(valor*imp1)+(valor*imp2)+(valor*imp3)+((1/qnt)*qnt)
        valordevenda = valordecusto+(valordecusto*lucro)
        cadastrar_produtos(Produtos,nome,valor,qnt,lucro,valordecusto,valordevenda,imp1,imp2,imp3)
        

    elif escolha == 2:
        imprimir_produtos(Produtos)
    elif escolha == 3:
        print("-------------ATUALIZAR PRODUTO-----------------")
        id = int(input("Digite o nome ID do produto: "))
        nome = input("Digite o nome do produto: ")
        valor= int(input("Digite o valor do produto: "))
        qnt = int(input("Digite a quantidade de produtos: "))
        imp1 = int(input("Digite a taxa de imposto 1 :"))
        imp2 = int(input("Digite a taxa de imposto 2 :"))       
        imp3 = int(input("Digite a taxa de imposto 3 :"))
        lucro = int(input("Digite a taxa de lucro:"))   
        lucro = lucro/100
        imp1 = imp1/100
        imp2 = imp2/100
        imp3 = imp3/100 
        valordecusto = valor+(valor*imp1)+(valor*imp2)+(valor*imp3)+((1/qnt)*qnt)
        valordevenda = valordecusto+(valordecusto*lucro)
        atualizar_produto(Produtos,id,nome,valor,qnt,lucro,valordecusto,valordevenda,imp1,imp2,imp3)


    elif escolha == 4:
        print("----------DELETAR PRODUTO-------------")
        id = int(input("Digite o id:"))
        deletar_produto(Produtos,id)

    elif escolha == 5:
        break

    else:
        print("Escolha Invalida")
        print("\n")