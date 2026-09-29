import subprocess

def run_student_code(input_value):
    """Run the student's code with the given input and return the output."""
    process = subprocess.Popen(['python', 'square.py'], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE, 
                               text=True)
    input_str = str(input_value) + '\n'
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for input_value, expected_output in test_cases:
        stdout, stderr = run_student_code(input_value)
        if stderr:
            results.append(f"Error: {stderr}")
        elif stdout == expected_output:
            results.append("Pass")
        else:
            results.append(f"Fail: Expected '{expected_output}', got '{stdout}'")
    return results

def main():
    # Define test cases as tuples of (input_value, expected_output)
    test_cases = [
        (2, '4'),
        (3, '9'),
        (10, '100'),
        (0, '0'),
        (-5, '25'),
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print results
    for i, result in enumerate(results):
        print(f"Test case {i + 1}: {result}")

if __name__ == '__main__':
    main()
