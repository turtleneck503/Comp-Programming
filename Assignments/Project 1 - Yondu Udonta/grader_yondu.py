import subprocess

def run_student_code(pirates, total_units):
    """Run the student's yondu.py code with the given inputs."""
    process = subprocess.Popen(['python', 'yondu.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    # Input format as expected by yondu.py (pirates, total_units)
    input_str = f"{pirates}\n{total_units}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def parse_output(stdout):
    """Parse the student's output into a dictionary."""
    result = {}
    for line in stdout.splitlines():
        if line:
            key, value = line.split(": ")
            result[key.strip()] = int(value.strip())
    return result

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for i, (pirates, total_units, expected_output) in enumerate(test_cases):
        stdout, stderr = run_student_code(pirates, total_units)

        # Check for errors
        if stderr:
            results.append({
                'test_case': i + 1,
                'status': 'Error',
                'inputs': (pirates, total_units),
                'expected': expected_output,
                'actual': stdout,
                'error': stderr
            })
        else:
            actual_output = parse_output(stdout)
            
            # Check if the output matches the expected output exactly
            if actual_output == expected_output:
                results.append({
                    'test_case': i + 1,
                    'status': 'Pass',
                    'inputs': (pirates, total_units),
                    'expected': expected_output,
                    'actual': actual_output
                })
            else:
                results.append({
                    'test_case': i + 1,
                    'status': 'Fail',
                    'inputs': (pirates, total_units),
                    'expected': expected_output,
                    'actual': actual_output,
                    'error': None
                })
    return results

def print_detailed_feedback(results):
    """Print detailed feedback for each test case."""
    for result in results:
        print(f"\nTest case {result['test_case']}:")
        print(f"  Inputs (pirates, total_units): {result['inputs']}")
        
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
    # Define test cases as tuples of (pirates, total_units, expected_output)
    test_cases = [
        (
            20, 1000, 
            {"Yondu's share": 158, "Peter's share": 126, 'Crew': 36, 'RBF': 14}
        ),  # Test case 1
        (
            15, 500, 
            {"Yondu's share": 82, "Peter's share": 67, 'Crew': 23, 'RBF': 13}
        ),  # Test case 2
        (
            25, 2000, 
            {"Yondu's share": 310, "Peter's share": 243, 'Crew': 59, 'RBF': 21}
        ),  # Test case 3
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print detailed feedback
    print_detailed_feedback(results)

if __name__ == '__main__':
    main()
