from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cm',views.cm,name='cm'),
    path('std',views.std,name='std'),
    path('stdshow',views.stdshow,name='stdshow'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editstd/<int:pk>',views.editstd,name='editstd'),
    path('deletepage/<int:pk>',views.deletepage,name="deletepage"),
   path('show_students/<int:sid>', views.show_students,name='show_students'),
   
]
