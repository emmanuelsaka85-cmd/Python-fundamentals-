import io
import sys

def run_python_code(code_string: str) -> dict:
    """
    Executes a string of Python code safely, capturing stdout and local variables.
    """
    # Create a stream to capture standard output
    output_buffer = io.StringIO()
    
    # Define custom globals and locals to avoid polluting the main environment
    exec_globals = {}
    exec_locals = {}
    
    # Redirect stdout to capture print statements
    sys.stdout = output_buffer
    
    try:
        # Execute the code
        exec(code_string, exec_globals, exec_locals)
        status = "SUCCESS"
    except Exception as e:
        status = "ERROR"
        # If there's an error, write it to the buffer or handle it
        print(f"Exception: {e}", file=sys.stdout)
    finally:
        # Reset the standard output
        sys.stdout = sys.__stdout__
        
    return {
        "status": status,
        "output": output_buffer.getvalue().strip(),
        "locals": exec_locals
    }

# --- Examples ---

# 1. Standard variable assignment and print
code1 = """
x = 10
y = 20
result = x + y
print(f"The result is: {result}")
"""

result1 = run_python_code(code1)
print("--- Example 1 Output ---")
print(result1["output"])
print(f"Variables: {result1['locals']}\n")

# 2. Example with errors
code2 = """
print("Starting...")
x = 5 / 0  # Will throw a ZeroDivisionError
"""

result2 = run_python_code(code2)
print("--- Example 2 Output ---")
print(result2["output"])
print(f"Status: {result2['status']}")
