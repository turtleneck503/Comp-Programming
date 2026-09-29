import subprocess

def run_student_code(hours, minutes, seconds):
    """Run the student's clock_face_1.py code with the given inputs."""
    process = subprocess.Popen(['python', 'clock_face_1.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    # Input format as expected by clock_face_1.py (hours, minutes, seconds)
    input_str = f"{hours}\n{minutes}\n{seconds}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for i, (hours, minutes, seconds, expected_output) in enumerate(test_cases):
        stdout, stderr = run_student_code(hours, minutes, seconds)

        # Check for errors
        if stderr:
            results.append({
                'test_case': i + 1,
                'status': 'Error',
                'inputs': (hours, minutes, seconds),
                'expected': expected_output,
                'actual': stdout,
                'error': stderr
            })
        # Check if the output matches the expected output (with rounding tolerance)
        elif abs(float(stdout) - expected_output) < 0.001:
            results.append({
                'test_case': i + 1,
                'status': 'Pass',
                'inputs': (hours, minutes, seconds),
                'expected': expected_output,
                'actual': stdout
            })
        else:
            results.append({
                'test_case': i + 1,
                'status': 'Fail',
                'inputs': (hours, minutes, seconds),
                'expected': expected_output,
                'actual': stdout,
                'error': None
            })
    return results

def print_detailed_feedback(results):
    """Print detailed feedback for each test case."""
    for result in results:
        print(f"\nTest case {result['test_case']}:")
        print(f"  Inputs (hours, minutes, seconds): {result['inputs']}")
        
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
    # Define test cases as tuples of (hours, minutes, seconds, expected_output)
    test_cases = [
        (0, 0, 0, 0.0),        # Midnight → 0.0 degrees
        (6, 0, 0, 180.0),      # 6 hours → 180.0 degrees
        (12, 0, 0, 0.0),       # 12 hours → 0.0 degrees (full circle)
        (3, 15, 0, 97.5),      # 3 hours, 15 minutes → 97.5 degrees
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print detailed feedback
    print_detailed_feedback(results)

if __name__ == '__main__':
    main()
