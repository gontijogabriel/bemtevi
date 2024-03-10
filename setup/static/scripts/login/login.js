// INICIO - Funcionalidade para ver a senha
const inputType = document.getElementById('input-password')
const eyeOpen = document.getElementById('input-eye-open')
const eyeClose = document.getElementById('input-eye-close')

function openPassword () {
    inputType.type = 'text'
    eyeOpen.style.display = 'none'
    eyeClose.style.display = 'flex'
}
function closePassword () {
    inputType.type = 'password'
    eyeOpen.style.display = 'flex'
    eyeClose.style.display = 'none'
}
// FIM - Funcionalidade para ver a senha