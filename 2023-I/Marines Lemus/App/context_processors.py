from .models import Avatar

def mi_avatar(request):
    mi_avatar = None
    if request.user.is_authenticated:
        try:
            #mi_avatar = Avatar.objects.get(user=request.user)
            mi_avatar = Avatar.objects.filter(user=request.user).first()
        except Avatar.DoesNotExist:
            pass
    return {'mi_avatar': mi_avatar}