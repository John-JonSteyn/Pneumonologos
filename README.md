<div align="center" id="top">

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT HEADING -->
<br />
    <h1>Pneumonologos</h1>
  </a>

  <h3 align="center">AI-powered Pneumonia Detection System, using Deep Learning and Chest X-rays.</h3>
  
  <hr>
  
  <p align="center">
    <a href="https://github.com/John-JonSteyn/Pneumonologos/"><strong>View Source Code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/John-JonSteyn/Pneumonologos/issues">Report Bug</a>
    ·
    <a href="https://github.com/John-JonSteyn/Pneumonologos/issues">Request Feature</a>
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
        <li><a href="#running-pneumonologos">Running Pneumonologos</a></li>
      </ul>
    </li>
    <li><a href="#the-basics-of-pneumonologos">The Basics of Pneumonologos</a></li>
    <ul>
        <li><a href="#login-screen">Login Screen</a></li>
        <li><a href="#registration">Registration</a></li>
        <li><a href="#home-screen">Home Screen</a></li>
        <li><a href="#visitor-features">Visitor Features</a></li>
        <li><a href="#patient-features">Patient Features</a></li>
        <li><a href="#staff-features">Staff Features</a></li>
        <li><a href="#logging-out">Logging Out</a></li>
    </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Pneumonologos is an AI-based project aimed at exploring the capabilities of deep learning in pneumonia detection using chest X-ray images. It is not intended for professional medical diagnosis but rather serves as an educational exploration of the potential of AI in healthcare. By leveraging deep learning techniques, Pneumonologos analyses chest X-ray images and provides predictions on whether a person may have pneumonia or not. This project highlights the power of artificial intelligence and its potential impact in assisting medical professionals in the near future.

Features:
* Pneumonia Detection: The core feature of Pneumonologos is its ability to analyse chest X-ray images and determine whether a person is likely to have pneumonia or not.
* Probability Estimation: Along with the detection results, Pneumonologos provides the probability of the presence of pneumonia, giving users an understanding of the level of confidence in the prediction.
* User-Friendly Interface: Pneumonologos offers a simple and intuitive user interface where users can upload their chest X-ray images and receive quick results. The interface is designed to be accessible and easy to navigate.

*Pneumonologos is not intended to replace professional medical diagnosis or serve as a substitute for consultation with qualified healthcare providers. It is solely a demonstration project to showcase the capabilities of AI in pneumonia detection and to foster understanding and discussion regarding the potential applications of Artificial Intelligence in healthcare.*

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Fast AI](https://www.fast.ai/)
* [PyQt](https://www.riverbankcomputing.com/software/pyqt/)
* [Python](https://www.python.org/)
* [PyTorch](https://pytorch.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



Sure! Here's an updated README with instructions on how to install, run, and use the Pneumonologos program:

```markdown
<!-- GETTING STARTED -->
## Getting Started

Setting up Pneumonologos might sound daunting, but not to fear - as long as README is here!
Simply follow these steps, as you would the doctor's instructions.

### Installation

1. Install Python:
   - Download the latest version of Python from the official website: [python.org](https://www.python.org/downloads/).
   - Follow the installation instructions specific to your operating system.
   - Make sure to select the option to add Python to the system PATH during the installation process.

2. Open a terminal or command prompt on your computer.

3. Navigate to the directory where you would like to install Pneumonologos:
   ```sh
   cd [DirectoryPathHere]
   ```

4. Clone the repository by entering the following command into your terminal:
   ```sh
   git clone https://github.com/John-JonSteyn/Pneumonologos.git
   ```

5. Once the repository is cloned, navigate into the project directory:
   ```sh
   cd Pneumonologos
   ```

6. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running Pneumonologos

1. Create a virtual environment for the project (optional but recommended):
   ```sh
   python -m venv env
   ```

2. Activate the virtual environment:
   - For Windows:
     ```sh
     env\Scripts\activate
     ```
   - For macOS/Linux:
     ```sh
     source env/bin/activate
     ```

3. After the dependencies are installed, you can run Pneumonologos by executing the following command:
   ```sh
   python Scripts/pneumologos.py
   ```

## The Basics of Pneumonologos

- Upon launching Pneumonologos, you will see a main window with two panels.
- The left panel, titled "CONTROLS," contains two buttons:
  - "Upload" button: Click this button to select and upload an X-ray image file.
  - "Analyse" button: Once an X-ray image is uploaded, click this button to analyze the X-ray for pneumonia.
- The right panel, titled "XRAY," initially displays a blank area. Once an X-ray image is uploaded, it will be displayed in this panel.
- The program provides diagnostic information and probability results in the left panel:
  - "Diagnosis" label: This label displays the diagnosis result based on the analysis.
  - "Probability" LCD: This LCD number display shows the probability of the diagnosis ( the likelihood of pneumonia).
- Disclaimer: The program includes a disclaimer text in the left panel, which emphasizes that Pneumonologos is a proof of concept program and should not replace professional medical advice.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Pneumonologos Project Roadmap

### Stage 1: Data Collection and Preparation
- [x] Download the Chest X-Ray Images (Pneumonia) dataset.
- [x] Preprocess the images, such as resizing and augmenting, if required.
- [x] Create data loaders to efficiently load and augment the data during training.

### Stage 2: Model Development
- [x] Write a training script, for example, train.py, using the Fastai library, to train a model on the prepared dataset.
- [x] Save the trained model for future use.

### Stage 3: GUI Development
- [x] Install PyQt to create the graphical user interface (GUI) for the application.
- [x] Design the GUI layout, including necessary elements like buttons, file upload functionality, and display areas for the results.
- [x] Implement the necessary logic to load the trained model and perform predictions on uploaded X-ray images.
- [x] Integrate the prediction results and display them in the GUI, including the classification (Pneumonia or Normal) and associated probabilities.
- [x] Test the GUI functionality thoroughly and make any necessary refinements.

### Stage 4: Integration
- [x] Integrate the trained model and the GUI by incorporating the model's prediction functionality into the GUI's code.
- [x] Handle the image submission from the GUI and pass it to the trained model for classification.
- [x] Display the classification result and the probability of pneumonia on the GUI interface.

### Stage 5: Testing and Refinement
- [x] Test the GUI by running it and submitting various X-ray images to ensure proper functionality.
- [x] Fine-tune the model and update the trained model if needed to improve performance.

### Stage 6: Deplayment
- [x] Update requirements.
- [x] Update Readme.

See the [open issues](https://github.com/John-JonSteyn/Pneumonologos/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU-3.0 License. See [LICENSE](https://github.com/John-JonSteyn/Pneumonologos/blob/main/LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Fast Ai](https://github.com/fastai) - for creating the amazing [Practical Deep Learning for Coders Course](https://course.fast.ai/).
* [Paul Mooney](https://www.kaggle.com/paultimothymooney) - for providing the [Dataset of X-Rays](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) used for training this model.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/John-JonSteyn/Pneumonologos.svg?style=for-the-badge&color=222bac
[contributors-url]: https://github.com/John-JonSteyn/Pneumonologos/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/John-JonSteyn/Pneumonologos.svg?style=for-the-badge&color=2240ac
[forks-url]: https://github.com/John-JonSteyn/Pneumonologos/network/members
[stars-shield]: https://img.shields.io/github/stars/John-JonSteyn/Pneumonologos.svg?style=for-the-badge&color=224bac
[stars-url]: https://github.com/John-JonSteyn/Pneumonologos/stargazers
[issues-shield]: https://img.shields.io/github/issues/John-JonSteyn/Pneumonologos.svg?style=for-the-badge&color=225bac
[issues-url]: https://github.com/John-JonSteyn/Pneumonologos/issues
[license-shield]: https://img.shields.io/github/license/John-JonSteyn/Pneumonologos.svg?style=for-the-badge&color=2267ac
[license-url]: https://github.com/John-JonSteyn/Pneumonologos/blob/master/LICENSE
