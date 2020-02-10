from django.urls import path
from . import views

app_name = "pwapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.gen_password, name="generate"),
    path('delete/<int:pass_id>', views.delete, name="delete"),
    path('edit/<int:pass_id>', views.edit, name='edit'),
    path('save/<int:pass_id>', views.save, name='save'),

]
