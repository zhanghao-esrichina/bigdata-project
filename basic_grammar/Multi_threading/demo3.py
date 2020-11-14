

def findNumvbers(path, num, fn):
    i = []
    rowNo = 1
    with open(path, 'r+') as f:
        for line in f.readlines():
            index = line.find(str(num))
            if index != -1:
                i.append([rowNo, index + 1])
            else:
                i.append([rowNo, -1])
            rowNo += 1
    fn(i)


def callback_(s1):
    print(s1)
    print('successful export result')


if __name__ == '__main__':
    findNumvbers('222.txt', 5, callback_)
