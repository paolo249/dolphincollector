from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dolphins/', views.dolphins_index, name='index'),
    path('dolphins/<int:dolphin_id>/', views.dolphins_detail, name='detail'),
    path('dolphins/create/', views.DolphinCreate.as_view(), name='dolphins_create'),
    path('dolphins/<int:pk>/update/', views.DolphinUpdate.as_view(), name='dolphins_update'),
    path('dolphins/<int:pk>/delete/', views.DolphinDelete.as_view(), name='dolphins_delete'),
    path('dolphins/<int:dolphin_id>/add_feeding/', views.add_feeding, name='add_feeding'),

    path('cats/<int:dolphin_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('cats/<int:dolphin_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    path('toys/',views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

]
