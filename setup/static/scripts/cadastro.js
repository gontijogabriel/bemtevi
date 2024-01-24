// Foto de Perfil
document.getElementById('img-preview').addEventListener('click', function () {
    var input = document.createElement('input');
    input.type = 'file';

    input.addEventListener('change', function () {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                var img = document.getElementById('img-preview').getElementsByTagName('img')[0];
                img.src = e.target.result;

                var formulario = document.getElementById('formCadastro');
                var dadosFormulario = new FormData(formulario);
                dadosFormulario.set('foto_perfil', input.files[0]);

                window.formData = dadosFormulario;
            };
            reader.readAsDataURL(input.files[0]);
        }
    });
    input.click();
});


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

// Cadastra usuario
async function cadastraUsuario() {
    var dadosFormulario = window.formData || new FormData(document.getElementById('formCadastro'));

    const csrftoken = getCookie('csrftoken');

    try {
        var resposta = await fetch('/cadastro/', {
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
