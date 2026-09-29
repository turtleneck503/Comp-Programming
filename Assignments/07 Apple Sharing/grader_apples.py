import subprocess

def run_student_code(n, k):
    """Run the student's code with the given inputs 'n' and 'k' and return the output."""
    process = subprocess.Popen(['python', 'apples.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    input_str = f"{n}\n{k}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for (n, k), expected_output in test_cases:
        stdout, stderr = run_student_code(n, k)
        if stderr:
            results.append(f"Error: {stderr}")
        elif stdout == expected_output:
            results.append("Pass")
        else:
            results.append(f"Fail: Expected '{expected_output}', got '{stdout}'")
    return results

def main():
    # Define test cases as tuples of ((n, k), expected_output)
    test_cases = [
        ((5, 10), "2\n0"),  # 5 students, 10 apples: each gets 2 apples, 0 remain
        ((4, 9), "2\n1"),   # 4 students, 9 apples: each gets 2 apples, 1 remains
        ((6, 14), "2\n2"),  # 6 students, 14 apples: each gets 2 apples, 2 remain
        ((3, 8), "2\n2"),   # 3 students, 8 apples: each gets 2 apples, 2 remain
        ((1, 5), "5\n0"),   # 1 student, 5 apples: each gets 5 apples, 0 remain
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print results
    for i, result in enumerate(results):
        print(f"Test case {i + 1}: {result}")

if __name__ == '__main__':
    main()
