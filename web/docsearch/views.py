from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from docsearch.models import File 
from docsearch.utils.update import find_all_files

# Create your views here.
def top(request):
    return render(request, 'docsearch/top.html', {'top': 'update here', 'search': 'search here'})

def update(request):
    for file in find_all_files('/home/jovyan/data/'):
        if file[-3:] == '.md':
            f = open(file)
            try:
                tmp_file = File.objects.get(filename=file)
                tmp_file.text = f.read()
                tmp_file.save()
            except File.DoesNotExist:
                File(filename=file, text=f.read()).save()           
            f.close()
    return HttpResponseRedirect(reverse('docsearch:update_result'))

def update_result(request):
    return render(request, 'docsearch/update_result.html', {'finish': 'finish update!'})

class SearchView(generic.ListView):
    model = File
    template_name = 'docsearch/search_result.html'
