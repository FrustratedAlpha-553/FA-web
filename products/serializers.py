from rest_framework import serializers
from .models import *

class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title','description','avatar','is_enable')
        
class FileSer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('title','file')
        
class ProductSer(serializers.ModelSerializer):
    categories = CategorySer(many=True)
    file_set = FileSer(many=True)
    class Meta:
        model = Product
        fields = ('title','description','avatar','is_enable','categories','file_set')