from django.urls import path
from . import views
from .views import ImageDetail, ImageDelete

urlpatterns = [
    path('', views.index, name="home"),
    path('<int:pk>/', ImageDetail.as_view(), name='image-detail'),
    path('<int:pk>/delete/', ImageDelete.as_view(), name='image-delete'),
]
