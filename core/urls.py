from django.urls import path
from . import views
urlpatterns=[
 path('app/sample1/',views.sample1,name='sample1'),
 path('app/sample2/',views.sample2,name='sample2'),
]