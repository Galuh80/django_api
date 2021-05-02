from rest_framework.serializers import ModelSerializer,FileField
from .models import *

class SubkategoriSerializer(ModelSerializer):
    class Meta:
        model = SubkategoriModel
        fields = '__all__'

class KategoriSerializer(ModelSerializer):
    class Meta:
        model = KategoriModel
        fields = '__all__'

class SoalEssaySerializer(ModelSerializer):
    kategori = KategoriSerializer(many=True,read_only=True)
    subkategori = SubkategoriSerializer(many=True, read_only=True)
    essay_image = FileField()

    class Meta:
        model = SoalEssayModel
        fields = '__all__'

class SoalPilganSerializer(ModelSerializer):
    kategori = KategoriSerializer(many=True,read_only=True)
    subkategori = SubkategoriSerializer(many=True, read_only=True)
    pilgan_image = FileField()

    class Meta:
        model = SoalPilganModel
        fields = '__all__'