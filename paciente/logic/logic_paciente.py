from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all()
    return (queryset)

def get_paciente_por_cedula(cedula):
    paciente = list(Paciente.objects.raw("SELECT * FROM epilepsia2_paciente WHERE cedula = %s", [cedula]))
    if paciente:
        return paciente[0]
    else:
        return None  # Manejar el caso en que no se encuentre

def create_paciente(form):
    paciente = form.save()
    paciente.save()
    return ()