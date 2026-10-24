from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo='BIBLIOTECA SABER Y CONOCIMIENTO',mensaje='¡Bienvenidos a la Biblioteca Saber y Conocimiento! 📚 Nos alegra recibirte en un espacio dedicado al aprendizaje, la lectura y el descubrimiento de nuevas ideas')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', titulo='BIBLIOTECA',mensaje='')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='BIBLIOTECA',mensaje='')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='BIBLIOTECA',mensaje='')

if __name__ == '__main__':
    app.run(debug=True, port=5050)
