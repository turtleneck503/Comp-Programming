import subprocess

def run_student_code(n):
    """Run the student's last.py code with the given input number."""
    process = subprocess.Popen(['python', 'last.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    # Input format as expected by last.py (single number input)
    input_str = f"{n}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for i, (input_value, expected_output) in enumerate(test_cases):
        stdout, stderr = run_student_code(input_value)

        # Check for errors
        if stderr:
            results.append({
                'test_case': i + 1,
                'status': 'Error',
                'inputs': input_value,
                'expected': expected_output,
                'actual': stdout,
                'error': stderr
            })
        # Check if the output matches the expected output
        elif stdout == expected_output:
            results.append({
                'test_case': i + 1,
                'status': 'Pass',
                'inputs': input_value,
                'expected': expected_output,
                'actual': stdout
            })
        else:
            results.append({
                'test_case': i + 1,
                'status': 'Fail',
                'inputs': input_value,
                'expected': expected_output,
                'actual': stdout,
                'error': None
            })
    return results

def print_detailed_feedback(results):
    """Print detailed feedback for each test case."""
    for result in results:
        print(f"\nTest case {result['test_case']}:")
        print(f"  Input: {result['inputs']}")
        
        if result['status'] == 'Pass':
            print("  Status: Pass ✅")
        elif result['status'] == 'Fail':
            print("  Status: Fail ❌")
            print(f"  Expected Output: {result['expected']}")
            print(f"  Actual Output: {result['actual']}")
        elif result['status'] == 'Error':
            print("  Status: Error 🚨")
            print(f"  Error Message: {result['error']}")
        
        print("-" * 40)

def main():
    # Define test cases as tuples of (input_number, expected_output)
    test_cases = [
        (12345, "5"),      # Last digit of 12345 is 5
        (100000, "0"),     # Last digit of 100000 is 0
        (0, "0"),          # Last digit of 0 is 0
        (987654321, "1"),  # Last digit of 987654321 is 1
        (1001, "1")       # Last digit of 1001 is 1
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print detailed feedback
    print_detailed_feedback(results)

if __name__ == '__main__':
    main()
