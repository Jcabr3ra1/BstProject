from Modelos.Transaccion import Transaccion
from Repositorios.RepositorioTransaccion import RepositorioTransaccion


class ControladorTransaccion():
    def __init__(self):
        self.RepositorioTransaccion = RepositorioTransaccion()


    def index(self):
        return self.RepositorioTransaccion.findAll()

    def create(self, infoTransaccion):
        nuevoTransaccion = Transaccion(infoTransaccion)
        return self.RepositorioTransaccion.save(nuevoTransaccion)

    def show(self, Transaction_id):
        elTransaction = Transaccion(self.RepositorioTransaccion.findById(Transaction_id))

        # Retorna los atributos del estudiante como un diccionario
        return elTransaction.__dict__

    def update(self, Transaction_id, infoTransaction):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        TransaccionActual = Transaccion(self.RepositorioTransaccion.findById(Transaction_id))
        # Actualiza los atributos del estudiante con la información recibida
        TransaccionActual.transaction_type = infoTransaction["Tipo_de_transaccion"]
        TransaccionActual.amount = infoTransaction["monto"]
        TransaccionActual.description = infoTransaction["descripcion"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.RepositorioTransaccion.save(TransaccionActual)

    def delete(self, Transaction_id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.RepositorioTransaccion.delete(Transaction_id)