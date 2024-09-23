from main import generate_summary_stats, generate_viz
import polars as pl


def test_generate_summary_stats():
    """testing out summary stats function"""
    summary = generate_summary_stats("StudentPerformanceFactors.csv")
    describe_stats = summary[0]
    medians = summary[1]
    describe_stats.select(pl.col("Previous_Scores").mean()).item() == 75.07053125472983
    medians.select(pl.col("Sleep_Hours").mean()).item() == 7.0
    describe_stats.select(pl.col("Physical_Activity").mean()).item() == 1.0312310926271286


def test_generate_viz():
    """testing out generate viz function"""
    generate_viz("StudentPerformanceFactors.csv")


if __name__ == "__main__":
    test_generate_summary_stats()
    test_generate_viz()
