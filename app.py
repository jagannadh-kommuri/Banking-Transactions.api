from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory transaction store (production would use PostgreSQL)
transactions = {}

@app.route('/api/transactions/status/<transaction_id>', methods=['GET'])
def get_transaction_status(transaction_id):
    transaction = transactions.get(transaction_id, {})
    if transaction:
        return jsonify({
            'transactionId': transaction_id,
            'status': transaction['status'],
            'amount': transaction['amount'],
            'account': transaction['account'],
            'timestamp': transaction['timestamp']
        })
    return jsonify({'error': 'Transaction not found'}), 404

@app.route('/api/transactions/transfer', methods=['POST'])
def create_transfer():
    data = request.json
    transaction_id = str(uuid.uuid4())[:8]
    
    transaction = {
        'transactionId': transaction_id,
        'status': 'Pending',
        'amount': data['amount'],
        'account': data['account'],
        'fromAccount': data['fromAccount'],
        'toAccount': data['toAccount'],
        'timestamp': datetime.utcnow().isoformat()
    }
    
    transactions[transaction_id] = transaction
    return jsonify(transaction), 201

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'Banking Transaction API'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
