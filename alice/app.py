from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ

def obter_produtos():
    # 1. Abrir o arquivo
    with open("produtos.csv", "r") as file:
        lista_produtos = []
        # 2. Ler o arquivo (cada linha)
        for linha in file:
            # 3. Quebrar a linha na vírgula ['Coca-cola', 'dsadas', '10', 'coca.jpg']
            nome, descricao, preco, imagem = linha.strip().split(",")
            # 4. Montar o dicionário com os valores da lista
            produto = {
                "nome": nome,
                "descricao": descricao,
                "preco": float(preco),
                "imagem": imagem
            }
            lista_produtos.append(produto)
        return lista_produtos
    
def adicionar_produto(produto):
    linha = f"\n{produto['nome']}, {produto['descricao']}, {produto['preco']}, {produto['imagem']}"
    with open("produtos.csv", 'a') as file:
        file.write(linha)
        

# lista_produtos = [
#     { "nome": "Coca-cola", "descricao": "bom", "preco": "5.99", "imagem": "https://images.tcdn.com.br/img/img_prod/948333/coca_cola_290ml_c24_769_1_eac646cd43dbe5f0b415423f9887f599.png"},
#     { "nome": "Doritos", "descricao": "suja mao", "preco": "8,99", "imagem": "https://atacadaobr.vtexassets.com/arquivos/ids/252509/g.jpg?v=638353972719200000"},
#     { "nome": "Chocolate", "descricao": "bom", "preco": "10,99", "imagem": "https://images.tcdn.com.br/img/img_prod/907279/barra_de_chocolate_ao_leite_oreo_100g_8629_1_1bba077622edae3b68daebf755ca4443.jpg"},
# ]

app = Flask(__name__)

# todo aplicativo tem essa dupla:
# rota e função

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template('produtos.html', produtos=obter_produtos())

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in obter_produtos():
        if produto["nome"].lower() == nome.lower():
            return render_template("produto.html", produto=produto)
        
    return "produto não encontrado"

#GET
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

#POST
@app.route("/produtos", methods = ["POST"])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']
    produto = {"nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
    adicionar_produto(produto)

    return redirect(url_for("produtos"))

@app.route("/gerarcpf")
def gerar_cpf():
    cpf = CPF()
    new_cpf = cpf.generate()
    return render_template('gerar-cpf.html', show_cpf=new_cpf)

@app.route("/gerarcnpj")
def gerar_cnpj():
    cnpj = CNPJ()
    new_cnpj = cnpj.generate()
    return render_template('gerar-cnpj.html', show_cnpj=new_cnpj)

app.run(port=5001)