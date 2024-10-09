from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from main.serialize.SerializeUpdate import UpdateSerialize
from main.models import DataCrud

class UpdateController(UpdateAPIView):
	serializer_class = UpdateSerialize
	renderer_classes = [JSONRenderer]
	allowed_methods = 'PUT'
	lookup_field = 'data_id'
	lookup_url_kwarg = 'uid'
	queryset = DataCrud.objects.all()

	def update(self,req,*args,**kwargs):
		instance = self.get_object()
		serialize = self.get_serializer(instance,data=req.data)
		serialize.is_valid(raise_exception=True)
		self.perform_destroy(instance)
		serialize.save()
		return Response(serialize.data,status=200)