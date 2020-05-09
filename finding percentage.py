if __name__ == '__main__':
    N = int(input())
    dc = dict()
    lst1 = list()
    for i in range(N):
        a = input()
        lst1 = a.split()
        d = lst1[0]
        lst1.remove(lst1[0])
        newlst1 = list(map(float, lst1))
        dc[d] = newlst1
    name = input()
    total = 0
    if name in dc:
        marks = dc[name]
        no = len(marks)
        for num in marks:
            total += num
    avg = total / no
    print("%.2f" % avg)





