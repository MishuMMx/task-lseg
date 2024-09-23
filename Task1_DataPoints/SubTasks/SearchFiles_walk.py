import os
csv_files = []

def search_files(listed_folder):
    for root, dirs, files in os.walk(listed_folder):
        found_file = None
        file_stats = None
        for file in files:
            file_stats = os.stat(file)
            if file.endswith(".csv") and int(os.stat(file_stats.st_size)) != 0:
                found_file = os.path.join(root, file)
                print(found_file)
                csv_files.append(found_file)
            else:
                pass

    return csv_files

        