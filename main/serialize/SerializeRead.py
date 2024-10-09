from rest_framework import serializers
from main.models import DataCrud

class ReadSerialize(serializers.ModelSerializer):
	class Meta:
		model = DataCrud
		fields = '__all__'