# DeepFake
Recent advances in visual media technology have led to new tools for processing and
multimedia contents. Modern AI-based technologies have provided tools to create extremely
realistic manipulated videos, without any efforts. Such spurious videos, named DeepFakes,
may constitute a serious threat to attack the reputation of public subjects or to address the
general opinion on a certain event. The term ‘DeepFake’ (a portmanteau of deep learning and
fake) can be unhelpful and confusing as the underlying technology has potential for both
creative and nefarious use.
## Dataset used
Deepfake Detection Google dataset will be used which contains original and deepfake videos of 28 actors, total consisting of 3000+ manipulated videos and 360 original. Manipulated videos are created using GAN. A GAN is a class of machine learning frameworks. Given a training set, this technique learns to generate new data with the same statistics as the training set. For example, a GAN trained on photographs can generate new photographs that look at least superficially authentic to human observers, having many realistic characteristics. 
### Methodology used
1.	To preprocess the input video, face coordinates are extracted using MTCNN. From each video, consecutive 32 frames are picked excluding first 100 frames with the help Open CV. Model is trained using these 32 frames as individual training examples.
2.	Exploited pre-trained models like VGG16, Inception, Resnet and Xception with little customization and compared the results these results.
#### Future Plans
We will be building our model that would be capable of detecting deepfake in real time accurately.
