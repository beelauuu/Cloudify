import os
import time

path = "static/img"
current_time = time.time()

for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    if os.path.isfile(file_path):
        file_stats = os.stat(file_path)
        last_modified_time = file_stats.st_mtime
        if current_time - last_modified_time > 900:
            if "wordcloud" in file_name and os.path.splitext(file_name)[1] == ".png":
                os.remove(file_path)
