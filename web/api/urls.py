from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('subkategori/list',SubkategoriView.list),
    path('subkategori/detail/<int:pk>',SubkategoriView.detail),
    path('subkategori/create/',SubkategoriView.create),
    path('subkategori/update/<int:pk>', SubkategoriView.update),
    path('subkategori/delete/<int:pk>', SubkategoriView.delete),
    path('kategori/list', KategoriView.list),
    path('kategori/detail/<int:pk>', KategoriView.detail),
    path('kategori/create/', KategoriView.create),
    path('kategori/update/<int:pk>', KategoriView.update),
    path('kategori/delete/<int:pk>', KategoriView.delete),
    path('essay/list', EssayView.list),
    path('essay/detail/<int:pk>', EssayView.detail),
    path('essay/create/', EssayView.create),
    path('essay/update/<int:pk>', EssayView.update),
    path('essay/delete/<int:pk>', EssayView.delete),
    path('pilgan/list', PilganView.list),
    path('pilgan/detail/<int:pk>', PilganView.detail),
    path('pilgan/create/', PilganView.create),
    path('pilgan/update/<int:pk>', PilganView.update),
    path('pilgan/delete/<int:pk>', PilganView.delete),
]