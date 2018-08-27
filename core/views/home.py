from django.shortcuts import redirect
from django.views.generic import ListView

from core.forms import ToyForm
from core.models import Toy


class HomeView(ListView):
    template_name = 'core/home.html'
    context_object_name = 'toys'

    def get_queryset(self):
        return Toy.objects.all().order_by('-created_at')

    def post(self, request):
        form = ToyForm(data=request.POST)

        if form.is_valid():
            form.save()

        return redirect('home')
