import random
import string


def generate_album_tag(n=6):
    letters = string.ascii_uppercase
    code = [random.choice(letters) for _ in range(n)]
    nums = [str(random.choice(range(10))) for _ in range(n)]
    random.shuffle(nums)
    return "".join(code[-2:])+ "".join(nums[:4])
        
        


def generate_code():
    a = []
    for _ in range(4):
        a.append(random.choice(string.ascii_lowercase))
        a.append(random.choice(string.ascii_uppercase))
        a.append(random.choice(string.digits))
        a.append(random.choice(["@","!","$","#","="]))
    random.shuffle(a)
    return "".join(a)