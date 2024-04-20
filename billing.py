from patientRegistration import Pacient

class Billing:
    """
    Representa un sistema de facturación que gestiona los pagos y los asocia con
    pacientes específicos.
    """
    
    def _init_(self):
        """
        Inicializa el sistema de facturación con una lista vacía para pagos y
        un marcador de posición para los datos de los pacientes.
        """
        self.payment = []
        self.data = Pacient()
    
    def add_payment(self, payment_method, dataPayment):
        """
        Registra un nuevo pago en el sistema.
        
        Args:
            payment_method (str): Método a través del cual se realizó el pago.
            dataPayment (Pacient): Datos del paciente asociados con el pago.
        """
        self.payment.append(payment_method)
        self.data = dataPayment
