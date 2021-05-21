import cv2
import math
import re


def decode(scores, geometry, scoreThresh):
    detections = []
    confidences = []

    ############ CHECK DIMENSIONS AND SHAPES OF geometry AND scores ############
    assert len(scores.shape) == 4, "Incorrect dimensions of scores"
    assert len(geometry.shape) == 4, "Incorrect dimensions of geometry"
    assert scores.shape[0] == 1, "Invalid dimensions of scores"
    assert geometry.shape[0] == 1, "Invalid dimensions of geometry"
    assert scores.shape[1] == 1, "Invalid dimensions of scores"
    assert geometry.shape[1] == 5, "Invalid dimensions of geometry"
    assert scores.shape[2] == geometry.shape[2], "Invalid dimensions of scores and geometry"
    assert scores.shape[3] == geometry.shape[3], "Invalid dimensions of scores and geometry"
    height = scores.shape[2]
    width = scores.shape[3]
    for y in range(0, height):

        # Extract data from scores
        scoresData = scores[0][0][y]
        x0_data = geometry[0][0][y]
        x1_data = geometry[0][1][y]
        x2_data = geometry[0][2][y]
        x3_data = geometry[0][3][y]
        anglesData = geometry[0][4][y]
        for x in range(0, width):
            score = scoresData[x]

            # If score is lower than threshold score, move to next x
            if (score < scoreThresh):
                continue

            # Calculate offset
            offsetX = x * 4.0
            offsetY = y * 4.0
            angle = anglesData[x]

            # Calculate cos and sin of angle
            cosA = math.cos(angle)
            sinA = math.sin(angle)
            h = x0_data[x] + x2_data[x]
            w = x1_data[x] + x3_data[x]

            # Calculate offset
            offset = ([offsetX + cosA * x1_data[x] + sinA * x2_data[x],
                      offsetY - sinA * x1_data[x] + cosA * x2_data[x]])

            # Find points for rectangle
            p1 = (-sinA * h + offset[0], -cosA * h + offset[1])
            p3 = (-cosA * w + offset[0], sinA * w + offset[1])
            center = (0.5 * (p1[0] + p3[0]), 0.5 * (p1[1] + p3[1]))
            detections.append((center, (w, h), -1 * angle * 180.0 / math.pi))
            confidences.append(float(score))

    # Return detections and confidences
    return [detections, confidences]


# This is the model we get after extraction
net = cv2.dnn.readNet("frozen_east_text_detection.pb")
frame = cv2.imread('./images/sample_0.jpg')

inpWidth = inpHeight = 320  # A default dimension
# Preparing a blob to pass the image through the neural network
# Subtracting mean values used while training the model.
image_blob = cv2.dnn.blobFromImage(
    frame, 1.0, (inpWidth, inpHeight), (123.68, 116.78, 103.94), True, False)
output_layer = []
output_layer.append("feature_fusion/Conv_7/Sigmoid")
output_layer.append("feature_fusion/concat_3")
net.setInput(image_blob)
output = net.forward(output_layer)
scores = output[0]
geometry = output[1]
confThreshold = 0.5
nmsThreshold = 0.3
[boxes, confidences] = decode(scores, geometry, confThreshold)
indices = cv2.dnn.NMSBoxesRotated(
    boxes, confidences, confThreshold, nmsThreshold)
height_ = frame.shape[0]
width_ = frame.shape[1]
rW = width_ / float(inpWidth)
rH = height_ / float(inpHeight)
frame2 = frame
x_min = 0
y_min = 0
x_max = 0
y_max = 0
cnt = 0

xmin = 0
xmax = 0
ymin = 0
ymax = 0
xminval = []
yminval = []
for i in indices:
    # get 4 corners of the rotated rect
    vertices = cv2.boxPoints(boxes[i[0]])
    #print(vertices)
    # scale the bounding box coordinates based on the respective ratios
    for j in range(4):
        vertices[j][0] *= rW
        vertices[j][1] *= rH
    #custom block
    crdns = str(vertices)
    crdns = crdns.replace('\n', '')
    crdns = crdns.replace('[', '')
    crdns = crdns.replace(']', '')
    crdns = re.sub('\s+', ' ', crdns)
    #print(crdns)
    list1 = crdns.split(' ')
    while '' in list1:
        list1.remove('')
    x = [float(list1[0]), float(list1[2]), float(list1[4]), float(list1[6])]
    y = [float(list1[1]), float(list1[3]), float(list1[5]), float(list1[7])]
    if cnt == 0:
        x_min = int(float(list1[0]))
        y_min = int(float(list1[1]))
    #cv2.line(frame2, ( int(float(list1[0])), int(float(list1[1])) ), ( int(float(list1[6])), int(float(list1[7])) ), (0,255,0), 2)
    #print(x,y)

    #block to crop each word
    xmin = int(float(list1[0]))
    ymin = int(float(list1[1]))
    xmax = int(float(list1[0]))
    ymax = int(float(list1[1]))
    for r, s in zip(x, y):
        if xmax < int(float(r)):
            xmax = int(float(r))
        if xmin > int(float(r)):
            xmin = int(float(r))
        if ymax < int(float(s)):
            ymax = int(float(s))
        if ymin > int(float(s)):
            ymin = int(float(s))
    #width = xmax - xmin
    #height = ymax - ymin
    xminval.append(xmin)
    yminval.append(ymin)
    word_crop = frame[ymin:ymax, xmin:xmax]
    #cv2.imshow('word_crop', word_crop)
    word_crop = cv2.cvtColor(word_crop, cv2.COLOR_BGR2GRAY)
    #word_crop = cv2.adaptiveThreshold(word_crop, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                                cv2.THRESH_BINARY, 199, 5)
    #ret, word_crop = cv2.threshold(word_crop, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./crop/crop_{}.jpg'.format(cnt), word_crop)
    #end
    for p, q in zip(x, y):
        if x_max < int(float(p)):
            x_max = int(float(p))
        if x_min > int(float(p)):
            x_min = int(float(p))
        if y_max < int(float(q)):
            y_max = int(float(q))
        if y_min > int(float(q)):
            y_min = int(float(q))
    cnt += 1
#print(x_min,y_min,x_max,y_max)
#print(width_,height_)
if x_min - 10 >= 0:
    x_min -= 10
if y_min - 10 >= 0:
    y_min -= 10
if x_max + 10 <= width_:
    x_max += 10
if y_max + 10 <= height_:
    y_max += 10
cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

#cv2.line(frame2, ( int(list1[0]), int(list1[1]) ), ( int(list1[6]), int(list1[7]) ), (0,255,0), 2)
#for j in range(4):
#    p1 = (int(vertices[j][0]), int(vertices[j][1]))
#    p2 = (int(vertices[(j + 1) % 4][0]), int(vertices[(j + 1) % 4][1]))
#    cv2.rectangle(frame, p1, p2, (0, 255, 0), 1)

cv2.imshow('line', frame2)
crop = frame2[y_min:y_max, x_min:x_max]
white_frame = crop
width, height, color = white_frame.shape
cv2.rectangle(white_frame, (0, 0), (height, width), (255, 255, 255), -1)
cv2.imshow('bg', white_frame)
cv2.imshow('croped', crop)


#cv2.imwrite('./images/sample_000.jpg', crop)
# To save the image:
#cv2.imwrite("./images/sample_0.jpg", frame2)
cv2.imshow('result', frame)
cv2.rectangle(frame, (0, 0), (width_, height_), (255, 255, 255), -1)
cv2.imwrite('./crop/crop.jpg', frame)
crop0 = cv2.imread('./crop/crop.jpg')
for i in range(0, cnt):
    xmin = xminval[i]
    ymin = yminval[i]
    crop_0 = cv2.imread('./crop/crop_{}.jpg'.format(i))
    height, width, clr = crop_0.shape
    ymax = ymin+height
    xmax = xmin+width
    crop0[ymin:ymax, xmin:xmax] = crop_0

cv2.imshow('croped233', crop0)
cv2.imwrite('./images/sample_00.jpg', crop0)
cv2.imshow('bgm', frame)
cv2.waitKey()
