"""Build legacy exam application paths and filenames."""


def _class_directory_name(class_name: str) -> str:
	return f"M{class_name[1]}-{class_name[3]}"


def student_details_csv_filename(class_name: str) -> str:
	return f"Student_Details_CSV_{_class_directory_name(class_name)}.csv"


def exam_questions_csv_path(exam_name: str) -> str:
	return f"{exam_name}\\{exam_name}_Questions.csv"


def student_photo_directory(network_location: str, class_name: str) -> str:
	return f"{network_location}/{_class_directory_name(class_name)}"


def student_photo_filename(student_number: int) -> str:
	return f"{student_number}.png"


def exam_content_directory(network_location: str, exam_name: str) -> str:
	return f"{network_location}/{exam_name}"


def exam_media_path(network_location: str, exam_name: str, media_filename: str) -> str:
	return f"{network_location}/{exam_name}/{media_filename}"


def results_directory(network_location: str, class_name: str, exam_name: str) -> str:
	return f"{network_location}\\{_class_directory_name(class_name)}_{exam_name}_results"


def running_result_filename(
	exam_title: str,
	exam_subtitle: str,
	student_number: int,
	student_name: str,
	student_nickname: str,
) -> str:
	return f"{exam_title}_{exam_subtitle}_Student_{student_number}_{student_name}_{student_nickname}_running_results.txt"


def completion_marker_filename(
	class_name: str,
	student_number: int,
	student_nickname: str,
) -> str:
	return f"{_class_directory_name(class_name)}_Student_{student_number}_{student_nickname}.txt"


def excel_result_filename(exam_title: str, exam_subtitle: str) -> str:
	return f"{exam_title} {exam_subtitle} results.xlsx"


def local_backup_filename(exam_title: str, exam_subtitle: str, student_number: int) -> str:
	return f"{exam_title} {exam_subtitle} Student {student_number} results.txt"
