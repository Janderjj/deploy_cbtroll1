from flask import Flask, jsonify, render_template, request
import buscanome
import json

app = Flask(__name__)
api_key = "RGAPI-5a8c30b5-d0bc-41c0-953f-788af715f5a7"
@app.route('/invocador', methods=['GET', 'POST']) 
def add_numbers():
    
    if request.method == 'POST':
        nomeinvocador = request.form['nome_invocador']
        tagname = request.form['tag_name']
        tagname = tagname[1:]
        retorno = buscanome.verificanome(nomeinvocador,tagname, api_key)
        #return str(retorno) 
    else:
      retorno=[]
      retorno.append("0")
    print(retorno)
    return retorno 

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/cadtorneio')
def cadtorneio():
    return render_template('cad_torneio.html')
if __name__ == "__main__":
    app.run(
        debug=True)
