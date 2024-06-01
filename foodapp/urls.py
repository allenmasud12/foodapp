from . import views
from django.urls import path


urlpatterns = [    
        path('', views.index, name = 'index'),    
        path('item/', views.item, name = 'item'),   
        path('<int:item_id>/', views.detail, name='detail'), 
        #/add item
        path('add/', views.create_item, name= 'create_item'),
        #/edit item
        path('update/<int:id>/', views.update_item, name='update_item'),
        #/delete item
        path('delete/<int:id>/', views.delete_item, name= 'delete_item'),
    ]

