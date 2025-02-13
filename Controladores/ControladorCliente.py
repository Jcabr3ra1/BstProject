from Modelos.Cliente import Cliente
from Repositorios.RepositorioCliente import RepositorioCliente


class ControladorCliente():
    def __init__(self):
        self.RepositorioCliente = RepositorioCliente()


    def index(self):
        return self.RepositorioCliente.findAll()

    def create(self, infoCliente):
        nuevoCliente = Cliente(infoCliente)
        return self.RepositorioCliente.save(nuevoCliente)

    def show(self, client_id):
        cliente_data = self.RepositorioCliente.findById(client_id)

        if not cliente_data:
            return None  # Retorna None si el cliente no existe

        elCliente = Cliente(cliente_data)
        return elCliente.__dict__

    def update(self, client_id, infoCliente):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        clienteActual = Cliente(self.RepositorioCliente.findById(client_id))
        # Actualiza los atributos del estudiante con la información recibida
        clienteActual.first_name = infoCliente["nombre"]
        clienteActual.last_name = infoCliente["apellido"]
        clienteActual.national_id = infoCliente["Identificacion"]
        clienteActual.email = infoCliente["Email"]
        clienteActual.phone = infoCliente["Telefono"]
        clienteActual.address = infoCliente["Direccion"]
        clienteActual.city = infoCliente["Ciudad"]
        clienteActual.country = infoCliente["Pais"]
        clienteActual.customer_status = infoCliente["Estado_del_cliente"]


        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.RepositorioCliente.save(clienteActual)

    def delete(self, client_id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.RepositorioCliente.delete(client_id)

