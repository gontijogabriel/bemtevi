const idModalComment = document.getElementById('modal-comment')

const tweetComment = document.getElementById('md-c-content')

async function openModalComment(id) {
    try {
       
        const response = await fetch('/get_tweet/' + id + '/');
        if(response.ok) {
            const data = await response.json();
            console.log(data)

            let  tweetHTML = ''
            data.forEach(tweet => {
                tweetHTML = `
                <div class="md-c-tweet">
                <div class="md-c-t-header">
                    <div class="mdcth-content">
                        <img src="${tweet.usuario_foto_perfil}" alt="foto de perfil">
                        <div class="mdcth-user">
                            <p>${tweet.usuario_nome} ${tweet.usuario_sobrenome}</p>
                            <p>@${tweet.user_username}</p>
                        </div>
                    </div>
                    <div class="mdcth-voltar">
                        <i class="fa-solid fa-arrow-left"></i>
                        <a onclick="closeModalComment()">Voltar</a>
                    </div>
                </div>
                <div class="md-c-t-main">
                    <p>${tweet.tweet}</p>
                </div>
                <div class="md-c-t-footer">
                    <div class="mdctf-reacts">
                        <div class="mdctf-r">
                            ${tweet.n_likes > 0 ? `<p>${tweet.n_likes}</p>` : ''}   
                            <i class="fa-solid fa-heart"></i>
                        </div>
                        <div class="mdctf-r">
                            ${tweet.n_retweets > 0 ? `<p>${tweet.n_retweets}</p>` : ''}
                            <i class="fa-solid fa-retweet"></i>
                        </div>
                    </div>
                    <div class="mdctf-data">
                        <p>${tweet.data} ${tweet.hora}</p>
                    </div>
                </div>
                </div>`
            });
            
            tweetComment.insertAdjacentHTML('afterbegin', tweetHTML);

        } else {
            console.log('Erro ao carregar os dados:', response.status);
        }
    } catch (error) {
        console.log('Erro ao carregar os dados:', error);
    }

    // Abrir modal de comentario
    idModalComment.style.display = 'block';
}
function closeModalComment() {
    idModalComment.style.display = 'none';
}