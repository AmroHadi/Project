# Numbers
a = 12
b = 9

# lets Convert to binary
a_binary = bin(a)  # bin() converts to binary (e.g., 12 -> '0b1100')
b_binary = bin(b)  # bin() converts to binary (e.g., 9 -> '0b1001')

# Perform bitwise operations
and_result = a & b  # AND operation
or_result = a | b   # OR operation

# Display results
print("a in binary:", a_binary)
print("b in binary:", b_binary)
print("a & b (binary):", bin(and_result))
print("a & b (decimal):", and_result)
print("a | b (binary):", bin(or_result))
print("a | b (decimal):", or_result)