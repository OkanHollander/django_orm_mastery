from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("new/", views.new, name="new"),
]
