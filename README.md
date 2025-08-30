# 2025년 JARAM 워크샵 대체과제
<img width="341" height="462" alt="screenshot" src="https://github.com/user-attachments/assets/1a48c6ba-41ad-4c6e-9cc3-aad3aa4408a0" />

https://github.com/user-attachments/assets/4ed3641e-34cd-4dcc-8c8e-7faef703b6d9

이 프로젝트는 [텍스트 배틀](https://plan9.kr/battle/#test) 게임 사이트의 모의 배틀 부분을 클론코딩한 웹 사이트입니다.  
사용자는 캐릭터의 이름과 캐릭터의 설명을 적을 수 있습니다. 이 때 캐릭터의 설명은 100자 이내로만 적을 수 있습니다.  
2개의 캐릭터 이름과 설명을 적은 후 전투를 시작하면 구글 Gemini가 캐릭터의 설명을 바탕으로 대결을 해주며 이에 대한 승패를 제공해줍니다.

## 사용 방법
1. [uv 가상 환경 설치](https://github.com/astral-sh/uv)
2. uv를 이용한 python 가상 환경 세팅
```
uv sync
.\.venv\Scripts\activate
uv pip install -r requirements.txt
```
3. 구글 Gemini API 키 발급
4. 루트 디렉토리에 .env 파일 생성 후 발급받은 Gemini API 키를 입력
```
# .env file
GEMINI_API_KEY=<API KEY>
```
5. 데이터베이스 생성
```
python manage.py migrate
```
6. Django 서버 시작
```
python manage.py runserver
```
7. 웹사이트에 접속해 두 캐릭터의 이름과 100자 이내의 설명을 입력한 뒤 "전투 시작" 버튼 클릭
8. Gemini가 캐릭터의 설명을 바탕으로 전투를 진행한 후 전투의 결과와 해설을 생성하여 보여줌
9. 입력한 캐릭터 내용을 저장하거나 불러올 수 있음 (저장, 불러오기 기능은 로그인 필요)
   - 회원가입, 로그인 : "<서버 주소>/common"에서 가능

## 주요 구현 기능

- 캐릭터 대결 : 캐릭터 이름과 100자 이내의 설명을 입력하면 Gemini API를 이용해 전투의 결과와 해설을 생성하여 보여줌
- 캐릭터 저장, 불러오기: 사용자가 입력한 캐릭터를 저장하고, 드롭다운에서 선택하여 불러올 수 있음
- 회원가입/로그인: Django 기본 인증 시스템을 이용해 회원가입, 로그인 기능 구현

## 기술 스택

- Django (백엔드, 인증, ORM)
- Gemini API (AI 텍스트 생성)
- HTML/CSS/JavaScript
- SQLite

## 프로젝트 참여 인원
- 38기 조인준
- 38기 김이삭