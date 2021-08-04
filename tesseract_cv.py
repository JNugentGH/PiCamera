# Jack Nugent - Elec Eng Intern - (2021/08/04)
# Program to capture an image of tote sticker and print the label as a string.

import pytesseract
import cv2
from picamera import PiCamera
from time import sleep
import re

def capture(output_filename):
	''' Show a 2 second preview and save a picture with the filename input. '''
	with PiCamera() as camera:
		camera.resolution = (1024, 768)		# Set the resolution.
	
		camera.zoom = (0.25, 0.25, 0.5, 0.5)	# Zoom in to the centre of the image.
	
		camera.start_preview()			# Show the capture to the screen.
	
		sleep(2)				# Display the prevoew for 2 seconds.
	
		camera.capture(output_filename)		# Capture the shot to the file.

def ocr_file(input_filename, output_filename):
	''' Process the image, Run OCR on the Image, Save the processed image
	    return the string.'''
	image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	# Read the image from the file.
	
	image = image[200:-200, :]				# Crop the top and bottom 200 pixels off.
	
	h, w = image.shape					# Collect the images shape.
	
	scale = 0.5						# Set a scaling factor.
	
	# Due to the tote sticker font being tall and narrow, scale the image in the Y direction only.
	height = int(h*scale)					# Scale the h value.
	
	width = int(w)						# Scale the w.
	
	desired_size = (width, height)				# Make a tuple
	
	resized = cv2.resize(image, desired_size, interpolation=cv2.INTER_NEAREST)	# Scale the image.
	
	k_size = (5, 5)						# Make the kernel size tuple.
	
	blur = cv2.GaussianBlur(resized, k_size, cv2.BORDER_DEFAULT)	# Blur the image.
	
	ret, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)	# Threshold the image to black or white (binary image).
	
	sticker = pytesseract.image_to_string(thresh)			# Use pytesseract to get the string.
	
	cv2.imwrite(output_filename, thresh)				# Save the image.

	return sticker							# return the string.

def get_sticker_id(string_in):
	''' Function to parse and tidy the string obtained from OCR on the tote sticker. '''
	string_out = ""

	id_pattern = re.compile(r"\w+-\w+-\w+")			# save the pattern the label should be in.

	string_out = re.sub(chr(8212), '-', string_in)		# Substitute the square character for a dash.

	string_out = re.sub(r'-+', '-', string_out)		# If a dash repeats more than once, replace with only a single.

	string_out = re.sub(r'\s+-', '-', string_out)		# Replace white space preceeding a dash with only a dash.

	string_out = re.sub(r'-\s+', '-', string_out)		# Replace white space after a dash with only a dash.

	id_match = id_pattern.search(string_out)		# Take any matched pattern to the label.
	
	if id_match is not None:				# If there is a match.
		string_out = id_match.string			# save the string.

		string_out = re.sub(r'\s+', '', string_out)	# Remove any whitespace.

	return string_out					# Return the string.

if __name__ == "__main__":				# If this file is run directly.
	filename = "pre_process.jpg"			# Name the file.

	output_file = "post_process.jpg"		# Name the output.

	capture(filename)				# Take a picture with preview.

	output = ocr_file(filename, output_file)	# Get the string rom the image.

	out = get_sticker_id(output)			# Tidy the sstring to find the label.

	print(out)					# Output the string.
