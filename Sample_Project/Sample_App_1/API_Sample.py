from __future__ import unicode_literals

from django.http import JsonResponse
from django_pandas.io import read_frame
from rest_framework.views import APIView

from .models import BaseTable


class GetBaseTableAPI(APIView):
    def get(self, request):
        skus_df = read_frame(BaseTable.objects.values()).to_json()
        return JsonResponse(skus_df, safe=False)