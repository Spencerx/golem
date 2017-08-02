import os
import stat

PASSWORD_LENGH = 50


def get_saved_password(datadir):
    password_file = os.path.join(datadir, 'password')
    if os.path.exists(password_file):
        with open(password_file, 'rb') as f:
            password = f.read(PASSWORD_LENGH)
            if len(password) < PASSWORD_LENGH:
                raise IOError(
                    "Invalid password in file {}".format(password_file)
                )
            return password

    password = os.urandom(PASSWORD_LENGH)
    fd = os.open(password_file, os.O_WRONLY | os.O_CREAT, stat.S_IREAD)
    with os.fdopen(fd, 'wb') as f:
        f.write(password)
    return password
