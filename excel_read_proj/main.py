import pandas as pd
data = pd.read_excel('data.xlsx')
print("Average Marks for Each Student:")
for index, row in data.iterrows():
    student_name = row['NAME']
    total_marks = row[['MATHS', 'SCIENCE', 'ENGLISH']].sum()
    average_marks = row[['MATHS', 'SCIENCE', 'ENGLISH']].mean()
    print(student_name)
    print("     total_marks: ", total_marks)
    print("     average_marks: ", average_marks)
