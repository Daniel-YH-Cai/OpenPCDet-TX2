import PIL.Image as Image
import numpy
import numpy as np

def imread(file_path):
    image=Image.open(file_path).convert("RGB")
    print(list(image.getdata()))
    data=np.asarray(image,dtype=numpy.uint8)
    return data
