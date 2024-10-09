from django.db import models
from uuid import uuid4

class DataCrud(models.Model):
	data_id = models.TextField(primary_key=True,default=uuid4())
	nama = models.CharField(max_length=255)
	umur = models.IntegerField()