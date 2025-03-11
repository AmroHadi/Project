def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Example usage
fahrenheit = 98.6
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"Celsius: {celsius:.2f}")