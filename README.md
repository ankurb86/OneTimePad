# OneTimePad
Cryptography Class Project to implement One Time Pad Encryption

README FILE

PROJECT ON ONE TIME PAD ENCRYPTION for CS 6058 DATA SECURITY AND PRIVACY, SPRING 2018,
by ANKUR BHATTACHARYA, MID #M12467767
bhattaar@mail.uc.edu
February 6th, 2018

[ABOUT THE PROJECT]
    This project is for implementing the One-Time-Pad Encryption to securely transfer files from sender to receiver.
    It includes encryption and decryption in different ways as mentioned in the project requirements.

---------------------------------------------------------------------------------------------------------------------------
CONTENTS
I.      SYSTEM AND SOFTWARE REQUIREMENTS
II.     RUNNING THE PROGRAM AND PROGRAM DESCRIPTIONS
III.    FILES AND STRUCTURE
IV.     KNOWN ISSUES AND WORKAROUNDS

---------------------------------------------------------------------------------------------------------------------------
I.  SYSTEM AND SOFTWARE REQUIREMENTS

1.  Operating System: Windows 7, Windows 8, Windows 10
2.  Software: Python 3.6.3
    Please note that the latest version of python i.e. Python 3.6.3 is required to run this if you're using Windows 10.
    Download the latest version at https://www.python.org/downloads/release/python-363/
    While Installing, check the button to include the Path to Python in Environment Variables

---------------------------------------------------------------------------------------------------------------------------
II. RUNNING THE PROGRAM AND PROGRAM DESCRIPTIONS

    1. Open up a command prompt window
    2. Check if Python is installed
        2.a.  To get to the command line, open the Windows menu and type “cmd” in the search bar. Select Command Prompt from the search results.
              In the Command Prompt window, type the following and press Enter.
                python
              If Python is installed and in your path, then this command will run python.exe and show you the version number.
                C:\Users\Nighthawk>python
                Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
                Type "help", "copyright", "credits" or "license" for more information.
              If python is installed, then type the following command and press Enter
                exit()
              If python is not installed, you will see
                'python' is not recognized as an internal or external command, operable program or batch file.
              In that case, please install python from the steps provided above
    3.  Go to the program location path by issuing the cd command with the path of the program's src folder
                cd <path>
                e.g. C:\Users\Nighthawk>cd /d D:\Development\Python\UC\opt_m12467767\src
    4.  COMMANDS FOR RUNNING THE PROGRAM
        If you need to change the message at any time then open the data/plaintext.txt folder and edit the message.
        You can change the secret key from the data/key.txt as well for the ENCRYPTION PROGRAM

        Type the required commands and press enter
        4.a.    ENCRYPTION PROGRAM
                This program takes the message from the plaintext.txt file in the data folder and generates a ciphertext based on the key in the
                key.txt file of the data folder. It stores the ciphertext in the ciphertext.txt file in the data folder. If you wish to change the
                message, You will need to open the plaintext.txt file and enter a message.

                The Key stored in the key.txt file is a 32bit key. Hence you can only pass a message that's 32 bits long.
                If the message size does not match the key size then you will receive a prompt stating the same.
                Command:
                    python Encryption.py

        4.b.    DECRYPTION PROGRAM
                This program takes the ciphertext from the ciphertext.txt file, takes the secret key from the key.txt file and then generates the
                original message back and saves this message in the result.txt file.
                If it finds a key value not matching the length of the ciphertext then it displays an error message mentioning the same
                Command:
                    python Decryption.py

        4.c.    NEW KEY GENERATION PROGRAM
                This program is used to generate a new key based on the number value that we enter.
                This number value must be between 1 and 128 (including 1 and 128).
                The new generated key will be stored in the newkey.txt and the key will hold the same number of bits as the number value we enter.
                Enter a value between 1 and 128 in the <Number> placeholder while issuing the command
                Command:
                    python Keygen.py <Number>
                    Example: python Keygen 32

        4.d.    CHECK KEY FREQUENCY PROGRAM
                This program runs 5001 times to check how frequently the same newly generated 3-digit secret keys repeat themselves.
                It maintains a counter and provides a list of keys and a list of frequencies to show how many times the same keys were generated.
                The list of Keys and Frequencies looks like this:

                    Keys    Frequencies
                    ----------------
                    000      621
                    001      664
                    010      635
                    011      588
                    100      604
                    101      647
                    110      636
                    111      607

                Command:
                    python KeyFrequency.py

         4.e.   FIND ENCRYPT FUNCTION RUN TIME
                This program is used to run the Enc() function 10 times and find the average running time that the function for Encryption takes.
                It will return the average time that the function runs for.
                Command:
                    python EncryptRunTime.py

---------------------------------------------------------------------------------------------------------------------------
III. FILES AND STRUCTURE

    The Files included in this project are:
    build
    data
    --ciphertext.txt
    --key.txt
    --newkey.txt
    --plaintext.txt
    --result.txt
    src
    --Decryption.py
    --Encryption.py
    --EncryptRunTime.py
    --KeyFrequency.py
    --KeyGen.py
    --main.py
    --XOREncrypt.py
    Readme.txt

---------------------------------------------------------------------------------------------------------------------------
IV. KNOWN ISSUES AND WORKAROUNDS

    If you receive the below error at any point of time, then follow the steps provided below as a fix.

    [ISSUE]
    OSError: raw write() returned invalid length
    This error mostly pops up while running the CHECK KEY FREQUENCY PROGRAM.

    [WORKAROUND]
    This occurs if you're running Windows 10 and a version of Python lower than 3.6.
    Update your python version to 3.6+ to fix the issue.

