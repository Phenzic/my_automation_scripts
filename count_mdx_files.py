import os

def count_mdx_files(directory):
    """
    Count all MDX files in a directory and its subdirectories.
    
    Args:
        directory (str): Path to the directory to search in
        
    Returns:
        int: Number of MDX files found
    """
    count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.mdx'):
                count += 1
                print(f"Found MDX file: {os.path.join(root, file)}")
    return count

if __name__ == '__main__':
    # Get the current directory if no path is specified
    search_dir = os.getcwd()
    
    total_files = count_mdx_files(search_dir)
    print(f"\nTotal MDX files found: {total_files}") 