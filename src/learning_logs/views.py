from django.shortcuts import render

def index(request):
	"""The Learning Log home page"""

	return render(request, 'learning_logs/index.html')