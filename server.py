from flask import Flask, render_template, request, redirect, url_for

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo='Ejemplo',mensaje='¡Bienvenido a nuestro sitio web!')
@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', titulo="Proyecto",mensaje='')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Proyecto',mensaje='')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Proyecto',mensaje='')

if __name__ == '__main__':
    app.run(debug=True, port=5050)
