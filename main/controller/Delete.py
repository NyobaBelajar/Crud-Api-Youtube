from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from main.models import DataCrud
from main.serialize.SerializeDelete import DeleteSerialize

class DeleteController(DestroyAPIView):
	renderer_classes = [JSONRenderer]
	allowed_methods = 'DELETE'
	lookup_field = 'data_id'
	lookup_url_kwarg = 'uid'
	serializer_class = DeleteSerialize
	queryset = DataCrud.objects.all()


	def destroy(self,req,*args,**kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		return Response({"message":"Data Berhasil Di Hapus","Kode":200})