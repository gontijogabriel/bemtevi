// Função para ajustar a altura do textarea
function ajustarAlturaTextarea(elemento) {
    elemento.style.height = 'auto';
    elemento.style.height = (elemento.scrollHeight) + 'px';
}

const textarea = document.getElementById('myTextarea');

textarea.addEventListener('input', function () {
    ajustarAlturaTextarea(this);
});

ajustarAlturaTextarea(textarea);

const tweetsTodosId = document.getElementById('tweetsTodos')
const tweetsSeguindoId = document.getElementById('tweetsSeguindo')
function tweetsSeguindo() {
    tweetsTodosId.style.fontWeight = ''
    tweetsTodosId.style.borderBottom = ''
    tweetsSeguindoId.style.fontWeight = 'bolder'
    tweetsSeguindoId.style.borderBottom = '2px solid'
}
function tweetsTodos() {
    tweetsTodosId.style.fontWeight = 'bolder'
    tweetsTodosId.style.borderBottom = '2px solid'
    tweetsSeguindoId.style.fontWeight = ''
    tweetsSeguindoId.style.borderBottom = ''
}

const btnSeguirId = document.getElementById('btnSeguir')
function btnSeguir() {
    btnSeguirId.innerText = 'Seguindo'
}

const idModalComment = document.getElementById('modal-comment')
function openModalComment() {
    idModalComment.style.display = 'block';
}
function closeModalComment() {
    idModalComment.style.display = 'none';
}