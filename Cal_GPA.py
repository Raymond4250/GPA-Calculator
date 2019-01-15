import csv
import math

filename = 'D:\Works\Database Systems\Code\Grade.csv'
data = []

def main():
  read_data()
  print('''Mode
  1 = Calulate GPA
  2 = Insert
  3 = Edit''')
  mode = input('Enter mode: ')

  if mode == '1':
    select_data = []
    year = input('Enter year: ')
    semeter = input('Enter semeter: ')
    for subject in data:
      if subject[0] == year and subject[1] == semeter:
        select_data.append(subject)
    display_subject(select_data)
    cal_GPA(select_data)
    print()
  elif mode == '2':
    insert()
    print()
  elif mode == '3':
    edit()
    print()

def read_data():
  '''Read all data'''
  data.clear()
  with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      data.append(row)
    # print(data)
  return data

def cal_GPA(data):
  '''This function calculate GPA'''
  print('Calculate GPA Mode')
  score, credit = cal_score(data)
  total_credit = sum(credit)
  total_score = sum(score)
  GPA = total_score/total_credit
  GPA = math.floor(GPA * 100) / 100
  print()
  print("GPA: ",GPA)

def cal_score(data):
  '''This function calculate score each subject'''
  credit = []
  score = []
  for row in data:
    credit.append(row[4])  # Keep only credit for calculate
  credit = list(map(int, credit))  # Convert string to integer
  for i in range(len(credit)):
    score.append(credit[i]*chage_grade_to_number(data[i][5]))
  return score, credit

def chage_grade_to_number(int):
  '''This function change grade form alphabet to numeric and then keep it to list'''
  grade = {'A': 4, 'B+': 3.5, 'B': 3, 'C+': 2.5,'C': 2, 'D+': 1.5, 'D': 1, 'F': 0}
  return grade[int]

def display_subject(data):
  print()
  print("{:5}|{:8}|{:11}|{:40}|{:8}|{:8}".format('Year', 'Semeter', 'Subject ID', 'Subject', 'Credit', 'Grade'))
  print('-'*80)
  for row in data:
    print("{:5}|{:8}|{:11}|{:40}|{:8}|{:8}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
  print('-'*80)

def insert():
  print('Insert Mode')
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
  print('Save finished!!!')

def edit():
  print('Edit Mode')
  year = input('Enter year you need to edit: ')
  semeter = input('Enter semeter you need to edit: ')
  select_data = []
  for subjects in data:
      if subjects[0] == year and subjects[1] == semeter:
        select_data.append(subjects)
  display_subject(select_data)

  old_subject_id = str(input('Enter subject id your need to edit: '))
  for subject in data:
    if subject[2] == old_subject_id:
      subject[2] = input('Enter new subject id: ')
      subject[3] = input('Enter new subject: ')
      subject[4] = input('Enter new credit: ')
      subject[5] = input('Enter new grade: ')
  # print(data)
  save_data(data)
  print('Save finished!!!')

def save_data(data):
  '''Save new data to CSVfile'''
  with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

while True:
  main()