# Download Manager with Python and ttkbootstrap

This is a simple **Download Manager** application built with Python, using the **`requests`** library for handling downloads and **`ttkbootstrap`** for creating a modern, user-friendly GUI.

## Features
- **User Interface**: A clean interface for entering the URL of the file to download.
- **Multithreading**: Downloads run on a separate thread to keep the application responsive.
- **Success Notification**: A message box appears after the download is completed.
- **File Storage**: Saves the downloaded file as `Sematec.mp4` in the `C:\Users\ASUS\Downloads` directory (can be modified as needed).

## How It Works
1. Enter the URL of the file you want to download in the provided text box.
2. Click the "Download" button to start the download.
3. The application downloads the file in the background, ensuring the UI remains responsive.
4. Once the download is complete, a success message is displayed.

## Prerequisites
- Python 3.7 or higher
- Install the required dependencies with:
  ```bash
  pip install requests ttkbootstrap
