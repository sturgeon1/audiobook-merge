# audiobook-merge
Python script to copy audiobook files from multiple subfolders, paste them in a new directory, and rename them sequentially.

If you're an audiobook enthusiast, you'll no doubt find that some of the audiobooks you've legally digitized are split into multiple 
"disk" folders within the parent directory. 
This file structure doesn't play well with services like audiobookshelf that are expecting all audiobook files in a single folder.
This script loops through a given audiobook directory, copies all audio files to a chosen destination, and renames them sequentially in the format 001.mp3.

I'm no python or filesystem expert, but this seems to work well enough. If others have a different way they go about this issue I'd love to hear it!
