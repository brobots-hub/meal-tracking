# #brobots school meal tracking

This is a system running on Raspberry Pi that helps to record at what exact time each student has taken. It uses personal RFID tags as user identifiers.

## Hardware

- Raspberry Pi 3B+
- RDM6300 RFID Reader - _125kHz_
- RFID wrist tags - _125kHz_

## Software

- **Python** as main project language
- **Google Sheets API** as data storage
  - I'd personally use **MySQL** for these purposes, but all school data is stored in **Google Sheets API** - [@andrewyazura](https://github.com/andrewyazura)
- **RDM6300** sensor library

## Setup

### Environment variables

- `ENVIRONMENT`
  - `DEVELOPMENT` - app will use `.env.dev`
  - `PRODUCTION` - app will use `.env`

### Configuration and authentication

1. Create a new Google Cloud Platform (or use an existing one) project. Enable **Google Sheets API** and create a service account for this device. Read this manual on how to get it: [Creating a service account](https://developers.google.com/identity/protocols/oauth2/service-account#python). Next, download a `JSON` key for that service account.
1. Create a Google Sheets document where your data will be stored.
   - Give your service account access to the document. Just copy email address of service
1. Insert data into `.env` file
   - Copy example from `.env.example`
   - Set `DOCUMENT_ID` to ID of a document you created
   - Set `SERVICE_ACCOUNT` to a path to `JSON` key you downloaded

#### How to get `service-account.json`

Follow this steps:

- Go to _Credentials_ tab
- Open _Manage service accounts_ link
  - It's located near _Service Accounts_ list
- Find the service account you need.
- Press _Actions_ button (three dots) and choose `Create key`
- Choose `JSON` and press `Create`

### Google Sheets document setup

Copy this example: [link](https://docs.google.com/spreadsheets/d/1PVWsVY0DHWhr39p7M89DaQVEtYfha_SqDXLo_IbTrdw/edit?usp=sharing).

If for some reason the link isn't working, here is how table looks:

| IDs | Users |     | Records             |                     |
| --- | ----- | --- | ------------------- | ------------------- |
| 1   | user1 | --- | 1970/01/01 00:00:00 |                     |
| 2   | user2 | --- | 1970/01/01 00:00:00 | 1970/01/01 00:00:00 |
| 3   | user3 | --- |                     |                     |
| 4   | user4 | --- | 1970/01/01 00:00:00 |                     |

New records are appended into user's row. Record only has date and time of the request.

## Raspberry Pi setup

If following instructions don't work, try using this tutorial: [link](https://www.circuits.dk/setup-raspberry-pi-3-gpio-uart/).

### Serial

Run `sudo raspi-config`. Select `Interfacing Options / Serial` then disable `Serial console` and enable `Serial hardware`. Now use `/dev/serial0` in any code which accesses the Serial Port.

### UART

You need to enable UART, as it's the way Raspberry Pi and RFID sensor will be connected.

Run `sudo nano /boot/config.txt`. At the end of the file append `enable_uart=1` and reboot.

### System Service Unit

You can use `mealtracker.service` that is provided in the repostitory or write your own unit. If you're using the existing one, you have to:

1. Enter path to your project in specified placed
1. Enter name of the user you're going to use
   - On the Raspberry Pi it's most probably `pi` user.
1. Copy the unit file to `/etc/systemd/system/`

Now the service is accessible over `sudo systemctl` command.

#### Usage

`sudo systemctl start mealtracker.service` - start the service

`sudo systemctl stop mealtracker.service` - stop the service

`sudo systemctl status mealtracker.service` - check status of the service

#### Custom Service

Here is a link to official Raspberry Pi documentation on writing services: [link](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)
