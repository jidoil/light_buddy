from model.server_connection_model import ServerConnectionModel
from view.server_connection_view_module.server_connection_view import ServerConnectionView


class ServerConnetionController:
    def __init__(self, gazu):
        self.gazu = gazu
        self.server_connection_model = ServerConnectionModel()
        self.server_connection_view = ServerConnectionView()  # 현재 열려있는 프로젝트와 에셋,샷 그리고 활동중인 아티스트의 수를 보여줍니다.
        self.server_connection_view.show()
        self.server_connection_model.server_statsChanged.connect(self.update_table)
        self.server_connection_view.id_and_passwordRecieved.connect(self.auth_login)
        self.server_connection_model.login_dataChanged.connect(self.log_in_to_project)


    def log_in_to_project(self, valid_login_data: dict) -> None:
        try:
            res = gazu.log_in(valid_login_data["id"], valid_login_data["password"])
            print(f'login: {res["login"]}')
        except Exception as ex:
            print(f'{repr(ex)}, exception occured')
        if res:
            self.server_connection_view.log_in_succeed()


    def auth_login(self, login_form_data: dict) -> None:
        self.server_connection_model.auth_login(login_form_data)


    def update_table(self, server_stats):
        self.server_connection_view.add_row(server_stats)
