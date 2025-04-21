def average_list(lst):
    def helper(lst, n):
        if n == 0:
            return 0, 0
        sum_rest, count_rest = helper(lst, n-1)
        return sum_rest + lst[n-1], count_rest + 1
    total_sum, total_count = helper(lst, len(lst))
    return total_sum / total_count if total_count != 0 else 0

# Example usage
numbers = [2, 4, 6, 8]
avg = average_list(numbers)
print("Average of list:", avg)
