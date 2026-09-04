"""Load legacy exam application CSV data."""

import csv


def load_class_list(csv_path):
	with open(csv_path, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		return [line['classes'] for line in csv_reader]


def load_exam_list(csv_path):
	with open(csv_path, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		return [line['exams'] for line in csv_reader]


def load_student_info(csv_path):
	with open(csv_path, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		return {
			int(line['Student number']): {
				"student_name": line['Name'],
				"student_nickname": line['Nickname'],
				"student_password": line['Password'],
			}
			for line in csv_reader
		}


def load_exam_info(csv_path):
	with open(csv_path, 'r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		return {
			int(line['QuestionNumber']): {
				"question": line['Questions'],
				"answer_a": line['AnswerA'],
				"answer_b": line['AnswerB'],
				"answer_c": line['AnswerC'],
				"answer_d": line['AnswerD'],
				"correct_answer": line['Rightanswer'],
				"photo_question": line['Photoquestion'],
			}
			for line in csv_reader
		}
