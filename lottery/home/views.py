from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import datetime,time
from games.models import Alpab
# Create your views here.
def home(request):
    #delta = datetime.datetime(0000,00,00 21:00:0) - datetime.datetime.now()
    #print(delta)
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    ddata = Alpab.objects.all()[::-1]
    data=ddata[:8]
    #data = ddata
    stu = {"Alphad": data,'dated':now}
    print(stu)

    return render(request, 'home.html',context=stu)

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request,'countdown.html')

def Alpha(request):
    data = Alpab.objects.all()

    stu = {"Alphad": data}
    print('Hello')

    print(stu)
    return render("home.html",context= data)

def dateDiffInSeconds(date1, date2):
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)
