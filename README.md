# Crowdsourcing Task Management with Machine Learning

This project uses machine learning to improve task management in a crowdsourcing environment. It includes models for task allocation, performance analysis, and quality control, with a simple web interface built using Flask.

## Table of Contents
- [Overview](#overview)
- [Deployed Link](#deployed-link)
- [Features](#features)
- [Models Used](#models-used)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [License](#license)

## Overview
Crowdsourcing platforms assign tasks to workers, monitor performance, and ensure task quality. This project implements machine learning models to automate these processes:

- **Task Allocation:** Assigns tasks to the best worker based on the difficulty and worker skill level.
- **Performance Analysis:** Predicts task completion time and worker performance.
- **Quality Control:** Predicts task quality based on performance and task attributes.

## Deployed Link
You can access the live application [here](https://crowdsourcing-task-management-with.onrender.com).

## Features
- **Task Allocation:** Uses a Decision Tree Classifier to allocate tasks based on skill and task difficulty.
- **Performance Analysis:** Linear Regression predicts task completion time and performance score.
- **Quality Control:** Logistic Regression predicts whether the task output will be high or low quality.
- **Flask Web Interface:** A simple web interface to interact with the machine learning models.
  
## Models Used
1. **Decision Tree Classifier** for task allocation.
2. **Linear Regression** for performance analysis.
3. **Logistic Regression** for quality control.

## Installation

To set up and run the project locally, follow these steps:

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [Anaconda (recommended)](https://www.anaconda.com/products/individual) to manage environments
- Flask, Scikit-learn, Pandas, Matplotlib (can be installed via `requirements.txt`)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Crowdsourcing-Task-Management.git
    cd Crowdsourcing-Task-Management
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    conda create -n ml_project python=3.8
    conda activate ml_project
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000` to access the web interface.

## Usage

- Select **Task Difficulty** and **Worker Skill Level** from the dropdown menus in the web interface.
- Optionally, enter a **Performance Score** for quality prediction.
- Click **Predict** to allocate the task, predict performance, and assess quality.

## Dataset

The dataset used for training includes features such as:
- **Task_Difficulty:** Difficulty level of the task (1-5 scale).
- **Worker_Skill_Level:** Skill level of the worker (1-5 scale).
- **Performance_Score:** A score representing worker performance (optional for quality prediction).
- **Quality_Score:** A binary value (high-quality or low-quality).

You can find the dataset in the `CrowdSourcing.csv` file in the project folder.


## Technologies Used
- **Python**
- **Flask**: For the web framework.
- **Scikit-learn**: For machine learning models.
- **Pandas**: For data manipulation.
- **Matplotlib**: For data visualization.
- **Bootstrap**: For front-end styling.

## Future Improvements
- Add more advanced models for better accuracy in task allocation and quality control.
- Implement user authentication to manage multiple users on the platform.
- Allow real-time feedback from workers to improve model predictions.

