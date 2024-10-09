from rest_framework import serializers
from main.models import DataCrud


class CreateSerialize(serializers.ModelSerializer):
	class Meta:
		model = DataCrud
		fields = ['nama','umur']