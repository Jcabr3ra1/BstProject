from Modelos.DepartamentodeBanco import DepartamentodeBanco
from Repositorios.RepositorioDepartamentodeBanco import RepositorioDepartamentodeBanco


class ControladorDepartamentodeBanco():
    def __init__(self):
        self.RepositorioDepartamentodeBanco = RepositorioDepartamentodeBanco()


    def index(self):
        return self.RepositorioDepartamentodeBanco.findAll()

    def create(self, infoDepartamentodeBanco):
        nuevoDepartamentodeBanco = DepartamentodeBanco(infoDepartamentodeBanco)
        return self.RepositorioDepartamentodeBanco.save(nuevoDepartamentodeBanco)

    def show(self, departamentodeBanco_id):
        elDepartamentodeBanco = DepartamentodeBanco(self.RepositorioDepartamentodeBanco.findById(departamentodeBanco_id))

        # Retorna los atributos del estudiante como un diccionario
        return elDepartamentodeBanco.__dict__

    def update(self, departamentodeBanco_id, infoDepartamentodeBanco):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        DepartamentodeBancoActual = DepartamentodeBanco(self.RepositorioDepartamentodeBanco.findById(departamentodeBanco_id))
        # Actualiza los atributos del estudiante con la información recibida
        DepartamentodeBancoActual.name = infoDepartamentodeBanco["nombre"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.RepositorioDepartamentodeBanco.save(DepartamentodeBancoActual)

    def delete(self, departamentodeBanco_id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.RepositorioDepartamentodeBanco.delete(departamentodeBanco_id)