# Neat-Hacking
Stay organised while pentesting/red-teaming (I know you aren't)! Simple Python script to make a habit in your workflow before initiating an engagement or moving onto new targets.

This script just creates a file tree of useful folders and files for each target, so that you keep track of the different attack stages and evidence gathered, in a uniform way.

# Super simple usage

0 - [Optional] Define an environment variable called BASE_DIR which will serve as the starting point of all file trees created by the script. I personally think this is worthwhile, as opposed to inputing this each time via CLI (but as fallback I allowed direct CLI input via user input).

1 - Input name of base directory (full file path) if not already specified by BASE_DIR environment variable.

2 - Input name of target you want to create file tree for.

3 - Visit the file tree as specified in the terminal output eg. /<base_directory>/<target_name>

# Customisation

Easily customize the files and folders created via the arrays at the top of the script (Should be clear based on comments in code).

Rest of code need not be touched unless you want to expand usage.
