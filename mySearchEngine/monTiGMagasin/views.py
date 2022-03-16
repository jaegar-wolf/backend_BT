from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from monTiGMagasin.config import baseUrl
from monTiGMagasin.models import InfoProduct
from monTiGMagasin.serializers import InfoProductSerializer

# Create your views here.
class InfoProductList(APIView):
    def get(self, request, format=None):
        products = InfoProduct.objects.all()
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)

class InfoProductDetail(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404
    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id==tig_id)
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

class PutOnSale(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, newprice, format=None):
        product = self.get_object(tig_id=tig_id)
        product.sale = True
        product.discount = newprice
        product.save()

        serializer = InfoProductSerializer(product)
        return Response(serializer.data)


class RemoveOnSale(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        product.sale = False
        product.discount = 0
        product.save()

        serializer = InfoProductSerializer(product)
        return Response(serializer.data)


class IncrementStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, number, format=None):
        product = self.get_object(tig_id=tig_id)
        product.quantityInStock += number
        product.save()
        
        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

class DecrementStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, number, format=None):
        product = self.get_object(tig_id=tig_id)
        product.quantityInStock -= number
        
        if product.quantityInStock < 0:
            product.quantityInStock = 0
            
        product.save()

        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

            