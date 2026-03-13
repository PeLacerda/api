from flask import Flask, jsonify
import os

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Scarface"},
    {"id": 2, "nome": "Gente Grande 2"},
    {"id": 3, "nome": "A espera de um milagre"},
]

@app.route("/alunos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Alunos - Acesse /alunos"})

@app.route("/", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)