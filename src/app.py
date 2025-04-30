from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html',titulo='Bienvenido a la aplicación de facturación')

@app.route('/lista_productos')
def lista_productos():
    return render_template('lista_productos.html',titulo='Ver productos')

@app.route('/formulario_producto')
def formulario_producto():
    return render_template('formulario_producto.html',titulo='Crear producto')

@app.route('/lista_cliente')
def lista_cliente():
    return render_template('lista_cliente.html',titulo='Ver clientes')   

@app.route('/formulario_cliente')
def formulario_cliente():
    return render_template('formulario_cliente.html',titulo='Crear cliente')
   
@app.route('/lista_usuario')    
def lista_usuario():
    return render_template('lista_usuario.html',titulo='Ver usuarios')

@app.route('/formulario_usuario')
def formulario_usuario():
    return render_template('formulario_usuario.html',titulo='Crear usuario')   

@app.route('/formulario_factura')
def formulario_factura():
    return render_template('formulario_factura.html',titulo='Facturas')   



