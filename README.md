[![CI](https://github.com/nogibjj/Rishika_Randev_MiniProject_1/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Rishika_Randev_MiniProject_1/actions/workflows/hello.yml)

# Rishika Randev's Pandas Descriptive Script for IDS706 Week 3

## ☑️ Requirements (Mini Project 2 & Individual Project 1):
1. Jupyter notebook performing descriptive statistics & tested with nbval plugin
2. Python script for statistics and generating one data visualization
3. Summary pdf or markdown file
4. Makefile that installs required packages, formats, lints, and tests
5. requirements.txt
6. Python testing scripts
7. Successful CI/CD badges

## ☑️ The Dataset
The dataset used in this project is a synthetic, free dataset from Kaggle called [Student Performance Factors](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors?resource=download). It contains various columns that could potentially impact student performance on exams, such as hours studied, hours slept, class attendance, tutoring sessions, and family income. The full list of columns can be viewed at the link above.

## ☑️ Steps
1. Prepare the necesary configuration files like the Dockerfile, devcontainer.json, Makefile, requirements.txt, and main.yml for GitHub Actions integration. Ensure that the requirements.txt lists all necessary packages (for example, matplotlib for visualizing and pandas for data manipulation).
2. Create a main.py script with two functions--
   * generate_summary_stats(csv): reads in any csv file passed to it into a pandas dataframe and then generates summary statistics (mean, median, mode, standard deviation) for its columns.
   * generate_data_viz(csv): reads in the csv file, creates a scatterplot of Hours Studied vs. Exam Score using matplotlib, and saves it as a png file (performance.png).
3. Create a test_main.py script with two functions--
   * test_generate_summary_stats(csv): calls generate_summary_stats() using the student performance factors csv file to validate a few of the sample statistics generated by this function.
     
   ![Sample Stats](https://github.com/user-attachments/assets/54a6c401-c230-46b9-948d-0e2929d952f4)
   * test_generate_data_viz(csv): calls generate_data_viz() using the student performance factors csv file in order to produce the below scatterplot.
     
     ![Visualization](performance.png)
4. Create a [Jupyter Notebook](summary.ipynb) with the same code as the main.py script to easily show the outputs of the descriptive statistics and data visualization.
5. Using the main.yml file, set up a GitHub Actions workflow so that every time changes are pushed to the repository, all of the Makefile commands are run to ensure that new code is properly formatted using Black, linted using Ruff, and tested using Pytest. A pdf or markdown summary file can also be generated through GH Actions (or it can be manually pushed to the repository, by converting the Jupyter notebook to html / pdf).

  - `make install`
    
    ![requirements](https://github.com/user-attachments/assets/0a88d102-f326-4961-83ea-ce40d5930178)

  - `make format`
    
    ![formatting](https://github.com/user-attachments/assets/87809dd7-7128-44be-9dfb-0f3528d2afde8)

  - `make lint`
    
    ![linting](https://github.com/user-attachments/assets/e186bb79-fe4d-4633-a04b-22f7b8d8bfb1)

  - `make test`
  
    ![testing](https://github.com/user-attachments/assets/888bdf3d-fad7-42b8-9d36-985d7625a718)

## ☑️ Summary File
The outputs of the descriptive statistics and visualization showing Hours Studied vs. Exam Scores are captured in this [pdf file](summary.pdf).
   


