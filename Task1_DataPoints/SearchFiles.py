import os, glob
csv_files = []

def search_files(selected_folder):
    os.chdir(selected_folder)
    for file_path in glob.glob(selected_folder+"/**/*", recursive=True):
        print(file_path)
        if str.lower(file_path).endswith(".csv"):
            file_stats = os.stat(file_path)
            file_size = int(file_stats.st_size)
            if file_size != 0:
                print(f"Adding file to list: {file_path}")
                csv_files.append(file_path)

    return csv_files

        