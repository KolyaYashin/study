component = [1, 2, 3, 7]
pairs = [(1,2), (2,3), (3,7)]

pairs = set(pairs)

for i in range(len(component)):
    for j in range(i+1, len(component)):
        if (component[i], component[j]) not in pairs and (component[j], component[i]) not in pairs:
            pairs.add((component[i], component[j]))


print(pairs)

print(sorted(pairs))