from PIL import Image
import sys
import os
from clip_interrogator import Config, Interrogator

# Define the constant for the image size
IMAGE_SIZE = 1024

if len(sys.argv) == 2:
	imagePath = sys.argv[1]
	if (not os.path.exists(imagePath)):
		sys.exit("Error: Invalid path.")
else:
	sys.exit("Error: Please provide a path as a command line argument.")

image = Image.open(imagePath).convert('RGB')


# Get the original image size
width, height = image.size

# Calculate the coordinates for the center crop
left, top = (width - IMAGE_SIZE) // 2, (height - IMAGE_SIZE) // 2

# Crop the image to the specified size at the center
cropped_image = image.crop((left, top, left + IMAGE_SIZE, top + IMAGE_SIZE))


#Interrogate
ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))
result_string = ci.interrogate(cropped_image)


# get the base name of the file (i.e., the file name without the directory)
base_name = os.path.basename(imagePath)

# split the base name into its name and extension parts
name, ext = os.path.splitext(base_name)

# add caption to the end of the name part
new_name = name + result_string

# get the maximum length of a file name for the file system where the file is located
max_name_length = os.pathconf(os.path.dirname(imagePath), 'PC_NAME_MAX')

# truncate the new name if it is too long
if len(new_name + ext) > max_name_length:
    new_name = new_name[:max_name_length - len(ext)]

# rebuild the path with the new file name and the original directory
new_path = os.path.join(os.path.dirname(imagePath), new_name + ext)


# rename the file
os.rename(imagePath, new_path)

print(f"Renamed file to: {new_path}")	

