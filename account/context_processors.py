from .models import NewUser


def users(request):
    if request.user.is_authenticated:
        last_name = NewUser.objects.filter(last_name=request.user)
    else:
        last_name = "Account"
        pass

    return {'last_name': last_name}
