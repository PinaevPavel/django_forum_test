from django.forms import ModelForm

from .models import Message

class MessageForm(ModelForm):
	class Meta:
		model = Message # класс модели с которой связана  форма
		fields = ('title', 'message') # последовательность из имен полей модели, которые должны присутствоать в форме

