from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"all_basball_leages":League.objects.filter(sport__contains='Baseball'),
		"all_womens_leagues":League.objects.filter(name__contains="women"),
		"hockey_leagues":League.objects.filter(sport__contains="hockey"),
		"leagues_without_football":League.objects.exclude(sport__contains="football"),
		"conferences_leagues":League.objects.filter(name__contains="Conferences"),
		"Atlantic_leagues":League.objects.filter(teams__location="Atlanta"),
		"Atlantic_leagues":League.objects.filter(teams__location="Atlanta"),
		"Dallas_teams":Team.objects.filter(location='Dallas'),
		"raptors_teams":Team.objects.filter(team_name='Raptors'),
		"city":Team.objects.filter(location__contains='city'),
		"starts_with_T":Team.objects.filter(team_name__startswith='T'),
		"order_teams":Team.objects.order_by("location"),
		"reverse_order_teams":Team.objects.order_by("-team_name"),
		"last_name_cooper":Player.objects.filter(last_name="Cooper"),
		"first_name_joshua":Player.objects.filter(first_name="Joshua"),
		"last_name_cooper_except":Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"fname_alexander_or_wyatt":Player.objects.filter(first_name__in=["Alexander","Wyatt"]),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")