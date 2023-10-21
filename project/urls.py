

from django.contrib import admin
from django.urls import path
from app import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.home,name="home"),
    path('',views.save,name="save"),
    # path('show/',views.show,name="show"),
    # path('pay/<int:id>/',views.pay_now,name="pay"),
    # path('card/',views.card_pay, name="card"),
    # path('bank/',views.bank_pay,name="bank"),
    # path('payment/',views.pay_detalis,name="payment")
]


