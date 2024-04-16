from patientRegistration import ClinicHistory
"""
el provedor de servicios tiene acceso a los resultados de lab e imagenes
NOTA: relacionar atributos especificos a los provedores de servicios

"""
class ServicesProvider:
    def __init__(self, id, name, specialty, phone, address):
        self.id_provider = id
        self.name_provider = name
        self.specialty= specialty
        self.phone_provider = phone
        self.address_provider = address
        

