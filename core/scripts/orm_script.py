from core.models import Restaurant
from django.utils import timezone
from django.db import connection

def run():
    restaurants = Restaurant.objects.all()[0]
    print(restaurants)
    print(connection.queries)