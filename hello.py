def greet(name):
    """Simple function to greet someone"""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def main():
    # Example usage of our functions
    print("=== Python Function Examples ===")
    print("\n1. String Manipulation:")
    print(greet("Python"))
    
    print("\n2. Basic Math:")
    area = calculate_area(5, 3)
    print(f"Area of 5x3 rectangle: {area}")
    
    print("\n3. Conditional Logic:")
    test_numbers = [2, 3, 4, 5]
    for num in test_numbers:
        print(f"Is {num} even? {is_even(num)}")

if __name__ == "__main__":
    main()
