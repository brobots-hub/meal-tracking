# #brobots school meal tracking

This a system running on Raspberry Pi that helps to identify what meals each student has taken. It uses personal RFID tags as student identifiers.

## Hardware

- Raspberry Pi 3B+
- RDM6300 RFID Reader - _125kHz_
- RFID wrist tags - _125kHz_

## Software

- **Python** as main project language
- **Google Sheets API** as data storage
  - I'd personally use **MySQL** for these purposes, but all school data is stored in **Google Sheets API** - [@andrewyazura](https://github.com/andrewyazura)
