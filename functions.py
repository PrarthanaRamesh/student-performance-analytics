import numpy as np

subjects = ["Python", "Maths", "Physics", "English", "Data_Structures"]


def calculate_total(df):
    # add up the marks of all subjects for each student
    marks = df[subjects].values
    df["Total"] = np.sum(marks, axis=1)
    return df


def calculate_average(df):
    # average marks for each student
    marks = df[subjects].values
    df["Average"] = np.mean(marks, axis=1)
    return df


def get_grade(avg):
    # grading rule based on average marks
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def add_grades(df):
    grades = []
    for avg in df["Average"]:
        grades.append(get_grade(avg))
    df["Grade"] = grades
    return df


def add_result(df):
    # pass if the student scored 40 or more in every subject
    results = []
    for i in range(len(df)):
        passed = True
        for sub in subjects:
            if df[sub][i] < 40:
                passed = False
        if passed:
            results.append("Pass")
        else:
            results.append("Fail")
    df["Result"] = results
    return df