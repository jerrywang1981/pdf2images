#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import random
from datetime import datetime
import tempfile
import glob
from pdf2image import convert_from_path

def generateRandomString():
    return '%s.%s' % (datetime.today().strftime('%Y%m%d'), str(random.randint(100000,999999)))

def pdf_to_images(file_name, output_folder):
    exportFolderName = generateRandomString()
    imageProcessedFolder = '%s/%s/' % (output_folder, exportFolderName)
    if not os.path.exists(imageProcessedFolder):
        os.makedirs(imageProcessedFolder)

    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path(file_name, output_folder=path)
        for index, img in enumerate(images, 300):
            imageFileName = '%s%s_%s.png' % (imageProcessedFolder, exportFolderName, index)
            img.save(imageFileName)


def pdf_folder_to_images(folder_name, output_folder):
    files = [f for f in glob.glob(os.path.join(folder_name, "**/*.pdf"), recursive=True)]
    files += [f for f in glob.glob(os.path.join(folder_name, "**/*.PDF"), recursive=True)]
    for f in files:
        pdf_to_images(f, output_folder)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('call in format python xxx.py input_file output_folder')
        sys.exit(0)

    input_file, output_folder = sys.argv[1], sys.argv[2]
    if not os.path.exists(input_file):
        print('input file does not exist')
        sys.exit(0)

    if not os.path.isdir(output_folder):
        print('output folder does not exist')
        sys.exit(0)

    if os.path.isdir(input_file):
        pdf_folder_to_images(input_file, output_folder)
    elif os.path.isfile(input_file):
        pdf_to_images(input_file, output_folder)

    print('done')
