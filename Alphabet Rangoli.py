import string


def print_rangoli(size):
    # your code goes here
    mid = size - 1
    for i in range(size - 1, 0, -1):
        row = ['-'] * (2 * size - 1)
        for j in range(size - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))
    for i in range(0, size):
        row = ['-'] * (2 * size - 1)
        for j in range(0, size - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

