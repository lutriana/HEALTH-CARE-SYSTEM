
class ClinicHistory:
    def __init__(self):
        self.vital_signs = []
        self.evolution_notes = []
        self.images = []
        self.exam_results = 0

    def add(self, signs, notes, image, result):
        self.vital_signs.append(signs)
        self.evolution_notes.append(notes)
        self.images.append(image)
        self.exam_results = result


class Pacient:
    def __init__(self, id, name, gender, phone, service):
        self.id_patient = id
        self.name_patient = name
        self.gender_patient = gender
        self.phone_patient = phone
        self.service = service
        self.clinic_history = ClinicHistory()
