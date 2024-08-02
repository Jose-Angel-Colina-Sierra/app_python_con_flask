#API  e um lugar para disponibilizar recursos ou funcionalidades
# 1. Objetivo - Criar um API que disponibiliza a consulta, criacao, modificacao e exclusao de livros.

# 2. URL Base - localhost

# 3. Endpoints - 
# localHost/livros (GET)
# localHost/livros (POST)
# localHost/livros/ID (GET com ID)
# localHost/livros/ID (PUT com ID)
# localHost/livros/ID (delete com ID)

# 4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': "O Senhor Dos Anéis A Sociedade Do Anel",
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': "Cem anos de solidão",
        'autor': 'Gabriel Garcia Marquez'
    },
    {
        'id': 3,
        'titulo': "To Kill a Mockingbird",
        'autor': 'Harper Lee'
    },
]

# Consultar(Todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(ID)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    return jsonify({'message': 'Livro não encontrado'}), 404

# Editar(ID)
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({'message': 'Livro não encontrado'}), 404

# Criar(ID)

@app.route("/livros", methods=['POST'])

def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# Deletar(ID)
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)