import os
import pandas as pd

EXCEL_FOLDER = "excel"

def calculate_percentage():
    if not os.path.exists(EXCEL_FOLDER):
        print("\nNo attendance folder found.")
        return

    files = [f for f in os.listdir(EXCEL_FOLDER) if f.lower().endswith(".xlsx")]
    all_data = []

    for file in files:
        if file.lower() in ("attendance_percentage.xlsx", "attendance_report.xlsx"):
            continue

        file_path = os.path.join(EXCEL_FOLDER, file)
        df = pd.read_excel(file_path)

        if len(df) == 0 or "Attended" not in df.columns or "Total Classes" not in df.columns:
            continue

        df["Total Classes"] = df["Total Classes"].fillna(0)
        df["Percentage"] = df.apply(
            lambda row: round((row["Attended"] / row["Total Classes"]) * 100, 2)
            if row["Total Classes"] else 0.0,
            axis=1,
        )

        subject_name = file.replace(".xlsx", "")
        df["Subject"] = subject_name
        all_data.append(df)

    if len(all_data) == 0:
        print("\nNo Attendance Data Found")
        return

    final_df = pd.concat(all_data, ignore_index=True)
    output_file = os.path.join(EXCEL_FOLDER, "attendance_percentage.xlsx")
    final_df.to_excel(output_file, index=False)

    print("\nAttendance Percentage Calculated")
    print(f"Saved In: {output_file}")
