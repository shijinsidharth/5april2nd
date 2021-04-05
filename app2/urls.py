from django.urls import path, include
from . import views
urlpatterns = [
path('test/',views.TestFn,name='test'),
path('home/',views.TestFn2),
path('test2',views.TestFn3),
]