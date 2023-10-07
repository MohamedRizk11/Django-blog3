from django.views import generic
from .models import post



class postlist(generic.ListView):
    model= post

class postdetail(generic.DetailView):
    model=post


class         