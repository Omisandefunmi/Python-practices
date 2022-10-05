import re


def signup(user_accounts, log_in, username, password):
    import re

    state = False

    def valid():
        for account in user_accounts:
            if account['username'] == username:
                if len(password) > 7:
                    if re.search(r'[A-Za-z0-9]', password):
                        if username != password:
                            state = True
        return state

    def change_password():
        for account in user_accounts:
            if account['username'] == username:
                account['password'] = password

    if valid():
        change_password()
