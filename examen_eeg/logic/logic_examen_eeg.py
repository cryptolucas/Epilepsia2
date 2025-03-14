from ..models import ExamenEEG

def get_examenesEEG():
    queryset = ExamenEEG.objects.all()
    return (queryset)

def create_examenEEG(form):
    examenEEG = form.save()
    examenEEG.save()
    return ()