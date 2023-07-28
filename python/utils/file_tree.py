import os
import gazu


class FileTree:
    def __init__(self, projects, file_tree_name):
        self.projects = projects
        self.file_tree_name = file_tree_name

    def initialize_full_file_tree_for_project(self, project):
        for asset in gazu.asset.all_assets_for_project(project):
            for task in gazu.task.all_tasks_for_asset(asset):
                path = os.path.dirname(
                    gazu.files.build_working_file_path(task))[1:]
                os.makedirs(path)
        for shot in gazu.shot.all_shots_for_project(project):
            for task in gazu.task.all_tasks_for_shot(shot):
                path = os.path.dirname(
                gazu.files.build_working_file_path(task))[1:]
                os.makedirs(path)
