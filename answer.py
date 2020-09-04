def average(array):
    set1 = set(arr)
    sum1 = sum(set1)
    return sum1/len(set1)

if __name__ == '__main__':
    n = 5
    arr = list(map(int, input("Write your marks seperated by space\n").split()))
    result = average(arr)

    print(f'your percentage is {result}% ')
