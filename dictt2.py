student={"name":"DEEPIKA",
         "age":"20",
         "reg_no":"1105",
         "gender":"female"}
print("student: ",student)
stu=student.keys()
print("keys:",stu)
a=student.get("age")
print("get:",a)
student.values()
print("values:",student)
student.items()
print("items:",student)
student.update({"reg_no":"4008"})
print("update: ",student)
student.pop("gender")
print("pop: ",student)
student.copy()
print(student)
student.clear()
print("clear: ",student)

