from main import generate_summary_stats, generate_viz


def test_generate_summary_stats():
    """testing out summary stats function"""
    summary = generate_summary_stats("StudentPerformanceFactors.csv")
    describe_stats = summary[0]
    medians = summary[1]
    assert describe_stats.loc["mean"]["Previous_Scores"] == 75.07053125472983
    assert medians["Sleep_Hours"] == 7.0
    assert describe_stats.loc["std"]["Physical_Activity"] == 1.0312310926271286

def test_generate_viz():
    """testing out generate viz function"""
    generate_viz("StudentPerformanceFactors.csv")


if __name__ == "__main__":
    test_generate_summary_stats()
    test_generate_viz()
