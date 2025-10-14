import os

def write_file(working_directory, file_path, content):
    # Construct the full path
    full_path = os.path.join(working_directory, file_path)

    # Resolve to absolute paths
    abs_working_dir = os.path.abspath(working_directory)
    abs_target_file = os.path.abspath(full_path)

    # Check if target directory stays within the working directory
    if not abs_target_file.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # If folders not exist create them
    if not os.path.exists(os.path.dirname(abs_target_file)):
        os.makedirs(os.path.dirname(abs_target_file), exist_ok=True)

    # Check if the file exist else create it
    if not os.path.isfile(abs_target_file):
        with open(file=abs_target_file, mode='w'):
            pass
    
    try:
        with open(file=abs_target_file,mode='w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return(f"Error: {e}")

    
