from django.urls import path
from .views import PoodleList, PoodleDetail

urlpatterns = [
    path('poodles/', PoodleList.as_view(), name='poodle_list'),

    path('poodles/<int:pk>/', PoodleDetail.as_view(), name='poodle_detail'),
]