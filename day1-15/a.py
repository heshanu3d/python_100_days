def set_test():
    set1 = {1,2,3,4,5}
    print(set1)
    print('set1 length:',len(set1))
    set2 = set(range(10))
    set2.update([10,11,12])
    print('set2:',set2)

    if 4 in set2:
        set2.remove(4)
    print('set2:', set2)
    for elem in set2:
        print(elem , ',', end='')
    set3 = set((1,2,3,4,4,3,2,1))
    print()
    print(set3.pop())
    print('set3:', set3)

    print('set2&set3:', set2 & set3)
    print('set2|set3:', set2 | set3)
    print('set2^set3:', set2 ^ set3)
    print('set2-set3:', set2 - set3)

def dict_test():
    dict = {'a1': 1, 'a2' : 12, 'a3' : 123}
    print('dict', dict)
    dict['a4'] = 1234
    print('dict', dict)
    if 'a3' in dict:
        dict.pop('a3')
    print('dict', dict)
    print(dict.get('a4'))
    dict.clear()
    print('dict', dict)


def main():
    # %timeit [1,2,3,4,5]
    # %timeit (1,2,3,4,5)
    # set_test()
    dict_test()

if __name__ == '__main__':
    main()