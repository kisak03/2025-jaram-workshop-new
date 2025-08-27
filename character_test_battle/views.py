from django.shortcuts import render

def index(request):
    return render(request, "character_test_battle/test_battle.html")
