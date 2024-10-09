from rest_framework.renderers import JSONRenderer
from main.serialize.SerializeCreate import CreateSerialize
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView


class CreateController(CreateAPIView):
	serializer_class = CreateSerialize
	renderer_classes = [JSONRenderer]
	allowed_methods = 'POST'

	def create(self,req,*args,**kwargs):
		serialize = self.serializer_class(data=req.data)
		serialize.is_valid(raise_exception=True)
		self.perform_create(serialize)
		headers = self.get_success_headers(serialize)
		return Response(serialize.data,status=200,headers=headers)