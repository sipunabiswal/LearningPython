from PIL import Image 
  
# Create a new image of size 640 X 480 
image = Image.new('RGB', (640, 480)) 
  
# Save the image 
image.save('my_image.png')