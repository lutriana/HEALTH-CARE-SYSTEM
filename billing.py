from patientRegistration import Pacient

class Billing:
    def __init__(self ):
        self.payment = []
        self.data = Pacient()
    
    def add_payment(self, payment_method, dataPayment):
        self.payment = payment_method
        self.data = dataPayment