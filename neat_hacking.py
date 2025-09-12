# Python script to create organised directory structures while pentesting
# Grouping documentation by target [network, host, CIDR etc.] eg. Win10-CEO or 10.0.0.35/24

# I know it's simple, but it works ;)

# P.S. Please create an environment variable BASE_DIR for where you want the specific target file directories to be created

# Author: Darren Sacks
# Find Me: https://www.darren-sacks.tech
# Promote Me: https://www.linkedin.com/in/darren-sacks

# Config the script variables
FILES = ["notes.txt", "rough_notes.txt", "scope.ip", "up.ip"]
FOLDERS = ["recon", "exploit", "post-exploit", "screenshots", "loot"]

# Module imports
import sys
from termcolor import cprint
import os
from pathlib import Path

# Code below...

# Utility for printing terminal output
def printMessage(message_type, message):
	match message_type:
		case "SUCCESS":
			cprint(message, 'green')
		case "INFO":
			print(message)
		case "WARNING":
			cprint(message, 'black', 'on_light_yellow')
		case "ERROR":
			cprint(message, 'black', 'on_red')
		case "CRAZY":
			BLUE = "\033[1;34;40m"
			PURPLE = "\033[1;35;40m"
			CYAN = "\033[1;36;40m"
			
			AVAIL_COLORS = [BLUE, PURPLE, CYAN]
			
			final_colored_text = ""
			
			for i in range(len(message)):

				# Get next color from available colors and put in final colored text string
				color_to_use = AVAIL_COLORS[i % len(AVAIL_COLORS)]
				final_colored_text = final_colored_text + color_to_use
				
				# Place letter now
				final_colored_text = final_colored_text + message[i]
				
			print(final_colored_text)
		case _:
			sys.exit("Fatal Error. Function printMessage() requires ENUM value for message_type.")

# Preliminary checks
def prelimChecks():
	# See if a base directory for the tree creation is defined in environment variable BASE_DIR
	BASE_DIR = os.getenv("BASEDIR")
	
	if not BASE_DIR:
		printMessage("WARNING", "Base directory for creation of file structure has not been specified by env var 'BASEDIR'.")
		BASE_DIR = input("Please provide full filepath for where to create the tree: ")
	printMessage("SUCCESS", f"Will create file structure in {BASE_DIR}")
	
	# Ask for target 
	TARGET = input("Name of target: ")
	
	# Create root of documentation file tree
	ROOT_FOLDER = os.path.join(BASE_DIR, TARGET)
	
	root_folder_path = Path(ROOT_FOLDER)
	
	if root_folder_path.is_dir():
		printMessage("ERROR", f"Folder already exists: {ROOT_FOLDER}")
		sys.exit(1)
		
	try:
		os.mkdir(ROOT_FOLDER)
	except:
		printMessage("ERROR", f"Unable to create: {ROOT_FOLDER}")
		sys.exit(1)
	
	printMessage("SUCCESS", f"Creating file structure at {ROOT_FOLDER}")

	
	
	return ROOT_FOLDER
	

# Create files and folders
def createItems(ROOT_FOLDER):

	printMessage("INFO", "Making file tree...")

	# Create folders
	for folder in FOLDERS:
		new_folder  = os.path.join(ROOT_FOLDER, folder)
		new_folder_path = Path(new_folder)
		
		if new_folder_path.is_dir():
			printMessage("ERROR", f"Folder already exists: {new_folder_path}")
			sys.exit(1)
			
		try:
			os.mkdir(new_folder)
		except:
			printMessage("ERROR", f"Unable to create: {new_folder}")
			sys.exit(1)
	# Create files
	for filename in FILES:
		new_file  = os.path.join(ROOT_FOLDER, filename)
		new_file_path = Path(new_file)
			
		try:
			with open(new_file, 'w') as fp:
    				pass
		except:
			printMessage("ERROR", f"Unable to create: {new_file}")
			sys.exit(1)


# Control flow
def main():
	# Rest of work here
	ROOT_FOLDER = prelimChecks()
	
	
	# Create folders and files (according to script config arrays)
	createItems(ROOT_FOLDER)
	
	printMessage("SUCCESS", "Finished creating folders and files.")
	
	printMessage("CRAZY", "Happy hacking ;) Don't break laws, don't get v&")
	
	

if __name__ == "__main__":
	main()
