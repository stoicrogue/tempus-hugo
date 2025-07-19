cd /z/code/tempus
robocopy "Z:\\documents\\obsidian\\Mark\\tempus-campaign\\" "Z:\\code\\tempus\\content\\" //MIR
python sync-obsidian-images.py