from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    area = None
    figura = None

    if request.method == 'POST':
        figura = request.form['figura']

        try:
            if figura == 'circulo':
                radio = float(request.form['radio'])
                area = math.pi * (radio ** 2)
            
            elif figura == 'cuadrado':
                lado = float(request.form['lado'])
                area = lado ** 2
            
            elif figura == 'triangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                area = (base * altura) / 2

        except ValueError:
            area = "Error: Ingrese valores numéricos válidos."

    return render_template('index3.html', area=area, figura=figura)

if __name__ == '__main__':
    app.run(debug=True)
