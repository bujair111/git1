from django.urls import path
from . import views 
app_name='facebook'


urlpatterns = [
    path('',views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('mypage',views.mypage, name='my')
]
