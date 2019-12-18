from django.forms import ModelForm

from .models import Bb

class BbForm(ModelForm):
	class Meta:
		model = Bb # класс модели с которой связана  форма
		fields = ('title', 'content', 'price', 'rubric') # последовательность из имен полей модели, которые должны присутствоать в форме

