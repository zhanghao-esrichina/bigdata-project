

try:
    with open('output.txt', 'r') as stream:
        line = stream.readline()
        while line:
            print(line.rstrip())
            line = stream.__next__()
except Exception as identifier:
    print(identifier)
