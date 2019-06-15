from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category, Photo
from django.views.generic import ListView, DetailView,UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

@login_required
def base(request):
    return render(request, 'base.html')

def first_view(request):
    return HttpResponse('Esta es mi primera vista!')

@login_required
def category(request):
    category_list = Category.objects.all()
    context = {'object_list':category_list}
    return render(request,'album/category_list.html',context)

@login_required
def category_detail(request,category_id):
    category = Category.objects.get(id=category_id)
    context = {'object':category}
    return render(request,'album/category_detail.html',context)

class PhotoListView(LoginRequiredMixin,ListView):
    model = Photo
    

class PhotoDetailView(LoginRequiredMixin,DetailView):
    model = Photo
    

class PhotoUpdate(LoginRequiredMixin,UpdateView):
    model = Photo
    fields = '__all__'

class PhotoCreate(LoginRequiredMixin,CreateView):
    model = Photo
    fields = '__all__'

class PhotoDelete(LoginRequiredMixin,DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')




# Create your views here.
