from django.db import models


class Location(models.Model):
    zip_code = models.IntegerField(
        verbose_name="Почтовый индекс",
    )
    latitude = models.FloatField(
        verbose_name="Широта",
    )
    longitude = models.FloatField(
        verbose_name="Долгота",
    )
    city = models.CharField(
        max_length=256,
        verbose_name="Город",
    )
    state_name = models.CharField(
        max_length=256,
        verbose_name="Штат",
    )
    country_name = models.CharField(
        max_length=256,
        verbose_name="Страна",
    )

    def __str__(self):
        return f"{self.city}({self.zip_code})"

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Car(models.Model):
    car_number = models.CharField(
        max_length=124,
        verbose_name="Уникальный номер",
    )
    location = models.ManyToManyField(
        Location,
        related_name="car_location",
        verbose_name="Локация",
    )
    load_capacity = models.PositiveIntegerField(
        default=1,
        verbose_name="Грузоподъемность",
    )

    def __str__(self):
        return f"{self.car_number}"

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class Cargo(models.Model):
    location_pickup = models.ManyToManyField(
        Location,
        related_name="сargo_location_pickup",
        verbose_name="Локация: откуда забрать",
    )
    location_delivery = models.ManyToManyField(
        Location,
        related_name="сargo_location_delivery",
        verbose_name="Локация: куда доставить",
    )
    cargo_weight = models.PositiveIntegerField(
        default=1,
        verbose_name="Вес груза",
    )
    cargo_description = models.TextField(
        max_length=2300,
        verbose_name="Описание груза",
    )

    def __str__(self):
        return f"{self.cargo_description}"

    class Meta:
        verbose_name = "Груз"
        verbose_name_plural = "Грузы"
