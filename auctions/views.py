from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

import datetime
from .models import *

CATEGORIES = ['Food', 'Toys', 'Fitness', 'Productivity', 'Electronics',
              'Clothing', 'Music', 'Decoration', 'Misc']

class Create_listing(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    starting_bid = forms.FloatField()
    image_url = forms.CharField()

    category_list = tuple((i,c) for i,c in enumerate(CATEGORIES))
    category = forms.ChoiceField(choices=category_list)
    
    
def index(request):
    items = Listing.objects.all()
    return render(request, "auctions/index.html", {
        'listings': items, 'empty': len(items)==0
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def creation_view(request):
    listing = Create_listing()
    return render(request, 'auctions/create.html', {
        'listing': listing
    })

@login_required()
def create_form(request):
    if request.method == 'POST':
        form = Create_listing(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            img = form.cleaned_data['image_url']
            price = form.cleaned_data['starting_bid']
            category = CATEGORIES[int(form.cleaned_data['category'])]

            new_listing = Listing(
                name = name, image = img, description = description,
                category = category, date =  datetime.datetime.now())
            new_listing.save()
            starting_bid = Bid(amount = price, user=request.user, listing=new_listing)
            starting_bid.save()

    return HttpResponseRedirect(reverse("index"))
    
