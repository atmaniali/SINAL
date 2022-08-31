from django.urls import path, include
from . import views


urlpatterns = [
    # home
    path('', views.index, name='index'),
    # presentations
    path('Certafications/', views.Certafications.as_view(),name='certafication'),
    path('Chiffres cles/', views.Chiffre.as_view(),name='chiffres-cles'),
    path('Missions/', views.Mission.as_view(),name='missions'),
    path('Services/', views.Services.as_view(),name='services'),
    # refernce
    path('EDP/', views.Edp.as_view(),name='EDP'),
    path('ESL/', views.Esl.as_view(),name='ESL'),
    # service apres vente
    path('FDD/', views.Fdd.as_view(),name='FDD'),
    # comercial
    path('FDDevis/', views.Fddevis.as_view(),name='FDDevis'),
    # cordones
    path('Coordonnees/', views.Coordonnes.as_view(),name='coordonnees'),
    # produit
    path('Instrumentation Analytique/', views.InstrumentationAnalytique.as_view(),name='instrumentation-analytique'),
    path('ECL/', views.ECL.as_view(),name='ECL'),
]