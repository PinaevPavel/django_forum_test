from django.db import models
from django.contrib.auth.models import User # Импортируем стандартную модель пользователя User 


class Message(models.Model):
	title = models.CharField(max_length=50, verbose_name='Имя') #Строковое поле фиксируемой длины, допустимая длина обозначется параметром max_length
	message = models.TextField(null=True, blank=True, verbose_name='Сообщение') #Строковое поле неограниченной длины. Присвоив True к null and blank, указываем, что поле можно не заполнять 
	published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации') # auto_now_add при создании записи присваивает текущую дату. db_index создает для поля индекс

	class Meta:
		verbose_name_plural = 'Сообщения' #Название модели во множественном числе
		verbose_name = 'Сообщение' #Название модели в единственном числе
		ordering = ['-published'] # Последовательность полей, по которым по умолчанию будет выполняться сортировка записей
# Create your models here.

