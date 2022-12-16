import nuke
import platform

# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\babis\.nuke'
MacOSX_Dir = 'Users/babis/.nuke'
Linux_Dir = 'home/babis/.nuke'

# Set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None
