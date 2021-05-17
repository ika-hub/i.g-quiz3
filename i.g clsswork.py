# # სავარჯიშო 1
#
# class Health:
#     def __init__(self, age, sex, pulse):
#         self.age = age
#         self.sex = sex
#         self.pulse = pulse
#
#     def __str__(self):
#         return "ასაკი {} წლის, სქესი {}, პულსი {} დარტყმა/წუთში".format(self.age, self.sex, self.pulse)
#
#     def calculate_max_heart_rate(self):
#         if(self.sex=="მამრობითი"):
#             return 226-0.9*self.age
#         else:
#             return 223-0.9*self.age
#
#     def h_average(self):
#         return 260000000//365*self.pulse*self.age//12
#
# h1 = Health(30,"მამრობითი", 87)
# print(h1)
# print(h1.calculate_max_heart_rate())
# print(h1.h_average())

# #ავარჯიშო2
# import sqlite3
# conn = sqlite3.connect('survey.sqlite')
# c = conn.cursor()
# conn.row_factory = sqlite3.Row
#
# c.execute(f'SELECT * FROM students WHERE SelfStudyHour>5')
# print(len(c.fetchall()))
#
# c.execute("SELECT * FROM students")
# for each in c.fetchall():
#     print(each['ManageStressMethod'])
#
# c.execute("UPDATE ")









