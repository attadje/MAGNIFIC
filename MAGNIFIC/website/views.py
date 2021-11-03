from django.shortcuts import render
from django.views import View

# Create your views here.

class LandingPage(View):
    
    template_name = 'landing-page.html'

    def get(self, request):
        return render(request , self.template_name, {})