<a id="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Jagdish9903/Intel-Project-TeleICU">
    <img src="https://cxotoday.com/wp-content/uploads/2019/12/Intel_logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Intel-Project-TeleICU</h3>

  <p align="center">
    An Intel Unnati summer internship project !
    <br />
    <a href="https://www.canva.com/design/DAGK7CNX3M0/m1ZAUU2e78wFqh-5YFAGGw/edit?utm_content=DAGK7CNX3M0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"><strong>Project PPT for detailed explanation »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Jagdish9903/Intel-Project-TeleICU">View Demo</a>
    ·
    <a href="https://github.com/Jagdish9903/Intel-Project-TeleICU/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Jagdish9903/Intel-Project-TeleICU/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-presentation">Project Presentation</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#technology-stack">Technology Stack</a></li>
        <li><a href="#about-github-repository">About Github Repository</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#system-workflow">System Workflow</a></li>
    <li><a href="#approach-taken">Approach Taken</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#considerations-and-future-improvements">Considerations and Future Improvements</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<!-- ABOUT THE PROJECT -->


<!-- ABOUT THE PROJECT -->
## About The Project

TeleICU is designed to enhance patient care by leveraging technology to provide remote monitoring and support in intensive care units (ICUs). This project aims to bridge the gap between healthcare professionals and patients by providing real-time data and communication tools.
## Project Presentation

### [🚀 **Click here to view the detailed project PPT!** 🚀](https://www.canva.com/design/DAGK7CNX3M0/m1ZAUU2e78wFqh-5YFAGGw/edit?utm_content=DAGK7CNX3M0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)


**Here's why teleICU is important:**

- Improved patient outcomes through continuous monitoring.
- Efficient use of healthcare resources.
- Enhanced collaboration among healthcare professionals.

This project presents an innovative system for analyzing ICU videos. The system leverages two machine learning models to achieve the following:

1. **People Detection and Classification**: Identifies and categorizes individuals in the video into three categories: doctors, patients, and other personnel.
2. **Patient Action Detection**: Detects and classifies the actions of patients in the ICU based on a sequence of video frames.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

1. **People Detection and Classification**:
   - Utilizes a YOLOv8 model trained on a manually annotated dataset of ICU show images.
   - Categorizes individuals in the video into doctors, patients, and other personnel.
   - Extracts portions of frames containing patients and creates a separate video.

2. **Patient Action Detection**:
   - Uses a second model, an LSTM-based action detection model, to classify patient actions from the extracted video.
   - Actions detected include clapping, sitting, standing still, and walking.
   - Generates a final video showcasing the detected actions and a graph displaying action probabilities over time.

3. **Graphical Representation**:
   - Displays a graph of action probabilities over time, with timestamps on the x-axis and activity percentage on the y-axis.
   - Plots points for the highest probability action at each timestamp, with unique colors for different actions.


### Technology Stack

This section highlights the key frameworks and libraries that were instrumental in building the teleICU project. Each technology was carefully selected to ensure robust functionality, scalability, and real-time capabilities required for a teleICU system.


* [![YOLO][YOLO]][YOLO-url]
* [![MediaPipe][MediaPipe]][MediaPipe-url]
* [![TensorFlow][TensorFlow]][TensorFlow-url]
* [![Streamlit][Streamlit]][Streamlit-url]
* [![OpenCV][OpenCV]][OpenCV-url]
* [![NumPy][NumPy]][NumPy-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![MoviePy][MoviePy]][MoviePy-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ABOUT THE PROJECT -->
## About Github Repository

Description of each file/folder of the repo and its relevance.

1. **`AnnotationsYOLO`**: Web scraped dataset yolo annotations for person classification model.
2. **`AnnotationsYOLO2`**: ICU webshow scraped dataset yolo annotations person classification model.
3. **`DoctorImages`**: Web scrapped images person classification model. (first 800 images)
4. **`DoctorImages2`**: Web scrapped images person classification model. (rest of images)
5. **`ICU season 1`**: ICU webshow frames as images.
6. **`ICU show annotations`**: ICU webshow images' json annotation. 
7. **`datasets`**: ICU webshow scraped images finished dataset.(Our current model trained on this)
8. **`datasets2`**: Web scraped images finished dataset.(Our current model is not trained on this, was used in development stage)
10. **`video test`**: Testing/inferencing videos.
11. **`Believers-TeleICU.pdf`**: PPT for detailed explaination of the project.
12. **`Doctors.ipynb`**: Training, testing and inferencing of person classification model notebook. 
13. **`Patient_classification_model.ipynb`**: Training, testing and inferencing of patient's activity classification model notebook. 
18. **`TeleICU.mp4`**: Infered video by the application.
19. **`action_30.h5`**: Trained model for patient's activity classification.
20. **`app.py`** Final inference code with streamlit interface.
21. **`icu_show_images_model.pt`**: Trained model for patient's activity classification.
22. **`model training data.txt`**: Training process data.
25. **`requirements.txt`**: List of all dependencies for running the application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

There are no special prerequisites required to use the teleICU project. The application is designed to be user-friendly and easy to set up. All necessary dependencies will be installed during the setup process.

The installation steps provided below will guide you through cloning the repository, installing dependencies, and configuring the project to get it running locally on your system.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Jagdish9903/Intel-Project-TeleICU
   ```
2. Navigate to the project directory 
   ```sh
   cd Intel-Project-TeleICU
   ```
3. Install dependencies with `requirements.txt` file
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## System Workflow

**Demo Video of Working Application :**

[![Watch the video](https://raw.githubusercontent.com/Jagdish9903/Intel-Project-TeleICU/main/Screenshot3.png)](https://raw.githubusercontent.com/Jagdish9903/Intel-Project-TeleICU/main/TeleICU.mp4)

Here are some examples demonstrating how to use the `Intel-Project-TeleICU`:

**1) Video Upload:**
   - The user uploads a video via the Streamlit interface.
   - The system processes the video to detect and classify people into doctors, patients, and other personnel.

**2) People Detection:**
   - The YOLOv8 model identifies and categorizes individuals in the video.
   - Portions of frames containing patients are extracted and compiled into a new video.

   _**People Detection Video Result**_

   [![Watch the video](https://raw.githubusercontent.com/Jagdish9903/Intel-Project-TeleICU/main/Screenshot1.png)](https://raw.githubusercontent.com/Jagdish9903/Intel-Project-TeleICU/main/processed_video_005052.mp4)

**3) Action Detection:**
   - The LSTM-based model takes the patient-only video as input and detects actions based on 30-frame sequences.
   - Due to the LSTM's sequence-based approach, action predictions occur after 30 frames of the actual action.

   _**Patient Analysis Video Result**_

   [![Watch the video](https://raw.githubusercontent.com/Jagdish9903/Intel-Project-TeleICU/main/Screenshot2.png)](https://raw.githubusercontent.com/Jagdish9903/Intel-Project-TeleICU/main/patient_video_005052.mp4)

**4) Graphical Representation:**
   - A graph is generated to display the probabilities of detected actions over time.
   - The graph helps visualize the confidence and distribution of actions throughout the video.

   _**Patient's Acitvity Graph Over Time**_
   
   ![Screenshot (186)](https://github.com/user-attachments/assets/46f69e01-5201-47bc-8a0f-2b3fa0273912)   

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Approach Taken

For the purpose of reducing inference time as much as possible, project splits the underlying model into two sub models.

1. Object detection model:
   * We utilize YOLOv8 (You Only Look Once), a SOTA object detection model, for real-time detection of patients, doctors, and family members within the ICU environment. This model ensure precise and contineous tracking and monitoring of mentioned objects.
   * It used Youtube@Holly Mullens `ICU` webshow as the dataset for training.
   * It uses frame skipping at the time of inference to quicken the process and it works wonders!
   
2. Patient's Activity Classification model:
   * As there was lack of quality hospital data, the approach of classifying activities with keypoints was chosen.
   * With this keypoints approach it doesn't really matter if the input is of particular ICU setting or not. So this allows us to train the classification model on well curated dataset of human actions. We used Kaggle's `human-activity-recognition-video-dataset`.
   * For Human keypoints detection we used robust `mediapipe` package. We detected face mesh, pose and hands keypoints.
   * For spatiotemporal classification of actiities lstm model was used which was fed with 1662 keypoints per frame.
   * The output to this model is 4 categories: 'standing still', 'walking', 'clapping' and 'sitting'.
   * On this model we achieved accuracy of 92%.
   * If this model gets a more intricate dataset containing more patient-like activities it can adapt with it quite easily and make application even better!
  


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Trained object detection model for identifying patients, doctors and others
- [x] Trained video classification model for analyzing patient's activities
- [x] Integrated both the models to generate quick inference
- [x] Created streamlit interface to use the application
- [ ] Make an efficient alert system on top of it 
- [ ] Integrate with hospital management systems

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Considerations and Future Improvements

- **Action Detection Accuracy**:
  - The action detection model's predictions are currently not ideal due to a limited training dataset.
  - With a more extensive and diverse dataset, the accuracy of action detection can be significantly improved.
  - Future work should focus on gathering more labeled data to train the action detection model.

- **Real-time Processing**:
  - Enhancements to the processing speed and real-time capabilities of the system can be made.
  - Incorporating GPU acceleration and optimizing model performance can help achieve this goal.
 
## Conclusion

The ICU Video Analysis System demonstrates the potential of using machine learning for automating the analysis of ICU videos. Despite the current limitations in action detection accuracy, the system lays a strong foundation for future improvements. With better datasets and optimized models, the system can provide accurate and real-time insights into patient activities, aiding in effective ICU monitoring and management.

---

We hope this project serves as a valuable step towards enhancing ICU monitoring systems and invites further research and development in this critical area. Contributions and feedback are welcome to improve the system's performance and capabilities.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/BetterFeature`)
3. Commit your Changes (`git commit -m 'Add some BetterFeature'`)
4. Push to the Branch (`git push origin feature/BetterFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jagdish Suthar - [@Jagdish Suthar](https://linkedin.com/in/jagdish-suthar-20934a227) - 21it404@bvmengineering.ac.in

Manmeet Patel - [@Mann7187](https://x.com/Mann7187) - 21it456@bvmengineering.ac.in

Project Link: [https://github.com/Jagdish9903/Intel-Project-TeleICU](https://github.com/Jagdish9903/Intel-Project-TeleICU)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Ultralytics Yolo documentation and tutorials](https://docs.ultralytics.com/)
* [Mediapipe documentation](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Streamlit documentation](https://flexbox.malven.co/)
* [Tensorflow guide](https://grid.malven.co/)
* [Kaggle human-activity-recognition-video-dataset](https://www.kaggle.com/datasets/sharjeelmazhar/human-activity-recognition-video-dataset)
* [Youtube @Holly Mullens ICU web show](https://www.youtube.com/@hollymullens8340)
* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [MoviePy](https://pypi.org/project/moviepy/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Jagdish9903/Intel-Project-TeleICU.svg?style=for-the-badge
[contributors-url]: https://github.com/Jagdish9903/Intel-Project-TeleICU/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Jagdish9903/Intel-Project-TeleICU.svg?style=for-the-badge
[forks-url]: https://github.com/Jagdish9903/Intel-Project-TeleICU/network/members
[stars-shield]: https://img.shields.io/github/stars/Jagdish9903/Intel-Project-TeleICU.svg?style=for-the-badge
[stars-url]: https://github.com/Jagdish9903/Intel-Project-TeleICU/stargazers
[issues-shield]: https://img.shields.io/github/issues/Jagdish9903/Intel-Project-TeleICU.svg?style=for-the-badge
[issues-url]: https://github.com/Jagdish9903/Intel-Project-TeleICU/issues
[license-shield]: https://img.shields.io/github/license/Jagdish9903/Intel-Project-TeleICU.svg?style=for-the-badge
[license-url]: https://github.com/Jagdish9903/Intel-Project-TeleICU/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jagdish-suthar-20934a227
[product-screenshot]: images/screenshot.png
[YOLO]: https://img.shields.io/badge/YOLO-FF6F00?style=for-the-badge&logo=yolo&logoColor=white
[YOLO-url]: https://docs.ultralytics.com/

[TensorFlow]: https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/

[MediaPipe]: https://img.shields.io/badge/MediaPipe-00C853?style=for-the-badge&logo=mediapipe&logoColor=white
[MediaPipe-url]: https://mediapipe.dev/

[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white
[Streamlit-url]: https://streamlit.io/

[OpenCV]: https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white
[OpenCV-url]: https://opencv.org/

[NumPy]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[NumPy-url]: https://numpy.org/

[Matplotlib]: https://img.shields.io/badge/Matplotlib-FF7043?style=for-the-badge&logo=matplotlib&logoColor=white
[Matplotlib-url]: https://matplotlib.org/

[MoviePy]: https://img.shields.io/badge/MoviePy-FFD700?style=for-the-badge&logo=python&logoColor=white
[MoviePy-url]: https://zulko.github.io/moviepy/

[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
