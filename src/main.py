import cv2

vcap = cv2.VideoCapture('https://zssd-platypus.hls.camzonecdn.com/CamzoneStreams/zssd-platypus/Playlist.m3u8')

while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    if frame is not None:
        # Do something with the frame now!
        # I wouldn't uncomment this, it was just testing.
        # cv2.imwrite('frame.png', frame)
        print("Got a frame")
    else:
        break

vcap.release()
