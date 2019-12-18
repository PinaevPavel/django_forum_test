#создаем список маршрутов для приложения bboard
from django.urls import path
from .views import index, by_rubric, BbCreateView, add_and_save

urlpatterns = [
	path('add/', add_and_save, name='add'), # В вызове функции path() подставляется не ссылка на сам контроллер-класс, а результат, возвращенный методом as_view() контроллера-класса.
	path('<int:rubric_id>/', by_rubric, name='by_rubric'), # конструкция int - челочисленный тип парамента, а rubric_id имя парамента контроллера, которому будет присвоено значение этого url-парамента
	#name - имя маршрута, необходимое для реализации обратного разрешения интернет-адресов
	path('', index, name='index'), #Пустая строка, означает корень пути из маршрута предыдущего уровля вложенности.
]