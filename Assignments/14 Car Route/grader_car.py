import subprocess

def run_student_code(n, m):
    """Run the student's car_route.py code with the given inputs."""
    process = subprocess.Popen(['python', 'car_route.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    # Input format as expected by car_route.py (two numbers: N and M)
    input_str = f"{n}\n{m}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for i, (n, m, expected_output) in enumerate(test_cases):
        stdout, stderr = run_student_code(n, m)

        # Check for errors
        if stderr:
            results.append({
                'test_case': i + 1,
                'status': 'Error',
                'inputs': (n, m),
                'expected': expected_output,
                'actual': stdout,
                'error': stderr
            })
        # Check if the output matches the expected output
        elif stdout == expected_output:
            results.append({
                'test_case': i + 1,
                'status': 'Pass',
                'inputs': (n, m),
                'expected': expected_output,
                'actual': stdout
            })
        else:
            results.append({
                'test_case': i + 1,
                'status': 'Fail',
                'inputs': (n, m),
                'expected': expected_output,
                'actual': stdout,
                'error': None
            })
    return results

def print_detailed_feedback(results):
    """Print detailed feedback for each test case."""
    for result in results:
        print(f"\nTest case {result['test_case']}:")
        print(f"  Inputs (N miles/day, M miles/route): {result['inputs']}")
        
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
    # Define test cases as tuples of (miles_per_day, route_miles, expected_output)
    test_cases = [
        (700, 750, "2"),   # 700 miles/day, 750 miles total → 2 days
        (300, 600, "2"),   # 300 miles/day, 600 miles total → 2 days
        (500, 1500, "3"),  # 500 miles/day, 1500 miles total → 3 days
        (800, 799, "1"),   # 800 miles/day, 799 miles total → 1 day
        (120, 130, "2"),   # 120 miles/day, 130 miles total → 2 days
        (1000, 2000, "2")  # 1000 miles/day, 2000 miles total → 2 days
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print detailed feedback
    print_detailed_feedback(results)

if __name__ == '__main__':
    main()
