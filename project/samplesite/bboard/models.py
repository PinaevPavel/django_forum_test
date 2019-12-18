from django.db import models
from django.contrib.auth.models import User # Импортируем стандартную модель пользователя User 


class Bb(models.Model):
	title = models.CharField(max_length=50, verbose_name='Товар') #Строковое поле фиксируемой длины, допустимая длина обозначется параметром max_length
	content = models.TextField(null=True, blank=True, verbose_name='Описание') #Строковое поле неограниченной длины. Присвоив True к null and blank, указываем, что поле можно не заполнять 
	price = models.FloatField(null=True, blank=True, verbose_name='Цена') # Поле для хранения вещественных чисел
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации') # auto_now_add при создании записи присваивает текущую дату. db_index создает для поля индекс
	#Поле во вторичной модели.
	rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика') # Класс ForeignKey представляет поле внешнего ключа, в котором будет храниться ключ записи из первичной модели. 
	#Первый параментр конструктору класса передаеться класс первичной модели в виде строки с именем класса, если вторичная модель объявлена раньше перчиной.
	#Помечаем поле rubric как необязательно, присвоив параметру null значение True. Только после этого поле будет успешно добавлено в модель
	#Параментр on_delete управляет каскадными удалениями записей вторичной модели после удаления записи первичной модели, с которой оин были связаны.
	#Значение PROTECT этого параметра запрещает каскадные удаления.

	class Meta:
		verbose_name_plural = 'Объявления' #Название модели во множественном числе
		verbose_name = 'Объявление' #Название модели в единственном числе
		ordering = ['-published'] # Последовательность полей, по которым по умолчанию будет выполняться сортировка записей
# Create your models here.

class Rubric(models.Model):
	#Поле в первичной модели.
	name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

	def __str__(self): # Переопределяем магический метод  __str__, возвращающий скоровое представление класса.
		return self.name # Данный метод удобнее применять для моделей с 1 полем

	class Meta:
		verbose_name_plural = 'Рубрики'
		verbose_name = 'Рубрика'
		ordering = ['name']

#Класс с полем OneToOneField для связи один с одним, с моделью User
class AbvUser(models.Model):
	is_activated = models.BooleanField(default=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

#Создаем 2 класса для связи многие со многими

class Spare(models.Model):
	name = models.CharField(max_length=30, verbose_name='Деталь')

class Machine(models.Model):
	name = models.CharField(max_length=30, verbose_name='Машина')
	spares = models.ManyToManyField(Spare)#поле, образующее связь Многие-со-многими