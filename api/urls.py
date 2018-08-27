from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter

from api.viewsets import ToyViewSet


router = SimpleRouter()
router.register(r'toys', ToyViewSet, base_name='toy')


urlpatterns = [
    url(r'^', include(router.urls)),
]
