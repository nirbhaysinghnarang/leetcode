import os
import glob
from pathlib import Path
from datetime import datetime

def get_latest_accepted_submission(submission_dir):
    accepted_submissions = glob.glob(os.path.join(submission_dir, "Accepted", "*"))

    if not accepted_submissions:
        return None

    latest_submission = max(accepted_submissions, key=os.path.getctime)
    return latest_submission

def replace_with_latest_accepted(problem_dir):
    accepted_dir = os.path.join(problem_dir, "Accepted")
    latest_accepted_submission = get_latest_accepted_submission(accepted_dir)

    if latest_accepted_submission is None:
        print(f"No accepted submissions found for problem '{os.path.basename(problem_dir)}'.")
        return

    for subfolder in os.listdir(problem_dir):
        subfolder_path = os.path.join(problem_dir, subfolder)

        if subfolder == "Accepted":
            continue

        if os.path.isdir(subfolder_path):
            print(f"Removing '{subfolder_path}'...")
            os.rmdir(subfolder_path)

    problem_name = os.path.basename(problem_dir)
    print(f"Replacing subfolders in '{problem_name}' with latest accepted submission...")
    latest_submission_dir = os.path.join(problem_dir, "Latest")
    os.rename(latest_accepted_submission, latest_submission_dir)

if __name__ == "__main__":
    submissions_dir = "submissions"
    for problem_dir in Path(submissions_dir).iterdir():
        if problem_dir.is_dir():
            replace_with_latest_accepted(problem_dir)
