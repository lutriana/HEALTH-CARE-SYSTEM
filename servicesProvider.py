from patientRegistration import ClinicHistory

class ServicesProvider:
    """
    Representa un proveedor de servicios que tiene acceso a los resultados de laboratorio
    e imágenes de los pacientes. Esta clase mantiene detalles específicos del proveedor.
    """
    
    def _init_(self, id, name, specialty, phone, address):
        """
        Inicializa un nuevo proveedor de servicios con los detalles especificados.
        
        Args:
            id (int): Identificador único para el proveedor de servicios.
            name (str): Nombre del proveedor de servicios.
            specialty (str): Especialidad médica del proveedor.
            phone (str): Número de teléfono de contacto del proveedor.
            address (str): Dirección de la oficina del proveedor.
        """
        self.id_provider = id
        self.name_provider = name
        self.specialty = specialty
        self.phone_provider = phone
        self.address_provider = address
        

