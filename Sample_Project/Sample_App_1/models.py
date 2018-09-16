from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class BaseTable(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    CustomerID = models.IntegerField()
    Account = models.TextField(max_length=100)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('Sample_App_1_basetable_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('Sample_App_1_basetable_update', args=(self.pk,))


