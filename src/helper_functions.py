import numpy as np 

def change_color(image, c_orig, c_new):
    colors = {'red': [255, 0, 0],
      'fushia': [255, 0, 255],
      'green': [0, 255, 0],
      'cyan': [0, 255, 255],
      'blue': [0, 0, 255],
      'yellow': [255, 255, 0],
      'white': [255, 255, 255],
      'black': [0, 0, 0]
     }
        
    r1, g1, b1 = colors[c_orig]
    r2, g2, b2 = colors[c_new]
    

    
    red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]
    mask = (red == r1) & (green == g1) & (blue == b1)
    new_image = image.copy()
    new_image[:,:,:3][mask] = [r2, g2, b2]
    return new_image