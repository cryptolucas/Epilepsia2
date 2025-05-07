from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all()
    return (queryset)

def get_paciente_por_cedula(cedula):
    paciente = Paciente.objects.raw("SELECT * FROM pacientes WHERE cedula=%s" % cedula)[0]
    return (paciente)

def create_paciente(form):
    paciente = form.save()
    paciente.save()
    return ()