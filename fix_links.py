import os

def add_md_extension_to_files(root_directory):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            # Check if the file has no extension
            if '.' not in file:
                # Add the .md extension
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, f"{file}.md")
                os.rename(old_file_path, new_file_path)

def create_md_files(root_directory):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(root_directory):
        # Get the current directory name
        dir_name = os.path.basename(root)
        
        # If we are in the root directory, set the filename to "tree.md"
        if root == root_directory:
            md_filename = os.path.join(root, "tree.md")
        else:
            # Otherwise, create a filename with the format directoryname.md
            md_filename = os.path.join(root, f"{dir_name}.md")
        
        # Filter and list only .md and .lst files
        relevant_files = [file for file in files if file.endswith('.md') or file.endswith('.lst')]
        
        # Only proceed if there are .md/.lst files or subdirectories
        if relevant_files or dirs:
            # Create the content to be written into the markdown file
            content = f"# {dir_name if root != root_directory else 'Root Directory'}\n\n"
            
            # Add subdirectories to the content with links to their .md files
            if dirs:
                content += "## Subdirectories:\n"
                for directory in dirs:
                    content += f"- [{directory}]({directory}/{directory}.md)\n"
            
            # Add the list of .md and .lst files to the content
            if relevant_files:
                content += "\n## Files:\n"
                for file in relevant_files:
                    content += f"- [{file}]({file})\n"
            
            # Write the content to the .md file
            with open(md_filename, 'w') as md_file:
                md_file.write(content)

# Set the root directory to be the current directory (".")
root_directory = "."

# First, add .md extensions to files without extensions
add_md_extension_to_files(root_directory)

# Then, create the markdown files as described
create_md_files(root_directory)
