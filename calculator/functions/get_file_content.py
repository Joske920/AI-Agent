import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    # Construct the full path
    full_path = os.path.join(working_directory, file_path)

    # Resolve to absolute paths
    abs_working_dir = os.path.abspath(working_directory)
    print(abs_working_dir)
    abs_target_file = os.path.abspath(full_path)
    print(abs_target_file)
    # Check if target directory stays within the working directory
    if not abs_target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # Check that the target exists and is a directory
    if not os.path.isfile(abs_target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_target_file) as f:
            file_contents = f.read(MAX_CHARS)
            if os.path.getsize(abs_target_file) > MAX_CHARS:
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_contents
    except Exception as e:
        return(f"Error: {e}")
    