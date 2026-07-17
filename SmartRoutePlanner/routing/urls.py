from django.urls import path
from . import views
urlpatterns = [
    path('',views.mainreq),
    path('calculate-route/',views.calculate_route, name="calculate_route")
]
