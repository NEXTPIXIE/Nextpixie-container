import random
import string
import base64



def generate_tag(n=6):
    letters = string.ascii_uppercase
    code = [random.choice(letters) for _ in range(n)]
    nums = [str(random.choice(range(10))) for _ in range(n)]
    random.shuffle(nums)
    return "".join(code[-2:])+ "".join(nums[:4])
        
        
        
def generate_code() -> str:
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    otp = "".join(str(random.choice(digits)) for _ in range(6))
    return otp



def encode_file(image):
    content = image.read()
    encoded_content = base64.b64encode(content)
    return encoded_content.decode('utf-8')
