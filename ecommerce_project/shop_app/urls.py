from django.urls import path
from. import views
app_name='shop_app'

urlpatterns = [
    path('',views.allprodcat,name='allprodCat'),
    path('<slug:c_slug>/',views.allprodcat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),

]