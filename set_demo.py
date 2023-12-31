# unordered data type
emptySet =set()
sampleSet = {1,'A','g', 3.86, 'Ata'}
print(sampleSet)

for _ in range(10):
    print(sampleSet)

print('=' *40)

odd = set(range(1,50,2))
power = {1,4,9,16,25,36,49}
print(len(odd))
print(odd.intersection(power))
print(odd.union(power))
print(len(odd.union(power)))