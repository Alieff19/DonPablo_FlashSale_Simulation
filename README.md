# 🚀 iPhone 17 Launch — Flash Sale Microservices System

![Docker](https://img.shields.io/badge/Container-Docker-blue.svg?style=for-the-badge&logo=docker)
![Python](https://img.shields.io/badge/Backend-Flask-green.svg?style=for-the-badge&logo=python)
![Redis](https://img.shields.io/badge/Cache-Redis-red.svg?style=for-the-badge&logo=redis)
![Nginx](https://img.shields.io/badge/Load%20Balancer-Nginx-009639.svg?style=for-the-badge&logo=nginx)
![Grafana](https://img.shields.io/badge/Monitoring-Grafana-F46800.svg?style=for-the-badge&logo=grafana)

> **SIMULASI ARSITEKTUR CLOUD UNTUK EVENT FLASH SALE HIGH-CONCURRENCY BERBASIS MICROSERVICES DAN DOCKER ORCHESTRATION**

Proyek ini merupakan simulasi sistem **Flash Sale** untuk peluncuran **iPhone 17 Pro Max (2025)**.  
Sistem dibangun menggunakan arsitektur **Microservices** untuk menangani **traffic ekstrem** dengan karakteristik:

- ⚡ High concurrency  
- ❌ Zero downtime  
- 🛡️ Zero overselling (anti stok minus)

---

## 🌟 Key Features

| Fitur | Deskripsi | Teknologi |
|------|----------|-----------|
| 🛡️ **Race Condition Proof** | Menjamin stok tetap akurat meskipun 1000+ request/detik | Redis Atomic Operation |
| ⚖️ **Load Balancing** | Distribusi beban otomatis ke beberapa replika server | Nginx (Round Robin) |
| ❤️ **Self-Healing System** | Container otomatis pulih saat terjadi kegagalan | Docker Compose |
| 👁️ **Observability** | Monitoring trafik sukses vs gagal secara real-time | Prometheus & Grafana |
| 💎 **Modern UI** | Tampilan frontend bertema *Apple Event* | HTML5 & CSS3 |

---

## 🏗️ System Architecture

Seluruh sistem berjalan dalam lingkungan **containerized microservices** dengan alur sebagai berikut:

```mermaid
graph TD
    User[User / Bot Attack] -->|HTTP Request| LB[Nginx Load Balancer]
    LB -->|Round Robin| App1[Web App Replica 1]
    LB -->|Round Robin| App2[Web App Replica 2]
    LB -->|Round Robin| App3[Web App Replica 3]
    App1 & App2 & App3 -->|Atomic Decrement| Redis[(Redis)]
    App1 & App2 & App3 -.->|Metrics| Prometheus
    Prometheus -.->|Visualization| Grafana
```

---

## 📂 Struktur Folder

```text
DONPABLO/
├── docker-compose.yml      # Orkestrator Utama (Jantung Sistem)
├── prometheus.yml          # Konfigurasi Monitoring
├── bot_attack.py           # Script Stress Test (Simulasi Serangan)
├── nginx/
│   └── nginx.conf          # Konfigurasi Load Balancer
└── app/
    ├── Dockerfile          # Resep Image Aplikasi
    ├── requirements.txt    # Dependensi Python
    ├── app.py              # Backend Logic
    ├── static/
    │   └── iphone17pro.png # Aset Gambar
    └── templates/
        └── index.html      # Frontend UI
```

---

## ⚡ Panduan Instalasi (Quick Start)

### Prasyarat

- [Docker Desktop](https://www.docker.com/products/docker-desktop) (Running)
- Python 3.x *(Opsional, untuk script bot)*

---

### 1️⃣ Clone & Build

```bash
git clone https://github.com/USERNAME_KAMU/repo-ini.git
cd repo-ini
docker-compose up -d --build
```

---

### 2️⃣ Akses Aplikasi

Buka browser favorit Anda dan kunjungi:  
👉 **http://localhost**

---

## 🧪 Skenario Pengujian (Demo Script)

### 🟢 Skenario A — Load Balancing Check

1. Buka `http://localhost`
2. Klik **BELI SEKARANG** beberapa kali
3. Perhatikan teks: `Dilayani oleh Node: [ID Container]`

✅ **Hasil:**  
ID container berubah-ubah → load balancing berjalan

---

### 🔴 Skenario B — Stress Test (High Traffic)

Mensimulasikan **500 pembeli bersamaan**:

```bash
pip install requests
python bot_attack.py
```

✅ **Hasil:**  
- Log terminal bergerak cepat  
- Stok berhenti tepat di **0**  
- ❌ Tidak ada stok minus

---

### 💥 Skenario C — Chaos Engineering (Fault Tolerance)

1. Cek container aktif:
```bash
docker ps
```

2. Matikan paksa salah satu container web:
```bash
docker kill donpablo-web-1
```

3. Website tetap dapat diakses (failover sukses)

4. Recovery sistem:
```bash
docker-compose up -d
```

✅ **Hasil:**  
Container otomatis hidup kembali

---

## 📊 Setup Monitoring (Grafana Dashboard)

1. Akses **http://localhost:3000**  
   Login: `admin / admin`
2. Add Data Source → **Prometheus**
3. URL:
```text
http://prometheus:9090
```

4. Buat Dashboard → Add Visualization  
5. Gunakan query berikut:

```promql
sum(rate(flash_sale_requests_total[1m])) by (status)
```

📈 Jalankan stress test dan lihat lonjakan trafik secara real-time

---

## 👨‍💻 Author

| Nama | NIM | Peran |
|------|-----|------|
| **M Alief Alfaridzi** | 1203230045 | Cloud Architect & Backend |
| **Rafif Muhammad** | 1203230018 | Frontend & Documentation |

**Informatika — Universitas Telkom**  
*Tugas Besar Mata Kuliah Komputasi Awan & Terdistribusi (2025/2026)*

---

Made with ❤️ and ☕ using **Docker**
