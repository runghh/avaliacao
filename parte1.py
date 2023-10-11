
Produtos = []
def cadastrar_produtos(Produtos,nome,valor,qnt,taxadelucro,valordecusto,valordevenda,imposto1,impostos2,imposto3):
    produto ={
        'Nome' : nome,
        'Valorinicial' : valor,
        'Valorcusto' : valordecusto,
        'taxadelucro' : taxadelucro,
        'Valorvenda': valordevenda,
        'qnt' : qnt,
        'imposto1' : imposto1,
        'impostos2' :,
        'imposto3' : imposto3
    }

    Produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def imprimir_produtos(Produtos):
    for i,produto in enumerate(Produtos):
        print("ID:", i)
        print("Produto:", produto['Nome'])
        print("Valor inicial: R$", {produto['Valorinicial']})
        print("Valor com imposto e frete:R$",produto['Valorcusto'])
        print(f"Taxa de taxadelucro:", {produto['taxadelucro']*100}%)
        print(f"Preço de venda: R$", {produto['Valorvenda']})
        print(f"Quantidade:", {produto['qnt']})
        print("\n")  

if escolha == 1:
        nome = input("Digite o nome do produto: ")
        valor= int(input("Digite o valor do produto: "))
        qnt = int(input("Digite a quantidade de produtos: "))
    imposto1 = int(input("Digite a taxa de imposto 1 :"))
    imposto2 = int(input("Digite a taxa de imposto 2 :"))       
    imposto3 = int(input("Digite a taxa de imposto 3 :"))
    taxadelucro = int(input("Digite a taxa de taxadelucro:"))
    taxadelucro = taxadelucro/100
    imposto1 = imposto1/100
    =/100
    imposto3 = imposto3/100 
        
    valordecusto = valor+(valor*imposto1)+(valor*impostos2)+(valor*imposto3)+((1/qnt)*qnt)
    
    valordevenda = valordecusto+(valordecusto*taxadelucro)
    cadastrar_produtos(Produtos,nome,valor,qnt,taxadelucro,valordecusto,valordevenda,imposto1,impostos2,imposto3)
        
elif escolha == 2:
    imprimir_produtos(Produtos)