def get_ip_address(request):
    x_forward = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forward:
        ip = x_forward.split(',')[0]
        return ip
    else:
        ip = request.META.get('REMOTE_ADDR')
        return ip


def get_user_agent(request):
    user_agent = request.META.get('HTTP_USER_AGENT')
    return user_agent


def get_user_initial(user):
    if user.first_name:
        return user.first_name[0].upper()
    elif user.last_name:
        return user.last_name[0].upper()
    elif user.username:
        return user.username[0].upper()
    return "?"  # fallback
