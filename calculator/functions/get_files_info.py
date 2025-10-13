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
    

    
    try:
        lines = [f"Result for {directory if directory != '.' else 'current directory'}:"]
        with os.scandir(full_path) as entries:
            for item in entries:
                lines.append(
                    f" - {item.name}: file_size={item.stat().st_size} bytes, is_dir={item.is_dir()}"
                )
        return "\n".join(lines)
    except Exception as e:
        return(f"Error: {e}")
