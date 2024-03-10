// INICIO - Modal Erro
function openModalErro(text) {
    const mdText = document.getElementById('md-text');
    mdText.innerText = text

    const modal = document.getElementById('md-error');
    modal.style.display = 'block';

    setTimeout(closeModalErro, 10000);
}

function closeModalErro() {
    const modal = document.getElementById('md-error');
    modal.style.display = 'none';
}
// FIM - Modal Erro