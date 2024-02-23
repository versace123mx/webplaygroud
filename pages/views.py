from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page

# Create your views here.
class PagesListView(ListView):
    model = Page
    #no se le tiene que pasar la ruta del template ya que django llama a un archivo por defaul page_list. html y asi es como se tiene que llamar nuestro template


class PageDetailView(DetailView):
    model = Page


