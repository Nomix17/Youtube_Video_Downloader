# Youtube_Video_Downloader
This Python script allows users to download YouTube videos. It provides an interactive command-line interface for users to input the desired video URL and select the video resolution for download.
## Features
- Download videos directly from YouTube via URL.

- Choose the resolution of the video to download.

- Automatically saves videos to a specified download folder.

- User-friendly command-line interface.

## Prerequisites
Before running this script, ensure you have the following installed:

- Python 3.x

- yt_dlp

- pytube 

- Requests

## Installation
- Clone this repository to your local machine using:

      git clone https://github.com/pa1n-sama/Youtube_Video_Downloader

- Navigate into the project directory:

      cd your-repository-name

- Install the required Python packages:

      pip install -r requirements.txt

## Configuration
On the first run, the script will ask for the path of the download folder where you want to save the videos. This path will be saved and reused in subsequent executions. To change the download folder, manually edit the YVD_download_path.txt file.
