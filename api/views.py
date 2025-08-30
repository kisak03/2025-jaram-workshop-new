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

def get_characters(request):
    if not request.user.is_authenticated:
        return JsonResponse({"result": "login required"})

    characters = CharacterDB.objects.filter(user=request.user)
    data = []
    for charcter in characters:
        data.append({
                "id": charcter.id,
                "name": charcter.name,
                "text": charcter.text
            }
        )
    return JsonResponse({"characters": data})

def get_character(request):
    if not request.user.is_authenticated:
        return JsonResponse({"result": "login required"})

    character_id = request.GET.get("id")
    print("[debug]", character_id)
    character = CharacterDB.objects.filter(user=request.user, id=character_id).first()


    if character:
        return JsonResponse({
            "name": character.name,
            "text": character.text,
        })
    else:
        return JsonResponse({"result": "fail"})