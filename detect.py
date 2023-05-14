def vech_no():
    return number
from paddleocr import PaddleOCR, draw_ocr
import cv2
import numpy as np
ocr = PaddleOCR(lang = 'en')
image_path = 'detections.jpg'
image_cv = cv2.imread(image_path)
image_height = image_cv.shape[0]
image_width = image_cv.shape[1]
print(image_height,image_width)
output = ocr.ocr(image_path)
print(output)
print(len(output))
arr2d = np.array(output)
arr1d = arr2d.flatten()
print(arr1d[1][0]) 
number = arr1d[1][0]
print(number)

'''boxes=[]
for out in range(0,len(arr1d),2):
    boxes.append(arr1d[out])
    print(arr1d[out])
#boxes=[line[0] for line in output]
#print(boxes)'''
'''texts=[]
#texts = [line[1][0] for line in output]
for out in range(1,len(arr1d),2):
    texts.append(arr1d[out])
    print(arr1d[out])'''
#probabilities = [line[1][1] for line in output]
'''probabilities=[]
for out in range(1,len(arr1d),2):
    probabilities.append(arr1d[out][1])
    print(arr1d[out][1])
    number = arr1d[out][0]
image_boxes = image_cv.copy()
print(output[0])'''
#print(image_boxes)
#print(result[0][0],result[0][2])
'''for box,text in zip(boxes,texts):
    #print(int(result[0]))
    cv2.rectangle(image_boxes, (int(box[0][0]),int(box[0][1])), (int(box[2][0]),int(box[2][1])), (0,0,255),1)
    cv2.putText(image_boxes,text[0],(int(box[0][0]),int(box[0][1])),cv2.FONT_HERSHEY_SIMPLEX,1,(222,0,0),0)

cv2.imwrite('displaying.jpg',image_boxes)
print(number)'''