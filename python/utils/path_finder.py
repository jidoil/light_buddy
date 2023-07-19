import os


def get_current_path():
    return os.getcwd()


def get_upper_path() -> str:
    current_dir = get_current_path()
    seperators_indexes = [ index for index, character in enumerate(current_dir) if current_dir[index] == '\\' or current_dir[index] == '/']
    last_seperators_index = max(seperators_indexes)
    upper_path = current_dir[0:last_seperators_index]
    print(f'current working directory: {current_dir}, upper path: {upper_path}')
    return upper_path


def get_upper_path_to_make_file_path(filename: str) -> str:
    file_path = os.path.join(get_upper_path(), filename)
    return file_path


def find_project_root_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    return project_dir


def find_images_path(rootpath) -> str:
    for root, dirs, files in os.walk(rootpath):
        if 'images' in dirs:
            images_path = os.path.join(root, 'images')
            return images_path

    for subdir in dirs:
        subdir_path = os.path.join(root, subdir)
        result = find_images_path(subdir_path)
        if result:
            return result

    return None


def get_all_files_in_directory(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(file)
    return  file_list


def print_all_files_in_images_directory():
    files = get_all_files_in_directory(find_images_path(find_project_root_path()))
    for file in files:
        print(file)
