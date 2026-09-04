import unittest

import paths


class PathBuilderTests(unittest.TestCase):
	def setUp(self):
		self.network_location = r"\\server\exam_share"
		self.class_name = "M1-2"
		self.exam_name = "Midterm"
		self.exam_title = "English"
		self.exam_subtitle = "Unit 1"
		self.student_number = 7
		self.student_name = "Student Name"
		self.student_nickname = "Nickname"

	def test_student_details_csv_filename_matches_legacy_expression(self):
		expected = f"Student_Details_CSV_M{self.class_name[1]}-{self.class_name[3]}.csv"
		self.assertEqual(paths.student_details_csv_filename(self.class_name), expected)

	def test_class_list_csv_path_matches_legacy_location(self):
		expected = f"{self.network_location}\\class_list.csv"
		self.assertEqual(paths.class_list_csv_path(self.network_location), expected)

	def test_exam_list_csv_path_matches_legacy_location(self):
		expected = f"{self.network_location}\\exam_list.csv"
		self.assertEqual(paths.exam_list_csv_path(self.network_location), expected)

	def test_student_details_csv_path_matches_legacy_location(self):
		expected = f"{self.network_location}\\Student_Details_CSV_M{self.class_name[1]}-{self.class_name[3]}.csv"
		self.assertEqual(paths.student_details_csv_path(self.network_location, self.class_name), expected)

	def test_exam_questions_csv_path_matches_legacy_expression(self):
		expected = f"{self.exam_name}\\{self.exam_name}_Questions.csv"
		self.assertEqual(paths.exam_questions_csv_path(self.exam_name), expected)

	def test_network_exam_questions_csv_path_matches_legacy_location(self):
		expected = f"{self.network_location}\\{self.exam_name}\\{self.exam_name}_Questions.csv"
		self.assertEqual(paths.network_exam_questions_csv_path(self.network_location, self.exam_name), expected)

	def test_student_photo_directory_matches_legacy_expression(self):
		expected = f"{self.network_location}/M{self.class_name[1]}-{self.class_name[3]}"
		self.assertEqual(paths.student_photo_directory(self.network_location, self.class_name), expected)

	def test_student_photo_filename_matches_legacy_expression(self):
		expected = f"{self.student_number}.png"
		self.assertEqual(paths.student_photo_filename(self.student_number), expected)

	def test_student_photo_path_matches_legacy_expression(self):
		expected = f"{self.network_location}/M{self.class_name[1]}-{self.class_name[3]}/{self.student_number}.png"
		self.assertEqual(paths.student_photo_path(self.network_location, self.class_name, self.student_number), expected)

	def test_blank_student_photo_path_matches_legacy_resource_location(self):
		application_directory = r"C:\ExamApp"
		expected = f"{application_directory}\\img\\blank_girl.png"
		self.assertEqual(paths.blank_student_photo_path(application_directory), expected)

	def test_exam_content_directory_matches_legacy_expression(self):
		expected = f"{self.network_location}/{self.exam_name}"
		self.assertEqual(paths.exam_content_directory(self.network_location, self.exam_name), expected)

	def test_exam_media_path_matches_legacy_expression(self):
		media_filename = "question_video.mp4"
		expected = f"{self.network_location}/{self.exam_name}/{media_filename}"
		self.assertEqual(paths.exam_media_path(self.network_location, self.exam_name, media_filename), expected)

	def test_results_directory_matches_legacy_expression(self):
		expected = f"{self.network_location}\\M{self.class_name[1]}-{self.class_name[3]}_{self.exam_name}_results"
		self.assertEqual(paths.results_directory(self.network_location, self.class_name, self.exam_name), expected)

	def test_running_result_filename_matches_legacy_expression(self):
		expected = f"{self.exam_title}_{self.exam_subtitle}_Student_{self.student_number}_{self.student_name}_{self.student_nickname}_running_results.txt"
		self.assertEqual(paths.running_result_filename(self.exam_title, self.exam_subtitle, self.student_number, self.student_name, self.student_nickname), expected)

	def test_completion_marker_filename_matches_legacy_expression(self):
		expected = f"M{self.class_name[1]}-{self.class_name[3]}_Student_{self.student_number}_{self.student_nickname}.txt"
		self.assertEqual(paths.completion_marker_filename(self.class_name, self.student_number, self.student_nickname), expected)

	def test_excel_result_filename_matches_legacy_expression(self):
		expected = f"{self.exam_title} {self.exam_subtitle} results.xlsx"
		self.assertEqual(paths.excel_result_filename(self.exam_title, self.exam_subtitle), expected)

	def test_local_backup_filename_matches_legacy_expression(self):
		expected = f"{self.exam_title} {self.exam_subtitle} Student {self.student_number} results.txt"
		self.assertEqual(paths.local_backup_filename(self.exam_title, self.exam_subtitle, self.student_number), expected)


if __name__ == "__main__":
	unittest.main()
