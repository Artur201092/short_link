import hashlib
import random
import string

from short_url.settings import SHORT_URL_LENGTH_BOUNDS

def generate_unique_key():

    salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(26)).encode(
        'utf-8')
    unique_key = hashlib.sha1(salt).hexdigest()

    return unique_key[:SHORT_URL_LENGTH_BOUNDS[1]]
