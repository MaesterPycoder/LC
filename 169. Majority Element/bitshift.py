def majorityElement(nums):
    n = len(nums)
    majority_bit_count = [0] * 32  # We will count bits for 32 positions
    
    # Count number of 1s for each bit position
    for num in nums:
        for i in range(32):
            if num & (1 << i):
                majority_bit_count[i] += 1
    
    majority_element = 0
    for i in range(32):
        if majority_bit_count[i] > n // 2:
            majority_element |= (1 << i)
    
    # Handle the sign bit (if the majority element is negative)
    if majority_element & (1 << 31):
        majority_element -= (1 << 32)
    
    return majority_element
