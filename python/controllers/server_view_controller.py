import gazu
from PySide2.QtCore import Qt
from view.server_connection_view_module.server_connection_view import ServerConnectionView
from validations.properties import ValidateID
from model.server_connection_model import ServerConnectionModel
from model.tasks_model import TasksModel
from model.selected_assets_model import SelectedAssetModel

from python.utils.file_tree import FileTree


class ServerConnetionController:
    gz = None
    _address = "https://9543-1-11-90-40.ngrok-free.app/api"
    _id = ValidateID()
    _password = None
    res = None
    tasks_model = None
    selected_asset_model = None
    selected_assets = set()
    assigned_shots = []
    tasks_names = []

    def __init__(self):
        self.server_connection_model = ServerConnectionModel()
        self.server_connection_view = ServerConnectionView()  # 현재 열려있는 프로젝트와 에셋,샷 그리고 활동중인 아티스트의 수를 보여줍니다.
        self.server_connection_view.show()
        self.server_connection_model.server_statsChanged.connect(self.update_table)
        self.server_connection_view.id_and_passwordRecieved.connect(self.log_in_to_project)
        self.server_connection_view.isLoggedIn.connect(self.log_in_controll)
        self.server_connection_view.sync_button_pushed.connect(self.sync_asset)
        self.server_connection_view.add_selected_asset_button_pushed.connect(self.add_selected_asset_to_import_list)
        self.server_connection_view.remove_selected_asset_button_pushed.connect(self.remove_selected_asset_from_import_list)
        self.server_connection_view.add_all_assets_button_pushed.connect(self.add_all_assigned_assets_to_import_list)
        self.server_connection_view.remove_all_assets_button_pushed.connect(self.remove_all_assets)
        self.server_connection_view.import_assets_button_pushed.connect(self.import_assets)

    def import_assets(self):
        print("import asset button clicked")
        if not self.selected_assets:
            print("you have no tasks to import")
            return

        self.selected_tasks = []
        for task in self.tasks:
            if "%s %s" % (task['entity_name'], task['sequence_name']) in self.selected_assets:
                print("%s %s" % (task['entity_name'], task['sequence_name']))
                self.selected_tasks.append(task)

        self.file_tree = FileTree()
        for project in self.projects:
            self.file_tree.initialize_selected_files_file_tree(project, self.selected_tasks)

    def remove_all_assets(self):
        if self.selected_assets:
            self.selected_assets = set()

        self.selected_asset_model.updateData(None, None)

    def add_all_assigned_assets_to_import_list(self):
        list_converted_assets = []

        model = self.server_connection_view.scene_asset_list_view.model()

        for row in range(model.rowCount()):
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data = index.data(Qt.DisplayRole)
                self.selected_assets.add(data)
        for asset in self.selected_assets:
            list_converted_assets.append([asset])

        header_data = ["선택한 에셋"]
        self.selected_asset_model.updateData(list_converted_assets, header_data)

    def add_selected_asset_to_import_list(self):
        list_converted_assets = []
        print("asset added to import list!")
        selected_indexes = self.server_connection_view.scene_asset_list_view.selectionModel().selectedIndexes()
        print(selected_indexes)
        for index in selected_indexes:
            row = index.row()
            column = index.column()
            data = index.data(Qt.DisplayRole)
            print(f"Row: {row}, Column: {column}, Data: {data}")
            self.selected_assets.add(data)

        for asset in self.selected_assets:
            list_converted_assets.append([asset])

        header_data = ["선택한 에셋"]
        print("selected assets: ", list_converted_assets)
        print("header_data: ", header_data)
        self.selected_asset_model.updateData(list_converted_assets, header_data)

    def remove_selected_asset_from_import_list(self):
        list_converted_assets = []
        print("asset removed from import list!")
        selected_indexes = self.server_connection_view.assets_to_import_list_view.selectionModel().selectedIndexes()
        print(selected_indexes)
        for index in selected_indexes:
            row = index.row()
            column = index.column()
            data = index.data(Qt.DisplayRole)
            print(f"Row: {row}, Column: {column}, Data: {data}")
            self.selected_assets.remove(data)

        for asset in self.selected_assets:
            list_converted_assets.pop([asset])

        header_data = ["선택한 에셋"]
        print("selected assets: ", list_converted_assets)
        print("header_data: ", header_data)
        self.selected_asset_model.updateData(list_converted_assets, header_data)

    def sync_asset(self, tasks: list = []) -> None:
        if self.assigned_shots:
            return
        if not tasks:
            print("no tasks")
            tasks = self.get_tasks()
            print("tasks: ", tasks)

        for task in tasks:
            if task["task_type_name"] == "Lighting":
                self.assigned_shots.append([task["sequence_name"] + " " + task["entity_name"]])
        header_data = ["에셋 이름"]

        if not self.tasks_model:
            self.tasks_model = TasksModel(self.assigned_shots, header_data)
            self.server_connection_view.scene_asset_list_view.setModel(self.tasks_model)
            self.selected_asset_model = SelectedAssetModel()
            self.server_connection_view.assets_to_import_list_view.setModel(self.selected_asset_model)
        else:
            self.tasks_model.updateData(self.assigned_shots, header_data)
        print("assigned shots: ", self.assigned_shots)
        print("as header_data: ", header_data)

    def log_in_to_project(self, valid_login_data: dict) -> None:
        self._id = valid_login_data["id"]
        self._password = valid_login_data["password"]
        try:
            gazu.set_host(self._address)
            self.res = gazu.log_in(self._id, self._password)
            print("res: ", self.res)
        except Exception as ex:
            print(f'repr{ex} log in error occured')
        if self.res["login"]:
            self.server_connection_view.log_in_succeed()
            self.gazu_init()
            self.get_tasks()
        else:
            print("login: false")

    def gazu_init(self) -> None:
        # self.person = gazu.person.get_person(self.res["user"]["id"])
        # self.tasks = gazu.task.all_tasks_for_person(self.person)
        tasks = self.get_tasks()
        self.sync_asset(tasks)
        self.projects = gazu.project.all_open_projects()

    def log_in_controll(self, is_logged_in : bool) -> None:
        if not is_logged_in:
            self.server_connection_view.regenerate_log_in_form()
            self.gz = None
            print("log out suceeded!")

    def update_table(self, server_stats) -> None:
        self.server_connection_view.add_row(server_stats)

    def get_tasks(self) -> list:
        self.person = gazu.person.get_person(self.res["user"]["id"])
        self.tasks = gazu.task.all_tasks_for_person(self.person)
        return self.tasks