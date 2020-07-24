
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auths/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auths/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns += router.urls


