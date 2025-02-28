from rest_framework.views import APIView
from rest_framework.response import Response
from categories.models import Category
from categories.serializers import CategorySerializer  

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


