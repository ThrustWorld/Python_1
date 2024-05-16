LETTER_FORMAT_WIDTH = 8.5
LETTER_FORMAT_HEIGHT = 11
ONE_INCH_TO_MM = 25.4

# Conversion from 'letter' format to millimeters
paper_width_in_mm = LETTER_FORMAT_WIDTH * ONE_INCH_TO_MM
paper_height_in_mm = LETTER_FORMAT_HEIGHT * ONE_INCH_TO_MM

print("The dimensions of a paper from 'letter' format to mm is %.2fmm x %.2fmm" %(paper_width_in_mm, paper_height_in_mm))