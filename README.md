# 🤖 Morse-Code-Bot (Telegram)

A simple and interactive **Telegram bot** that **encrypts text into Morse code** and **decrypts Morse code back into readable text**. Built with Python and Telebot, this project is ideal for learning Morse code, educational demos, and Telegram bot practice.

---

## ✨ Features

* 🔐 Text ➜ Morse code encryption
* 🔓 Morse code ➜ Text decryption
* ⚡ Fast, chat-based interaction
* 📱 Works directly inside Telegram chats
* 🧠 Supports letters, numbers, and common punctuation

---

## 🖼️ Screenshots

> Add screenshots of the bot conversation here.

```
/screenshots
 ├── encrypt.png
 ├── decrypt.png
```

---

## 🎞️ Demo (GIF)

> Add a short GIF showing encryption and decryption.

```
/demo
 └── morse-bot-demo.gif
```

---

## 🛠️ Tech Stack

* **Python 3**
* **pyTelegramBotAPI (telebot)**
* **python-dotenv**

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Morse-Code-Bot.git
cd Morse-Code-Bot
```

### 2️⃣ Install Dependencies

```bash
pip install pyTelegramBotAPI python-dotenv
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
API_KEY=YOUR_TELEGRAM_BOT_TOKEN
```

---

## 🚀 Run the Bot

```bash
python bot.py
```

You should see:

```bash
started......
```

---

## 🤖 Bot Commands

| Command          | Description                 |
| ---------------- | --------------------------- |
| `/start`         | Start the bot               |
| `/help`          | Get help                    |
| `/encrypt`, `/e` | Prompt for Morse encryption |

---

## 🔁 Usage Examples

### 🔐 Encrypt Text

**Input:**

```
HELLO WORLD
```

**Output:**

```
.... . .-.. .-.. ---  .-- --- .-. .-.. -..
```

### 🔓 Decrypt Morse

**Input:**

```
.... . .-.. .-.. ---  .-- --- .-. .-.. -..
```

**Output:**

```
HELLO WORLD
```

---

## 🧠 Supported Characters

* **A–Z**
* **0–9**
* **Punctuation:** `. , ? / - ( )`

---

## ⚠️ Improved Error Handling (Recommended)

* Gracefully handle unknown characters
* Validate Morse patterns before decoding
* Return friendly error messages instead of exceptions

---

## ⚡ Optimized Morse Decoding (Recommended)

For better performance, create a **reverse dictionary** instead of searching indexes:

```python
REVERSE_MORSE = {v: k for k, v in MORSE_CODE_DICT.items()}
```

This avoids costly list searches and makes decoding faster and cleaner.

---

## 📂 Project Structure

```
Morse-Code-Bot/
│
├── bot.py
├── .env
├── README.md
├── screenshots/
├── demo/
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

**MIT License**

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND
```
