import sys, os, tarfile
import os

def open_tar_file(filename):
	tar = tarfile.open(filename)
	tar.extractall()
	tar.close()

def extract_all_content(directory_path):
	for root, dirs, files in os.walk(directory_path):
		for file in files:
			if file.endswith(".tgz"):
				open_tar_file(os.path.join(root, file))

dirname = sys.argv[1]
extract_all_content(dirname)
