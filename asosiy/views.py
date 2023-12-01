from django.shortcuts import render
from django.views import View
from .models import *
from django.db.models import Avg

def bosh_sahifa(request):
    return render(request, 'page-index-2.html')

class HomeView(View):
    def get(self, request):
        data = {
            'bolimlar' : Bolim.objects.all()[:8]
        }
        return render(request, 'page-index.html', data)

class BolimlarView(View):
    def get(self, request):
        data = {
            "bolimlar": Bolim.objects.all()
        }
        return render(request, 'page-category.html', data)

class MahsulotlarView(View):
    def get(self, request, pk):
        b1= Bolim.objects.get(id=pk)
        data = {
            'mahsulotlar': b1.mahsulot_set.all()
        }
        return render(request, 'page-listing-grid.html', data)

class MahsulotView(View):
    def get(self, request, pk):
        data = {
            'mahsulot': Mahsulot.objects.get(id=pk)
        }
        return render(request, 'page-detail-product.html', data)