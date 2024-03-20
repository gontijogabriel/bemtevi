// Função para obter o valor do token CSRF do cookie
function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            return cookie.substring('csrftoken='.length, cookie.length);
        }
    }
    return null;
}


async function validateForm() {
    const csrfToken = getCSRFToken();
    const email = document.getElementsByName('email')[0].value.trim();
    const password = document.getElementsByName('password')[0].value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (email !== '' && password !== '') {
        if (!emailRegex.test(email)) {
            openModalErro('Email inválido!');
        } else {
            try {
                const response = await fetch('/login_func/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': csrfToken
                    },
                    body: new URLSearchParams({
                        'email': email,
                        'password': password
                    })
                });

                if (response.ok) {
                    // Redirecionar ou fazer outras ações após o login bem-sucedido
                    window.location.href = '/home/';
                    console.log('login realizado!');
                    return await response.json();
                } else {
                    const data = await response.json();
                    openModalErro(data.message);
                }
            } catch (error) {
                openModalErro('Erro ao fazer login ' + error);
            }
        }
    } else {
        openModalErro('Campos inválidos');
    }
}