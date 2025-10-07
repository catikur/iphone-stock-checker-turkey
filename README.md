# iPhone Stock Checker - Apple Turkey

A web application to check iPhone 17 Pro / Pro Max Cosmic Orange stock availability at Apple Stores in Istanbul, Turkey.

## Live Demo

**Application URL:** https://w5hni7cp1m5w.manus.space

> **Note:** This is the latest version with all bug fixes. The application is deployed and ready to use!

## Features

### 🔍 Manual Stock Check
- Instantly check stock availability across all products and stores
- Real-time data from Apple's official API
- Visual results with color-coded cards (green = in stock, red = out of stock)

### ⏰ Automatic Stock Check
- Schedule periodic stock checks (minimum 5 minutes interval)
- Background monitoring with customizable intervals
- Desktop notifications when stock becomes available
- Status tracking (active/inactive, last check, next check)

### 🌐 Bilingual Support
- Full Turkish and English language support
- Easy language switching with TR/EN buttons

### 📱 Responsive Design
- Works seamlessly on desktop, tablet, and mobile devices
- Modern gradient design with smooth animations
- Professional UI with hover effects and transitions

## Monitored Products

The application monitors the following iPhone models in Cosmic Orange color:

1. iPhone 17 Pro 256GB
2. iPhone 17 Pro 512GB
3. iPhone 17 Pro Max 256GB
4. iPhone 17 Pro Max 512GB

## Monitored Stores

Three Apple Store locations in Istanbul are monitored:

### 1. Apple Bağdat Caddesi (Kadıköy)
- **Address:** Bağdat Caddesi, No: 342, Caddebostan, Kadıköy İstanbul 34728
- **Phone:** (0216) 468 01 00

### 2. Apple Zorlu Center (Beşiktaş)
- **Address:** Zorlu Center, Koru Sok. No: 2, Beşiktaş İstanbul 34340
- **Phone:** (0212) 708 37 00

### 3. Apple Akasya (Üsküdar)
- **Address:** Akasya AVM, Acıbadem Mah, Çeçen Sok No: 25, Üsküdar İstanbul 34660
- **Phone:** (0216) 250 71 00

## Technology Stack

### Backend
- **Framework:** Flask (Python)
- **API Integration:** Apple Store Pickup API
- **Threading:** Background scheduler for automated checks
- **CORS:** Flask-CORS for cross-origin requests

### Frontend
- **HTML5 & CSS3:** Modern, responsive design
- **JavaScript:** Vanilla JS for interactivity
- **Design:** Gradient backgrounds, card-based layout, smooth animations

### Deployment
- **Platform:** Manus Cloud
- **URL:** https://lnh8imcw1qqm.manus.space

## Project Structure

```
iphone_stock_checker/
├── src/
│   ├── main.py                 # Flask application entry point
│   ├── routes/
│   │   ├── stock.py           # Stock checking endpoints
│   │   └── scheduler.py       # Automated scheduling endpoints
│   └── static/
│       ├── index.html         # Main HTML page
│       ├── style.css          # Styling
│       └── app.js             # Frontend JavaScript
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## API Endpoints

### Stock Endpoints

#### GET `/api/stock/products`
Returns list of all monitored products.

**Response:**
```json
{
  "success": true,
  "products": {
    "iphone_17_pro_max_256gb_cosmic_orange": {
      "name": "iPhone 17 Pro Max 256GB Kozmik Turuncu",
      "part_number": "MFYN4TU/A",
      "capacity": "256GB",
      "model": "iPhone 17 Pro Max"
    }
  }
}
```

#### GET `/api/stock/stores`
Returns list of all monitored stores.

**Response:**
```json
{
  "success": true,
  "stores": {
    "bagdat_caddesi": {
      "name": "Apple Bağdat Caddesi",
      "location": "Kadıköy, İstanbul",
      "address": "Bağdat Caddesi, No: 342, Caddebostan",
      "phone": "(0216) 468 01 00"
    }
  }
}
```

#### POST `/api/stock/check`
Check stock availability for specified products and stores.

**Request Body:**
```json
{
  "products": ["iphone_17_pro_max_256gb_cosmic_orange"],
  "stores": ["bagdat_caddesi"]
}
```

**Response:**
```json
{
  "success": true,
  "results": [
    {
      "product": {
        "id": "iphone_17_pro_max_256gb_cosmic_orange",
        "name": "iPhone 17 Pro Max 256GB Kozmik Turuncu",
        "part_number": "MFYN4TU/A"
      },
      "store": {
        "id": "bagdat_caddesi",
        "name": "Apple Bağdat Caddesi",
        "location": "Kadıköy, İstanbul"
      },
      "stock": {
        "available": false,
        "pickup_display": "unavailable",
        "store_pickup_label": "Stokta yok",
        "checked_at": "2025-10-07T02:50:00"
      }
    }
  ]
}
```

### Scheduler Endpoints

#### POST `/api/scheduler/start`
Start automated stock checking.

**Request Body:**
```json
{
  "interval_minutes": 30
}
```

#### POST `/api/scheduler/stop`
Stop automated stock checking.

#### GET `/api/scheduler/status`
Get current scheduler status.

#### GET `/api/scheduler/results`
Get latest stock check results from scheduler.

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd iphone_stock_checker
```

2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python src/main.py
```

5. Open browser and navigate to:
```
http://localhost:5000
```

## Usage Guide

### Manual Check
1. Open the application
2. Click **"Şimdi Kontrol Et"** (Check Now) button
3. View results in color-coded cards
4. Green cards indicate available stock
5. Red cards indicate out of stock

### Automatic Check
1. Enter check interval in minutes (minimum 5)
2. Click **"Başlat"** (Start) button
3. Application will check stock periodically
4. Notifications appear when stock is found
5. Click **"Durdur"** (Stop) to stop monitoring

### Language Switch
- Click **TR** button for Turkish
- Click **EN** button for English

## Important Notes

1. **Real-time Data:** Stock information is fetched directly from Apple's official API
2. **Minimum Interval:** Automatic checks require minimum 5-minute intervals
3. **Browser Required:** Keep browser tab open for automatic checks to work
4. **Notifications:** In-app notifications appear when stock is found
5. **Mobile Friendly:** Fully responsive design works on all devices

## Privacy

This application does not collect or store any personal information. It only accesses publicly available stock information from Apple's API.

## License

This project is for educational and personal use only.

## Repository

**GitHub:** https://github.com/catikur/iphone-stock-checker-turkey

## Author

Created with Manus AI

## Support

For issues or questions, please open an issue on the repository.
