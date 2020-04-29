from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('search-customer/', views.search_customer, name='search-customer'),
    path('search-distributor/', views.search_Distributor, name='search-distributor'),
    path('search-product/', views.search_product, name='search-product'),
    path('track-delivery/', views.track_delivery, name='track-delivery'),
    path('Analysis.htm', views.analysis, name='analysis'),
    path('NewRecords.htm', views.newrecord, name='newrecord'),
    path('Shoprecords.htm', views.shoprecord, name='shoprecord'),
    path('chartj', views.chartj, name='chartj'),
    path('chartjy', views.chartjy, name='chartjy'),
    path('chart', views.charts, name='charts'),
    path('chartsy', views.chartsy, name='chartsy'),
    path('chartoe', views.chartoe, name='chartoe'),
    path('chartoey', views.chartoey, name='chartoey'),
    path('purchasechart', views.purchasechart, name='purchasechart'),
    path('purchasecharty', views.purchasechartyear, name='purchasecharty'),
    path('salechart/', views.salechart, name='salechart'),
    path('oechart', views.oechart, name='oechart'),
    path('oecharty', views.oecharty, name='oecharty'),
    path('salechartyear', views.salechartyear, name='salechartyear'),
    path('chartpl', views.chartpl, name='chartpl'),
    path('chartply', views.chartply, name='chartply'),
    path('plchart', views.profitchart, name='plchart'),
    path('plcharty', views.profitcharty, name='plcharty'),
    path('test', views.salechartcrm, name='tes'),
    path('testy', views.salechartcry, name='tesy'),
    path('testpm', views.purchasechartcrm, name='testpm'),
    path('testpy', views.purchasechartcry, name='testpy'),
    path('testoem', views.oechartcrm, name='testoem'),
    path('testoey', views.oechartcry, name='testoey'),
    path('testplm', views.profitchartcrm, name='testplm'),
    path('testply', views.profitchartcry, name='testply'),
]