from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import pandas as pd
import os

from percentage_calculator import (
    calculate_percentage
)

from report_generator import (
    generate_report
)

app = Flask(__name__)

EXCEL_FOLDER = "excel"

# =========================
# HOME PAGE
# =========================

@app.route("/")

def home():

    subjects = []

    try:

        with open(
            "Subjects.txt",
            "r"
        ) as file:

            subjects = [

                line.strip()

                for line in file

                if line.strip()

            ]

    except:

        pass

    return render_template(

        "index.html",

        subjects=subjects

    )

# =========================
# START SCANNER
# =========================

@app.route(
    "/start_scanner",
    methods=["POST"]
)

def scanner():

    subject = request.form.get(
        "subject"
    )
   

    return jsonify({

        "message":
        f"Attendance Completed For {subject}"

    })



# =========================
# CALCULATE PERCENTAGE
# =========================

@app.route(
    "/calculate_percentage"
)

def percentage():

    calculate_percentage()

    return jsonify({

        "message":
        "Percentage Calculated"

    })

# =========================
# GENERATE REPORT
# =========================

@app.route(
    "/generate_report"
)

def report():

    generate_report()

    return jsonify({

        "message":
        "Report Generated"

    })

# =========================
# VIEW ATTENDANCE PAGE
# =========================

@app.route(
    "/view_attendance"
)

def view_attendance():

    subjects = []

    try:

        with open(
            "Subjects.txt",
            "r"
        ) as file:

            subjects = [

                line.strip()

                for line in file

                if line.strip()

            ]

    except:

        pass

    return render_template(

        "select_subject.html",

        subjects=subjects

    )

# =========================
# VIEW PARTICULAR SUBJECT
# =========================

@app.route(
    "/subject_attendance/<subject>"
)

def subject_attendance(subject):

    file_path = os.path.join(

        EXCEL_FOLDER,

        f"{subject}.xlsx"

    )

    if not os.path.exists(
        file_path
    ):

        return (
            "Subject File Not Found"
        )

    df = pd.read_excel(
        file_path
    )

    data = df.to_dict(
        orient="records"
    )

    total_students = len(df)

    present_students = (
        df["Attended"] > 0
    ).sum()

    absent_students = (
        df["Attended"] == 0
    ).sum()

    attendance_rate = round(

        (
            present_students
            /
            total_students
        ) * 100,

        2

    )

    return render_template(

        "attendance.html",

        data=data,

        subject=subject,

        total_students=total_students,

        present_students=present_students,

        absent_students=absent_students,

        attendance_rate=attendance_rate

    )

# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":

    app.run(
        debug=True
    )
