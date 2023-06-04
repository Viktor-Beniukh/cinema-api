from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("api/cinema/genres", GenreViewSet)
router.register("api/cinema/actors", ActorViewSet)
router.register("api/cinema/cinema_halls", CinemaHallViewSet)
router.register("api/cinema/movies", MovieViewSet)
router.register("api/cinema/movie_sessions", MovieSessionViewSet)
router.register("api/cinema/orders", OrderViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "cinema"
