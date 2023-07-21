import gazu
from view.server_connection_view_module.server_connection_view import ServerConnectionView
from model.server_connection_model import ServerConnectionModel

from model.tasks_model import TasksModel
from validations.properties import ValidateID


class ServerConnetionController:
    gz = None
    _address = "https://9543-1-11-90-40.ngrok-free.app/api"
    _id = ValidateID()
    _password = None
    res = None
    def __init__(self):
        self.server_connection_model = ServerConnectionModel()
        self.server_connection_view = ServerConnectionView()  # 현재 열려있는 프로젝트와 에셋,샷 그리고 활동중인 아티스트의 수를 보여줍니다.
        self.server_connection_view.show()
        self.server_connection_model.server_statsChanged.connect(self.update_table)
        self.server_connection_view.id_and_passwordRecieved.connect(self.log_in_to_project)
        self.server_connection_view.isLoggedIn.connect(self.log_in_controll)


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
            print("login: ", self.gz["login"])

### 마테리얼 어셋을보는게 좋다. 모델링이 끝나면 리깅, 룩뎁팀의 작업이간다., 룩뎁이 동시에 리깅이 되는
### 카메라 해상도, 렌더, 프레임레인지, 렌더픽스 aov에 관련된거
    ### 아웃풋 어디에 뽑을건지 자동화되면좋다.
    ### 렌더가 걸릴거고 시작하는 동시에 약속된 데이터가 취합이 될거고..
    ### 어디 옵션, 체크, 바꿔줘야할것들 세팅...
    ### 라이팅이끝나면 컴프팀으로 간다 프리컴프를 하면 결과물 ,패스들을 취합해서 실제플레이트에 올려서 합성
    ### Ok된걸 컴프팀으로.. 합성이된 nukefile이 컴프팀으로 전달된다.
    ### 컴프파일까지...되면 좋다. 턴테이블 돌리던지, 필요한 렌더패스들, 기본적으로 렌더에서 제공하는 패스들을 뽑아서
    ### 누크파일에 자동으로 세팅이되서 켜져서
### 실행을 했을때 누크, 라이팅 뽑는 패스는 같다. 연결된 노드 구조가 있는데 이걸 자동화...
### 데이터, 버전이 다를때 어떻게 할건지
### 보통은 인터넷은 버전이 하나라서
### 마야에선 레퍼런스로 끌어감
    ### 현재버전이랑 업데이트랑 버전이 다를때 어떻게 처리할것인지?


    def gazu_init(self):
        self.person = gazu.person.get_person(self.res["user"]["id"])
        self.tasks = gazu.task.all_tasks_for_person(self.person)
        self.tasks_names = []
        self.projects = gazu.project.all_open_projects()
        # self.sequences = self.gz.shot.all_sequences_for_project(project)
        self.server_connection_view.sync_assets(self.tasks)
    def log_in_controll(self, data):
        if not data:
            self.server_connection_view.regenerate_log_in_form()
            self.gz = None
            print("log out suceeded!")
    def auth_login(self, login_form_data: dict) -> None:
        self.server_connection_model.auth_login(login_form_data)

    def update_table(self, server_stats):
        self.server_connection_view.add_row(server_stats)

    def get_tasks(self):
        self.tasks_model = TasksModel("dummy data", "dummy_header")