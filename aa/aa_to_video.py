import cv2
import os

width = 1272
height = 720
image_folder = 'images'
video_name = 'aavideos/matrix.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fps = 23.98

videoWriter = cv2.VideoWriter(video_name, fourcc, fps, (width,height))

for i in range(359):
    aafilepath = f'aaframes/frame{i}.jpg'
    frame = cv2.imread(aafilepath)
    videoWriter.write(frame)
    print(i)

videoWriter.release()