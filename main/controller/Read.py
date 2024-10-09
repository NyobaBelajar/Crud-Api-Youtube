from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from main.serialize.SerializeRead import ReadSerialize
from rest_framework.renderers import JSONRenderer
from main.models import DataCrud


class ReadController(ListAPIView):
	serializer_class = ReadSerialize
	renderer_classes = [JSONRenderer]
	allowed_methods = 'GET'
	queryset = DataCrud.objects.all()