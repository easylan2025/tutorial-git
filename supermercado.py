nome_produto = input('nome do produto: ').lower().strip()
categoria = input('qual a caegoria do produto: ').lower().strip()
estoque_produto = int(input('qual a quantidade disponivel: '))
estoque_atual= nome_produto

dolly = 500
coca = 800
peixe = 5080
arroz = 18
bombril = 900
assolan = 49


if categoria == "alimentos" and estoque_produto > 50:
    if nome_produto == 'peixe':
        print('a venda de peixe foi confirmada')
    elif nome_produto == 'arroz':
        print('a venda foi arroz confirmada')

elif categoria == "bebidas" and estoque_produto > 75:
    if nome_produto == 'dolly':
        print('a venda de dolly foi confirmada')
    elif nome_produto == 'coca':
        print('a venda de coca foi confirmada')

elif categoria == "limpeza" and estoque_produto > 30:
    if nome_produto == 'assolan':
        print('a venda de assolan foi confirmada')
    elif nome_produto == 'bombril':
        print('a venda foi bombri foi confirmada')
else:
    estoque_atual = locals().get(nome_produto, "desconhecido")
    print(f"solicitar a equipe de compras: {nome_produto}, estoque atual: {estoque_atual}")
