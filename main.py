from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCliente import ControladorCliente
from Controladores.ControladorCuenta import ControladorCuenta
from Controladores.ControladorDepartamentodeBanco import ControladorDepartamentodeBanco

app = Flask(__name__)
cors = CORS(app)


miControladorCliente=ControladorCliente()
miControladorCuenta=ControladorCuenta()
miControladordepartamentodeBanco=ControladorDepartamentodeBanco()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

###########################################Cliente##################################################################

@app.route("/cliente",methods=['GET'])
def getClientes():
    json=miControladorCliente.index()
    return jsonify(json)

@app.route("/cliente",methods=['POST'])
def crearCliente():
    data = request.get_json()
    json=miControladorCliente.create(data)
    return jsonify(json)

@app.route("/cliente/<string:client_id>",methods=['GET'])
def getCliente(client_id):
    json=miControladorCliente.show(client_id)
    return jsonify(json)

@app.route("/cliente/<string:client_id>",methods=['PUT'])
def modificarCliente(client_id):
    data = request.get_json()
    json=miControladorCliente.update(client_id,data)
    return jsonify(json)

@app.route("/cliente/<string:client_id>",methods=['DELETE'])
def eliminarCliente(client_id):
    json=miControladorCliente.delete(client_id)
    return jsonify(json)

###########################################Cuenta##################################################################

@app.route("/cuenta",methods=['GET'])
def getCuentas():
    json=miControladorCuenta.index()
    return jsonify(json)

@app.route("/cuenta",methods=['POST'])
def crearCuenta():
    data = request.get_json()
    json=miControladorCuenta.create(data)
    return jsonify(json)

@app.route("/cuenta/<string:Account_id>",methods=['GET'])
def getCuenta(Account_id):
    json=miControladorCuenta.show(Account_id)
    return jsonify(json)

@app.route("/cuenta/<string:Account_id>",methods=['PUT'])
def modificarCuenta(Account_id):
    data = request.get_json()
    json=miControladorCuenta.update(Account_id,data)
    return jsonify(json)

@app.route("/cuenta/<string:Account_id>",methods=['DELETE'])
def eliminarCuenta(Account_id):
    json=miControladorCuenta.delete(Account_id)
    return jsonify(json)

@app.route("/cuenta/<string:Account_id>/cliente/<string:client_id>",methods=['PUT'])
def asignarClienteACuenta(Account_id,client_id):
    json=miControladorCuenta.asignarCliente(Account_id,client_id)
    return jsonify(json)

@app.route("/cuenta/<string:Account_id>/departamentodeBanco/<string:departamentodeBanco_id>",methods=['PUT'])
def asignarasignarDepartamentodeBancoACuenta(Account_id,departamentodeBanco_id):
    json=miControladorCuenta.asignarasignarDepartamentodeBancoACuenta(Account_id,departamentodeBanco_id)
    return jsonify(json)


###########################################DepartamentodeBanco##################################################################

@app.route("/departamentodeBanco",methods=['GET'])
def getdepartamentodeBancos():
    json=miControladordepartamentodeBanco.index()
    return jsonify(json)

@app.route("/departamentodeBanco",methods=['POST'])
def creardepartamentodeBanco():
    data = request.get_json()
    json=miControladordepartamentodeBanco.create(data)
    return jsonify(json)

@app.route("/departamentodeBanco/<string:departamentodeBanco_id>",methods=['GET'])
def getdepartamentodeBanco(departamentodeBanco_id):
    json=miControladordepartamentodeBanco.show(departamentodeBanco_id)
    return jsonify(json)

@app.route("/departamentodeBanco/<string:departamentodeBanco_id>",methods=['PUT'])
def modificardepartamentodeBanco(departamentodeBanco_id):
    data = request.get_json()
    json=miControladordepartamentodeBanco.update(departamentodeBanco_id,data)
    return jsonify(json)

@app.route("/departamentodeBanco/<string:departamentodeBanco_id>",methods=['DELETE'])
def eliminardepartamentodeBanco(departamentodeBanco_id):
    json=miControladordepartamentodeBanco.delete(departamentodeBanco_id)
    return jsonify(json)

###########################################Transaccion##################################################################

# Obtener todas las transacciones
@app.route("/transaccion", methods=['GET'])
def getTransacciones():
    json = miControladortransaccion.obtener_todas_las_transacciones()
    return jsonify(json)

# Crear una transacción (realizar transferencia)
@app.route("/transaccion", methods=['POST'])
def crearTransaccion():
    data = request.get_json()
    json = miControladortransaccion.transferir(data["cuentaOrigen"], data["cuentaDestino"], data["monto"])
    return jsonify(json)

# Obtener una transacción específica
@app.route("/transaccion/<string:Transaction_id>", methods=['GET'])
def getTransaccion(Transaction_id):
    json = miControladortransaccion.obtener_transaccion(Transaction_id)
    return jsonify(json)

# Actualizar estado de una transacción
@app.route("/transaccion/<string:Transaction_id>", methods=['PUT'])
def modificarTransaccion(Transaction_id):
    data = request.get_json()
    json = miControladortransaccion.actualizar_estado_transaccion(Transaction_id, data["estado"])
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
