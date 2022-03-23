from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.conf import settings
import json

#forms
from Library.forms import LoginForm

# models
from django.contrib.auth.models import User
from Library.models import Library



# Create your views here.
def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('Library:dashboard')
            else:
                return redirect('Library:login')
    else:
        form= LoginForm()
        return render(request,'pages-login.html',{'form' : form})
def Logout(request):
    logout(request)
    return redirect('Library:login')

class dashboard(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Home_page.html'
    def post(self, request):
        if request.method == 'POST' and request.is_ajax():
            if request.POST['action'] == 'search_event_action':
                pick_search=request.POST.get('search_key')
                print('pick_search',pick_search)
                search_db = Library.objects.filter(book_name__icontains= pick_search) | Library.objects.filter(
                    publish_date__icontains= pick_search)
                if len(search_db) > 0 and  len(pick_search) > 0:
                    data=[]
                    for pos in search_db:
                        items = {
                            'pk':pos.pk,
                            'book_name':pos.book_name,
                            'author' : pos.author,
                            'publish_date':pos.publish_date,
                            'image':str(pos.image.url),
                            'borrow_start_date':pos.borrow_start_date,
                            'borrow_end_date':pos.borrow_end_date,
                        }
                        data.append(items)
                    res= data
                else:
                    res= 'No result found..'
                return  JsonResponse({'data': res})

    def get(self, request):

        queryset = Library.objects.order_by('book_name')
            
            # pagination
            
        page = request.GET.get('page', 1)
        print('event_page',page)
        paginator = Paginator(queryset, 4)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
            
        
        context = {
            'Library': queryset,
            'users':users,
            }
        
        return Response(context)
class BookDetails(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Event.html'
    
    def get(self, request,pk):
        print('pk',pk)
        event_db=Library.objects.filter(pk=pk)
        print("event_db",event_db)
        context={
            "event_db":event_db,
            }
        return Response(context)
    
    
    
    
