from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # What tag applied to What object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    # We need 2 things:
    # 1. Object Type
    # 2. ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    object_content = GenericForeignKey()
