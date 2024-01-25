document.addEventListener('DOMContentLoaded', function () {
    var input = document.getElementById('foto_perfil');
    var imgPreview = document.getElementById('img-preview').querySelector('img');

    imgPreview.addEventListener('click', function () {
        input.click();
    });

    input.addEventListener('change', function (event) {
        var reader = new FileReader();

        reader.onload = function () {
            imgPreview.src = reader.result;
        };

        if (event.target.files[0]) {
            reader.readAsDataURL(event.target.files[0]);
        }
    });
});