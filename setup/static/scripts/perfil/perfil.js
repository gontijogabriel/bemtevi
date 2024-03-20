const pageUrl = window.location.href;
const partesUrl = pageUrl.split('/')
const username = partesUrl[3]

async function tweetsPerfil() {

    const tweetsContainer = document.getElementById('home-tweets');
    try {
        const response = await fetch('/tweetsPerfil/' + username + '/');
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
                                    <i onclick="openModalComment()" class="fa-solid fa-comment"></i>
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


document.addEventListener("DOMContentLoaded", tweetsPerfil);