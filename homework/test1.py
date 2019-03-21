a = {1, 2, 3, 4}
for x in a:
    for y in a:
        for z in a:
            if x != y and x != z and y != z:
                print(x, y, z)
