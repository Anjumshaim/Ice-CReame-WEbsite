from multiprocessing    import context 
from django.shortcuts import render,HttpResponse
from home.models import Contact

def index(request):
     context={



     }
     return  render(request,'index.html',context)



     
def about(request):
     return  render(request,'about.html',)


def services(request):
     return  render(request,'services.html',) 
               

def contact(request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          password = request.POST.get('password')
          address= request.POST.get('address')
          address2 = request.POST.get('address2')
          city = request.POST.get('city')
          Contact = Contact(name=name, email=email,password=password,address=address,address2=address2,city=city,)
          contact.save()
     
     return  render(request,'contact.html',)

