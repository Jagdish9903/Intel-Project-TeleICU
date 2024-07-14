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
    <a href="https://github.com/Jagdish9903/Intel-Project-TeleICU"><strong>Explore the project repo »</strong></a>
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
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#approach-taken">Approach Taken</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<!-- ABOUT THE PROJECT -->


<!-- ABOUT THE PROJECT -->
## About The Project



TeleICU is designed to enhance patient care by leveraging technology to provide remote monitoring and support in intensive care units (ICUs). This project aims to bridge the gap between healthcare professionals and patients by providing real-time data and communication tools.

Here's why teleICU is important:

Improved patient outcomes through continuous monitoring.
Efficient use of healthcare resources.
Enhanced collaboration among healthcare professionals.

This project uses computer vision techniques to detect and identify subjects like patients, doctors and others. And also analyse the activities of patients.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section highlights the key frameworks and libraries that were instrumental in building the teleICU project. Each technology was carefully selected to ensure robust functionality, scalability, and real-time capabilities required for a teleICU system.


* [![YOLO][YOLO]][YOLO-url]
* [![MediaPipe][MediaPipe]][MediaPipe-url]
* [![TensorFlow][TensorFlow]][TensorFlow-url]
* [![Streamlit][Streamlit]][Streamlit-url]

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
## Usage

Here are some examples demonstrating how to use the `Intel-Project-TeleICU`:
1. Streamlit interface:
   
   ![Streamlit interface](demo-content/streamlit_interface.png)

3. Upload video:
   
   ![Upload video](demo-content/upload_video.png)
   
5. Video results:
   
   _People detection result_
   
    [![Watch the video](https://github.com/Jagdish9903/Intel-Project-TeleICU/blob/4bc053e42266131d045a4852eb99ce64b12766d8/demo%20videos/Screenshot%20(180).png)](https://github.com/Jagdish9903/Intel-Project-TeleICU/blob/main/demo%20videos/processed_video_004553.mp4)

   _Only patient cropped result_
   
   ![Video results2](demo-content/result2.png)

   _Patient analysis result_
   
   [![Watch the video](https://github.com/Jagdish9903/Intel-Project-TeleICU/blob/4bc053e42266131d045a4852eb99ce64b12766d8/demo%20videos/Screenshot%20(181).png)](https://github.com/Jagdish9903/Intel-Project-TeleICU/blob/96a1e0bc00b4787d41783c75d1af87b947a01a8f/demo%20videos/vid_walk_gpu10.mp4)


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
  
### Results generated by model
1. Object detection model:

<video width="640" height="360" controls>
  <source src="demo-content/yolo_object_detection.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


2. Patient's Activity Classification model:

<video width="640" height="360" controls>
  <source src="demo-content/yolo_object_detection.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


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
