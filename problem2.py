def dot_product(v1, v2):
    ps = sum(v1[i] * v2[i] for i in range(len(v1)))
    return ps

def check_orthogonal_vectors(n):
    results = []

    for _ in range(n):
        # Read vectors v1 and v2
        v1 = list(map(float, input("Enter vector v1 (comma-separated values): ").split(',')))
        v2 = list(map(float, input("Enter vector v2 (comma-separated values): ").split(',')))

        # Calculate dot product
        ps = dot_product(v1, v2)

        # Check if the dot product is zero (orthogonal)
        if ps == 0:
            results.append("Orthogonal")
        else:
            results.append("Not Orthogonal")

    return results

# Example usage:
n = int(input("Enter the number of vector pairs to check: "))
results = check_orthogonal_vectors(n)
for i, result in enumerate(results):
    print(f"Pair {i + 1}: {result}")
