import subprocess

def run_student_code(input_values):
    """Run the student's next.py code with the given inputs."""
    process = subprocess.Popen(['python', 'next.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    # Input format: month and day, each on a new line
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
        ([3, 30], "3\n31"),     # Normal case: March 30 -> March 31
        ([3, 31], "4\n1"),      # Transition to next month: March 31 -> April 1
        ([12, 31], "1\n1"),     # Transition to next year: December 31 -> January 1
        ([4, 30], "5\n1"),      # April 30 -> May 1
        ([7, 15], "7\n16"),     # Regular case: July 15 -> July 16
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print detailed feedback
    print_detailed_feedback(results)

if __name__ == '__main__':
    main()
