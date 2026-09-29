import subprocess

def run_student_code(d, c, n):
    """Run the student's cost.py code with the given inputs."""
    process = subprocess.Popen(['python', 'cost.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    # Input format as expected by cost.py (three numbers: D, C, and N)
    input_str = f"{d}\n{c}\n{n}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for i, (d, c, n, expected_output) in enumerate(test_cases):
        stdout, stderr = run_student_code(d, c, n)

        # Check for errors
        if stderr:
            results.append({
                'test_case': i + 1,
                'status': 'Error',
                'inputs': (d, c, n),
                'expected': expected_output,
                'actual': stdout,
                'error': stderr
            })
        # Check if the output matches the expected output
        elif stdout == expected_output:
            results.append({
                'test_case': i + 1,
                'status': 'Pass',
                'inputs': (d, c, n),
                'expected': expected_output,
                'actual': stdout
            })
        else:
            results.append({
                'test_case': i + 1,
                'status': 'Fail',
                'inputs': (d, c, n),
                'expected': expected_output,
                'actual': stdout,
                'error': None
            })
    return results

def print_detailed_feedback(results):
    """Print detailed feedback for each test case."""
    for result in results:
        print(f"\nTest case {result['test_case']}:")
        print(f"  Inputs (D dollars, C cents, N cupcakes): {result['inputs']}")
        
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
    # Define test cases as tuples of (dollars, cents, cupcakes, expected_output)
    test_cases = [
        (10, 15, 2, "20 30"),  # 10 dollars 15 cents each, 2 cupcakes → 20 dollars 30 cents
        (1, 50, 4, "6 0"),     # 1 dollar 50 cents each, 4 cupcakes → 6 dollars 0 cents
        (0, 99, 5, "4 95"),    # 0 dollars 99 cents each, 5 cupcakes → 4 dollars 95 cents
        (3, 33, 3, "9 99"),    # 3 dollars 33 cents each, 3 cupcakes → 9 dollars 99 cents
        (0, 50, 10, "5 0"),    # 0 dollars 50 cents each, 10 cupcakes → 5 dollars 0 cents
        (5, 75, 1, "5 75")     # 5 dollars 75 cents each, 1 cupcake → 5 dollars 75 cents
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print detailed feedback
    print_detailed_feedback(results)

if __name__ == '__main__':
    main()
