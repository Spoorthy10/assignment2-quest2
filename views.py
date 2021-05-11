from django.shortcuts import render
import datetime
# Create your views here.

def sample(request):
    date=datetime.datetime.now()
    return render(request, "page.html",{'dt':date, 'sname':'dimple', 'sroll':'py12',
     'sbranch':'django', 'saddress':'bangalore'})