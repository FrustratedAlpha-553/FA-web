from django.shortcuts import render
from django.http import Http404


from .serializers import *



from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ProductView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSer(products,many=True,context = {'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        products = ProductSer(data = request.data)
        if products.is_valid():
            products.save()
            return Response(products.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_304_NOT_MODIFIED)
    
    
class ProductDetail(APIView):
    def get_obj(self,pk):
        try : 
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        return product
    
    def get(self,request,pk):
        product = self.get_obj(pk)
        serializer = ProductSer(product,context = {'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        product = self.get_obj(pk)
        serializer = ProductSer(product,data = request.data , context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        product=self.get_obj(pk)
        product.delete()
        return Response(status=status.HTTP_202_ACCEPTED)        
            

class CategoryView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySer(categories,many=True,context = {'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class CategoryDetail(APIView):
    def get_obj(self,pk):
        try : 
            category = Category.objects.get(pk=pk)
        except category.DoesNotExist:
            raise Http404
        return category
    
    def get(self,request,pk):
        category = self.get_obj(pk)
        serializer = CategorySer(category,context = {'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class FileView(APIView):
    def get(self,request,product_id):
        files = File.objects.filter(product_id = product_id)
        serializers = FileSer(files,many=True,context = {'request':request})
        return Response(serializers.data,status=status.HTTP_200_OK)
    

class FileDetail(APIView):
    def get(self,request,product_id,pk):
        try:
            file = File.objects.get(product_id=product_id,pk=pk)
        except File.DoesNotExist:
            raise Http404
        serializer = FileSer(file,context = {'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
        