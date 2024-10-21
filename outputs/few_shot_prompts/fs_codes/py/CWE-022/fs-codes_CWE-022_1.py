first:
    with tarfile.open(file_name) as f:
        f.extractall()
second:
import json
import urllib.request as request
import tarfile
import os

def extract_zip(file_name):
    # extract the zip file

###
first:
    # Open the tar archive
    tar = tarfile.open(tar_path)

    # Iterate over the files in the tar archive
    for tarinfo in tar:

       tar.extract(tarinfo, path=dest_dir)

    # Close the tar archive
    tar.close()

second:
import os
import tarfile

def extract_files(tar_path, dest_dir):
    """
    Extract the files from a tar archive
    """


###
first:
    tar = tarfile.open(fileName, "r")
    tar.extractall()
    tar.close()
second:
import tarfile
import os

def readArchive(fileName):
    '''
    Read the archive file and extract it to the current directory
    '''

###
first:
    with tarfile.open(image, mode='r:gz') as tar:
        tar.extractall()
        tar.close()
        os.remove(image)

second:
import tarfile
import os
from urllib.request import urlopen