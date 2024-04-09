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
The model was tested uisng some of the videos which were unseen by the model. Here are some of the output videos:<br>

https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/c0da8f15-0137-4efc-980b-d303ff151fe6

https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/c0e636ce-1ad1-4d2c-adf3-6bc46db509f8 

https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/b82c84ca-d884-45d9-80c1-bb1bf314ff57


Screenshots: <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/03b40e34-3f23-4232-97fb-8bfcbbda3382) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/db98d53e-d7b4-4400-952a-4dd33043cca1) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/3f15e890-8e46-46de-92b5-b73f5fc2a92b) <br>

![image](https://github.com/chetan0220/Running-Gesture-Detector/assets/97821311/77ca06b6-d2f8-403c-ae50-7f0b4b072c54) <br>

