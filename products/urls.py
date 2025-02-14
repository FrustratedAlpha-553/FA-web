
from django.urls import path
from .views import ProductView,ProductDetail,CategoryView,CategoryDetail,FileView,FileDetail

urlpatterns = [
    path('product/',ProductView.as_view(),name='product'),
    path('product/<int:pk>/',ProductDetail.as_view()),
    path('category/',CategoryView.as_view()),
    path('category/<int:pk>/',CategoryDetail.as_view()),
    path('file/<int:product_id>/',FileView.as_view()),
    path('file/<int:product_id>/<int:pk>/',FileDetail.as_view()),
]