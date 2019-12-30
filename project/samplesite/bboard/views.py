from django.http import HttpResponse, HttpResponseRedirect
from .models import Message
from django.shortcuts import render
from .forms import MessageForm # Импорь нужной формы
from django.urls import reverse # Эта функция принимает имя маршрута и значения всех входящих в маршрут URL параметров
from django.template.loader import get_template



def index(request):
	
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('index'))
	else:

		form = MessageForm #класс формы, связанный с моделью
		bbs = Message.objects.all()
		context = {'bbs': bbs, 'form': form}
		template = get_template('bboard/index.html')
		#return HttpResponse(request, 'bboard/index.html', context) # Запускаем обработку шаблона, в процессе которого шаблонизатор выполяет объеденение его с данными из контекста. Рендерин запускаеться вызовом метода render() класса Template.
		return HttpResponse(template.render(context=context, request=request))
	


