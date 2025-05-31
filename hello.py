import httpx

def greet(name):
    """Simple function to greet someone"""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def reverse_string(text):
    """Reverse a string using slicing"""
    return text[::-1]

def count_words(text):
    """Count words in a string"""
    return len(text.split())

def get_current_time():
    """Get current time in a formatted string"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_person(first_name, last_name, age):
    """Create a dictionary representing a person"""
    return {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'full_name': f"{first_name} {last_name}"
    }

def get_person_info(person):
    """Get formatted information about a person"""
    return f"{person['full_name']} is {person['age']} years old"

def safe_divide(num1, num2):
    """Safely divide two numbers with error handling"""
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Both arguments must be numbers"

def read_file(filename):
    """Read and print contents of a file"""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File '{filename}' not found"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_random_joke():
    """Get a random joke from the Chuck Norris API using httpx"""
    try:
        response = httpx.get('https://api.chucknorris.io/jokes/random')
        if response.status_code == 200:
            joke = response.json()['value']
            return joke
        else:
            return "Error fetching joke"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Example usage of our functions
    print("=== Python Function Examples ===")
    print("\n1. String Manipulation:")
    print(greet("Python"))
    print(f"Reversed: {reverse_string('hello')}")
    
    print("\n2. Basic Math:")
    area = calculate_area(5, 3)
    print(f"Area of 5x3 rectangle: {area}")
    print(f"Safe division: {safe_divide(10, 2)}")
    print(f"Safe division by zero: {safe_divide(10, 0)}")
    
    print("\n3. Conditional Logic:")
    test_numbers = [2, 3, 4, 5]
    for num in test_numbers:
        print(f"Is {num} even? {is_even(num)}")
    
    print("\n4. String Operations:")
    test_text = "Hello Python World"
    print(f"Original: {test_text}")
    print(f"Word count: {count_words(test_text)}")
    
    print("\n5. Date and Time:")
    print(f"Current time: {get_current_time()}")
    
    print("\n6. Data Structures:")
    person = create_person("John", "Doe", 30)
    print(get_person_info(person))
    
    print("\n7. File Operations:")
    print(f"Reading chat.txt: {read_file('chat.txt')[:100]}...")
    
    print("\n8. API Examples:")
    print("\nChuck Norris Joke:")
    print(get_random_joke())

if __name__ == "__main__":
    main()
