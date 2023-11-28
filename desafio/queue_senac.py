from flask import Flask, jsonify, request, render_template
import random
from fila import Fila, FilaService
app = Flask(__name__)

fila = Fila();
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/mostrar-fila', methods=['GET'])
def mostrarFila():
   '''Mostra todos os elementos da fila'''
   return jsonify(fila.__str__()), 200

@app.route('/start_processing', methods=['POST'])
def start_queue_senac():
    '''Adiciona número aleatório de 0 até 9 na fila'''
    number = random.randint(0,9)
    fila.inserir(number)
    print(number, flush=True) 
    return '', 200

@app.route('/pos_processing', methods=['POST'])
def processing_queue_senac():
    '''Recuperar o número da fila'''
    elemento =  request.get_json() #Pegando o json vindo do post
    numero = int(elemento['numero']); # Convertendo o valor json do campo número de string para inteiro
    response = FilaService.recoverElemento(fila, numero)
    print("Pos_Processing", flush=True)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=__debug__)