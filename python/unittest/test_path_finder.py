import os
import pytest

from gazu_api.vfx_pipeline_api.vfx_pipeline_api.utils.path_finder \
import get_upper_path, \
    get_upper_path_to_make_file_path, find_project_root_path, \
    find_images_path, get_all_files_in_directory, \
    print_all_files_in_images_directory

test_directory = os.path.dirname(os.path.abspath(__file__))
test_root_path = os.path.dirname(test_directory)
test_images_path = os.path.join(test_root_path, 'images')
test_files = ['Character_John_Wick.jpg']

def test_get_upper_path():
    os.chdir('C:\\Users\\dotte')
    assert get_upper_path() == 'C:\\Users'
    os.chdir('C:\\Users\\dotte\\Documents')
    assert get_upper_path() == 'C:\\Users\\dotte'


def test_get_upper_path_to_make_file_path():
    os.chdir('C:\\Users\\dotte')
    assert get_upper_path_to_make_file_path('file.txt') == 'C:\\Users\\file.txt'
    os.chdir('C:\\Users\\dotte\\Documents')
    assert get_upper_path_to_make_file_path('file.txt') == \
                                            'C:\\Users\\dotte\\file.txt'

def test_find_project_root_path():
    assert find_project_root_path() == test_root_path

def test_find_images_path():
    assert find_images_path(test_root_path) == test_images_path

def test_get_all_files_in_directory():
    assert get_all_files_in_directory(test_images_path) == ['Character_John_Wick.jpg']

def test_print_all_files_in_images_directory(capsys):
    print_all_files_in_images_directory()
    captured = capsys.readouterr()
    assert captured.out.strip().split('\n') == test_files


pytest.main()
