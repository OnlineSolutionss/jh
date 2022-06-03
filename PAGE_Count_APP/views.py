from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
#<h2> Create your views here.

def Details(request, pk):
    post = Post.objects.filter(id = pk)
    ct = request.session.get('cart', 0)
    already_added = ct + 1
    request.session['cart'] = already_added
    return render(request, 'session/setsession.html',{'post':post, 'added':already_added})

def Page_Count(request):
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    allpost = Post.objects.all()
    return render(request, 'session/pagecount.html',{'counter':newcount, 'post':allpost})

def set_session (request):
    request.session['name'] = 'krishns'
    return render(request, 'session/setsession.html')

def get_session(request):
    if 'name' in request.session:
        return_session_valuess = request.session['name']
        request.session.modified = True
        return render(request, 'session/getsession.html')
    else:
        return HttpResponse('<h2>Your Session Has Been Expired Login Again <h2>')

def delete_session(request):
    if 'name' in request.session:
        request.session.flush()
        request.session.clear_expired()
        return render(request, 'session/delsession.html')
    else:
        return HttpResponse('<h2>Your Session Has Been Expired Login Again <h2>')