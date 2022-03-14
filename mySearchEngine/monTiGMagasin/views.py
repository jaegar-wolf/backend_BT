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
            return InfoProduct.objects.get(id=id)
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
        serializer = InfoProductSerializer(product, data={ 'discount': newprice,
                                                            'sale': True })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

class RemoveOnSale(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product, data={ 'sale': False })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

class IncrementStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, number, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product, data={'quantityInStock': product.quantityInStock+number})
        if serializer.is_valid():
            serializer.save()
            if serializer.data['quantityInStock'] > 16 and serializer.data['quantityInStock'] < 64:
                serializer = InfoProductSerializer(product, data={  'discount': round(product.price*0.8, 2),
                                                                    'sale': True,
                                                                    'percentage_reduc': 20})
                if serializer.is_valid(): 
                    serializer.save()
                    return Response(serializer.data)
            
            elif serializer.data['quantityInStock'] > 64:
                serializer = InfoProductSerializer(product, data={  'discount': round(product.price*0.5, 2),
                                                                    'sale': True,
                                                                    'percentage_reduc': 50})
                if serializer.is_valid(): 
                    serializer.save()
                    return Response(serializer.data)
            
            else: 
                serializer = InfoProductSerializer(product, data={  'discount': 0,
                                                                    'sale': False,
                                                                    'percentage_reduc': 0})
                if serializer.is_valid(): 
                    serializer.save()
                    return Response(serializer.data)
            
            return Response(serializer.data)

class DecrementStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, number, format=None):
        product = self.get_object(tig_id=tig_id)
        serializer = InfoProductSerializer(product, data={'quantityInStock': product.quantityInStock-number})
        if serializer.is_valid():
            serializer.save()
            if serializer.data['quantityInStock'] > 16 and serializer.data['quantityInStock'] < 64:
                serializer = InfoProductSerializer(product, data={  'discount': round(product.price*0.8, 2),
                                                                    'sale': True,
                                                                    'percentage_reduc': 20})
                if serializer.is_valid(): 
                    serializer.save()
                    return Response(serializer.data)
            
            elif serializer.data['quantityInStock'] > 64:
                serializer = InfoProductSerializer(product, data={  'discount': round(product.price*0.5, 2),
                                                                    'sale': True,
                                                                    'percentage_reduc': 50})
                if serializer.is_valid(): 
                    serializer.save()
                    return Response(serializer.data)
            
            else: 
                serializer = InfoProductSerializer(product, data={  'discount': 0,
                                                                    'sale': False,
                                                                    'percentage_reduc': 0})
                if serializer.is_valid(): 
                    serializer.save()
                    return Response(serializer.data)
            
            return Response(serializer.data)

            