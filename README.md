# babich-tg-bot
## Prerequisites
- [Python3](https://www.python.org/downloads/)
## Installation
1. Clone the repository:
   ```
   git clone https://github.com/babichgh/babich-tg-bot.git
   cd babich-tg-bot
   ```
2. Create the venv
  ```
  python3 -m venv venv
  source ./venv/bin/activate # for MacOS/Linux
  venv\Scripts\activate # for Windows
  ```
3. Install dependencies
  ```
  pip install -r requirements.txt
  ```
4. Create .env file as .env.example
5. Run the bot
  ```
  python3 ./main.py
  ```
## Project structure
```
babich-tg-bot/
├── .env.example     # .env example
├── .gitignore       # Ignores .env
├── README.md        # You read it right now
├── main.py          # Python source code
└── requirements.txt # Dependencies are here
```
