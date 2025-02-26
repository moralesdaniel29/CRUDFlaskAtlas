from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from product import Product
from client import Client 
from prov import Prov

db = dbase.dbConnection()

app = Flask(__name__)

# Rutas de la aplicación
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/productos")
def algo():
    products = db['products']
    productsReceived = products.find()
    return render_template("productos.html", products = productsReceived) 

# Method Post 
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        product = Product(name, price, quantity)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'price' : price,
            'quantity' : quantity
        })
        return redirect(url_for('algo'))
    else:
        return notFound()

# Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('algo'))

# Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'price' : price, 'quantity' : quantity}})
        response = jsonify({'message' : 'Producto' + product_name + ' actualizado correctamente'})
        return redirect(url_for('algo'))
    else:
        return notFound()




@app.route("/clientes")
def clientView():
    clients = db['clients']  # Accede a la colección de clientes en la base de datos
    clientsReceived = clients.find()  # Obtiene los clientes de la BD
    return render_template("clientes.html", clients=clientsReceived)  # Renderiza la plantilla con los datos


# Method Post 
@app.route('/clients', methods=['POST'])
def addClient():
    clients = db['clients']
    fullName = request.form['fullName']
    email = request.form['email']
    direction = request.form['direction']
    note = request.form['note']

    if fullName and email and direction and note:
        client = Client(fullName, email, direction, note)
        clients.insert_one(client.toDBCollection())
        response = jsonify({
            'fullName' : fullName,
            'email' : email,
            'direction' : direction,
            'note' : note
        })
        return redirect(url_for('clientView'))
    else:
        return notFound()

# Method delete
@app.route('/deleteClient/<string:client_name>')
def deleteClient(client_name):
    clients = db['clients']
    clients.delete_one({'fullName' : client_name})
    return redirect(url_for('clientView'))

# Method Put
@app.route('/editClient/<string:client_name>', methods=['POST'])
def editClient(client_name):
    clients = db['clients']
    fullName = request.form['fullName']
    email = request.form['email']
    direction = request.form['direction']
    note = request.form['note']


    if fullName and email and direction and note:
        clients.update_one({'fullName' : client_name}, {'$set' : {'fullName' : fullName, 'email' : email, 'direction' : direction, 'note' : note}})
        response = jsonify({'message' : 'Client' + client_name + ' actualizado correctamente'})
        return redirect(url_for('clientView'))
    else:
        return notFound()







@app.route("/proveedores")
def provView():
    provs = db['provs']  # Accede a la colección de clientes en la base de datos
    provsReceived = provs.find()  # Obtiene los clientes de la BD
    return render_template("proveedores.html", provs=provsReceived)  # Renderiza la plantilla con los datos


# Method Post 
@app.route('/provs', methods=['POST'])
def addProv():
    provs = db['provs']
    namePro = request.form['namePro']
    email = request.form['email']
    direction = request.form['direction']
    phone = request.form['phone']

    if namePro and email and direction and phone:
        prov = Prov(namePro, email, direction, phone)
        provs.insert_one(prov.toDBCollection())
        response = jsonify({
            'namePro' : namePro,
            'email' : email,
            'direction' : direction,
            'phone' : phone
        })
        return redirect(url_for('provView'))
    else:
        return notFound()

# Method delete
@app.route('/deleteProv/<string:prov_name>')
def deleteProv(prov_name):
    provs = db['provs']
    provs.delete_one({'namePro' : prov_name})
    return redirect(url_for('provView'))

# Method Put
@app.route('/editProv/<string:prov_name>', methods=['POST'])
def editProv(prov_name):
    provs = db['provs']
    namePro = request.form['namePro']
    email = request.form['email']
    direction = request.form['direction']
    phone = request.form['phone']


    if namePro and email and direction and phone:
        provs.update_one({'namePro' : prov_name}, {'$set' : {'namePro' : namePro, 'email' : email, 'direction' : direction, 'phone' : phone}})
        response = jsonify({'message' : 'Prov' + prov_name + ' actualizado correctamente'})
        return redirect(url_for('provView'))
    else:
        return notFound()












@app.errorhandler(404)
def notFound(error):
    """ message = {
        'message' : 'No encontrado ' + request.url,
        'status' : '404 Not Found'
    }"""
    response = (error)
    response.status_code = 404
    return response 

if __name__ == '__main__':
    app.run(debug=True, port=4000)