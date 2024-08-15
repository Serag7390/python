def main():
    name = input("اسم الطالب: ")
    id_number = input("رقم القيد: ")
    semester = input("الفصل الدراسي: ")
    num_subjects = int(input("عدد المواد التي درسها الطالب: "))

    total_grade = 0
    for i in range(num_subjects):
        grade = float(input("العلامة في المادة رقم {}: ".format(i+1)))
    total_grade += grade

    average_grade = total_grade / num_subjects

    print("معلومات الطالب:")
    print("الاسم: ", name)
    print("رقم القيد: ", id_number)
    print("الفصل الدراسي: ", semester)
    print("عدد المواد التي درسهاالطالب: ", num_subjects)
    print("المعدل العام: ", average_grade)
main()