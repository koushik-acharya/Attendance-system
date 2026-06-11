from attendance_scanner import start_scanner

from percentage_calculator import (
    calculate_percentage
)

from report_generator import (
    generate_report
)

from subject_manager import (
    add_subject
)

# =========================
# MAIN LOOP
# =========================

while True:

    print("\n===== QR Attendance System =====")

    print("1. Add Subjects")

    print("2. Start Attendance Scanner")

    print("3. Calculate Attendance Percentage")

    print("4. Generate Attendance Report")

    print("5. Exit")

    # =========================
    # USER CHOICE
    # =========================

    choice = input(
        "\nEnter choice: "
    )

    # =========================
    # ADD SUBJECTS
    # =========================

    if choice == "1":

        add_subject()

    # =========================
    # START SCANNER
    # =========================

    elif choice == "2":

        start_scanner()

    # =========================
    # CALCULATE PERCENTAGE
    # =========================

    elif choice == "3":

        calculate_percentage()

    # =========================
    # GENERATE REPORT
    # =========================

    elif choice == "4":

        generate_report()

    # =========================
    # EXIT
    # =========================

    elif choice == "5":

        print(
            "\nExiting Program..."
        )

        break

    # =========================
    # INVALID INPUT
    # =========================

    else:

        print(
            "\nInvalid Choice"
        )