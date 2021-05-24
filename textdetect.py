import cv2
import math
import re
import numpy as np

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
net = cv2.dnn.readNet("pretrained_model.pb")
frame = cv2.imread('./output/sample00.jpg')
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
angles = []

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

    angles_of_current_box = [[x[0],y[0]],[x[3],y[3]]]
    angles.append(angles_of_current_box)

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

    #tweaking word boundries
    for i in range(0, 2):
        if xmin - 10 >= 0:
            xmin -= 10
        if ymin - 3 >= 0:
            ymin -= 3
        if xmax + 10 <= width_:
            xmax += 10
        if ymax + 3 <= height_:
            ymax += 3

    xminval.append(xmin)
    yminval.append(ymin)
    word_crop = frame[ymin:ymax, xmin:xmax]
    #cv2.imshow('word_crop', word_crop)
    #word_crop = cv2.cvtColor(word_crop, cv2.COLOR_BGR2GRAY)
    #word_crop = cv2.adaptiveThreshold(word_crop, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                                cv2.THRESH_BINARY, 199, 5)
    #ret, word_crop = cv2.threshold(word_crop, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite('./crop/crop_{}.jpg'.format(cnt), word_crop)
    #preprocessing each crop directly
    word_crop2 = word_crop
    img = cv2.cvtColor(word_crop2, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY +
                                 cv2.THRESH_OTSU)
    cv2.imwrite('./crop/procrop{}.jpg'.format(cnt),thresh)
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
for i in range(0,2):
    if x_min - 10 >= 0:
        x_min -= 10
    if y_min - 10 >= 0:
        y_min -= 10
    if x_max + 10 <= width_:
        x_max += 10
    if y_max + 10 <= height_:
        y_max += 10
cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
cv2.imshow('line', frame2)
crop = frame2[y_min:y_max, x_min:x_max]
white_frame = crop
width, height, color = white_frame.shape
cv2.rectangle(white_frame, (0, 0), (height, width), (255, 255, 255), -1)
cv2.rectangle(frame, (0, 0), (width_, height_), (144, 153, 146), -1)
cv2.imwrite('./crop/crop.jpg', frame)
cv2.rectangle(frame, (0, 0), (width_, height_), (0, 0, 0), -1)
cv2.imwrite('./crop/procrop.jpg',frame)
cv2.rectangle(frame, (0, 0), (width_, height_), (255, 255, 255), -1)
cv2.imwrite('./crop/procropz.jpg', frame)
crop0 = cv2.imread('./crop/crop.jpg')
crop1 = cv2.imread('./crop/procrop.jpg')
crop2 = cv2.imread('./crop/procropz.jpg')
for i in range(0, cnt):
    xmin = xminval[i]
    ymin = yminval[i]
    crop_0 = cv2.imread('./crop/crop_{}.jpg'.format(i))
    crop_1 = cv2.imread('./crop/procrop{}.jpg'.format(i))
    height, width, clr = crop_0.shape
    ymax = ymin+height
    xmax = xmin+width
    crop0[ymin:ymax, xmin:xmax] = crop_0
    crop1[ymin:ymax, xmin:xmax] = crop_1
    crop2[ymin:ymax, xmin:xmax] = crop_1

cv2.imwrite('./output/sample01.jpg', crop0)
cv2.imwrite('./output/sample04.jpg', crop1)
cv2.imwrite('./output/sample07.jpg', crop2)
crop0 = crop0[y_min:y_max,x_min:x_max]
crop1 = crop1[y_min:y_max, x_min:x_max]
crop2 = crop2[y_min:y_max, x_min:x_max]
cv2.imwrite('./output/sample02.jpg',crop0)
cv2.imwrite('./output/sample05.jpg', crop1)
cv2.imwrite('./output/sample08.jpg', crop2)
#cv2.waitKey()

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result
framez = cv2.imread('./output/sample02.jpg')
framey = cv2.imread('./output/sample05.jpg')
framex = cv2.imread('./output/sample08.jpg')
angles_degree = []
for z in angles:
    p1 = z[0]
    p2 = z[1]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    #cv2.line(framez, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles_degree.append(angle)
median_angle = np.median(angles_degree)
img_rotated = rotate_image(framez, median_angle)
img_rotated1 = rotate_image(framey, median_angle)
img_rotated2 = rotate_image(framex, median_angle)
#cv2.imshow('angles',framez)
cv2.imshow('rotated',img_rotated)
cv2.imshow('rotated1', img_rotated1)
cv2.imwrite('./output/sample03.jpg',img_rotated)
cv2.imwrite('./output/sample06.jpg', img_rotated1)
cv2.imwrite('./output/sample09.jpg', img_rotated2)
cv2.waitKey()
#print(angles)
