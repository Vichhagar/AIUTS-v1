from django.urls import path
from .  import views
from django.views import generic

app_name = 'User'

urlpatterns = [
    path('', views.UserList.as_view(), name='home'),
    path('detail/<str:pk>', views.UserDetail.as_view(), name='detail'),
    #path('create/', views.AddUser.as_view(), name='create'),
    path('create/', views.newUser, name='create'),
    #makeTransaction
    path('makeTransaction/', views.makeTransaction.as_view(), name='makeTransaction'),
    path('Transaction/', views.AllTransaction.as_view(), name='transaction'),
]