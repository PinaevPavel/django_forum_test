from django.contrib import admin

from .models import Bb, Rubric # Импортируем модели в административную панель

class BbAdmin(admin.ModelAdmin): # Объявлем редактор модели, он содержит набор атрибутов класса, которые задают параменты представления модели в админ панели.
	list_display = ('title', 'content', 'price', 'published', 'rubric') # Последовательность имен полей, которые должны выводиться в списке записей
	list_display_links = ('title', 'content') #Последовательность имен полей, которые должны быть преобразованы в гиперссылки, ведущие на страницу правки записи
	search_fields = ('title', 'content')# Последовательность имен полей, по которым должна выполняться фильтрация


admin.site.register(Bb, BbAdmin) #Вызываем метод register у экземпляра класса AdminSite, представляющего сам аодминистративный сайт и передаем ему ссылку на класс модели Bb
admin.site.register(Rubric) 

# Register your models here.
