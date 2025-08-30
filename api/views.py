import json
from django.http import JsonResponse
from common.models import CharacterDB

def save_character(request):
    if not request.user.is_authenticated:
        return JsonResponse({"result": "login required"})

    if request.method == "POST":
        data = json.loads(request.body)
        user = request.user

        character = CharacterDB(
            user=user,
            name=data.get("name"),
            text=data.get("text")
        )
        character.save()

        return JsonResponse({"result": "ok"})

    return JsonResponse({"result": "fail"})