from rest_framework import generics
from .models import Category, Omonim
from .serializers import CategorySerializer, OmonimSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OmonimListView(generics.ListAPIView):
    queryset = Omonim.objects.all()
    serializer_class = OmonimSerializer

class OmonimByCategoryView(generics.ListAPIView):
    serializer_class = OmonimSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Omonim.objects.filter(categories__id=category_id)
