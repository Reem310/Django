from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"atlantic_soccer_teams": Team.objects.filter(league__name='Atlantic Soccer Conference'),
		"curr_boston_players": Player.objects.filter(curr_team__team_name='Penguins',curr_team__location='Boston'),
		"Baseball_curr_players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"american_curr_players": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football", last_name='Lopez'),
		'football_players':Player.objects.filter(curr_team__league__sport="Football"),
		'sophia_teams':Team.objects.filter(curr_players__first_name="Sophia"),
		'sophia_leagues':League.objects.filter(teams__curr_players__first_name="Sophia"),
		'Flores_not_in_Roughriders':Player.objects.filter(last_name='Flores').exclude(curr_team__location='Washington',curr_team__team_name='Roughriders'),
		'Samuel_teams':Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		'Tiger_Cats_Players':Player.objects.filter(all_teams__location="Manitoba", all_teams__team_name='Tiger-Cats'),
		'vikings_formerly_players':Player.objects.filter(all_teams__location="Wichita" , all_teams__team_name="Vikings").exclude(curr_team__location="Wichita", curr_team__team_name='Vikings'),
		'jacob_former_teams':Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(team_name='Colts', location='Oregon'),
		'all_joshua_in_atlantic':Player.objects.filter(first_name="Joshua", all_teams__league__name='Atlantic Federation of Amateur Baseball Players'),
		'12_players_teams':Team.objects.annotate(counter=Count('all_players')).filter(counter__gte=12),
		'players_and_counts':Player.objects.annotate(counts=Count('all_teams')).order_by('counts'),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")