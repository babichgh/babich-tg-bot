# babich-tg-bot
## Installation with Python
### Prerequisites
- [Python3](https://www.python.org/downloads/)
1. Clone the repository:
   ```
   git clone https://github.com/babichgh/babich-tg-bot.git
   cd babich-tg-bot
   ```
2. Create .env file as .env.example
3. Create the venv
   ```
   python3 -m venv {venv_name}
   source ./venv/bin/activate # for MacOS/Linux
   venv\Scripts\activate # for Windows
   ```
4. Install dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run the bot
   ```
   python3 ./main.py
   ```
## Installation with Docker
### Prerequisites
- [Docker](https://www.docker.com/)
1. Clone the repository:
   ```
   git clone https://github.com/babichgh/babich-tg-bot.git
   cd babich-tg-bot
   ```
2. Create .env file as .env.example
3. Build the image
   ```
   docker build -t {image_name}
   ```
4. Run the container
   ```
   docker run {image_name}
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
