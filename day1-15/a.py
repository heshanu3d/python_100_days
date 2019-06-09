def set_test():
    set1 = {1,2,3,4,5}
    print(set1)
    print('set1 length:',len(set1))
    set2 = set(range(10))
    set2.update([11,12])
    print('set2:',set2)

def main():
    # %timeit [1,2,3,4,5]
    # %timeit (1,2,3,4,5)
    set_test()


if __name__ == '__main__':
    main()