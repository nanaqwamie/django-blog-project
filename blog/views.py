# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    #print type(post_list)
    #print post_list
    
    return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
    p = Post.objects.get(pk=id)
    return HttpResponse(p)
	    



def post_search(request, term):
    result=Post.objects.filter(body_container=term)
    temp=''
    for x in result:
        temp='<u1><li><em>'+str(i)+'</em><li><u1>'
    
    return HttpResponse(res)
def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
