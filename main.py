""""Main Python script using polars and matplotlib to read in a csv,
generate summary stats, and create a data visualization."""

import polars as pl
import matplotlib.pyplot as plt


def generate_summary_stats(file_name):
    """Using the csv file passed in as an argument, this function creates a polars
    dataframe from it, and then generates summary statistics (mean, median,
    mode, standard deviation, as well as percentiles) for each column of the dataframe
    using the polars describe method.
    """
    data_frame = pl.read_csv(file_name)
    return data_frame.describe(), data_frame.median()


def generate_viz(file_name):
    """This function generates a scatter plot visualization of hours studied vs. exam scores
    from the Student Performance dataset."""
    data_frame = pl.read_csv(file_name)
    plt.scatter(data_frame["Hours_Studied"], data_frame["Exam_Score"], color="Green")
    plt.xlabel("Hours Studied")
    plt.ylabel("Student Exam Scores")
    plt.title("Relationship Between Hours Studied and Student Exam Scores")
    plt.savefig("performance.png")
    plt.show()
