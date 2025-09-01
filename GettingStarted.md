# HOW TO SET UP THE 2025 SPECTRASOLIS DOWNLINK PARSER:

## Prerequisites

### 1: [Download](https://code.visualstudio.com/download) VS Code
If you feel comfortable using a different IDE, feel free, but note these instructions were created with VS Code in mind. Both the software and electrical teams use VS Code so there is no guarantee they can help with an IDE they're unfamiliar with.

### 2: [Download](https://www.python.org/downloads/) Python
If you don't already have Python downloaded, follow the instructions to download the latest version of Python for your OS.

### 3: Install [Requests](https://requests.readthedocs.io/en/latest/user/install/#install)
The easiest way to do this is to open your command terminal:
- For Windows: Press the Windows key and search 'pw' to open Powershell.
- For Mac: Press ctrl + space and search 'terminal' to open your terminal.

For both Windows and Mac, enter the command:
```
    pip install requests
```

### 4: Install [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup)
Open your command terminal as directed in the previous step.
Enter the command:
```
    pip install beautifulsoup4
```

### 5: Run the DownlinkParser.py script!
There are two methods of running this script I'd recommend:

1) Run directly from VS Code
    Open the DownlinkParser.py file in VS Code and press the small play button in the upper right corner of your screen.
    This will open a terminal in VS Code where you can see the downlink data being parsed.
    
2) Run from the command line
    If you're familiar with your terminal, I'd highly recommend running the code using this method. VS Code has a tendency to cut off the first couple hundred lines in its terminal and I've found it's easier to see ALL the data from Powershell or Terminal.

    First, open your terminal and navigate to the directory you stored the DownlinkParser.py file to. For example, if you saved the file to your HASP-25 folder, which is within your Projects folder, you'll want to navigate there.

    You'll use the command
    ```
    cd <Whichever-Folder-You-Want-To-Navigate-To>
    ```

    That may look something like:
    ```
    C:\Users\Breeze\> cd Projects
    C:\Users\Breeze\Projects> cd HASP-25
    ```

    Once you've navigated to the directory the script is in, you can run it!

    Run it using the command
    ```
    python3 DownlinkParser.py
    ```

## NOTES
- The downlink log does NOT update automatically. You will have to rerun the script in order to "refresh" and see any changes to the data.
- Noted in line 24 of the DownlinkParser.py script: the variable `log_difference` determines which downlink raw data file we are parsing. The default value is 3. This specifically chooses the MOST RECENT log to parse. As of 8/31/25, the most recent log has no data and therefore returns nothing. This is perfectly normal. I adjusted the variable for testing, since I knew which had data to parse. Please leave this variable set to 3 so it will ALWAYS parse only the latest file.
- Feel free to reach out to me (Breeze Aguilar) for any questions! I will gladly assist with setting up or updating any part of this tool for you.