from .models import NewUser


def users(request):
    if request.user.is_authenticated:
        username = NewUser.objects.get(last_name=request.user)
        last_name = username.last_name
    else:
        last_name = "Account"
        pass

    return {'last_name': last_name}
