import os
from dotenv import load_dotenv
load_dotenv()

password = os.getenv('PASSWORD')
print(password)


id = os.getenv('id')
print(id)

print('id:{0},password:{1}'.format(id, password))


def demo(name: str) -> str:
    print('hello '+name)
    return 'wibble'


sk = demo('kone')
print(sk)
