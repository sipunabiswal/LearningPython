#import the necessary libraries
import numpy as np 
from PIL import Image 
  
# Create a 1024x1024x3 array of 8 bit unsigned integers 
data = np.zeros( (1024,1024, 3), dtype=np.uint8 ) 
  
# Create an image from the data 
img = Image.fromarray( data ) 
  
# Save the image 
img.save('AI_image.png')