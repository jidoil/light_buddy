import os
import gazu


class FileTree:

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

    def initialize_selected_files_file_tree(self, project, selected_tasks):
        for task in selected_tasks:
            path = os.path.dirname(gazu.files.build_working_file_path(task))[1:]
            if os.path.exists(path):
                print(f"{path} already exists!")
                continue
            else:
                path = os.path.dirname(
                    gazu.files.build_working_file_path(task))[1:]
                if os.path.exists(path):
                    print(f"deleting useless path: {path} ")
                    os.rmdir(path)
            os.makedirs(path)

        for shot in gazu.shot.all_shots_for_project(project):
            for task in gazu.task.all_tasks_for_shot(shot):
                path = os.path.dirname(
                gazu.files.build_working_file_path(task))[1:]
                if os.path.exists(path):
                    print(f"{path} already exists!")
                    continue
            else:
                path = os.path.dirname(
                gazu.files.build_working_file_path(task))[1:]
                if os.path.exists(path):
                    print(f"deleting useless path: {path} ")
                    os.rmdir(path)
            os.makedirs(path)