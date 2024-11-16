#define URL route for index() view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet, MenuItemView, SingleMenuItemView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
   path('', views.index, name='index'),  # Route for the index view
    path('', include(router.urls)),      # Include router-generated URLs
    path('api-token-auth/', obtain_auth_token)
]
