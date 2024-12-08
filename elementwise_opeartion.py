import numpy as np # Function to perform element-wise operations def elementwise_operations(A, B): # 1. Add corresponding elements of A and B A_add_B = A + B # 2. Multiply each element of array B by 2
B_multiply_2 = B * 2
# 3. Add arrays A and B element-wise
A_plus_B = A + B
# 4. Subtract array B from array A element-wise
A_minus_B = A - B
# 5. Square each element of array A
A_square = A ** 2
# Print results
print("Array A + Array B:", A_add_B)
print("Array B after multiplying by 2:", B_multiply_2)
print("Element-wise addition of A and B:", A_plus_B)
print("Element-wise subtraction of B from A:", A_minus_B)
print("Element-wise square of A:", A_square)
# Main program to input arrays A and B
def main():
# Input arrays from the user
    A = np.array(list(map(int, input("Enter elements for array A separated by space: ").split())))
    B = np.array(list(map(int, input("Enter elements for array B separated by space: ").split())))
    # Perform element-wise operations
    elementwise_operations(A, B)
# Run the program
if __name__ == "__main__":
    main()
    