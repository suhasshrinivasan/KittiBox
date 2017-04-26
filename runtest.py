"""
Calls demo.py on a series of test images.

IN: dir containing series of test images.
OUT: output of demo.py.

Run instruction:
python runtest.py <dir>

NOTE: dir must be absolute.
"""

import sys
import os
import subprocess

if len(sys.argv) < 2:
	print "Run instruction: python runtest.py <dir>\nABORTING"
	sys.exit()

run_command = "python demo.py --input_image"

# Directory of images
dir_in = sys.argv[1]

# Loop over each image file in given directory
frame_number = 1
for file in sorted(os.listdir(dir_in)):
	image_file = dir_in + '/' + str(file)
	print image_file
	subprocess.call(run_command + " " + image_file + " " + frame_number)
	frame_number = frame_number + 1