// Função para obter o token CSRF do cookie
function getCSRFToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        .split('=')[1];
    return cookieValue;
}

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



function tweetsSeguindo() {
    tweetsTodosId.classList.remove('btn-selecionado')
    tweetsSeguindoId.classList.add('btn-selecionado')
}


const tweetsTodosId = document.getElementById('tweetsTodos')
const tweetsSeguindoId = document.getElementById('tweetsSeguindo')


async function tweetsTodos() {

    tweetsTodosId.classList.add('btn-selecionado')
    tweetsSeguindoId.classList.remove('btn-selecionado')

    const tweetsContainer = document.getElementById('home-tweets');
    try {
        const response = await fetch('/tweets/');
        if (response.ok) {
            const data = await response.json();

            let tweetsHTML = '';
            console.log(data)
            data.forEach(tweet => {
                if (tweet.comentario) {
                    console.log('retweet')
                } else {
                    tweetsHTML += `
                    <div class="tweet">
                        <div class="tw-head">
                            <p>@${tweet.user_username}
                            <!-- <div class="tw-h-rt">
                                    <i class="fa-solid fa-retweet"></i>
                                    <p style="font-size: 12px;">retweet by</p>
                                    <p>@user</p>
                                </div> -->
                            </p>
                            <p>${tweet.data}</p>
                        </div>
                        <div class="tw-main">
                            <div class="tw-m-img">
                                <img src="${tweet.usuario_foto_perfil}" alt="foto de perfil">
                            </div>
                            <div class="tw-m-text">
                                <p>${tweet.tweet}</p>
                            </div>
                        </div>
                        <div class="tw-footer">
                            <div class="tw-f-react">
                                <div class="tw-f-r">
                                    <p>0</p>
                                    <i class="fa-solid fa-heart"></i>
                                </div>
                                <div class="tw-f-r">
                                    <p>0</p>
                                    <i class="fa-solid fa-retweet"></i>
                                </div>
                                <div class="tw-f-r">
                                    <p>0</p>
                                    <i onclick="openModalComment(${tweet.id})" class="fa-solid fa-comment"></i>
                                </div>
                            </div>
                            <p>${tweet.hora}</p>
                        </div>
                    </div>
                `;
                }

            });

            tweetsContainer.innerHTML = tweetsHTML;

        } else {
            console.log('Erro ao carregar os dados:', response.status);
        }
    } catch (error) {
        console.log('Erro ao carregar os dados:', error);
    }
};


function postarTweet() {

    if (textarea.value != '') {

        const data = {
            tweet: textarea.value,
        };
    
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('X-CSRFToken', getCSRFToken());
    
        const requestOptions = {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(data)
        };
    
        fetch(`/postar/`, requestOptions)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro ao fazer a solicitação POST');
                }
                return response.json();
            })
            .then(data => {
                console.log('Resposta:', data.message);
                tweetsTodos()
            })
            .catch(error => {
                console.error('Erro:', error);
            });
    
    }

}



document.addEventListener("DOMContentLoaded", tweetsTodos);