# Running Gesture Detector
### Task: To detect running gesture

### Solution: 

**Step 1**: Collected running videos from [Pexels](https://www.pexels.com/search/videos/running/ "Pexels").

---

**Step 2**: Extracted Frames from these videos using opencv-python

---

**Step 3**: Prepared data accoridng to YOLO format. To annotate the images, [CVAT.ai](https://www.cvat.ai/) was used. 

---

**Step 4**: Training<br>
This annotated dataset was trained using YOLOv8 Medium sized model. <br>
Parameters and results are as follows: <br>
**Version**: YOLOv8<br>
**Size**: Medium<br>
**Epochs**: 30<br>
**Batch Size**: 32<br>
**Optimizer**: Adamax<br>
**Mean Average Precision**: 99.5%<br>

---

**Step 5**: Testing<br>
The model was tested uisng some of the videos which were unseen by the model. Here are some of the screenshots of output videos:<br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/03b40e34-3f23-4232-97fb-8bfcbbda3382) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/db98d53e-d7b4-4400-952a-4dd33043cca1) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/3f15e890-8e46-46de-92b5-b73f5fc2a92b) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/77ca06b6-d2f8-403c-ae50-7f0b4b072c54) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/9def5bf0-0b10-41dc-ac67-23ec3cbb6776) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/9e051280-d9a3-416e-9682-1e5b67fed708) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/ff95661e-b85b-4b0c-a325-0ebdc7a06c52) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/2e1fe49a-e0de-40d1-a7c5-a68dfe300091) <br>

---
If you have any query, feedback or suggestion feel free to drop a mail at chetan.mahale0220@gmail.com :) 
