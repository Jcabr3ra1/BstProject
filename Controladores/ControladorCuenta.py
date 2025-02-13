from Modelos.Cliente import Cliente
from Modelos.Cuenta import Cuenta
from Modelos.DepartamentodeBanco import DepartamentodeBanco
from Repositorios.RepositorioCuenta import RepositorioCuenta
from Repositorios.RepositorioCliente import RepositorioCliente
from Repositorios.RepositorioDepartamentodeBanco import RepositorioDepartamentodeBanco


class ControladorCuenta():
    def __init__(self):
        self.RepositorioCuenta = RepositorioCuenta()
        self.RepositorioCliente = RepositorioCliente()
        self.RepositorioDepartamentodeBanco = RepositorioDepartamentodeBanco

    def index(self):
        return self.RepositorioCuenta.findAll()

    def create(self, infoCuenta):
        nuevoCuenta = Cuenta(infoCuenta)
        return self.RepositorioCuenta.save(nuevoCuenta)

    def show(self, Account_id):
        laCuenta = Cuenta(self.RepositorioCuenta.findById(Account_id))

        # Retorna los atributos del estudiante como un diccionario
        return laCuenta.__dict__

    def update(self, Account_id, infoCuenta):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        cuentaActual = Cuenta(self.RepositorioCuenta.findById(Account_id))
        # Actualiza los atributos del estudiante con la información recibida
        cuentaActual.account_number = infoCuenta["numero_de_cuenta"]
        cuentaActual.balance = infoCuenta["balance"]
        cuentaActual.account_type = infoCuenta["tipo_de_cuenta"]


        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.RepositorioCuenta.save(cuentaActual)

    def delete(self, Account_id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.RepositorioCuenta.delete(Account_id)

    """
           Relación cuenta y cliente
    """

    def asignarCliente(self, Account_id, client_id):
        # Obtiene la materia actual por su ID desde la base de datos utilizando el repositorio
        cuentaActual = Cuenta(self.RepositorioCuenta.findById(Account_id))

        # Obtiene el departamento actual por su ID desde la base de datos utilizando el repositorio
        clienteActual = Cliente(self.RepositorioCliente.findById(client_id))

        # Asigna el departamento actual a la materia actual
        cuentaActual.Cliente = clienteActual

        # Guarda los cambios de la materia actualizada en la base de datos utilizando el repositorio
        return self.RepositorioCuenta.save(cuentaActual)

    """
               Relación cuenta y Departamento de banco
    """

    def asignarDepartamentodeBanco(self, Account_id, DepartamentodeBanco_id):
        # Obtiene la materia actual por su ID desde la base de datos utilizando el repositorio
        cuentaActual = Cuenta(self.RepositorioCuenta.findById(Account_id))

        # Obtiene el departamento actual por su ID desde la base de datos utilizando el repositorio
        DepartamentodeBancoActual = DepartamentodeBanco(self.RepositorioDepartamentodeBanco.findById(DepartamentodeBanco_id))

        # Asigna el departamento actual a la materia actual
        cuentaActual.DepartamentodeBanco = DepartamentodeBancoActual

        # Guarda los cambios de la materia actualizada en la base de datos utilizando el repositorio
        return self.RepositorioCuenta.save(cuentaActual)
    
