from django.contrib.auth.models import User
from bemtevi.models import Usuario


def user_data_context(request):
    user = User.objects.get(username=request.user)
    usuario = Usuario.objects.get(user=user)

    contexto = {
        'id_user':user.pk,
        'username':user.username,
        'id':usuario.pk,
        'nome':usuario.nome,
        'sobrenome':usuario.sobrenome,
        'email':usuario.email,
        'birthday':usuario.data_nascimento,
        'foto':usuario.foto_perfil,
    }
    
    return contexto