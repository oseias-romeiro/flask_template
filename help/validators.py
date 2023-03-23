import string


def valid_pw(pw: str):
    for p in string.punctuation:
        if p in pw:
            break
    return (
        len(pw) >= 8 and
        True in [(p in pw) for p in string.punctuation]
    )

