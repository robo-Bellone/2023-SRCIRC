import cv2
import time
import numpy as np

video = cv2.VideoCapture(0)			# WebCam의 경우 0 또는 1
						# 비디오 파일의 경우 '경로/파일명.확장자'

prev_time = 0
FPS = 0.5

while True:

    ret, frame = video.read()
    
    current_time = time.time() - prev_time
    
    orginimg = frame        # 다음 프레임 읽기
    img = cv2.resize(orginimg, (300, 300))
    
    img_original = img.copy()
    img2 = img.astype(np.uint16)                # dtype 변경 ---①
    b,g,r = cv2.split(img2)                     # 채널 별로 분리 ---②
    #b,g,r = img2[:,:,0], img2[:,:,1], img2[:,:,2]
    gray1 = ((b + g + r)/3).astype(np.uint8)    # 평균 값 연산후 dtype 변경 ---③
    
    gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR을 그레이 스케일로 변경 ---④
    
    
    edges = cv2.Canny(gray2,50,150,apertureSize=3)
    lines = cv2.HoughLines(edges,1,np.pi/180,100)
        
    for i in range(len(lines)):
        for rho, theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0+1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 -1000*(a))

            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    res = np.vstack((img_original,img))
    
    if (ret is True) and (current_time > 1./ FPS) :
    	
        prev_time = time.time()
        
        cv2.imshow('VideoCapture', frame)
        cv2.imshow('camera', img)   # 다음 프레임 이미지 표시
        cv2.imshow('gray1', gray1)
        cv2.imshow('gray2', gray2)
    	
        if cv2.waitKey(1) > 0 :
            
            break