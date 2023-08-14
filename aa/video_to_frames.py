import cv2

video_path = 'videos/matrix.mp4'
vidcap = cv2.VideoCapture(video_path)


width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)
print('width:', width)

height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('height:', height)

fps = vidcap.get(cv2.CAP_PROP_FPS)
print('fps (frame/sec):', fps)

framecount = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
print('total framecount (frame):', framecount)

print('total length (sec):', framecount / fps)

count = 0
while True:
    ret, image = vidcap.read()
    if not ret or cv2.waitKey(1) == ord('q'):
        break
    cv2.imwrite("frames/frame%d.jpg" % count, image)
    print(count)
    count += 1

vidcap.release()
