from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from monTiGMagasin.config import baseUrl
from monTiGMagasin.models import InfoProduct, DonneeHisto
from monTiGMagasin.serializers import InfoProductSerializer, DonneeHistoSerializer
from rest_framework import status

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

    def get(self, request, tig_id, newpromo, format=None):
        product = self.get_object(tig_id=tig_id)
        product.sale = True
        product.percentage_reduc = newpromo
        product.discount = round(product.price * (1 - product.percentage_reduc / 100), 2)
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
        product.percentage_reduc = 0
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

    def get(self, request, tig_id, number, vente, format=None):
        product = self.get_object(tig_id=tig_id)
        product.quantityInStock -= number
        if vente == 1:
            product.quantitySold += number

        if product.quantityInStock < 0:
            product.quantityInStock = 0

        product.save()

        serializer = InfoProductSerializer(product)
        return Response(serializer.data)

    
class IncrementAndReturnStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, number, format=None):
        product = self.get_object(tig_id=tig_id)
        product.quantityInStock += number
        product.save()

        products = InfoProduct.objects.all()
        
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)

class DecrementAndReturnStock(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, number, vente, format=None):
        product = self.get_object(tig_id=tig_id)
        if product.quantityInStock - number < 0:
            products = InfoProduct.objects.all()
            serializer = InfoProductSerializer(products, many=True)
            return Response(serializer.data)

        product.quantityInStock -= number
        if product.quantityInStock < 0:
            product.quantityInStock = 0
        
        if vente == 1:
            product.quantitySold += number

        product.save()

        products = InfoProduct.objects.all()
        
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)

class PutOnSaleAndReturn(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, newpromo, format=None):
        product = self.get_object(tig_id=tig_id)
        product.sale = True
        product.percentage_reduc = newpromo
        product.discount = round(product.price * (1 - product.percentage_reduc / 100), 2)
        product.save()

        products = InfoProduct.objects.all()
        
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)

class RemoveOnSaleAndReturn(APIView):
    def get_object(self, tig_id):
        try:
            return InfoProduct.objects.get(tig_id=tig_id)
        except InfoProduct.DoesNotExist:
            raise Http404

    def get(self, request, tig_id, format=None):
        product = self.get_object(tig_id=tig_id)
        product.sale = False
        product.percentage_reduc = 0
        product.discount = 0
        product.save()

        products = InfoProduct.objects.all()
        
        serializer = InfoProductSerializer(products, many=True)
        return Response(serializer.data)


class ListTransaction(APIView):
    def get(self, request, format=None):
        donnees = DonneeHisto.objects.all()
        serializer = DonneeHistoSerializer(donnees, many=True)
        return Response(serializer.data)

class DetailTransaction(APIView):
    def get_object(self, id):
        try:
            return DonneeHisto.objects.get(id=id)
        except DonneeHisto.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        transa = self.get_object(id)
        serializer = DonneeHistoSerializer(transa)
        return Response(serializer.data)
    
    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddTransaction(APIView):
    def get(self, request, nom, type, prixT, quantité, category, id, format=None):
        product = InfoProduct.objects.get(tig_id=id)
        if product.quantityInStock == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = DonneeHistoSerializer(data={
                                                     'nameProd': nom,
                                                     'typeT': type,
                                                     'valeurT': prixT,
                                                     'quantityT': quantité,
                                                     'category': category
                                                })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
