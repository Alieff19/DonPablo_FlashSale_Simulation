from flask import Flask, jsonify, render_template, Response
import redis
import os
import socket
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# --- MONITORING SETUP (MATA DEWA) ---
# Ini yang menghitung berapa kali orang klik tombol BELI
REQUEST_COUNT = Counter('flash_sale_requests', 'Total Request Pembelian', ['status'])

redis_host = os.environ.get('REDIS_HOST', 'localhost')
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

if not r.exists('stok_iphone'):
    r.set('stok_iphone', 100)

@app.route('/')
def index():
    stok = r.get('stok_iphone')
    container = socket.gethostname()
    return render_template('index.html', stok=stok, container=container)

# Endpoint khusus agar Prometheus bisa ambil data
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

@app.route('/beli', methods=['POST'])
def beli():
    container = socket.gethostname()
    
    # Cek Stok (Atomic)
    stok_baru = r.decr('stok_iphone')

    if stok_baru >= 0:
        # Lapor ke Monitoring: "Ada 1 Sukses"
        REQUEST_COUNT.labels(status='success').inc()
        
        return jsonify({
            'status': 'success',
            'msg': 'TRANSAKSI BERHASIL! Unit diamankan.',
            'container': container,
            'sisa': stok_baru
        })
    else:
        # Lapor ke Monitoring: "Ada 1 Gagal"
        REQUEST_COUNT.labels(status='fail').inc()
        
        r.incr('stok_iphone') 
        return jsonify({
            'status': 'fail',
            'msg': 'MAAF, STOK HABIS (SOLD OUT).',
            'container': container,
            'sisa': 0
        })

@app.route('/reset', methods=['POST'])
def reset():
    r.set('stok_iphone', 100)
    return jsonify({'msg': 'System Reset'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)