import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from recorder import AudioRecorder
from utils import get_default_audio_file_path, resource_path

class SoundRecorderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RGB.DEV | Primitive Sound Recorder")
        app_icon = QIcon(resource_path("assets/icon.ico"))
        self.setWindowIcon(app_icon)

        if sys.platform == "win32":
            import ctypes
            myappid = 'rgb.dev.primitivesoundrecorder.app'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
        self.resize(400, 200)

        # Initialize components
        self.init_ui()
        self.recorder = AudioRecorder()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Labels
        self.status_label = QLabel("Ready to record...")
        layout.addWidget(self.status_label)

        # Buttons
        self.record_button = QPushButton("Start Recording")
        self.record_button.clicked.connect(self.toggle_recording)
        layout.addWidget(self.record_button)

        self.save_button = QPushButton("Save Recording")
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_recording)
        layout.addWidget(self.save_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def toggle_recording(self):
        if not self.recorder.is_recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.recorder.start_recording()
        self.status_label.setText("Recording...")
        self.record_button.setText("Stop Recording")
        self.save_button.setEnabled(False)

    def stop_recording(self):
        self.recorder.stop_recording()
        self.status_label.setText("Recording stopped.")
        self.record_button.setText("Start Recording")
        self.save_button.setEnabled(True)

    def save_recording(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Recording", get_default_audio_file_path(), "WAV Files (*.wav)", options=options
        )
        if file_path:
            try:
                self.recorder.save_recording(file_path)
                QMessageBox.information(self, "Success", "Recording saved successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save recording: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SoundRecorderApp()
    window.show()
    sys.exit(app.exec_())