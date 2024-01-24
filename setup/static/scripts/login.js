// Gera CSRF_Token
function getCookie(name) {
    let cookieValue = null
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';')
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim()
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break
            }
        }
    }
    return cookieValue
}

// Login usuario
async function loginUsuario() {
    var formulario = document.getElementById('formLogin')
    var dadosFormulario = new FormData(formulario);

    const csrftoken = getCookie('csrftoken');

    try {
        var resposta = await fetch('/login_user/', {
            method: 'POST',
            body: dadosFormulario,
            headers: {
                'X-CSRFToken': csrftoken
            }
        });
    } catch (erro) {
        console.error('Erro na requisição:', erro);
    }
}
