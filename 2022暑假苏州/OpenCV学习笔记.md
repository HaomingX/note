# OpenCV学习笔记：

## 第一节课：

- RGB颜色通道：所有彩图都是三颜色图
- 0~255，亮度从黑色到白色
- R：红， G：绿， B：蓝
- 而对于一个灰度图，不需要RGB颜色通道

```python
import cv2
import numpy as np
```

- 读取图像：

```python
img = cv2:imread('', )
#两个参数：cv2.IMREAD_COLOR（彩图），cv2.IMREAD_GRAYSCALE（灰度图）
```

- OpenCV默认读取格式为BGR
- 显示图像：

```python
cv2.imshow('', )
cv2.waitKey()
#cv2.destoryALLWindows()
```

- 获取hwc：

```
img.shape
```

- 保存：

```python
cv2.imwrite('',)
```

- 视频打开：

```python
vc = cv2.VideoCapture('')
```

## 第二节课：

- 视频转换为灰度视频：

```python
#if img.isOpend():
#    open = img.read()
if vc.isOpend():
    open, frame = vc.read()
else:
    open = False
    
while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret = True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if cv2.waitKey() & OxFF == 27:
            break
vc.release()
cv2.destoryALLWindows()
```

## 第三节课：

- 截取部分图像：

```
img = cv2.imread('')
image = img[a:b, c:d]
cv2.imshow('', )
```

- 颜色通道提取与合并：

```
b,g,r = cv2.split(img)
img = cv2.merge(b,g,r)
```

- 分别取BGR：

```python
cur_img = img.copy()
cur_img[:,:,0] = 0 #B = 0
cur_img[:,:,1] = 0 #G = 0
cv2.imshow('R', cur_img)
```

## 第四节课：

- 边界填充：

```
top_size,bottom_size,left_size,right_size = (a,b,c,d)
replace = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.方式)

方式：
复制法，反射法，反射对称，外包装法，常量法
```

- 数值计算：

```
img = img + n #在每个像素点上加n,但shape值不变
img1 + img2 #越界取余
cv2.add(img1, img2) #越界取255
```

- 改变shape值：

```python
img = cv2.resize(img, (x, y))
img = cv2.resize(img, (0,0), fx = a, fy = b) #改变倍数
```

## 第五节课：

- 图像阈值：

```python
ret, dst = cv2.threshoid(src, thresh, maxval, type)
#src:输入图，只能输入单通道图像，通常为灰度图
#dst:输出图
#thresh:阈值
#maxval:当像素值超过了阈值（或者小于阈值，依type定），所赋予的值
#type:二值化操作类型，五种
例:ret, dst = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
```

## 第六，七节课：

- 图像平滑：

```python
#均值滤波
blur = cv2.blur(img, (x, x))
#方框滤波
box = cv2.boxFilter(img, -1, (x,x), normalize = Ture) #或者(normalize去掉)
#高斯滤波
gaussian = cv2.GaussianBlur(img, (x,x), 1)
#中值滤波
median = cv2.medianBlur(img, x)
#展示所有
res = np.hstack(vstaack)(blur,gaussian,median)
cv2.imshow('', res)
cv2.waitKey(0)
cv2.destoryALLWindow()
```

## 第八节课：

- 形态学腐蚀操作：

```python
kernel = np.ones((x,x), np.uint8)
erosion = cv2.erode(img, kernel, iterations = y)
#y为腐蚀次数
cv2.imshow('', erosion)
cv2.waitKey(0)
cv2.destoryALLWindow()
```

## 第九节课：

- 形态学膨胀操作：

```python
kernel = np,ones((x,x), np.unit8)
dilate = cv2.dilate(img, kernel, iterations = y)
#y为膨胀次数
cv2.imshow('', dilate)
cv2.waitKey(0)
cv2.destoryALLWindow()
```

## 第十节课：

- 开运算与闭运算：
- 开运算：

```python
#先腐蚀，再膨胀
kernel = np,ones((x,x), np.unit8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
```

- 闭运算：

```python
#先膨胀，再腐蚀
kernel = np,ones((x,x), np.unit8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
```

## 第十一节课：

- 梯度运算：

```python
#膨胀-腐蚀
kernel = np,ones((x,x), np.unit8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('', gradient)
cv2.waitKey(0)
cv2.destoryALLWindow()
```

## 第十二节课：

- 礼帽（末节）：

```python
#原始输入-开运算结果
kernel = np,ones((x,x), np.unit8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('', tophat)
cv2.waitKey(0)
cv2.destoryALLWindow()
```

- 黑帽（轮廓）：

```python
#闭运算结果-原始输入
kernel = np,ones((x,x), np.unit8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('', blackhat)
cv2.waitKey(0)
cv2.destoryALLWindow()
```

