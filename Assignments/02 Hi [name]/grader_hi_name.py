import unittest
import io
import contextlib
from unittest.mock import patch

class TestHiName(unittest.TestCase):
    def test_hi_name_output(self):
        test_cases = [("fred", "Hi fred!"), ("caveman", "Hi caveman!"), ("julie", "Hi julie!")]

        for name, expected_output in test_cases:
            with patch('builtins.input', return_value=name):
                # Capture the output
                f = io.StringIO()
                with contextlib.redirect_stdout(f):
                    try:
                        import hi_name  # Assuming your script is named hi_name.py
                        # Re-import the module to reset its state for each test case
                        import importlib
                        importlib.reload(hi_name)
                    except Exception as e:
                        self.fail(f"Your code encountered an error: {str(e)}")

                # Get the output and remove any surrounding whitespace
                output = f.getvalue().strip().splitlines()[0]  # Capture only the first line of output

                # Check if the output matches the expected output
                if output != expected_output:
                    self.fail(self.generate_feedback(output, expected_output))
                else:
                    print(f"Test passed for input '{name}'! Good job.")

    def generate_feedback(self, actual_output, expected_output):
        feedback = "Your code did not print the expected output.\n"
        feedback += f"Expected: '{expected_output}'\n"
        feedback += f"Got: '{actual_output}'\n"

        # Provide specific feedback
        if actual_output.lower() == expected_output.lower():
            feedback += "Check the capitalization of your output."
        elif actual_output.strip() != expected_output:
            feedback += "There might be extra spaces or characters in your output."
        else:
            feedback += "Ensure your output matches exactly with " + expected_output + "."
        
        return feedback

if __name__ == "__main__":
    unittest.main()
