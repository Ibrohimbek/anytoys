import logging

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from api.serialisers import ToySerializer
from core.models import Toy

logger = logging.getLogger(__name__)


class ToyViewSet(ModelViewSet):
    serializer_class = ToySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Toy.objects.all()
