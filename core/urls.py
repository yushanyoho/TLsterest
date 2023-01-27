# import the path function from the framework package
from django.urls import path
# import views.py under the same root
from . import views

urlpatterns = [
    # set up an empty url: '' as the home url
    path('', views.index, name='index')
]