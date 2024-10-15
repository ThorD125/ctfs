import os

def create_md_files(root_directory):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(root_directory):
        # Get the current directory name
        dir_name = os.path.basename(root)
        # Filter and list only .md files
        md_files = [file for file in files if file.endswith('.md')]
        
        # Only proceed if there are .md files or subdirectories
        if md_files or dirs:
            # Create a filename with the format directoryname.md
            md_filename = os.path.join(root, f"{dir_name}.md")
            
            # Create the content to be written into the markdown file
            content = f"# {dir_name}\n\n"
            
            # Add subdirectories to the content with links to their .md files
            if dirs:
                content += "## Subdirectories:\n"
                for directory in dirs:
                    content += f"- [{directory}]({directory}/{directory}.md)\n"
            
            # Add the list of .md files to the content
            if md_files:
                content += "\n## Files:\n"
                for file in md_files:
                    content += f"- [{file}]({file})\n"
            
            # Write the content to the .md file
            with open(md_filename, 'w') as md_file:
                md_file.write(content)

# Specify the root directory where you want the script to start
root_directory = "challenges"
create_md_files(root_directory)
