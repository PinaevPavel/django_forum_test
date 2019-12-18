from django.http import HttpResponse, HttpResponseRedirect
from .models import Bb, Rubric
from django.shortcuts import render
from django.views.generic.edit import CreateView # базовый класс, реализует функциональность по созданию формы, выводу ее на экран с применением указанного шаблона, 
#получению занесенных данных в форму данных, проверке их на корректность, сохранению их в  новой записи модели и перенаправленю в случае успеха на интернет-адрес, который мы зададим.
from .forms import BbForm # Импорь нужной формы
from django.urls import reverse_lazy, reverse # Эта функция принимает имя маршрута и значения всех входящих в маршрут URL параметров
from django.template.loader import get_template



def index(request):
	#template = loader.get_template('bboard/index.html') #Загружаем шаблон, с помощью функции get_template(). В качестве парамента передаем путь к файлу шаблона, отчитанному от папки template, результатом возвращенным функцией, станет экземпляр класса Template, представляющий хранящийся в заданном файле шаблон
	bbs = Bb.objects.all()
	rubrics = Rubric.objects.all()
	context = {'bbs': bbs, 'rubrics': rubrics}
	template = get_template('bboard/index.html')
	#return HttpResponse(request, 'bboard/index.html', context) # Запускаем обработку шаблона, в процессе которого шаблонизатор выполяет объеденение его с данными из контекста. Рендерин запускаеться вызовом метода render() класса Template.
	return HttpResponse(template.render(context=context, request=request))
	
def by_rubric(request, rubric_id):
	bbs = Bb.objects.filter(rubric=rubric_id) # список объявления, отфильтрованных по полу ключа rubric
	rubrics = Rubric.objects.all() 
	current_rubric = Rubric.objects.get(pk=rubric_id) #Фильтруем из списка рубрик 1 объявление с нужным ИД pk - принимает что нужно искать
	context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
	return render(request, 'bboard/by_rubric.html', context)

class BbCreateView(CreateView):
	template_name = 'bboard/create.html' #Путь к файлу шаблона, который будет использован для вывода страницы с формой
	form_class = BbForm #класс формы, связанный с моделью
	success_url = reverse_lazy('index') # Интернет адрес, по которому будет выполнено перенаправление после успешного сохранения данных

	def get_context_data(self, **kwargs): #Метод, который будет генерировать панель навигации, содержащая список рубрик
		context = super().get_context_data(**kwargs) # получаем контекст шаблона из метода базового класса
		context['rubrics'] = Rubric.objects.all() # добовляем список рубрик 
		return context #возвращаем список в качесве результата

def add_and_save(request): #Данная контроллер функция выполняет и вывод формы на страницу и отправление POST Запроса с данным формы на сервер.
	if request.method == 'POST':
		bbf = BbForm(request.POST)
		if bbf.is_valid():
			bbf.save()
			return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
		else:
			context = {'form': bbf}
			return render(request, 'bboard/create.html', context)
	else:
		bbf = BbForm()
		context = {'form': bbf}
		return render(request, 'bboard/create.html', context)


