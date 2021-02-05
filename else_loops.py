# Integrating else with loops


count = 1
while count <= 4:
    print(count)
    count += 1
else:
    print('Print while loop completed')


for i in [1 ,2, 3, 4, 5]:
    print(i)
else:
    print('For loop completed')


colors = ['orange', 'pink', 'red', 'blue', 'yellow']
for color in colors:
    if color == 'green':
        print('Green is in the list')
        break
else:
    print('Green is not in the list')