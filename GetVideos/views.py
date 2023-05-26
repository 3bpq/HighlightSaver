from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm
from .VideosGrabber import VideosGrabber

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            VideosGrabber(form.cleaned_data['your_name'])
            return HttpResponseRedirect('/Videos/')
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

def Videos(request):
    return render(request, 'Videos.html')