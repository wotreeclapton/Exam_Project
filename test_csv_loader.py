import os
import tempfile
import unittest

import csv_loader


class CsvLoaderTests(unittest.TestCase):
	def write_csv(self, contents):
		temporary_file = tempfile.NamedTemporaryFile(
			mode='w', delete=False, newline='', encoding='utf-8'
		)
		self.addCleanup(os.unlink, temporary_file.name)
		with temporary_file:
			temporary_file.write(contents)
		return temporary_file.name

	def test_load_class_list_preserves_order_and_values(self):
		csv_path = self.write_csv('classes\nChoose a class\nM1-1\n')

		self.assertEqual(
			csv_loader.load_class_list(csv_path),
			['Choose a class', 'M1-1'],
		)

	def test_load_exam_list_preserves_order_and_values(self):
		csv_path = self.write_csv('exams\nChoose an exam\nMidterm\n')

		self.assertEqual(
			csv_loader.load_exam_list(csv_path),
			['Choose an exam', 'Midterm'],
		)

	def test_load_student_info_preserves_integer_keys_and_record_zero(self):
		csv_path = self.write_csv(
			'Student number,Name,Nickname,Password\n'
			'0,Master User,Master,master-password\n'
			'1,Student Name,Nickname,student-password\n'
		)

		self.assertEqual(
			csv_loader.load_student_info(csv_path),
			{
				0: {
					'student_name': 'Master User',
					'student_nickname': 'Master',
					'student_password': 'master-password',
				},
				1: {
					'student_name': 'Student Name',
					'student_nickname': 'Nickname',
					'student_password': 'student-password',
				},
			},
		)

	def test_load_exam_info_preserves_integer_keys_and_record_zero(self):
		csv_path = self.write_csv(
			'QuestionNumber,Questions,AnswerA,AnswerB,AnswerC,AnswerD,Rightanswer,Photoquestion\n'
			'0,Exam title,Exam subtitle,30,,,A,\n'
			'1,Question text,First,Second,Third,Fourth,B,image.png\n'
		)

		self.assertEqual(
			csv_loader.load_exam_info(csv_path),
			{
				0: {
					'question': 'Exam title',
					'answer_a': 'Exam subtitle',
					'answer_b': '30',
					'answer_c': '',
					'answer_d': '',
					'correct_answer': 'A',
					'photo_question': '',
				},
				1: {
					'question': 'Question text',
					'answer_a': 'First',
					'answer_b': 'Second',
					'answer_c': 'Third',
					'answer_d': 'Fourth',
					'correct_answer': 'B',
					'photo_question': 'image.png',
				},
			},
		)


if __name__ == '__main__':
	unittest.main()
