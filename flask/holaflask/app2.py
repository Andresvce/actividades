from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    numero = None
    resultado=[]

    if request.method == 'POST':
        try:
            numero = int(request.form['numero'])
            resultado= [(numero, i, numero*i)  for i in range(1, 11)]
        except ValueError:
            tabla = ["Error: Ingrese un número válido."]        

    return render_template('index2.html', resultado=resultado, numero=numero)

if __name__ == '__main__':
    app.run(debug=True)
