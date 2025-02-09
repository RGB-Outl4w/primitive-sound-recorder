import sys
from PyQt5.QtWidgets import QApplication
from gui import SoundRecorderApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SoundRecorderApp()
    window.show()
    sys.exit(app.exec_())