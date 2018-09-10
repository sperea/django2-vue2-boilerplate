from rest_framework import serializers
from .models import Profile, Noticia

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class NoticiaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Noticia
		fields = '__all__'