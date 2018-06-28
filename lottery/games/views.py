from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required

from games.models import Game,Alpab

# Create your views here.
@login_required
def available_games_list(request):
	return render(request, 'games/games.html', {
        'available_games': Game.objects.available_games(request.user)
    })

def Alpha(request):
    data = Alpab.objects.all()

    stu = {"Alphad": data}

    return render_to_response("home/home.html",context= stu)