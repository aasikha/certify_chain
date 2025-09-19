
# 🎓 Blockchain-Based Certificate Verification

## 📌 Project Overview

This project implements a **Blockchain-based Certificate Verification System**. The system ensures that issued certificates are **tamper-proof, immutable, and easily verifiable** by leveraging blockchain technology and cryptographic hashing.

Traditional certificate systems are prone to forgery and require manual verification. Our solution provides a **transparent, secure, and decentralized** approach where certificates are stored on a blockchain, making them verifiable by employers, universities, or any third party.

## 🚀 Features

* **Add Certificate**: Issue new digital certificates with student details.
* **Verify Certificate**: Instantly check whether a certificate is genuine.
* **View Blockchain**: Display the complete chain of certificates stored in the blockchain.
* **Immutable Security**: Any modification in data changes the block hash, breaking the chain.
* **Simple Web Interface** using Flask + HTML.

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Frontend**: HTML, CSS
* **Blockchain Logic**: Custom blockchain with SHA-256 hashing (`hashlib`)
* **Storage**: In-memory blockchain (can be extended to DB/Distributed ledger)

## 📂 Project Structure

```
.
├── app.py                # Main Flask application
├── blockchain.py         # Blockchain logic (Block, Chain, Hashing)
├── templates/            # HTML files (Home, Add, Verify, View Blockchain)
├── static/               # CSS/JS files
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## 🔒 How It Works

1. Each certificate is stored as a **block** containing:

   * Student details
   * Timestamp
   * Previous block’s hash
   * Current block’s hash

2. Blocks are linked together forming a **chain**.

3. **SHA-256 hashing** ensures **immutability** → even a single data change alters the hash, breaking the chain.

4. The blockchain can be viewed anytime for **audit & transparency**.

---

## 🌟 Uniqueness of the Project

* Secure storage using **blockchain & hashing**.
* Independent certificate **verification system**.
* **Immutable & transparent** record-keeping.
* Scalable to other domains (property, medical, IDs).

---

## 📸 Screenshots

<img width="979" height="367" alt="image" src="https://github.com/user-attachments/assets/499cd69e-a788-46ab-90d7-b0d78e391874" />
<img width="979" height="404" alt="image" src="https://github.com/user-attachments/assets/2b7548aa-19b2-41a8-bb71-98ffc552b2be" />
<img width="979" height="373" alt="image" src="https://github.com/user-attachments/assets/005d21e6-d6df-4a0e-9df1-199c21c98ac3" />
<img width="979" height="390" alt="image" src="https://github.com/user-attachments/assets/d0df8d03-1fcd-4e34-9509-90bf130b0a52" /> 
<img width="979" height="310" alt="image" src="https://github.com/user-attachments/assets/01746519-0f83-4454-a3f4-c7d0627c5efd" />

---

## 🤝 Contributors

* \[AASIKHA A]
* \[FAAMIDHA PARVEEN M]



