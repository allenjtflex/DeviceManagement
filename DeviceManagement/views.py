from django.shortcuts import render



def index(request):
	title = "Device Managment System"
	return render(request, "index.html", locals())