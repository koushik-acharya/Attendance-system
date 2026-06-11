import os
import pandas as pd

EXCEL_FOLDER = "excel"

if not os.path.exists(EXCEL_FOLDER):
    os.makedirs(EXCEL_FOLDER)


def get_subject_file(subject):
    return os.path.join(EXCEL_FOLDER, f"{subject}.xlsx")


def setup_subject_file(subject):
    file_path = get_subject_file(subject)
    if os.path.exists(file_path):
        return

    try:
        students_df = pd.read_excel("students.xlsx")
    except FileNotFoundError:
        raise FileNotFoundError("students.xlsx not found. Create the student database before adding subjects.")

    if "SRN" not in students_df.columns or "Name" not in students_df.columns:
        raise ValueError("students.xlsx must contain SRN and Name columns.")

    df = pd.DataFrame({
        "SRN": students_df["SRN"],
        "Name": students_df["Name"],
        "Attended": 0,
        "Total Classes": 0,
    })
    df.to_excel(file_path, index=False)


def increase_total_classes(subject):
    setup_subject_file(subject)
    file_path = get_subject_file(subject)
    df = pd.read_excel(file_path)
    df["Total Classes"] = df["Total Classes"].fillna(0).astype(int) + 1
    df.to_excel(file_path, index=False)


def mark_attendance(srn, name, subject):
    file_path = get_subject_file(subject)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Subject file does not exist for {subject}.")

    df = pd.read_excel(file_path)
    matching = df["SRN"].astype(str).str.strip() == str(srn).strip()

    if not matching.any():
        print(f"SRN {srn} not found in subject file. Attendance not marked.")
        return False

    df.loc[matching, "Attended"] = df.loc[matching, "Attended"].fillna(0).astype(int) + 1
    df.to_excel(file_path, index=False)
    return True
