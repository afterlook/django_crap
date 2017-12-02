from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DeleteView, UpdateView, CreateView

from bookshit.models import Author


def index(request):
    return render(request, 'index.html')


class AuthorCreate(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name']


class AuthorUpdate(UpdateView):
    model = Author
    template_name = 'author_update.html'
    fields = ['name']


class AuthorDelete(DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author-list')


class AuthorDetail(generic.DetailView):
    template_name = 'author_detail.html'
    model = Author


class AuthorList(generic.ListView):
    template_name = 'author_list.html'
    model = Author
