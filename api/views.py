from rest_framework import viewsets
from api.models import Persona, Catalogo ,Institucion
from api.serializers import PersonaSerializer, CatalogoSerializer, InstitucionSerializer

class CatalogoViewSet ( viewsets.ModelViewSet ):
    serializer_class = CatalogoSerializer
    queryset = Catalogo.objects.all()
   
class PersonaViewSet ( viewsets.ModelViewSet ):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

class InstitucionViewSet ( viewsets.ModelViewSet ):
    serializer_class = InstitucionSerializer
    queryset = Institucion.objects.all()

