from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'basetable', api.BaseTableViewSet)

from .API_Sample import GetBaseTableAPI                           ###Line added

urlpatterns = [
            url(r'^CalltoAPI', GetBaseTableAPI.as_view(), name='CalltoAPI')
]

