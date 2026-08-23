from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
QVBoxLayout, QWidget, QFileDialog)
from func import watermark_it
import sys


class WatermarkApp(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
    self.file_path = None

  def open_hell_gate(self):
    file_path, _ = QFileDialog.getOpenFileName(
      self,
      "Choose image",
      "",
      "Images (*.png *.jpg *.jpeg);;All files (*.*)",
    )
    if file_path:
      self.file_path = file_path

  def initUI(self):
    # Set main window
    self.setWindowTitle("Watermark App")
    self.resize(400, 200)
    # Main vertical layout for main window
    main_layout = QVBoxLayout()
    # Label on top
    self.label = QLabel("Choose file and put watermark on it.", self)
    main_layout.addWidget(self.label)
    # Buttons layout
    buttons_layout = QHBoxLayout()
    btn_load = QPushButton("Load File", self)
    btn_watermark = QPushButton("Generate watermark", self)
    btn_exit = QPushButton("Exit", self)
    # Actions
    btn_exit.clicked.connect(self.close)
    btn_load.clicked.connect(self.open_hell_gate)
    btn_watermark.clicked.connect(lambda: watermark_it(self.file_path))
    # Vertical layout buttons
    buttons_layout.addWidget(btn_load)
    buttons_layout.addWidget(btn_watermark)
    buttons_layout.addWidget(btn_exit)
    main_layout.addLayout(buttons_layout)
    # Set window main layout
    self.setLayout(main_layout)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  ex = WatermarkApp()
  ex.show()
  sys.exit(app.exec())