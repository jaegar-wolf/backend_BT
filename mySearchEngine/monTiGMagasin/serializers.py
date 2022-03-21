from rest_framework.serializers import ModelSerializer
from monTiGMagasin.models import InfoProduct, DonneeHisto

class InfoProductSerializer(ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = ('id', 'tig_id', 'name', 'category', 'price', 'unit', 'availability', 
        'sale', 'discount', 'comments', 'owner', 'quantityInStock', 'percentage_reduc', 'quantitySold')


class DonneeHistoSerializer(ModelSerializer):
    class Meta:
        model = DonneeHisto
        fields = "__all__"