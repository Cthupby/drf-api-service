from django.urls import path

from api.views import (
    CargoCreate,
    CargoList,
    CargoUpdate,
    CargoRemove,
)


urlpatterns = [
    path("api/create_cargo", CargoCreate.as_view()),
    path("api/cargo_list", CargoList.as_view()),
    path("api/update_cargo/<int:pk>", CargoUpdate.as_view()),
    path("api/remove_cargo/<int:pk>", CargoRemove.as_view()),
]
