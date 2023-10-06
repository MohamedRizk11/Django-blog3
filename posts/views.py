from django.shortcuts import render,redirect
from .models import post
from .forms import postforms

# Create your views here.
def post_list(request):
    data = post.objects.all()  #orm==>sql-->db-->list
    return render(request,'posts.html',{'posts':data})



def post_detail(request,post_id):
    date=post.objects.get(id=post_id)
    return render(request,'post_detail.html',{'post':date})


def add_post(request):
    if request.method=='POST':
        form=postforms(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.auther=request.user
            myform.save()
            return redirect('/blog/')
    else:    
        form= postforms
    return render(request,'add_post.html',{'form':form})


def edit_post(request,post_id):
    data=post.objects.get(id=post_id)
    if request.method=='POST':
        form=postforms(request.POST,request.FILES,instance=data)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.auther=request.user
            myform.save()
            return redirect('/blog/')
    else:    
        form= postforms(instance=data)
    return render(request,'edit_post.html',{'form':form})
