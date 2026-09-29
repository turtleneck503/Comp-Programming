import subprocess

def run_student_code(minutes):
    """Run the student's clock.py code with the given input."""
    process = subprocess.Popen(['python', 'clock.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    # Input format as expected by clock.py (single number: minutes)
    input_str = f"{minutes}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for i, (minutes, expected_output) in enumerate(test_cases):
        stdout, stderr = run_student_code(minutes)

        # Check for errors
        if stderr:
            results.append({
                'test_case': i + 1,
                'status': 'Error',
                'inputs': minutes,
                'expected': expected_output,
                'actual': stdout,
                'error': stderr
            })
        # Check if the output matches the expected output
        elif stdout == expected_output:
            results.append({
                'test_case': i + 1,
                'status': 'Pass',
                'inputs': minutes,
                'expected': expected_output,
                'actual': stdout
            })
        else:
            results.append({
                'test_case': i + 1,
                'status': 'Fail',
                'inputs': minutes,
                'expected': expected_output,
                'actual': stdout,
                'error': None
            })
    return results

def print_detailed_feedback(results):
    """Print detailed feedback for each test case."""
    for result in results:
        print(f"\nTest case {result['test_case']}:")
        print(f"  Input (minutes since midnight): {result['inputs']}")
        
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
    # Define test cases as tuples of (minutes since midnight, expected_output)
    test_cases = [
        (150, "2 30"),  # 150 minutes past midnight → 2:30 AM
        (0, "0 0"),     # 0 minutes past midnight → 0:00 AM
        (60, "1 0"),    # 60 minutes past midnight → 1:00 AM
        (75, "1 15"),   # 75 minutes past midnight → 1:15 AM
        (1440, "0 0"),  # 1440 minutes (exactly 24 hours) → 0:00 AM
        (1439, "23 59") # 1439 minutes past midnight → 23:59 PM
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print detailed feedback
    print_detailed_feedback(results)

if __name__ == '__main__':
    main()
