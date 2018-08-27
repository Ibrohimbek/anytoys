import logging
import uuid

from django.utils import timezone
from django.db import models

from core.models.base import BaseModel

logger = logging.getLogger(__name__)


def photos_upload_path(instance, filename):
    current_dt = timezone.now()
    return 'photos/{day}/{uuid}/{filename}'.format(
        day=current_dt.strftime('%Y/%m/%d'),
        uuid=uuid.uuid4().hex,
        filename=filename
    )


class Toy(BaseModel):
    DONATION = 'donation'
    RENT = 'rent'
    SALE = 'sale'

    SALE_TYPE = (
        (DONATION, 'Donation'),
        (RENT, 'Rent'),
        (SALE, 'Sale'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    photo = models.ImageField(upload_to=photos_upload_path, blank=True, null=True)

    type = models.CharField(max_length=50, choices=SALE_TYPE, default=SALE)
    owner_name = models.CharField(max_length=100, blank=True, default='')
    owner_phone_number = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.id < 42:
            return "static/photos/{}.jpg".format(self.id)

        return "static/photos/0.jpg"
