small = None
for i in [12,13,14,45,6,0]:
    if small is None:
        small = i
    elif i < small:
        small = i


print("smallest number",small)
