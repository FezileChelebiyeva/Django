from django.urls import path, re_path
from women import views


# urlpatterns = [
#     path("",views.index, name="Home"), #view - sorgu emal eden teqdimat funksiyasini
#     path("about/", views.about, name="About"),# name - yolun(marsurtun) adi
#     path("contact/", views.contact, name="Contact")
# ]
urlpatterns = [
    path('', views.index),
    re_path(r'^about', views.about),
    re_path(r'^contact', views.contact),
    re_path(r'^archive/(?P<year>[0-9]{4})/',views.archive),
    re_path(r"^users/(?P<username>\w+)/", views.users),
    path('categories/',views.categories, kwargs={"name":"Fezile","age":20}),
    #kwargs - teqdimat funksiyasina gonderilen elave arqumentler
    path("user", views.user), #defoult verdiyimiz deyerleri gormek ucun
    path("user/<name>", views.user), #defoult verdiyimiz deyerleri gormek ucun
    path("user/<str:name>/<int:age>", views.user),]
# re_path - ^about  ifadəsi ünvanın “about” ilə başlamalı olduğunu bildirir. 
# path funksiyasında olduğu kimi, "about" sətirinə tam uyğun gəlməməlidir.
