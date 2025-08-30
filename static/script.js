function showBattleResult() {
    document.getElementById('result-container').style.display = 'block';
}

function setCharacterText(data) {
    document.querySelector('input[name="character1_name"]').value = data.character1_name;
    document.querySelector('input[name="character1_text"]').value = data.character1_text;
    document.querySelector('input[name="character2_name"]').value = data.character2_name;
    document.querySelector('input[name="character2_text"]').value = data.character2_text;
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function saveCharacter(character) {
    let characterNameTag = character + "_name"
    let characterTextTag = character + "_text"
    const name = document.querySelector(`input[name="${characterNameTag}"]`).value;
    const text = document.querySelector(`input[name="${characterTextTag}"]`).value;
    if (name === "" || text === "") {
        alert("내용을 입력해주세요")
        return
    }
    const csrftoken = getCookie('csrftoken');

    fetch('api/save_character/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ name, text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.result === "ok") {
            alert("저장 완료");
        } else if (data.result === "login required") {
            alert("로그인 필요")
            window.location.href = "/common/login"
        } else {
            alert("저장 실패");
        }

        setCharacterSelect();
    });
}

function setCharacterSelect() {
    let selects = []
    selects.push(document.querySelector('select[name="character1_select"]'));
    selects.push(document.querySelector('select[name="character2_select"]'));
    const csrftoken = getCookie('csrftoken');

    fetch('api/get_characters/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        selects.forEach(select => {
            select.innerHTML = "";
            data.characters.forEach(character => {
                const option = document.createElement('option');
                option.value = character.id;
                option.textContent = character.name;
                select.appendChild(option);
            });
        });
    });
}

function loadCharacter(character) {
    const select = document.querySelector(`select[name="${character}_select"]`);
    const characterName = select.value;
    fetch(`/api/get_character/?id=${encodeURIComponent(characterName)}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)

            if (data.name && data.text) {
                document.querySelector(`input[name="${character}_name"]`).value = data.name;
                document.querySelector(`input[name="${character}_text"]`).value = data.text;
            } else {
                alert("캐릭터 정보를 찾을 수 없음");
            }
        });
}