def max_pairwise_product_fast(numbers):
    max1 = 0
    for pos in range(len(numbers)):
        if (pos+1) < len(numbers):
            if numbers[pos] > max1 and numbers[pos] > numbers[pos+1]:
                max1 = numbers[pos]
            elif numbers[pos+1] > max1 and numbers[pos+1] > max1:
                max1 = numbers[pos+1]
        else:
            numbers.remove(max1)

    max2 = 0    
    for pos in range(len(numbers)):
        if len(numbers) > 1:
            if (pos+1) < len(numbers):
                if numbers[pos] > max2 and numbers[pos] > numbers[pos+1]:
                    max2 = numbers[pos]
                elif numbers[pos+1] > max2 and numbers[pos+1] > max2:
                    max2 = numbers[pos+1]
            else:
                numbers.remove(max2)
        else:
            max2 = numbers[0]

    return max1 * max2

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_fast(input_numbers))