from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('edit/',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),


# ------------- Ali s way of doing ------------

    # path('add/',views.add,name='add'),

]