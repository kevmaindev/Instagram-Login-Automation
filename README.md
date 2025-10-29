# Instagram Login Automation

## Description
This script automates the process of logging in to instagram using code.

## Prerequisites
- Python 3.x
- camoufox
- python-dotenv

Install the required packages with:
```
pip install requirements.txt

```

## Important Setup
**You must create a `.env` file in the project root directory with your instagram credentials:**

```
Insta_username=your_Insta_username
Insta_password=your_Insta_password 
```

Without this file containing your valid credentials, the script will not work!


Run the script:
```
python Instagram_Login.py
```

## Notes
- The script saves your login session to avoid repeated logins
- It runs in headed mode by default (you can see the browser)
- Be careful with your credentials - never commit the `.env` file to version control

## Disclaimer
Use this script responsibly and in compliance with instagram's Terms of Service. The developers are not responsible for any misuse or consequences of using this script.