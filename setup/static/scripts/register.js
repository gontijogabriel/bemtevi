// Foto de Perfil
function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('img-preview');
        output.innerHTML = '<img src="' + reader.result + '"/>';
    };
    reader.readAsDataURL(event.target.files[0]);
}
