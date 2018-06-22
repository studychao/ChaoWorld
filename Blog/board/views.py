from django.shortcuts import render, get_object_or_404, redirect,HttpResponseRedirect
from django.urls import reverse
from .models import usercomment
from .forms import commentform
from myplace.views import board
from django.contrib import messages
# Create your views here.

def user_comment(request):

    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('../../board?show=1')
        else:
            comment_list = usercomment
            context = {'form':form , 'comment_list':comment_list}
            return render(request,'myplace/board.html',context=context,show=show)


    return redirect('../../board')

