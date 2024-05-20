from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from form import views as auth_views



# Create your views here.

def index (request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been successfully submitted!')
            return redirect('index')
        else:
            messages.error(request, 'Form has some invalid fields!')
    else:
        form = StudentForm()
    return render(request, 'form/index.html', {'form': form})
    
     






