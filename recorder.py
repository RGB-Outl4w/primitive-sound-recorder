import pyaudio
import wave
import threading

class AudioRecorder:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.frames = []
        self.is_recording = False
        self._audio_interface = pyaudio.PyAudio()
        self.stream = None

    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.stream = self._audio_interface.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.CHUNK
            )
            self.frames = []
            threading.Thread(target=self._record).start()

    def _record(self):
        while self.is_recording:
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.stream.stop_stream()
            self.stream.close()

    def save_recording(self, file_path):
        wf = wave.open(file_path, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self._audio_interface.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()