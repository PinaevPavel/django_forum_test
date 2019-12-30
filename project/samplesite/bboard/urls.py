#создаем список маршрутов для приложения bboard
from django.urls import path
from .views import index

urlpatterns = [
	path('', index, name='index'), #Пустая строка, означает корень пути из маршрута предыдущего уровля вложенности.
]