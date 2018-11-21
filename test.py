import eca
from PIL import Image

for id in range(255):
    data = [0 for x in range(199 * 100)]

    ec = eca.ECA(id)

    for i in range(100):
        for j in range(199):
            data[i * 199 + j] = not ec.array[j]
        ec.step()

    img = Image.new('1', (199, 100))
    img.putdata(data)
    img.save('images/eca' + str(id) + '.png')


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
