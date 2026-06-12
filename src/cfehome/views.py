from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

def home_view(request,*args,**kwargs):
    return about_view(request,*args,**kwargs)
    

def about_view(request,*args,**kwargs):
    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    try:
        percent=(page_qs.count()*100.0)/qs.count()
    except:
        percent=0
    context={
        'mypage' : 'My_Page_Title',
        'page_visits_count':page_qs.count(),
        'Percent':percent,
        'total_vists_count':qs.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request,"home.html",context)