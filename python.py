from collections import Counter

def top_three_frequent_elements(lst):
    # Count the frequency of each element
    freq = Counter(lst)
    # Get the 3 most common elements
    top_three = freq.most_common(3)
    # Return only the elements, not their counts
    return [item for item, count in top_three]

# Example usage:
input_list = [1, 3, 3, 2, 1, 1, 4, 4, 4, 4]
print(top_three_frequent_elements(input_list))  # Output: [4, 1, 3]
