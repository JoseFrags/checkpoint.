def sum_of_distinct_elements(set1, set2):
    distinct_elements = {}
    
    # Count distinct elements from set1
    for element in set1:
        distinct_elements[element] = distinct_elements.get(element, 0) + 1
    
    # Count distinct elements from set2
    for element in set2:
        distinct_elements[element] = distinct_elements.get(element, 0) + 1

    result = 0
    for element, count in distinct_elements.items():
        if count == 1:
            result += element
    
    return result

# Example usage:
set1 = [3, 1, 7, 9]
set2 = [2, 4, 1, 9, 3]
print(sum_of_distinct_elements(set1, set2))  # Output: 13 (distinct elements 2, 4, 7)
