from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.index, name='index'),
    path('static/<name>', views.staticfiles, name='sttic'),
    path('menu/items', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/',obtain_auth_token),
]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
