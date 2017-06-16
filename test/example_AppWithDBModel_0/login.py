import hmac

if __name__ == '__main__':

    loginname = "Duck"
    password = "P4ssw0rd"

    password_hash = hmac.new(password).hexdigest()

    del password

    while True:

        password = raw_input("Hallo {}, enter password".format(loginname))
        entered_password_hash = hmac.new(password).hexdigest()

        if password_hash == entered_password_hash:
            print "Willkommen {}".format(loginname)
            break
        else:
            print "Wrong password. Warning!"


