import sys
import datetime
import os

NOTES_DIRECTORY = "notes"

def main(action_name, value_data=None):
	print action_name, " ", value_data
	if action_name == "add":
		save_file(value_data)
	elif action_name == "list":
		list_all_notes()
	elif action_name == "recent":
		show_recent_note()


def save_file(value):
	now = datetime.datetime.now()
	filename = "{0}/new_{1}".format(NOTES_DIRECTORY, now.strftime("%Y-%m-%d-%H-%M-%S"))
	target = open (filename, 'w')
	target.write("Note created at: {0}\n".format(now.strftime("%Y-%m-%d %H:%M:%S")))
	target.write("--------\n")
	target.write(value)
	target.close()

def read_file(f):
	f = open(f, 'r')
	print f.read()
	f.close()

def get_directory_files(directory_name):
	entries = [os.path.join(directory_name, fn) for fn in os.listdir(directory_name)]
	return entries

def list_all_notes():
	files = get_directory_files(NOTES_DIRECTORY)
	for f in files:
		print ""
		read_file(f)
			

def show_recent_note():
	files = sorted(get_directory_files(NOTES_DIRECTORY), key=os.path.getmtime, reverse=True)
	if files:
		read_file(files[0])
	


if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		main(sys.argv[1],sys.argv[2])



