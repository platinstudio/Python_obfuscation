import os
import base64
import zlib
import sys
################################################
#
#   Code by Pl4ten @ platinco.ir
#
###############################################
def obfuscate_python_file(file_path, output_path=None):
    """
    Obfuscate a Python file using base64 and zlib compression
    
    Args:
        file_path: Path to the Python file to obfuscate
        output_path: Path for the obfuscated file (if None, overwrites original)
    """
    try:
        # Read the original Python code
        with open(file_path, 'r', encoding='utf-8') as f:
            original_code = f.read()
        
        # Compress with zlib and encode with base64
        compressed = zlib.compress(original_code.encode('utf-8'), 9)
        encoded = base64.b64encode(compressed)
        
        # Reverse the encoded string (like in your example)
        reversed_encoded = encoded[::-1]
        
        # Create the obfuscated code template
        obfuscated_code = f"""# Python obfuscation tool
# Obfuscated file: {os.path.basename(file_path)}

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'{reversed_encoded.decode('utf-8')}'))
"""
        
        # Write the obfuscated code
        output = output_path if output_path else file_path
        with open(output, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
        
        return True
    
    except Exception as e:
        print(f"Error obfuscating {file_path}: {e}")
        return False

def find_and_obfuscate_python_files(root_directory, backup=True, exclude_dirs=None):
    """
    Find and obfuscate all Python files in a directory recursively
    
    Args:
        root_directory: Root directory to search for Python files
        backup: Create backup files before obfuscation (.py.bak)
        exclude_dirs: List of directory names to exclude (e.g., ['venv', '__pycache__'])
    """
    if exclude_dirs is None:
        exclude_dirs = ['venv', 'env', '__pycache__', '.git', 'dist', 'build']
    
    obfuscated_count = 0
    failed_count = 0
    
    # Walk through the directory tree
    for root, dirs, files in os.walk(root_directory):
        # Remove excluded directories from the search
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        # Process each Python file
        for file in files:
            if file.endswith('.py') and not file.endswith('.bak.py'):
                file_path = os.path.join(root, file)
                
                # Create backup if requested
                if backup:
                    backup_path = file_path + '.bak'
                    try:
                        with open(file_path, 'r', encoding='utf-8') as original:
                            with open(backup_path, 'w', encoding='utf-8') as backup_file:
                                backup_file.write(original.read())
                        print(f"Backup created: {backup_path}")
                    except Exception as e:
                        print(f"Failed to create backup for {file_path}: {e}")
                        continue
                
                # Obfuscate the file
                print(f"Obfuscating: {file_path}")
                if obfuscate_python_file(file_path):
                    obfuscated_count += 1
                    print(f"✓ Successfully obfuscated: {file_path}")
                else:
                    failed_count += 1
                    print(f"✗ Failed to obfuscate: {file_path}")
    
    # Print summary
    print("\n" + "="*50)
    print(f"Obfuscation completed!")
    print(f"Successfully obfuscated: {obfuscated_count} files")
    print(f"Failed: {failed_count} files")
    print("="*50)

def main():
    """
    Main function to run the obfuscator
    """
    print("Python File Obfuscator")
    print("="*50)
    
    # Get directory from command line argument or ask user
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        target_directory = input("Enter the directory path to obfuscate (or '.' for current directory): ").strip()
    
    # Validate directory
    if not os.path.isdir(target_directory):
        print(f"Error: '{target_directory}' is not a valid directory!")
        return
    
    # Confirm action
    print(f"\nTarget directory: {os.path.abspath(target_directory)}")
    print("WARNING: This will modify all Python files in this directory and subdirectories!")
    print("Backup files (.py.bak) will be created automatically.")
    
    confirm = input("\nDo you want to continue? (yes/no): ").strip().lower()
    
    if confirm in ['yes', 'y']:
        print("\nStarting obfuscation process...\n")
        find_and_obfuscate_python_files(target_directory, backup=True)
    else:
        print("Obfuscation cancelled.")

if __name__ == "__main__":
    main()
