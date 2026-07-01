# 🚀 NFT Wallet Tracker Bot

A Python-based Telegram bot that monitors **Ethereum wallets** in real time and sends rich Telegram alerts whenever NFTs are **bought** or **received**.

---

## ✨ Features

- 🔔 Real-time Telegram notifications
- 🛒 Detects NFT purchases
- 📥 Detects NFT transfers / airdrops
- 🏪 Marketplace detection (OpenSea, Blur, etc.)
- 🖼 Collection logo preview
- 💎 Live floor price
- 🌊 OpenSea collection link
- 🔗 Etherscan transaction link
- 🚫 Duplicate alert prevention
- ⚡ Built with AsyncIO

---

## 🛠 Tech Stack

- Python 3.13
- AsyncIO
- Alchemy NFT API
- Ethereum JSON-RPC
- Telegram Bot API
- Requests
- python-dotenv
- Git

---

## 📁 Project Structure

```text
NFTAlertBot/
│
├── alchemy.py
├── config.py
├── main.py
├── marketplace.py
├── monitor.py
├── telegram_bot.py
├── transaction.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📸 Example Telegram Alert

![Telegram Alert](images/example-alert.jpg)

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/NFTAlertBot.git

cd NFTAlertBot

```bash
git clone https://github.com/...

cd NFTAlertBot

python -m venv .venv

source .venv/bin/activate      # Linux/macOS

# or

.venv\Scripts\activate         # Windows

pip install -r requirements.txt

python main.py
```
```

---

## ✅ Current Features

- [x] Ethereum wallet monitoring
- [x] Telegram alerts
- [x] Purchase vs Received detection
- [x] Marketplace detection
- [x] Collection logo preview
- [x] Live floor price
- [x] OpenSea collection link
- [x] Etherscan transaction link
- [x] Duplicate transaction prevention

---

## 🔮 Roadmap

- [ ] Actual purchase price
- [ ] Multi-wallet support
- [ ] Discord notifications
- [ ] Cloud deployment
- [ ] Dashboard
- [ ] Database support

---


## 🚀 Next Project

### Whale Wallet Intelligence Platform ( Coming Soon )

- Multi-wallet tracking
- Web dashboard
- Telegram alerts
- Analytics
- SQLite database


---

## 💡 Why I Built This

I built this project to learn blockchain development by creating a real-world application that monitors Ethereum wallets and sends instant Telegram alerts for NFT purchases and transfers. It demonstrates working with blockchain APIs, asynchronous programming, and event-driven automation.

---

## 👨‍💻 Author

**Krishna Chaitanya**

---

## 📄 License

This project is licensed under the MIT License.