# audiobook-merge

If you're an audiobook enthusiast, you'll no doubt find that some of the audiobooks you've legally digitized are split into multiple "disk" folders within the parent directory. 
This file structure doesn't play well with services like audiobookshelf that are expecting all
audiobook files in a single folder.

This script loops through a given audiobook directory, copies all audio files to a chosen destination, and renames them sequentially in the format 001.mp3, 002.mp3, etc. It prompts the user for both source and destination directories, and saves the destination directory to a dest_dir.txt file. When the script runs again, it will pull the destination from the text file and offer it for quick use.

I'm no python or filesystem expert, but this seems to work well enough. If others have a different way they go about this issue I'd love to hear about it!
