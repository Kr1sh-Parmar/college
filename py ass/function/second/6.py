def sanitize_list(lst):
    if not lst:
        return []
    first = lst[0] if lst[0] >= 0 else 0
    return [first] + sanitize_list(lst[1:])

# Example usage
lst = [1, -2, 3, -4, 5]
sanitized = sanitize_list(lst)
print("Sanitized list:", sanitized)
