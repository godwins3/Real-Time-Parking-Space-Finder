try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Parking Space Detector using OpenCV and RPI",
    "author": "Project Team DSA",
    "url": "t",
    "download_url": "",
    "version": "0.1",
    "install_requires": ["cv2", "numpy", "yml"],
    "packages": ["parking_lot"],
    "scripts": [],
    "name": "ParkingLot"
}

setup(**config)
