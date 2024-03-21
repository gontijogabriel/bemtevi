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


document.addEventListener("DOMContentLoaded", function() {
    const profileImage = document.getElementById("profile-image");
    const currentImage = document.getElementById("current-image");

    profileImage.addEventListener("click", function() {
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = 'image/*';
        input.onchange = function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = function() {
                    currentImage.src = reader.result;
                    // Aqui você pode enviar a imagem para o servidor ou fazer qualquer outra coisa com ela
                };
            }
        };
        input.click();
    });
});

// INICIO - Funcionalidade para ver a senha
const inputType1 = document.getElementById('input-password-1')
const inputType2 = document.getElementById('input-password-2')
const eyeOpen = document.getElementById('input-eye-open')
const eyeClose = document.getElementById('input-eye-close')

function openPassword () {
    inputType1.type = 'text'
    inputType2.type = 'text'
    eyeOpen.style.display = 'none'
    eyeClose.style.display = 'flex'
}
function closePassword () {
    inputType1.type = 'password'
    inputType2.type = 'password'
    eyeOpen.style.display = 'flex'
    eyeClose.style.display = 'none'
}
// FIM - Funcionalidade para ver a senha


// INICIO - Modal Erro
function openModal(text) {
    const mdText = document.getElementById('md-text');
    mdText.innerText = text

    const modal = document.getElementById('md-error');
    modal.style.display = 'block';

    setTimeout(closeModal, 10000);
}
function closeModal() {
    const modal = document.getElementById('md-error');
    modal.style.display = 'none';
}
// FIM - Modal Erro


// INICIO - Validacão dos dados / envio dos dados
function validateData() {
    const imgProfile = document.getElementById("current-image");
    const username = document.getElementById('username');
    const name = document.getElementById('name');
    const lastName = document.getElementById('last-name');
    const email = document.getElementById('email');
    const password1 = document.getElementById('input-password-1');
    const password2 = document.getElementById('input-password-2');

    // Verificar se a imagem de perfil foi selecionada
    if (imgProfile.src === "") {
        openModal("Por favor, selecione uma imagem de perfil");
        return false;
    }

    // Verificar se os campos de texto estão preenchidos
    if (username.value === "" || name.value === "" || lastName.value === "" || email.value === "" || password1.value === "" || password2.value === "") {
        openModal("Por favor, preencha todos os campos");
        return false;
    }

    // Verificar se as senhas são iguais
    if (password1.value !== password2.value) {
        openModal("As senhas não coincidem. Por favor, tente novamente");
        return false;
    }

    // Aqui você pode adicionar mais validações, como verificar se o e-mail é válido, etc.

    // Se todas as validações passarem, retornar true
    return true;
}
// FIM - Validacão dos dados / envio dos dados


// Função para enviar os dados de forma assíncrona usando Fetch
async function sendData() {
    // Chama a função para validar os dados
    if (!validateData()) {
        return; // Se os dados não forem válidos, não envia a requisição
    }

    const formData = new FormData(); // Cria um objeto FormData para enviar os dados do formulário

    // Adiciona os campos do formulário ao objeto FormData
    formData.append('username', document.getElementById('username').value);
    formData.append('name', document.getElementById('name').value);
    formData.append('lastName', document.getElementById('last-name').value);
    formData.append('email', document.getElementById('email').value);
    formData.append('password1', document.getElementById('input-password-1').value);
    formData.append('password2', document.getElementById('input-password-2').value);
    formData.append('profileImage', document.getElementById('current-image').src);

    try {
        // Obter o token CSRF do cookie
        const csrfToken = getCSRFToken(); // Implemente esta função para obter o token CSRF do cookie

        // Adiciona o token CSRF ao corpo da solicitação
        formData.append('csrfmiddlewaretoken', csrfToken);

        const response = await fetch('/cadastro_user/', {
            method: 'POST',
            body: formData,
            credentials: 'same-origin'
        });

        if (response.ok) {
            // Se a solicitação for bem-sucedida, você pode fazer o que quiser aqui, como exibir uma mensagem de sucesso
            console.log('Cadastro realizado com sucesso!');
        } else {
            // Se a solicitação não for bem-sucedida, você pode exibir uma mensagem de erro
            console.log('Erro ao cadastrar usuário');
        }
    } catch (error) {
        // Se ocorrer um erro ao enviar a solicitação, você pode lidar com ele aqui
        console.log('Erro ao enviar requisição:', error);
    }
}