#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Ji Doil"
__credits__ = ["Ji Doil"]
__lisence__ = "BSD"
__maintainer__ = "Ji Doil"
__email__ = "dotteda@gmail.com"
__status__ = "Development"
__version__ = "0.0.1"

import gazu

from model.server_connection_model import *
from controllers.server_view_controller import ServerConnetionController
from validations.properties import *
from view.server_connection_view_module.server_connection_view import ServerConnectionView

class KiyaAPI:
    _address = ValidateURL()
    _id = ValidateID()
    _password = None  # TODO:
    project = ValidateProject()
    _assets = []
    _asset_types = []

    def __init__(self,
                 address: str = "https://9543-1-11-90-40.ngrok-free.app/api",  # 주의: ngrok 리셋마다 주소가 바뀜
                 id: str = "admin@netflixacademy.com",
                 password: str = "netflixacademy"
        ):
        self._address = address
        self._id = id
        self._password = password

        gazu.set_host(self._address)
        self.gazu = gazu.log_in(self._id, self._password)
        self.server_connection_controller = ServerConnetionController()
        self.server_connection_controller.server_connection_model.arrange_project_status(self.get_all_open_projects())

    def print_all_assets(self) -> list:
        all_asset_list = gazu.asset.all_assets_for_project(self.project)
        if all_asset_list:
            for asset in all_asset_list:
                print(f'{asset["name"]}, shotgun_id: {asset["shotgun_id"]}')
        else:
            print("프로젝트가 없습니다.")
        return all_asset_list

    def load_current_project_stats_on_view(self):
        projects = gazu.project.all_open_projects()

    def print_all_open_projects(self) -> None:
        all_open_project = gazu.project.all_open_projects()
        if all_open_project:
            print("현재 열려있는 프로젝트는 다음과 같습니다.")
            for projects in all_open_project:
                print(f'{projects["name"]}, shotgun_id: {projects["shotgun_id"]}')
        else:
            print("현재 열려있는 프로젝트가 없습니다.")

    def get_all_open_projects(self) -> list:
        all_open_project = gazu.project.all_open_projects()
        return all_open_project

    def choose_project_by_name(self, project_name: str) -> None:
        try:
            project = gazu.project.get_project_by_name(project_name)
            if project:
                self.project = project
                print(f'{project_name}를 선택하였습니다.')
            else:
                print(f'{project_name} 존재하지 않습니다.')
        except Exception as ex:
            print(f'{repr(ex)}')

    def get_all_assets(self) -> list:
        if self.project:
            self._assets = gazu.asset.all_assets_for_project(self.project)
            print(f'Total assets in project "{self.project["name"]}", is [{len(self.assets)}]')
            for asset in self.assets:
                print(f'{asset["name"]}, {asset["description"]}, {asset["status"]}')
        else:
            print("Empty project. choose project first")
        return list(self._assets)

    def get_all_asset_types(self) -> None:
        if self.project:
            asset_types = gazu.asset.all_asset_types_for_project(self.project)
            if asset_types and isinstance(asset_types, list) and (len(asset_types) > 0):
                for asset_type in asset_types:
                    print(asset_type['name'])
            else:
                print("asset_type이 없습니다.")

    def print_all_asset_types_in_current_proejct(self) -> None:
        if self._asset_types:
            for asset_type in self._asset_types:
                print(f'{asset_type["name"]}')
        else:
            print(f'{self.project}에 asset types이 존재하지 않습니다.')

    def print_current_tasks_todo(self) -> None:
        try:
            tasks_todo = gazu.user.all_tasks_to_do()
            if tasks_todo:
                for task in tasks_todo:
                    print(
                        f'{task["task_status_name"]}: -{task["entity_type_name"]}- "{task["entity_name"]}", [{task["task_type_for_entity"]}]')
            else:
                print("you have no task to do")
        except ValueError as ex:
            print(f'{repr(ex)}, tasks 가져오는 것에 실패하였습니다.')

    def get_asset_type_by_name(self, name: str) -> dict:
        if not isinstance(name, str):
            raise ValueError("worng type")
        if not self.project:
            raise ValueError("no project")
        asset_type = gazu.asset.get_asset_type_by_name(self.project, name)
        if asset_type and isinstance(asset_type, dict):
            print(f'{asset_type["name"]} OK')
            return asset_type


    # TODO: CRUD - ASSET
    # TODO: Post Preview
    # TODO: Posst Comment
    # TODO: Change Task Status
    # TODO: CRUD - SHOT
    # TODO: CRUD - SEQUENCE