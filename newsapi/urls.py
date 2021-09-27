from newsapi import views
from django.urls import path


urlpatterns = [
    path('',views.index,name="index"),
    path('india',views.india,name="india"),
    path('america',views.america,name="america"),
    path('russia',views.russia,name="russia"),



    path('hindi',views.hindi,name="hindi"),
    path('english',views.english,name="english"),
    path('russian',views.russian,name="russian"),


    path('business',views.business,name="business"),
    path('entertainment',views.entertainment,name="entertainment"),
    path('general',views.general,name="general"),
    path('health',views.health,name="health"),
    path('science',views.science,name="science"),
    path('sports',views.sports,name="sports"),
    path('technology',views.technology,name="technology"),




]
