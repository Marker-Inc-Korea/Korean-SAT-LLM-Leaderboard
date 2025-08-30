import pandas as pd
import os

# Constants for file paths and coefficients
EXAM_DATA_PATH = "../data/exam_data/2023.csv"
SCORING_RESULT_PATH = "../data/result/grading_report_card.csv"
AUTORAG_PROJECT_DIR = "../autorag_project_dir"

STD_COEFFICIENT_INFO = {
    'year': 2023,
    'common_coefft': 0.980,
    'selection_coefft': 0.866,
    'constant': 35.1
}


class ReportCard:
    def __int__(self):
        pass

    @staticmethod
    def generate_report_card(scoring_result):
        """Generate a table of scores and save it to a CSV file."""
        scoring_result_statics = ReportCard.cal_std_score_grade(scoring_result)

        score_name_score_pairs = [(score_name, score) for score_name, score in scoring_result_statics.items()]
        score_name, scores = zip(*score_name_score_pairs)

        df = pd.DataFrame(list(zip(score_name, scores)), columns=['score_name', 'score'])
        df.to_csv(SCORING_RESULT_PATH, index=False)
        return df

    @staticmethod
    def calculate_standard_score(common_score, choice_score):
        """Calculate the standard score based on given scores and coefficients."""
        return round(
            STD_COEFFICIENT_INFO['common_coefft'] * common_score +
            STD_COEFFICIENT_INFO['selection_coefft'] * choice_score +
            STD_COEFFICIENT_INFO['constant']
        ).iloc[0]

    @staticmethod
    def get_grade_info(standard_score, grading_df):
        """Retrieve percentile and grade information for a given standard score."""

        grading_df_row = grading_df[grading_df['std_score'] == standard_score]
        if grading_df_row.empty:
            raise ValueError("Standard score not found in grading data.")
        percentile_score = int(grading_df_row['percentile'].iloc[0])
        grade = int(grading_df_row['grade'].iloc[0])
        return percentile_score, grade

    @staticmethod
    def cal_std_score_grade(result):
        """Calculate the standard score, percentile, and grade for a given result."""
        grading_df = pd.read_csv(EXAM_DATA_PATH)

        common_problem_score = result['common_problem_score']
        choice_problem_score = result['choice_problem_score']

        raw_score = int(result['overall_sum'].iloc[0])
        standard_score = ReportCard.calculate_standard_score(common_problem_score, choice_problem_score)

        percentile_score, grade = ReportCard.get_grade_info(standard_score, grading_df)

        return {
            'raw_score': raw_score,
            'std_score': standard_score,
            'percentile': percentile_score,
            'grade': grade
        }

    @staticmethod
    def process_scores(df):
        """Process the DataFrame to calculate and separate common and choice problem scores."""
        df['qid_for_merge'] = df['qid'].apply(lambda x: x[:4])
        df = df.groupby('qid_for_merge').agg({'kice_metric': list}).reset_index()

        def calculate_and_separate(row_scores):
            """Calculate scores from a list of scores."""
            common_problem_score = sum(row_scores[:34])
            choice_problem_score = sum(row_scores[34:])

            # Ensure that the number of common problems is as expected
            assert len(row_scores[:34]) + len(row_scores[34:]), "The number of total problems length should be 45."
            return {
                'common_problem_score': common_problem_score,
                'choice_problem_score': choice_problem_score,
                'overall_sum': common_problem_score + choice_problem_score
            }

        df['score_result'] = df['kice_metric'].apply(calculate_and_separate)

        result = pd.concat([df, df['score_result'].apply(pd.Series)], axis=1)

        return result


def find_recent_experiment_file():
    path = AUTORAG_PROJECT_DIR
    entries = os.listdir(path)

    numeric_dirs = [entry for entry in entries if entry.isdigit() and os.path.isdir(os.path.join(path, entry))]

    if not numeric_dirs:
        raise ValueError("No numeric directories found.")

    numeric_values = [int(dir_name) for dir_name in numeric_dirs]

    largest_numeric_value = max(numeric_values)

    return str(largest_numeric_value)
