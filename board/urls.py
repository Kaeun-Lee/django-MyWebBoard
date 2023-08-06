from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:board_id>", views.detail, name="detail"),
    path("write", views.write, name="write"),
    path("create_post", views.create_post, name="create_post"),
]
