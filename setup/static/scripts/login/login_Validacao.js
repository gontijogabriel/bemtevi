// Função para obter o valor do token CSRF do cookie
function getCSRF(name) {
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


function validateForm() {
    const email = document.getElementsByName('email')[0].value.trim();
    const password = document.getElementsByName('password')[0].value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (email !== '' && password !== '') {
        if (!emailRegex.test(email)) {
            openModalErro('Email inválido!');
        } else {
            fetch('/login_func/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCSRF('csrftoken')  // Obtendo o token CSRF
                },
                body: new URLSearchParams({
                    'email': email,
                    'password': password
                })
            })
            .then(response => {
                if (response.ok) {
                    // Redirecionar ou fazer outras ações após o login bem-sucedido
                    window.location.href = '/home/';
                    console.log('login realizado!')
                    return response.json();
                } else {
                    // Tratar erros de login
                    return response.json().then(data => {
                        openModalErro(data.message);
                    }).catch(error => {
                        openModalErro('Erro ao fazer login');
                    });
                }
            })
            .catch(error => {
                openModalErro('Erro:', error);
            });
        }
        
    } else {
        openModalErro('Campos inválidos');
    }
}


