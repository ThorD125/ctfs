import os
import re
import urllib.parse

def remove_directory_md_files(root_directory):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(root_directory):
        # Get the current directory name
        dir_name = os.path.basename(root)
        
        # Remove the directory's .md file if it exists (e.g., tree.md or directoryname.md)
        if root == root_directory:
            md_filename = os.path.join(root, "tree.md")  # Root directory's .md file
        else:
            md_filename = os.path.join(root, f"{dir_name}.md")  # Subdirectory's .md file

        if os.path.exists(md_filename):
            os.remove(md_filename)

def add_md_extension_to_files(root_directory):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(root_directory):
        # Skip .vscode and .git folders
        dirs[:] = [d for d in dirs if d not in ['.vscode', '.git']]
        
        for file in files:
            # Check if the file has no extension and is not purely numeric
            if '.' not in file and not re.match(r'^\d+$', file):
                # Add the .md extension
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, f"{file}.md")
                os.rename(old_file_path, new_file_path)

def create_md_files(root_directory):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(root_directory):
        # Skip .vscode and .git folders
        dirs[:] = [d for d in dirs if d not in ['.vscode', '.git']]
        
        # Get the current directory name
        dir_name = os.path.basename(root)
        
        # If we are in the root directory, set the filename to "tree.md"
        if root == root_directory:
            md_filename = os.path.join(root, "tree.md")
        else:
            # Otherwise, create a filename with the format directoryname.md
            md_filename = os.path.join(root, f"{dir_name}.md")
        
        # Filter and list only .md and .lst files, excluding the current .md file itself
        relevant_files = [
            file for file in files 
            if (file.endswith('.md') or file.endswith('.lst')) 
            and file != os.path.basename(md_filename) 
            and not re.match(r'^\d+\.(md|lst)$', file)  # Ignore files that are only numbers
        ]
        
        # Check if there are subdirectories or relevant files
        subdirs_with_content = []
        for directory in dirs:
            subdir_path = os.path.join(root, directory)
            subdir_md_file = os.path.join(subdir_path, f"{directory}.md")
            
            # Check if subdirectory contains any files or subdirectories
            subdir_files = [f for f in os.listdir(subdir_path) if not re.match(r'^\d+\.(md|lst)$', f)]
            
            # Include subdirectory if it contains files or sub-subdirectories, or has its own .md file
            if subdir_files or os.path.exists(subdir_md_file):
                encoded_directory = urllib.parse.quote(directory)  # Replace spaces with %20
                subdirs_with_content.append(f"- [{directory}]({encoded_directory}/{encoded_directory}.md)\n")
        
        # Only proceed if there are relevant files or subdirectories with content
        if relevant_files or subdirs_with_content:
            # Create the content to be written into the markdown file
            content = f"# {dir_name if root != root_directory else 'Root Directory'}\n\n"
            
            # Add subdirectories with content to the parent file
            if subdirs_with_content:
                content += "## Subdirectories:\n" + "".join(subdirs_with_content)
            
            # Add the list of .md and .lst files to the content
            if relevant_files:
                content += "\n## Files:\n"
                for file in relevant_files:
                    encoded_file = urllib.parse.quote(file)  # Replace spaces with %20
                    content += f"- [{file}]({encoded_file})\n"
            
            # Write the content to the .md file
            with open(md_filename, 'w') as md_file:
                md_file.write(content)

# Set the root directory to be the current directory (".")
root_directory = "."

# First, remove only the existing directory .md files (tree.md and subdirectory .md files)
remove_directory_md_files(root_directory)

# Then, add .md extensions to files without extensions, ignoring numeric filenames
add_md_extension_to_files(root_directory)

# Finally, create the markdown files as described
create_md_files(root_directory)
