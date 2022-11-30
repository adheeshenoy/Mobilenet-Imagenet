import tarfile
import numpy as np
import cv2
import os

def extract(path = 'dataset.tar'):
    file = tarfile.TarFile.open(path)
    file.extractall()

if __name__ == '__main__':
    extract()