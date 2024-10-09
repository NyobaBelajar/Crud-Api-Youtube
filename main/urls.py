from main.controller.Create import CreateController
from main.controller.Read import ReadController
from main.controller.Update import UpdateController
from main.controller.Delete import DeleteController
from django.urls import path


urlpatterns = [
	path('create',CreateController.as_view()),
	path('list',ReadController.as_view()),
	path('update/<str:uid>',UpdateController.as_view()),
	path('delete/<str:uid>',DeleteController.as_view()),
]