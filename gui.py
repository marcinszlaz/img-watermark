import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget


class WatermarkApp(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    # Ustawienia głównego okna
    self.setWindowTitle("Watermark App")
    self.resize(400, 200)

    # Główny układ pionowy dla całego okna
    main_layout = QVBoxLayout()

    # Etekista na górze
    self.label = QLabel("Wybierz plik i nałóż watermark", self)
    main_layout.addWidget(self.label)

    # Układ poziomy na przyciski na dole
    buttons_layout = QHBoxLayout()

    btn_load = QPushButton("Wczytaj", self)
    btn_watermark = QPushButton("Wygeneruj", self)
    btn_exit = QPushButton("Wyjdź", self)

    # Podpinamy akcje (przykład)
    btn_exit.clicked.connect(self.close)

    # Dodajemy przyciski do układu poziomego
    buttons_layout.addWidget(btn_load)
    buttons_layout.addWidget(btn_watermark)
    buttons_layout.addWidget(btn_exit)

    # Dodajemy układ poziom do głównego układu pionowego
    main_layout.addLayout(buttons_layout)

    # Ustawiamy główny layout dla okna
    self.setLayout(main_layout)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  ex = WatermarkApp()
  ex.show()
  sys.exit(app.exec())