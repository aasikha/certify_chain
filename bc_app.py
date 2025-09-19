from flask import Flask, request, render_template, redirect, url_for
import hashlib
import datetime
import json

app = Flask(__name__)

# Blockchain setup
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode())
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), {"certificate": "Genesis Block"}, "0")

    def add_block(self, data):
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), str(datetime.datetime.now()), data, last_block.hash)
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.hash_block() or current.previous_hash != previous.hash:
                return False
        return True

blockchain = Blockchain()

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return render_template("index.html")  # Home Page

@app.route('/add', methods=['GET', 'POST'])
def add_certificate():
    if request.method == 'POST':
        student_name = request.form['student_name']
        course = request.form['course']
        certificate_id = request.form['certificate_id']
        blockchain.add_block({
            "student_name": student_name,
            "course": course,
            "certificate_id": certificate_id
        })
        return redirect(url_for('view_blockchain'))
    return render_template("add_certificate.html")

@app.route('/verify', methods=['GET', 'POST'])
def verify_certificate():
    result = None
    cert_details = None
    if request.method == 'POST':
        cert_id = request.form['certificate_id']
        # Skip genesis block and search by cert_id
        for block in blockchain.chain:
            if block.index == 0:
                continue
            if block.data.get("certificate_id") == cert_id:
                result = True
                cert_details = {
                    "student_name": block.data.get("student_name"),
                    "course": block.data.get("course"),
                    "certificate_id": block.data.get("certificate_id"),
                    "timestamp": block.timestamp,
                    "hash": block.hash
                }
                break
        else:
            result = False
    return render_template("verify.html", result=result, cert_details=cert_details)

@app.route('/blockchain')
def view_blockchain():
    return render_template("blockchain.html", blocks=blockchain.chain)

if __name__ == '__main__':
    app.run(debug=True)
