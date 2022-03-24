from django.urls import path
from monTiGMagasin import views
from django.urls import register_converter

class FloatConverter:
    regex = "[\d\.\d]+"

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return "{}".format(value)


register_converter(FloatConverter, "float")

urlpatterns = [
    path('', views.InfoProductList.as_view(), name='projectRoot'),
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('incrementForStock/<int:tig_id>/<int:number>/', views.IncrementAndReturnStock.as_view()),
    path('decrementForStock/<int:tig_id>/<int:number>/<int:vente>/', views.DecrementAndReturnStock.as_view()),
    path('putonsaleForStock/<int:tig_id>/<float:newpromo>/', views.PutOnSaleAndReturn.as_view()),
    path('removesaleForStock/<int:tig_id>/', views.RemoveOnSaleAndReturn.as_view()),
    path('donneesHisto/', views.ListTransaction.as_view()),
    path('detailHisto/<int:id>/', views.DetailTransaction.as_view()),
]
