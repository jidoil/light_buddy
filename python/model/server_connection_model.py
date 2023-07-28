from collections import OrderedDict
import gazu
from PySide2.QtCore import QObject, Signal
from validations.properties import ValidateID


class ServerConnectionModel(QObject):
    server_statsChanged = Signal(list)
    login_dataChanged = Signal(dict)

    def __init__(self):
        super().__init__()
        self.server_stats = []
        self._id = ValidateID()
        self._password = None

    def arrange_project_status(self, projects: list) -> None:
        if projects:
            for project in projects:
                data_for_server_view_table = OrderedDict()
                data_for_server_view_table["name"] = project["name"]
                data_for_server_view_table["assets"] = len(gazu.asset.all_assets_for_project(project))
                # shot
                data_for_server_view_table["shots"] = len(gazu.shot.all_shots_for_project(project))
                # seq
                data_for_server_view_table["sequences"] = len(gazu.shot.all_sequences_for_project(project))
                data_for_server_view_table["artists"] = len(project["team"])
                data_for_server_view_table["end_date"] = project['end_date']
                self.server_stats.append(data_for_server_view_table)

        self.server_statsChanged.emit(self.server_stats)