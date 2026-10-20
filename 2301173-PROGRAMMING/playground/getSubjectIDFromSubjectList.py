import json

file_read = open("subjectlist.json", "r")

subject_list = json.load(file_read)
subject_ids = []

for i in range(len(subject_list)):
  subject_ids.append(subject_list[i]["id"])

file_write = open("subjectids.json", "w")
json.dump(subject_ids, file_write)
file_write.close()

file_read.close()