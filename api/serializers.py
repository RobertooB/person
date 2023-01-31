from rest_framework import serializers
from api.models import Persona, Catalogo, Institucion

class CatalogoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = "__all__"

class PersonaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"
        
class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = "__all__"
