import subprocess

def run_student_code(base, height):
    """Run the student's code with the given base and height inputs and return the output."""
    process = subprocess.Popen(['python', 'triangle.py'], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE, 
                               text=True)
    input_str = f"{base}\n{height}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for base, height, expected_output in test_cases:
        stdout, stderr = run_student_code(base, height)
        if stderr:
            results.append(f"Error: {stderr}")
        elif stdout == expected_output:
            results.append("Pass")
        else:
            results.append(f"Fail: Expected '{expected_output}', got '{stdout}'")
    return results

def main():
    # Define test cases as tuples of (base, height, expected_output)
    test_cases = [
        (4, 5, '10.0'),
        (3, 7, '10.5'),
        (10, 0, '0.0'),
        (0, 0, '0.0'),
        (-5, 4, '-10.0'),
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print results
    for i, result in enumerate(results):
        print(f"Test case {i + 1}: {result}")

if __name__ == '__main__':
    main()
