import os

def get_files_info(working_directory, directory=".") -> str:
    # Construct the full path
    full_path = os.path.join(working_directory, directory)

    # Resolve to absolute paths
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_dir = os.path.abspath(full_path)

    # Check if target directory stays within the working directory
    if not abs_target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # Check that the target exists and is a directory
    if not os.path.isdir(abs_target_dir):
        return f'Error: "{directory}" is not a directory'
    
    