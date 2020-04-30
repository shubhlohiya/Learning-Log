from django.shortcuts import render

from .models import Topic

def index(request):
	"""The Learning Log home page"""

	return render(request, 'learning_logs/index.html')

def topics(request):
	"""Shows all the topics"""

	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)