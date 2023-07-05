import csv

path="J:\\My Drive\\02Office & Programing\\103Exam_Project\\M2_C22203_Midterm_Exam_Questions.csv"

with open(path,'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	exam_info = {int(line['QuestionNumber']): {"question": line['Questions'], "answer_a": line['AnswerA'], "answer_b": line['AnswerB'], "answer_c": line['AnswerC'], "answer_d": line['AnswerD'], "correct_answer": line['Rightanswer'], "photo_question": line['Photoquestion']} for line in csv_reader}


print(exam_info)
