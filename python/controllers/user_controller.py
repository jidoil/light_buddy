
class ServerConnectionController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # Connect signals and slots
        self.view.connect_button.clicked.connect(self.connect_button_clicked)
        self.view.disconnect_button.clicked.connect(self.disconnect_button_clicked)

        # Connect model signals to controller slots
        self.model.connected.connect(self.server_connected)
        self.model.disconnected.connect(self.server_disconnected)

    def connect_button_clicked(self):
        # Handle the connect button click event
        self.model.connect_to_server()

    def disconnect_button_clicked(self):
        # Handle the disconnect button click event
        self.model.disconnect_from_server()

    def server_connected(self):
        # Handle the server connected event
        print("Server connected")

    def server_disconnected(self):
        # Handle the server disconnected event
        print("Server disconnected")
