# insights/urls.py

from django.urls import path
from .views import InsightList

urlpatterns = [
    path('insights/', InsightList.as_view(), name='insight-list'),
]
