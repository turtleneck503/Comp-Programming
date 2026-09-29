import subprocess

def run_student_code(n):
    """Run the student's code with the given input 'n' and return the output."""
    process = subprocess.Popen(['python', 'previous_next.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    input_str = f"{n}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for n, expected_output in test_cases:
        stdout, stderr = run_student_code(n)
        if stderr:
            results.append(f"Error: {stderr}")
        elif stdout == expected_output:
            results.append("Pass")
        else:
            results.append(f"Fail: Expected '{expected_output}', got '{stdout}'")
    return results

def main():
    # Define test cases as tuples of (n, expected_output)
    test_cases = [
        (5, "The next number for the number 5 is 6.\nThe previous number for the number 5 is 4."),
        (0, "The next number for the number 0 is 1.\nThe previous number for the number 0 is -1."),
        (-3, "The next number for the number -3 is -2.\nThe previous number for the number -3 is -4."),
        (100, "The next number for the number 100 is 101.\nThe previous number for the number 100 is 99."),
        (-1, "The next number for the number -1 is 0.\nThe previous number for the number -1 is -2."),
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print results
    for i, result in enumerate(results):
        print(f"Test case {i + 1}: {result}")

if __name__ == '__main__':
    main()
