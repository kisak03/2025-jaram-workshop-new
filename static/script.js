function showBattleResult() {
    document.getElementById('result-container').style.display = 'block';
}

function setCharacterText(data) {
    document.querySelector('input[name="character1_name"]').value = data.character1_name;
    document.querySelector('input[name="character1_text"]').value = data.character1_text;
    document.querySelector('input[name="character2_name"]').value = data.character2_name;
    document.querySelector('input[name="character2_text"]').value = data.character2_text;
}