from django.views import generic
from .models import post



class postlist(generic.ListView):
    model= post

class postdetail(generic.DetailView):
    model=post


class ADDpost(generic.CreateView):
    model=post
    fields=['auther','title','content','tags','image']       
    success_url='/blog/'


class Editpost(generic.UpdateView):
    model=post
    fields=['auther','title','content','tags','image']       
    success_url='/blog/'  
    template_name='posts/post_edit.html'  

class deletepost(generic.DeleteView):
    model=post
    success_url='/blog/'