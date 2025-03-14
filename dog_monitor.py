import cv2 as cv
import numpy as np
from ultralytics import YOLO
import action_script
import time
import atexit
import json

# Load YOLOv8 model (pretrained on COCO)
model = YOLO("yolov11n.pt", verbose=False)

# Load configuration from JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Initialize beep log
beep_log = []

def log_beep():
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    beep_log.append({"timestamp": timestamp})
    action_script.beep_dog()

def save_beep_log():
    if beep_log == []:
        beep_log.append({"timestamp": "No beeps logged."})
    with open("beep_log.txt", "w") as f:
        json.dump(beep_log, f, indent=4)

atexit.register(save_beep_log)

action_script.beep_dog
time.sleep(1)
action_script.buzz_dog()

if config["rtsp_url"] == "":
    rtsp_url = str(input("Please enter your RTSP URL like rtsp://username:password@IP.ADD.R.ESS/live: "))
else:
    rtsp_url = config["rtsp_url"]

video_feed = cv.VideoCapture(rtsp_url)

if not video_feed.isOpened():
    print("Could not open video feed.")
    exit()

couch_boundary = None  # Will be dynamically set
frame_skip = 20 # Skip every 20 frames, decrease for more frequent detection
frame_count = 0

while True:
    ret, frame = video_feed.read()
    if not ret:
        print("Unable to grab frame.")
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    # Run YOLOv8 detection
    results = model(frame)

    # Initialize variables
    dog_position = None
    new_couch_boundary = None

    for r in results:
        for box in r.boxes:
            class_id = int(box.cls[0])
            conf = box.conf[0].item()
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box

            # If a couch is detected, update couch_boundary
            if class_id == 57:  # COCO label for "couch"
                new_couch_boundary = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
                cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Blue box
                cv.putText(frame, "Couch", (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

            # If a dog is detected, track its position
            if class_id == 16:  # COCO label for "dog"
                print(f"Dog detected with confidence: {conf}")
                dog_position = (x1, y1, x2, y2)
                print(f"Dog position: {dog_position}")
                cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green box
                cv.putText(frame, "Dog", (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Update couch boundary only if detected
    if new_couch_boundary:
        couch_boundary = new_couch_boundary
        print(f"Couch boundary: {couch_boundary}")

    # Calculate middle third of the couch boundary
    if couch_boundary:
        couch_x1, couch_y1 = couch_boundary[0]
        couch_x2, couch_y2 = couch_boundary[2]
        middle_third_y1 = -100 + couch_y1 + (couch_y2 - couch_y1) // 3
        middle_third_y2 = couch_y2 - (couch_y2 - couch_y1) // 3

        # Draw the middle third boundary on the frame
        cv.rectangle(frame, (couch_x1, middle_third_y1), (couch_x2, middle_third_y2), (0, 0, 255), 2)  # Red box

        # Update couch_boundary to middle third boundary
        couch_boundary = [(couch_x1, middle_third_y1), (couch_x2, middle_third_y1), (couch_x2, middle_third_y2), (couch_x1, middle_third_y2)]
        print(f"Updated couch boundary to middle third: {couch_boundary}")

    # Check if the dog is inside the couch boundary
    if dog_position and couch_boundary:
        x1, y1, x2, y2 = dog_position
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        # Plot the dog position as a point for debugging
        cv.circle(frame, (center_x, center_y), 5, (255, 255, 0), -1)  # Cyan point

        # Convert couch boundary to a polygon
        couch_poly = np.array(couch_boundary, np.int32).reshape((-1, 1, 2))
        if cv.pointPolygonTest(couch_poly, (center_x, center_y), False) >= 0:
            print("Dog is on the couch!")
            log_beep()
            #action_script.buzz_dog()
        else:
            print("Dog is not on the couch.")

    cv.imshow("Dog & Couch Detection", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_feed.release()
cv.destroyAllWindows()