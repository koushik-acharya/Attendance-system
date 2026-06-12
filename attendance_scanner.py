
import pandas as pd
from attendance_manager import mark_attendance, increase_total_classes


def start_scanner(subject):
    import cv2
    from pyzbar.pyzbar import decode
    
    subject = str(subject).strip()
    if not subject:
        print("Subject is required.")
        return

    try:
        increase_total_classes(subject)
    except Exception as exc:
        print(f"Unable to prepare subject file: {exc}")
        return

    try:
        students_df = pd.read_excel("students.xlsx")
    except FileNotFoundError:
        print("students.xlsx not found. Create the student database before scanning.")
        return

    if "SRN" not in students_df.columns or "Name" not in students_df.columns:
        print("students.xlsx must contain SRN and Name columns.")
        return

    students_df.columns = students_df.columns.astype(str).str.strip()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Unable to open camera.")
        return

    print("\nScanner Started...")
    print("Show College ID Barcode")
    print("Press Q to Exit")

    scanned_students = set()

    while True:
        success, frame = cap.read()
        if not success:
            print("Camera Error")
            break

        detected_codes = decode(frame)
        for code in detected_codes:
            srn = code.data.decode("utf-8").strip()
            if srn in scanned_students:
                continue

            student = students_df[students_df["SRN"].astype(str).str.strip() == srn]
            if not student.empty:
                name = student.iloc[0]["Name"]
                if mark_attendance(srn, name, subject):
                    scanned_students.add(srn)
                    print(f"Attendance Marked: {name}")
                    cv2.putText(frame, f"{name} Marked", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                print(f"Student Not Found: {srn}")
                cv2.putText(frame, "Student Not Found", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Attendance Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("\nScanner Closed")
