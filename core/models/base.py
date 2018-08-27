from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
