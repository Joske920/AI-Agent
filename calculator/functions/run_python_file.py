import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    # Construct the full path
    full_path = os.path.join(working_directory, file_path)

    # Resolve to absolute paths
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(full_path)

    # Check if target directory stays within the working directory
    if not abs_target_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # Check if the file exists
    if not os.path.isfile(abs_target_file):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        # Construct the command to run the Python file
        cmd = ['python', abs_target_file] + args
        
        # Execute the Python file using subprocess.run
        completed_process = subprocess.run(
            cmd,
            timeout=30,
            capture_output=True,
            text=True,  # Decode bytes to string
            cwd=abs_working_dir
        )
        
        # Format the output
        output_lines = []
        
        # Add stdout if present
        if completed_process.stdout:
            output_lines.append(f"STDOUT: {completed_process.stdout.strip()}")
        
        # Add stderr if present
        if completed_process.stderr:
            output_lines.append(f"STDERR: {completed_process.stderr.strip()}")
        
        # Check for non-zero exit code
        if completed_process.returncode != 0:
            output_lines.append(f"Process exited with code {completed_process.returncode}")
        
        # Return formatted output or "No output produced."
        if output_lines:
            return '\n'.join(output_lines)
        else:
            return "No output produced."
    
    except Exception as e:
        return f"Error: {e}"
