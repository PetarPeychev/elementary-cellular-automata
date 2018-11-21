import eca
from PIL import Image
import random

def generate_single():
    for id in range(256):
        data = [0 for x in range(199 * 100)]

        ec = eca.ECA(id)

        for i in range(100):
            for j in range(199):
                data[i * 199 + j] = not ec.array[j]
            ec.step()

        img = Image.new('1', (199, 100))
        img.putdata(data)
        img.save('images/eca' + str(id) + '.png')

def generate_random_small():
    for id in range(256):
        data = [0 for x in range(199 * 100)]

        ec = eca.ECA(id)
        ec.array = [random.randint(0, 1) for x in range(199)]

        for i in range(100):
            for j in range(199):
                data[i * 199 + j] = not ec.array[j]
            ec.step()

        img = Image.new('1', (199, 100))
        img.putdata(data)
        img.save('images-random/eca' + str(id) + '.png')

def generate_random_big():
    for id in range(256):
        data = [0 for x in range(1024 * 512)]

        ec = eca.ECA(id)
        ec.array = [random.randint(0, 1) for x in range(1024)]

        for i in range(512):
            for j in range(1024):
                data[i * 1024 + j] = not ec.array[j]
            ec.step()

        img = Image.new('1', (1024, 512))
        img.putdata(data)
        img.save('images-random-big/eca' + str(id) + '.png')

generate_single()
generate_random_small()
generate_random_big()

# while True:
#     id = int(input('ECM ID: '))
#     ec = eca.ECA(id)
#     print(ec.array)
#     print(ec.id)
#     print(ec.dict)
#
#     while True:
#         inp = input("")
#         if inp == 'x':
#             break
#         for i in ec.array:
#             if i == 0:
#                 print('   ', end='')
#                 #print(' ◻ ', end='')
#             else:
#                 print(' ◼ ', end='')
#         print()
#         ec.step()
