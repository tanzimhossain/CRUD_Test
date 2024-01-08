from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("add/", add, name="add"),
    path("addrec/", addrec, name="addrec"),
    path("delete/<int:id>", delete, name="delete"),
    path("update/<int:id>", update, name="update"),
    path("update/uprec/<int:id>", uprec, name="uprec"),
]