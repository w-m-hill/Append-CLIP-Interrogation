import sys
import argparse
import os

from PIL import Image
from clip_interrogator import Config, Interrogator


parser = argparse.ArgumentParser(description='Appened CLIP interrogation to file')

parser.add_argument('--path', type=str, help='Path to the image')
parser.add_argument('--replace', action='store_true', help='Replace the original name with caption instead of appending to it')

parser.add_argument('--crop', action='store_true', help='Pass a cropped version of the image to interrogator if it is larger than --res')
parser.add_argument('--res', type=int, help='Cropped resolution', default=1024)

args = parser.parse_args()

if (args.path):
	imagePath = args.path
	if (not os.path.exists(imagePath)):
		sys.exit("Error: Invalid path.")
else:
	sys.exit("Error: Please provide a path to the image using --path path/to/image.")

image = Image.open(imagePath).convert('RGB')

if (args.crop):
	# Define the constant for the image size
	IMAGE_SIZE = args.res

	## Get the original image size
	width, height = image.size
	if (width > size or height > size):
		# Calculate the coordinates for the center crop
		left, top = (width - IMAGE_SIZE) // 2, (height - IMAGE_SIZE) // 2

		# Crop the image to the specified size at the center
		image = image.crop((left, top, left + IMAGE_SIZE, top + IMAGE_SIZE))

		print(f"Copy of image was cropped to {args.res} by {args.res}")
	else:
		print(f"Image was already smaller than supplied resolution of {args.res}")

#Interrogate
ci = Interrogator(Config(clip_model_name="ViT-L-14/openai"))
result_string = ci.interrogate(image)


# get the base name of the file (i.e., the file name without the directory)
base_name = os.path.basename(imagePath)
# split the base name into its name and extension parts
name, ext = os.path.splitext(base_name)
# get the maximum length of a file name for the file system where the file is located
max_name_length = os.pathconf(os.path.dirname(imagePath), 'PC_NAME_MAX')

if (args.replace):
	# truncate the result_string if it is too long
	if len(result_string + ext) > max_name_length:
	    result_string = result_string[:max_name_length - len(ext)]

	# rebuild the path with the new file name and the original directory
	new_path = os.path.join(os.path.dirname(imagePath), result_string + ext)
else:
	# add caption to the end of the name part
	new_name = name + result_string

	# truncate the new name if it is too long
	if len(new_name + ext) > max_name_length:
	    new_name = new_name[:max_name_length - len(ext)]

	# rebuild the path with the new file name and the original directory
	new_path = os.path.join(os.path.dirname(imagePath), new_name + ext)


# rename the file
os.rename(imagePath, new_path)

print(f"Renamed file to: {new_path}")	

