def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def sum_of_digits_in_range(L, U):
    def sum_digits_to_n(n):
        if n < 0:
            return 0
        total_sum = 0
        factor = 1
        while factor <= n:
            lower_numbers = n % factor
            current_digit = (n // factor) % 10
            higher_numbers = n // (factor * 10)
            
            # Add the sum for the current digit position
            total_sum += higher_numbers * 45 * factor  # Sum for all digits 0-9 in the current position
            total_sum += current_digit * (current_digit - 1) // 2 * factor  # Sum of digits less than current digit
            total_sum += current_digit * (lower_numbers + 1)  # Sum of digits exactly equal to current digit
            
            factor *= 10
        
        return total_sum

    return sum_digits_to_n(U) - sum_digits_to_n(L - 1)

L, U = list(map(int, input().split(" ")))
print(sum_of_digits_in_range(L, U))

