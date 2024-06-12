from flask import Flask, render_template

lista_produtos = [
    { "nome": "Coca-cola", "descricao": "bom"},
    { "nome": "Doritos", "descricao": "suja mao"},
    { "nome": "Chocolate", "descricao": "bom"},
]

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
    return render_template('produtos.html', produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto["nome"].lower() == nome.lower():
            return render_template("produto.html", produto=produto)
        
    return "produto não encontrado"