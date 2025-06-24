from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.creation_view, name="creation_view"),
    path("listing_redirect", views.create_form, name='create_form'),
    path("listing/<str:id>", views.listing_view, name='listing_view'),
    path("wishlist", views.wishlisted, name='wishlist')
]
