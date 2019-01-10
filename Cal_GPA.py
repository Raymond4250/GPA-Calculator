import csv
import math

filename = 'D:\Works\Database Systems\Code\Grade.csv'
data = []
grade = []
credit = []
score = []

def main():
  print('''Mode
  1 = Calulate GPA
  2 = Insert
  3 = Edit''')
  mode = input('Enter mode: ')

  if mode == '1':
    x = input('Enter year: ')
    y = input('Enter semeter: ')
    read_data(x,y)
    display_subject()
    chage_grade_to_number()
    cal_score()
    cal_GPA()
    print()
  elif mode == '2':
    print('Insert Mode')
    insert()

def read_data(x,y):
  '''Read data by select year and term then keep it to list'''
  data.clear()
  with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if row[0] == x and row[1] == y:
        data.append(row)
    # print(data)
  return data

def cal_GPA():
  '''This function calculate GPA'''
  total_credit = sum(credit)
  total_score = sum(score)
  GPA = total_score/total_credit
  GPA = round_down(GPA, 2)
  print()
  print("GPA: ",GPA)

def cal_score():
  '''This function calculate score each subject'''
  global credit

  credit.clear()
  score.clear()

  for row in data:
    credit.append(row[4])  # Keep only credit for calculate
  credit = list(map(int, credit))  # Convert string to integer

  for i in range(len(credit)):
    score.append(credit[i]*grade[i])

  return score

def chage_grade_to_number():
  '''This function change grade form alphabet to numeric and then keep it to list'''
  grade.clear()
  for row in data:
    if row[5] == "A":
      grade.append(4)
    elif row[5] == "B+":
      grade.append(3.5)
    elif row[5] == "B":
      grade.append(3)
    elif row[5] == "C+":
      grade.append(2.5)
    elif row[5] == "C":
      grade.append(2)
    elif row[5] == "D+":
      grade.append(1.5)
    elif row[5] == "D":
      grade.append(1)
  return grade

def round_down(n, decimals=0):
  multiplier = 10 ** decimals
  return math.floor(n * multiplier) / multiplier

def display_subject():
  print()
  print("{:5}|{:8}|{:11}|{:40}|{:8}|{:8}".format('Year', 'Semeter', 'Subject ID', 'Subject', 'Credit', 'Grade'))
  print('-'*80)
  for row in data:
    print("{:5}|{:8}|{:11}|{:40}|{:8}|{:8}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
  print('-'*80)

def insert():
  '''This function add grade into the next row in the same file'''
  with open(filename, 'a', newline='') as csvfile:
    fieldnames = ['Year', 'Semeter', 'Subject ID', 'Subject', 'Credit', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    year = input('Enter year: ')
    semeter = input('Enter semeter: ')
    subject_id = input('Enter subject id: ')
    subject = input('Enter Subject: ')
    credit = input('Enter credit: ')
    grade = input('Enter grade: ')
    writer.writerow({'Year': year, 'Semeter': semeter, 'Subject ID': subject_id, 'Subject': subject, 'Credit': credit, 'Grade': grade})

while True:
  main()