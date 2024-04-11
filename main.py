def partition(numbers: list, begin: int, end: int):
    # Right element as pivot
    pivot = numbers[end]
    i = begin - 1

    for j in range(begin, end):
        if numbers[j] >= pivot:
            i += 1
            (numbers[i], numbers[j]) = (numbers[j], numbers[i])
    (numbers[i + 1], numbers[end]) = (numbers[end], numbers[i + 1])

    return i + 1


def quick_sort(numbers: list, begin: int, end: int):
    if begin < end:
        # Pivot  element: left elements - more, right elements - less.
        pivot = partition(numbers, begin, end)

        # Left side of pivot
        quick_sort(numbers, begin, pivot - 1)

        # Right side of pivot
        quick_sort(numbers, pivot + 1, end)


def max_amount_candies(pinatas: list) -> int:
    max_candies = 0
    # Sort descending
    quick_sort(pinatas, 0, len(pinatas) - 1)

    # Calculation candies
    length = len(pinatas)
    i = 0
    while i < length:
        if i == 0:
            max_candies += pinatas[1] * pinatas[i] * pinatas[i + 1]
        elif i == length - 1:
            max_candies += pinatas[i - 1] * pinatas[i] * pinatas[1]
        else:
            max_candies += pinatas[i - 1] * pinatas[i] * pinatas[i + 1]
        i += 1
    return max_candies


def main():
    while True:
        pinatas = []
        size = 2
        while True:
            try:
                size = int(input('Enter amount pinatas: '))
            except ValueError:
                print('Must be an integer!')
                continue
            if size > 1:
                break
            else:
                print('The pinatas must have at least 2 elements!')

        print('Enter candies:')
        for i in range(size):
            while True:
                try:
                    item = int(input())
                except ValueError:
                    print('Must be an integer!')
                    continue
                if item >= 1:
                    pinatas.append(item)
                    break
                else:
                    print('At least 1 candy!')

        print(f'Input pinatas: {pinatas}')
        result = max_amount_candies(pinatas)
        print(f'Max amount of candies: {result}')

        control = input('Continue? (y/n): ')
        if control == 'n':
            break


if __name__ == '__main__':
    main()
