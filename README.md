# 🚀 NFT Wallet Tracker Bot

A Python-based Telegram bot that monitors Ethereum wallets in real time and sends rich alerts whenever NFTs are bought or received.

## ✨ Features

- 🔔 Real-time Telegram notifications
- 🛒 Detects NFT purchases
- 📥 Detects NFT transfers/airdrops
- 🏪 Marketplace detection (OpenSea, Blur, etc.)
- 🖼 Collection logo preview
- 💎 Live floor price
- 🌊 OpenSea collection link
- 🔗 Etherscan transaction link
- 🚫 Duplicate alert prevention
- ⚡ Built with AsyncIO

## 🛠 Tech Stack

- Python 3.13
- AsyncIO
- Alchemy NFT API
- Ethereum JSON-RPC
- Telegram Bot API
- Requests
- python-dotenv
- Git

## 📁 Project Structure

```
NFTAlertBot/

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

## 📸 Example Alert

```text
🛒 NFT BOUGHT

🎨 Collection: Nightborn

🏪 Marketplace: OpenSea

📦 NFTs Bought: 20

💎 Floor: 0.0022 ETH

🌊 OpenSea
https://opensea.io/collection/nightborneth

🔗 Transaction
https://etherscan.io/tx/...
```

## 🚀 Installation

```bash
git clone <your-repository>

cd NFTAlertBot

pip install -r requirements.txt

python main.py
```

## ✅ Completed

- [x] Ethereum wallet monitoring
- [x] Telegram alerts
- [x] Purchase vs Received detection
- [x] Marketplace detection
- [x] Collection logo
- [x] Live floor price
- [x] OpenSea link
- [x] Etherscan link
- [x] Duplicate transaction prevention

## 🔮 Roadmap

- [ ] Actual purchase price
- [ ] Multi-wallet tracking
- [ ] Discord notifications
- [ ] Dashboard
- [ ] Cloud deployment
- [ ] Database support

## 👨‍💻 Author

**Krishna Chaitanya**