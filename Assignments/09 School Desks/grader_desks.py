import subprocess

def run_student_code(a, b, c):
    """Run the student's desks.py code with the given inputs for the number of students."""
    process = subprocess.Popen(['python', 'desks.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    # Input format as expected by desks.py (3 inputs for number of students)
    input_str = f"{a}\n{b}\n{c}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for i, (inputs, expected_output) in enumerate(test_cases):
        a, b, c = inputs
        stdout, stderr = run_student_code(a, b, c)

        # Check for errors
        if stderr:
            results.append({
                'test_case': i + 1,
                'status': 'Error',
                'inputs': (a, b, c),
                'expected': expected_output,
                'actual': stdout,
                'error': stderr
            })
        # Check if the output matches the expected output
        elif stdout == expected_output:
            results.append({
                'test_case': i + 1,
                'status': 'Pass',
                'inputs': (a, b, c),
                'expected': expected_output,
                'actual': stdout
            })
        else:
            results.append({
                'test_case': i + 1,
                'status': 'Fail',
                'inputs': (a, b, c),
                'expected': expected_output,
                'actual': stdout,
                'error': None
            })
    return results

def print_detailed_feedback(results):
    """Print detailed feedback for each test case."""
    for result in results:
        print(f"\nTest case {result['test_case']}:")
        print(f"  Inputs: {result['inputs']}")
        
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
    # Define test cases as tuples of ((a, b, c), expected_output)
    test_cases = [
        ((20, 21, 22), "32"),  # 10 desks for 20 students, 11 for 21, 11 for 22 => 32 desks
        ((15, 15, 15), "24"),  # Each class needs 8 desks => 24 total
        ((1, 1, 1), "3"),      # 1 desk per class => 3 desks total
        ((30, 30, 30), "45"),  # Each class needs 15 desks => 45 total
        ((0, 0, 0), "0"),      # No students, no desks needed
        ((9, 9, 9), "15"),     # Each class needs 5 desks => 15 total
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print detailed feedback
    print_detailed_feedback(results)

if __name__ == '__main__':
    main()
