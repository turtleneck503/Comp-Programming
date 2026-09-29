import subprocess

def run_student_code(input_values):
    """Run the student's minimum.py code with the given inputs."""
    process = subprocess.Popen(['python', 'minimum.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    # Input format: each value on a new line
    input_str = f"{input_values[0]}\n{input_values[1]}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for i, (input_values, expected_output) in enumerate(test_cases):
        stdout, stderr = run_student_code(input_values)

        # Check for errors
        if stderr:
            results.append({
                'test_case': i + 1,
                'status': 'Error',
                'input': input_values,
                'expected': expected_output,
                'actual': stdout,
                'error': stderr
            })
        # Check if the output matches the expected output
        elif stdout == expected_output:
            results.append({
                'test_case': i + 1,
                'status': 'Pass',
                'input': input_values,
                'expected': expected_output,
                'actual': stdout
            })
        else:
            results.append({
                'test_case': i + 1,
                'status': 'Fail',
                'input': input_values,
                'expected': expected_output,
                'actual': stdout,
                'error': None
            })
    return results

def print_detailed_feedback(results):
    """Print detailed feedback for each test case."""
    for result in results:
        print(f"\nTest case {result['test_case']}:")
        print(f"  Input: {result['input']}")
        
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
    # Define test cases as tuples of (input_values, expected_output)
    test_cases = [
        ([12, 13], "12"),    # 12 is smaller
        ([8, 8], "8"),       # Both are the same
        ([-5, 0], "-5"),     # Negative and zero
        ([100, 99], "99"),   # 99 is smaller
        ([-2, -3], "-3"),    # -3 is smaller
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print detailed feedback
    print_detailed_feedback(results)

if __name__ == '__main__':
    main()
