from werkzeug.security  import generate_password_hash, check_password_hash

def encode(text:str):
    encode_text = generate_password_hash(text, 'pbkdf2:sha256:30',30)
    return encode_text[17:]

def verify(text_encipted:str, text:str):
    encripted_text = 'pbkdf2:sha256:30$' + text_encipted
    return check_password_hash(encripted_text, text)