def max_pairwise_product(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to find a product.")
    
    max1 = max2 = 0 # Initialize the two largest numbers
    
    for number in numbers:
        if number > max1: # Update both max1 and max2
            max2 = max1 
            max1 = number
        elif number > max2: # Update only max2
            max2 = number
    
    return max1 * max2

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))