import requests
import json

response = requests.get(
    "https://cas.reg.chula.ac.th/class/api/course-studies/course-header?studyprogramsystem=S&acadyear=2026&semester=1&courseid=2301173-2023-1",
    verify=False,
)
response_data = json.loads(response.text)["data"]

file_write = open("subjectdetails.json", "w")
json.dump(response_data, file_write)
file_write.close()
