SUBJECT_FILE = "Subjects.txt"



def add_subject():

    while True:

        subject = input(
            "Enter Subject Name: "
        ).upper()

        # Save permanently
        with open(
            SUBJECT_FILE,
            "a"
        ) as file:

            file.write(subject + "\n")

        print(
            f"{subject} Added Successfully"
        )

        choice = input(
            "Add Another Subject? (y/n): "
        ).lower()

        if choice != "y":
            break


def get_subjects():

    try:

        with open(
            SUBJECT_FILE,
            "r"
        ) as file:

            subjects = file.readlines()

        return [
            s.strip()
            for s in subjects
        ]

    except FileNotFoundError:

        return []
                                
                                
