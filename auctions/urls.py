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
    path("wishlist", views.wishlisted, name='wishlist'),
    path('bid_redirect/<str:id>', views.listing_bid, name='add_bid'),
    path('comment_redirect/<str:id>', views.listing_comment, name='add_comment')
]
