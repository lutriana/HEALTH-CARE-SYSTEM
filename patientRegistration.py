class ClinicHistory:
    """Representa la historia clínica de un paciente, incluyendo signos vitales,
    notas de evolución, imágenes y resultados de exámenes."""

    def _init_(self):
        """Inicializa la historia clínica con listas vacías para signos, notas,
        imágenes y cero por defecto para los resultados de exámenes."""
        self.vital_signs = []
        self.evolution_notes = []
        self.images = []
        self.exam_results = 0

    def add(self, signs, notes, image, result):
        """Añade nuevas entradas a la historia clínica.
        
        Args:
            signs: Nuevos signos vitales para añadir.
            notes: Nuevas notas de evolución para añadir.
            image: Nueva imagen para añadir.
            result: Nuevo resultado de examen para reemplazar el anterior.
        """
        self.vital_signs.append(signs)
        self.evolution_notes.append(notes)
        self.images.append(image)
        self.exam_results = result


class Pacient:
    """Representa un paciente con detalles personales e historia clínica."""

    def _init_(self, id, name, gender, phone, service):
        """Inicializa un nuevo paciente con los detalles especificados.
        
        Args:
            id: ID del paciente.
            name: Nombre del paciente.
            gender: Género del paciente.
            phone: Número de teléfono del paciente.
            service: Tipo de servicio asociado al paciente.
        """
        self.id_patient = id
        self.name_patient = name
        self.gender_patient = gender
        self.phone_patient = phone
        self.service = service
        self.clinic_history = ClinicHistory()
