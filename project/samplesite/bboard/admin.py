from django.contrib import admin

from .models import Message # Импортируем модели в административную панель

class BbAdmin(admin.ModelAdmin): # Объявлем редактор модели, он содержит набор атрибутов класса, которые задают параменты представления модели в админ панели.
	list_display = ('title', 'message', 'published') # Последовательность имен полей, которые должны выводиться в списке записей
	list_display_links = ('title', 'message') #Последовательность имен полей, которые должны быть преобразованы в гиперссылки, ведущие на страницу правки записи
	search_fields = ('title', 'message')# Последовательность имен полей, по которым должна выполняться фильтрация


admin.site.register(Message, BbAdmin) #Вызываем метод register у экземпляра класса AdminSite, представляющего сам аодминистративный сайт и передаем ему ссылку на класс модели Bb


# Register your models here.
