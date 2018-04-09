from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from docsearch.models import File 
from docsearch.utils.update import find_all_files
from docsearch.forms import SearchForm
from docsearch.utils.search import search_text

# Create your views here.

class TopView(generic.TemplateView):
    template_name = 'docsearch/top.html'
    form_class = SearchForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top'] = 'update here'
        context['search'] = 'search here'
        context['form'] = self.form_class
        return context

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
    form_class = SearchForm
    template_name = 'docsearch/search_result.html'
    context_object_name = 'file_list'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form = None

    def get_queryset(self):
        qs = super().get_queryset()
        self.form = self.form_class(self.request.GET or None)
        if self.form.is_valid() and self.form.cleaned_data.get('word'):
            target_files = search_text(self.form.cleaned_data['word'])
            qs = qs.filter(filename__in=target_files)
        return qs
