import sys
import io
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QRadioButton, QComboBox, QCheckBox, QPushButton, QGridLayout
from PyQt6.QtGui import QIntValidator, QValidator, QDoubleValidator
class Formularz(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Pole imienia z walidatorem liter
        self.label_imie = QLabel("Imię:")
        self.input_imie = QLineEdit(self)
        imie_validator = TextValidator(self)  # Użyj niestandardowego walidatora
        self.input_imie.setValidator(imie_validator)
        layout.addWidget(self.label_imie)
        layout.addWidget(self.input_imie)

        # Pole nazwiska z walidatorem liter
        self.label_nazwisko = QLabel("Nazwisko:")
        self.input_nazwisko = QLineEdit(self)
        nazwisko_validator = TextValidator(self)  # Użyj niestandardowego walidatora
        self.input_nazwisko.setValidator(nazwisko_validator)
        layout.addWidget(self.label_nazwisko)
        layout.addWidget(self.input_nazwisko)

        # Pole PESEL z walidatorem cyfr
        self.label_pesel = QLabel("PESEL:")
        self.input_pesel = QLineEdit(self)
        pesel_validator = QDoubleValidator(self)
        self.input_pesel.setValidator(pesel_validator)
        self.input_pesel.setMaxLength(11)
        layout.addWidget(self.label_pesel)
        layout.addWidget(self.input_pesel)

        # Pola kodu pocztowego z walidatorem cyfr
        self.label_kod_pocztowy = QLabel("Kod pocztowy:")
        self.input_kod_pocztowy1 = QLineEdit(self)
        self.input_kod_pocztowy2 = QLineEdit(self)
        kod_pocztowy_validator = QIntValidator(self)
        self.input_kod_pocztowy1.setValidator(kod_pocztowy_validator)
        self.input_kod_pocztowy2.setValidator(kod_pocztowy_validator)
        self.input_kod_pocztowy1.setMaxLength(2)
        self.input_kod_pocztowy2.setMaxLength(3)
        self.input_kod_pocztowy1.textChanged.connect(self.sprawdz_kod_pocztowy)
        self.input_kod_pocztowy2.textChanged.connect(self.sprawdz_kod_pocztowy)
        kod_pocztowy_layout = QHBoxLayout()
        kod_pocztowy_layout.addWidget(self.input_kod_pocztowy1)
        kod_pocztowy_layout.addWidget(QLabel("-"))
        kod_pocztowy_layout.addWidget(self.input_kod_pocztowy2)
        layout.addWidget(self.label_kod_pocztowy)
        layout.addLayout(kod_pocztowy_layout)

        # Pole płci (radio buttons)
        self.label_plec = QLabel("Płeć:")
        self.radio_kobieta = QRadioButton("Kobieta")
        self.radio_mezczyzna = QRadioButton("Mężczyzna")
        layout.addWidget(self.label_plec)
        layout.addWidget(self.radio_kobieta)
        layout.addWidget(self.radio_mezczyzna)

        # Lista rozwijana z województwami
        self.label_wojewodztwo = QLabel("Wybierz województwo:")
        self.combobox_wojewodztwo = QComboBox()
        wojewodztwa = ["Dolnośląskie", "Kujawsko-Pomorskie", "Lubelskie", "Łódzkie", "Małopolskie", "Mazowieckie", "Opolskie", "Podkarpackie", "Podlaskie", "Pomorskie", "Śląskie", "Świętokrzyskie", "Warmińsko-Mazurskie", "Wielkopolskie", "Zachodniopomorskie"]
        self.combobox_wojewodztwo.addItems(wojewodztwa)
        layout.addWidget(self.label_wojewodztwo)
        layout.addWidget(self.combobox_wojewodztwo)

        # Pola wyboru zainteresowań w dwóch kolumnach
        self.label_zainteresowania = QLabel("Zainteresowania:")
        self.zainteresowania_checkboxes = []

        zainteresowania_layout = QGridLayout()
        zainteresowania = [
    "Zainteresowanie 1",
    "Zainteresowanie 2",
    "Zainteresowanie 3",
    "Zainteresowanie 4",
    "Zainteresowanie 5",
    "Zainteresowanie 6",
    "Zainteresowanie 7",
    "Zainteresowanie 8"
]

        for row, zainteresowanie in enumerate(zainteresowania):
            checkbox = QCheckBox(zainteresowanie)
            self.zainteresowania_checkboxes.append(checkbox)
            zainteresowania_layout.addWidget(checkbox, row // 2, row % 2)

        layout.addWidget(self.label_zainteresowania)
        layout.addLayout(zainteresowania_layout)

        # Przyciski "Wyczyść" i "Wyślij"
        button_layout = QHBoxLayout()
        self.button_wyczysc = QPushButton("Wyczyść", self)
        self.button_wyczysc.clicked.connect(self.wyczysc_formularz)
        self.button_wyslij = QPushButton("Wyślij", self)
        self.button_wyslij.clicked.connect(self.zapisz_do_pliku)
        button_layout.addWidget(self.button_wyczysc)
        button_layout.addWidget(self.button_wyslij)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.setWindowTitle("Formularz Elektroniczny")

    def wyczysc_formularz(self):
        # Czyszczenie pól formularza
        self.input_imie.clear()
        self.input_nazwisko.clear()
        self.input_pesel.clear()
        self.input_kod_pocztowy1.clear()
        self.input_kod_pocztowy2.clear()
        self.radio_kobieta.setChecked(False)
        self.radio_mezczyzna.setChecked(False)
        self.combobox_wojewodztwo.setCurrentIndex(0)
        for checkbox in self.zainteresowania_checkboxes:
            checkbox.setChecked(False)

    def zapisz_do_pliku(self):
        # Zapis danych do pliku
        imie = self.input_imie.text()
        nazwisko = self.input_nazwisko.text()
        pesel = self.input_pesel.text()
        kod_pocztowy1 = self.input_kod_pocztowy1.text()
        kod_pocztowy2 = self.input_kod_pocztowy2.text()
        plec = "Kobieta" if self.radio_kobieta.isChecked() else "Mężczyzna"
        wojewodztwo = self.combobox_wojewodztwo.currentText()

        zainteresowania = []
        for checkbox in self.zainteresowania_checkboxes:
            if checkbox.isChecked():
                zainteresowania.append(checkbox.text())

        dane = f"Imię: {imie}\nNazwisko: {nazwisko}\nPESEL: {pesel}\nKod pocztowy: {kod_pocztowy1}-{kod_pocztowy2}\nPłeć: {plec}\nWojewództwo: {wojewodztwo}\nZainteresowania: {zainteresowania}\n"

        # Zapisz dane do pliku
        with io.open("dane_formularza.txt", "w", encoding="utf-8") as file:
            file.write(dane)

    def sprawdz_kod_pocztowy(self):
        # Usuń znak "-" z pól kodu pocztowego
        self.input_kod_pocztowy1.setText(self.input_kod_pocztowy1.text().replace("-", ""))
        self.input_kod_pocztowy2.setText(self.input_kod_pocztowy2.text().replace("-", ""))

class TextValidator(QValidator):
    def validate(self, input_text, pos):
        # Walidacja tekstu: tylko litery
        if input_text.isalpha() or input_text == "":
            return (QValidator.State.Acceptable, input_text, pos)
        else:
            return (QValidator.State.Invalid, input_text, pos)

def main():
    app = QApplication(sys.argv)
    formularz = Formularz()
    formularz.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
