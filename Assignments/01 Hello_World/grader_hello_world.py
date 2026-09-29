import unittest
import io
import contextlib

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        # Capture the output
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            try:
                import hello_world
            except Exception as e:
                self.fail(f"Your code encountered an error: {str(e)}")

        # Get the output and remove any surrounding whitespace
        output = f.getvalue().strip()

        # Define the expected output
        expected_output = "Hello world!"

        # Check if the output matches the expected output
        if output != expected_output:
            self.fail(self.generate_feedback(output, expected_output))
        else:
            print("Test passed! Good job.")

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
