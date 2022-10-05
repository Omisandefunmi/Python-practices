def valid(password, username):
    if len(password) < 8:
        return False
    elif password == username :
        return False
    elif not any(x.islower() for x in password):
        return False
    elif not any(x.isupper() for x in password):
        return False
    elif not any(x.isdigit() for x in password):
        return False
    else:
        return True

