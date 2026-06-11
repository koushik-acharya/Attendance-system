import pandas as pd
import os

EXCEL_FOLDER = "excel"

def generate_report():

    file_path = os.path.join(

        EXCEL_FOLDER,

        "attendance_percentage.xlsx"

    )

    # =========================
    # CHECK FILE EXISTS
    # =========================

    if not os.path.exists(file_path):

        print(
            "\nPercentage File Not Found"
        )

        return

    # =========================
    # READ FILE
    # =========================

    df = pd.read_excel(
        file_path
    )

    print(
        "\n===== Attendance Report ====="
    )

    print(df)

    # =========================
    # LOW ATTENDANCE
    # =========================

    low_attendance = df[
        df["Percentage"] < 75
    ]

    if len(low_attendance) > 0:

        print(
            "\n===== Low Attendance Students ====="
        )

        print(low_attendance)

    # =========================
    # SAVE REPORT
    # =========================

    report_path = os.path.join(

        EXCEL_FOLDER,

        "attendance_report.xlsx"

    )

    df.to_excel(

        report_path,

        index=False

    )

    print(
        f"\nReport Saved In: {report_path}"
    )