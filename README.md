# #brobots school meal tracking

This is a system running on Raspberry Pi that helps to identify what meals each student has taken. It uses personal RFID tags as user identifiers.

## Hardware

- Raspberry Pi 3B+
- RDM6300 RFID Reader - _125kHz_
- RFID wrist tags - _125kHz_

## Software

- **Python** as main project language
- **Google Sheets API** as data storage
  - I'd personally use **MySQL** for these purposes, but all school data is stored in **Google Sheets API** - [@andrewyazura](https://github.com/andrewyazura)

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

Still working on that...
