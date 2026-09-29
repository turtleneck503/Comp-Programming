import subprocess

def run_student_code(h1, m1, s1, h2, m2, s2):
    """Run the student's code with the given timestamp inputs and return the output."""
    process = subprocess.Popen(['python', 'timestamp.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    input_str = f"{h1}\n{m1}\n{s1}\n{h2}\n{m2}\n{s2}\n"
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip(), stderr

def grade_code(test_cases):
    """Grade the student's code using the given test cases."""
    results = []
    for (h1, m1, s1, h2, m2, s2), expected_output in test_cases:
        stdout, stderr = run_student_code(h1, m1, s1, h2, m2, s2)
        if stderr:
            results.append(f"Error: {stderr}")
        elif stdout == expected_output:
            results.append("Pass")
        else:
            results.append(f"Fail: Expected '{expected_output}', got '{stdout}'")
    return results

def main():
    # Define test cases as tuples of ((h1, m1, s1, h2, m2, s2), expected_output)
    test_cases = [
        # Same timestamp: no difference
        ((0, 0, 0, 0, 0, 0), "0"),
        
        # One second difference
        ((0, 0, 0, 0, 0, 1), "1"),
        
        # One minute difference
        ((0, 0, 0, 0, 1, 0), "60"),
        
        # One hour difference
        ((0, 0, 0, 1, 0, 0), "3600"),
        
        # Crossing minute boundary (59 seconds)
        ((0, 59, 59, 1, 0, 0), "1"),
        
        # Crossing hour boundary (59 minutes, 59 seconds)
        ((1, 59, 59, 2, 0, 0), "1"),
        
        # Midnight boundary (23:59:59 to 00:00:00 next day)
        ((23, 59, 59, 0, 0, 0), "-86399"),  # Negative or invalid case
        
        # Full day (24-hour difference)
        ((0, 0, 0, 23, 59, 59), "86399"),  # Almost a full day (1 second short)
        
        # Random case
        ((12, 0, 0, 14, 30, 30), "9030"),  # 2 hours, 30 min, 30 sec difference
    ]
    
    # Run grading
    results = grade_code(test_cases)
    
    # Print results
    for i, result in enumerate(results):
        print(f"Test case {i + 1}: {result}")

if __name__ == '__main__':
    main()

