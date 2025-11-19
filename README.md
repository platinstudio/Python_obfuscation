
# Python File Obfuscator

A lightweight Python tool for obfuscating Python files in a directory using zlib compression and base64 encoding.[1]

## Description

This tool recursively searches for Python files in a specified directory and obfuscates them using a combination of zlib compression and base64 encoding techniques. The obfuscation makes the code harder to read while maintaining full functionality.[3][9][1]

## Features

- **Recursive Directory Scanning**: Automatically finds all Python files in a directory and its subdirectories
- **Automatic Backup**: Creates backup files (`.py.bak`) before obfuscation to prevent data loss
- **Smart Directory Exclusion**: Automatically skips common directories like `venv`, `__pycache__`, `.git`, `dist`, and `build`
- **Compression & Encoding**: Uses zlib compression combined with base64 encoding for effective obfuscation
- **Detailed Reporting**: Provides comprehensive output showing successful and failed obfuscations
- **Interactive & CLI Modes**: Can be run interactively or with command-line arguments

## Requirements

- Python 3.6 or higher
- Standard library modules: `os`, `base64`, `zlib`, `sys` (no external dependencies required)

## Installation

### Method 1: Clone the Repository

```bash
git clone https://github.com/yourusername/python-obfuscator.git
cd python-obfuscator
```

### Method 2: Download Script

Download the `obfuscator.py` file directly and save it to your project directory.[1]

## Usage

### Interactive Mode

Run the script without arguments for interactive mode:

```bash
python obfuscator.py
```

You will be prompted to enter the directory path and confirm the operation.[3][1]

### Command-Line Mode

Specify the target directory as a command-line argument:

```bash
python obfuscator.py /path/to/your/directory
```

### Programmatic Usage

You can also import and use the obfuscator in your Python code:

```python
from obfuscator import find_and_obfuscate_python_files, obfuscate_python_file

# Obfuscate all Python files in a directory
find_and_obfuscate_python_files('/path/to/directory', backup=True)

# Obfuscate a single file
obfuscate_python_file('input.py', 'output_obfuscated.py')
```

## How It Works

The obfuscation process follows these steps:[6][1]

1. **Read Original Code**: The script reads the source Python file
2. **Compress**: The code is compressed using zlib with maximum compression level (9)
3. **Encode**: The compressed data is encoded using base64
4. **Reverse**: The encoded string is reversed for additional obfuscation
5. **Wrap**: The result is wrapped in an exec statement with lambda function
6. **Write**: The obfuscated code replaces the original file (with backup created)

### Obfuscated Code Structure

The obfuscated output follows this pattern:

```python
# Python obfuscation tool
# Obfuscated file: original_filename.py

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'encoded_data_here'))
```

## Examples

### Example 1: Obfuscate Current Directory

```bash
python obfuscator.py .
```

### Example 2: Obfuscate Specific Project

```bash
python obfuscator.py /home/user/myproject
```

### Example 3: Custom Directory Exclusion

Modify the `exclude_dirs` parameter in the code:

```python
find_and_obfuscate_python_files(
    '/path/to/directory',
    backup=True,
    exclude_dirs=['venv', 'tests', 'docs']
)
```

## Output Example

```
Python File Obfuscator
==================================================
Target directory: /home/user/project
WARNING: This will modify all Python files in this directory and subdirectories!
Backup files (.py.bak) will be created automatically.

Do you want to continue? (yes/no): yes

Starting obfuscation process...

Backup created: /home/user/project/script1.py.bak
Obfuscating: /home/user/project/script1.py
✓ Successfully obfuscated: /home/user/project/script1.py

Backup created: /home/user/project/utils/helper.py.bak
Obfuscating: /home/user/project/utils/helper.py
✓ Successfully obfuscated: /home/user/project/utils/helper.py

==================================================
Obfuscation completed!
Successfully obfuscated: 2 files
Failed: 0 files
==================================================
```

## Security Considerations

**Important**: This obfuscation method is designed to make code harder to read but does not provide complete security. The obfuscated code can be reverse-engineered with effort. For production-level protection, consider using:[8][9]

- **PyArmor**: Professional obfuscation with bytecode protection
- **Nuitka**: Compiles Python to C/C++ executables
- **Cython**: Converts Python to C extensions

This tool is best suited for:
- Protecting intellectual property from casual inspection
- Educational purposes
- Making code distribution less transparent
- Adding a basic layer of code protection

## Restoring Original Files

If you need to restore the original files, simply rename the backup files:[1]

```bash
# Restore a single file
mv script.py.bak script.py

# Restore all files in directory (Linux/Mac)
find . -name "*.py.bak" -exec sh -c 'mv "$1" "${1%.bak}"' _ {} \;

# Restore all files (Windows PowerShell)
Get-ChildItem -Recurse -Filter "*.py.bak" | Rename-Item -NewName { $_.Name -replace '.bak$','' }
```

## Limitations

- Does not obfuscate variable names or function names within the code
- Performance overhead due to decompression at runtime
- Not suitable for protecting against determined reverse engineering
- Slightly increases file size due to encoding

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.[1]

## License

This project is licensed under the MIT License - see the LICENSE file for details.[1]

## Disclaimer

This tool is provided for educational and legitimate code protection purposes only. Users are responsible for ensuring compliance with applicable laws and regulations when using this tool.[1]

## Author

[[platinstudio](https://github.com/platinstudio/)]

## Support

For issues, questions, or suggestions, please open an issue on GitHub.[3][1]

[1](https://github.com/malwarekid/Pyfuscator)
[2](https://github.com/dashingsoft/pyarmor)
[3](https://github.com/davidteather/python-obfuscator)
[4](https://github.com/billythegoat356/Kramer)
[5](https://pypi.org/project/PyObfuscator/)
[6](https://github.com/phanxuanphucnd/Code-Obfuscation)
[7](https://github.com/liftoff/pyminifier)
[8](https://albertuskelvin.github.io/posts/2019/12/code-obfuscation-with-pyarmor/)
[9](https://stackoverflow.com/questions/3344115/how-to-obfuscate-python-code-effectively)
[10](https://pyarmor.readthedocs.io/en/v6.6.1/mode.html)
