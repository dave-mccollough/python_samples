
# Continue
# Stops the loop for the current iteration
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd number: {count}")
    count += 1



# Break
#stops the loop entirely
count = 1
while count < 10:
    if count % 2 == 0:
        break
    print(f"We're counting odd number: {count}")
    count += 1


colors = ['blue', 'green', 'red', 'yellow']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break
    print(color)
