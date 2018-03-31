from django.shortcuts import render

from docsearch.models import File 
from docsearch.utils.update import find_all_files

# Create your views here.
def top(request):
    return render(request, 'docsearch/top.html', {'top': 'update here'})

def update(request):
    tmp = 'bad'
    for file in find_all_files('/home/jovyan/data/'):
        tmp = 'partially ok'
        if file[-3:] == '.md':
            tmp = 'ok'
            f = open(file)
            File(filename=file, text=f.read()).save()
            f.close()
    return render(request, 'docsearch/update.html', {'finish': tmp})
