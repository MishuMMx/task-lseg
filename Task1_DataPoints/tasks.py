from robocorp.tasks import task
from SelectFolder import select_folder
from SearchFiles import search_files
from ShowMessage import show_popup_msg

@task

def main():
    """Get the list of files"""
    message = "Get the list of files"
    
    selected_folder = select_folder()

    if selected_folder:
        print(f"Selected folder: {selected_folder}")
        file_list = search_files(selected_folder)
        print(file_list)
        show_popup_msg("Found + {str(file_list.count)} files")

    else:
        msg = "No folder selected."
        print(msg)
        show_popup_msg(msg)



