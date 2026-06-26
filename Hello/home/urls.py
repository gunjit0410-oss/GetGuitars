from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("contact/", views.contact, name='contact'),
    path("acoustic/", views.acoustic, name='acoustic'),
    path("electric/", views.electric, name='electric'),
    path("bass/", views.bass, name='bass'),
    path("ukulele/", views.ukulele, name='ukulele'),
    path("covers/", views.covers, name='covers'),
    path("straps/", views.straps, name='straps'),
    path("amplifiers/", views.amplifiers, name='amplifiers'),
    path("picks/", views.picks, name='picks'),
    path('login/',views.loginUser, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path("search/", views.search, name='search'),
    # API endpoints
    path("api/guitars/", views.api_guitar_list, name='api_guitar_list'),
    path("api/guitars/<int:guitar_id>/", views.api_guitar_detail, name='api_guitar_detail'),
    path("api/contact/", views.api_contact_submit, name='api_contact_submit'),
]