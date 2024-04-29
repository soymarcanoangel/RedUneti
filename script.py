from flask import Flask, render_template

# Nombre de la aplicación
app = Flask(__name__)

# Rutas
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ingresar')
def ingresar():
	return render_template('ingresar.html')

@app.route('/registrarse')
def registrarse():
	return render_template('registrarse.html')

@app.route('/comunidad')
def comunidad():
	return render_template('comunidad.html')

@app.route('/uneti')
def uneti():
	return render_template('uneti.html')

@app.route('/cursos')
def cursos():
	return render_template('cursos.html')

@app.route('/contacto')
def contacto():
	return render_template('contacto.html')

# Inicializador
if __name__ == '__main__':
	app.run(debug=True)