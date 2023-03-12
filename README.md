# Append-CLIP-Interrogation
Simple python script to automatically append caption generated by CLIP interrogator to an image file

The main use case is to quickly give a more descriptive and searchable name to an image.

## Installation
Download append-clip-interrogation.py and place it in a directory. Navigate to that directory in the terminal and follow instructions at https://github.com/pharmapsychotic/clip-interrogator to create venv with CLIP interrogator package

## Usage
Single image:   
`python append-clip-interrogation.py --path /path/to/image`  

    Appened CLIP interrogation to file

    optional arguments:
      -h, --help   show this help message and exit
      --path PATH  Path to the image
      --crop       Pass a cropped version of the image to interrogator if it is larger than --res
      --res RES    Cropped resolution

Batch process:   
`chmod +x batch-process.sh`
`./batch-process.sh path/to/image-directory`
