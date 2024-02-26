import cv2     # for capturing videos
count = 0
filename = "Carspeed2"
videoFile = filename+".mp4"
cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    filename2 = filename + "frame%d.jpg" % count
    count+=1
    cv2.imwrite(filename2, frame)
cap.release()
print ("Done!")
