from rest_framework import serializers
from main.models import DataCrud

class DeleteSerialize(serializers.ModelSerializer):
	class Meta:
		model = DataCrud
		fields = []