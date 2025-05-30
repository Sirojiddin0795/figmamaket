from django.urls import path
from .views import CategoryListView, OmonimListView, OmonimByCategoryView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('omonims/', OmonimListView.as_view()),
    path('categories/<int:category_id>/omonims/', OmonimByCategoryView.as_view()),
]
