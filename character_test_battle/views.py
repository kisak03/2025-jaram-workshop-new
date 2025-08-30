import os
from django.shortcuts import render
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def index(request):
    if request.method == "POST":
        post_data = request.POST
        battle_result = battle(post_data)

        return render(request, "character_test_battle/test_battle.html", battle_result)

    return render(request, "character_test_battle/test_battle.html")

def battle(input_data):
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    character = [{}, {}]
    character[0]['name'] = input_data.get("character1_name")
    character[0]['text'] = input_data.get("character1_text")
    character[1]['name'] = input_data.get("character2_name")
    character[1]['text'] = input_data.get("character2_text")

    message = f"""
        너는 웹툰 전투 해설자다.
        사용자 두 명의 "능력"을 바탕으로, 대결 상황을 장난스럽고 긴박하게 요약해라.
        규칙:

        - 첫번째 문장에는 "<캐릭터 이름> 승리!" 형식으로 승패 결과를 포함
        - 최대 100자 이내
        - 승패 결과를 나타내는 첫번째 문장을 제외하고 3~4문장으로만 작성
        - 결말은 무조건 명확해야 한다 (승패 결과 포함)
        - 과장된 표현과 의성어를 사용해도 좋다.
        - 예시 스타일:
            - "나의 역전 능력이 폭발! 이유찬은 그대로 무릎 꿇고 패배했다!"
            - "시간을 멈춘 이유찬, 하지만 내 능력이 그걸 뚫고 승리! 압도적이었다."
        입력:
        - A 이름: {character[0]['name']}
        - A 능력: {character[0]['text']}
        - B 이름: {character[1]['name']}
        - B 능력: {character[1]['text']}
        - 상황: {character[0]['name']}와 {character[1]['name']}이 링 위에서 싸웠다.

        출력 예시: 나 승리! 이유찬이 시간을 멈추려는 순간, 내 역전 능력이 폭발! 결국 이유찬은 KO, 나의 완벽한 승리!
    """

    response = model.generate_content(message)
    print("[AI 답변]\n" + response.text)

    result, text = response.text.split('!', 1)
    result += "!"

    return {
            'battle_result': {
                    'character1_name' : character[0]['name'],
                    'character1_text' : character[0]['text'],
                    'character2_name' : character[1]['name'], 
                    'character2_text' : character[1]['text'],
                    'result' : result,
                    'text' : text,
            }
    }