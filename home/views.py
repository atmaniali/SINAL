from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

#presentations

class Certafications(TemplateView):
    template_name = 'home/presentation/certafication.html'


class Chiffre(TemplateView):
    template_name = 'home/presentation/chiffre_cle.html' 


class Mission(TemplateView):
    template_name = 'home/presentation/missions.html' 


class Services(TemplateView):
    template_name = 'home/presentation/services.html' 

# refernces

class Edp(TemplateView):
    template_name = 'home/refernce/edp.html' 


class Esl(TemplateView):
    template_name = 'home/refernce/esl.html'  


# service apres vente

class Fdd(TemplateView):
    template_name = 'home/SAP/fdd.html' 

# comercial
 
class Fddevis(TemplateView):
    template_name = 'home/comercial/fddevis.html'   

# cordonnes

class Coordonnes(TemplateView):
    template_name= 'home/cordonnes.html' 


# produit


class InstrumentationAnalytique(TemplateView):
    template_name= 'home/produit/ia.html' 


class ECL(TemplateView):
    template_name= 'home/produit/ecl.html'     





