import subprocess

def run_student_code(inputs):
    """Run the student's code with the given inputs and return the output."""
    process = subprocess.Popen(['python', 'add_three.py'], 
                               stdin=subprocess.PIPE, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE, 
                               text=True)
    input_str = '\n'.join(map(str, inputs)) + '\n'
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for inputs, expected_output in test_cases:
        stdout, stderr = run_student_code(inputs)
        if stderr:
            results.append(f"Error: {stderr}")
        elif stdout == expected_output:
            results.append("Pass")
        else:
            results.append(f"Fail: Expected '{expected_output}', got '{stdout}'")
    return results

def main():
    # Define test cases as tuples of (inputs, expected_output)
    test_cases = [
        ([1, 2, 3], '6'),
        ([10, 20, 30], '60'),
        ([0, 0, 0], '0'),
        ([-1, -2, -3], '-6'),
        ([100, 200, 300], '600'),
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print results
    for i, result in enumerate(results):
        print(f"Test case {i + 1}: {result}")

if __name__ == '__main__':
    main()
