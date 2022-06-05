from django.shortcuts import render
from .models import room
from .models import project
# Create your views here.
def index(request):
	p=project.objects.all()
	return render(request,'index.html',{'pro':p})

def blog(request):
	d=room.objects.all()
	return render(request,'blog.html',{'dest':d})
	


