import secrets
import string

# Default length
length = 100

print('\nPASSWORD: ' + "".join(secrets.choice(string.digits + string.ascii_letters + string.punctuation) for i in range(length)))
