from django.urls import path
from .views import login, write_mode, index, home,signup,dynamic_form

urlpatterns = [
    path("login", login),
    path("write/<section>/<page>", write_mode,name='write'),
    path("<int:id>/index", index,name='index'),
    path("", home),
    path("signup",signup,name='signup'),
    path("Section-form/",dynamic_form ,name='dynamic_form')
]
