function openModal() {
    var modal = document.getElementById('myModal');
    modal.style.display = 'block';
}

function closeModal() {
    var modal = document.getElementById('myModal');
    modal.style.display = 'none';
}

// Fechar o modal se clicar fora da área do modal
window.onclick = function(event) {
    var modal = document.getElementById('myModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};

function like(tweetId, userId) {
    console.log('LIKE / id_user: ' + userId + ' id_tweet: ' + tweetId);

    // Obtenha o token CSRF do cookie
    const csrftoken = getCookie('csrftoken');

    fetch('/likes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,  // Inclua o token CSRF no cabeçalho
            // Adicione outros cabeçalhos conforme necessário
        },
        body: new URLSearchParams({
            'id_tweet': tweetId,
            'id_user': userId,
            // Adicione outros parâmetros conforme necessário
        }),
    }).then(() => {
        // Recarrega a página após a execução da função
        location.reload();
    });
}

// Função para obter o valor do cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
