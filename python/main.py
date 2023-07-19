import sys

from PySide2 import QtWidgets

from kiya_api import KiyaAPI

def main():
"""
rez_env_command = 'rez-env vfx_pipeline_api -- python /home/rapa/maya/projects/ghost_busters_box/scripts/vfx_pipeline_api/python/main.py'
subprocess.call(rez_env_command, shell=True)
"""

    app = QtWidgets.QApplication(sys.argv)
    gz = KiyaAPI()
    gz.print_all_open_projects()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

