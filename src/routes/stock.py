"""Stock checking routes for iPhone availability"""
import requests
from flask import Blueprint, jsonify, request
from datetime import datetime

stock_bp = Blueprint('stock', __name__)

# Product configurations
PRODUCTS = {
    'iphone_17_pro_256gb_cosmic_orange': {
        'name': 'iPhone 17 Pro 256GB Kozmik Turuncu',
        'part_number': 'MG8H4TU/A',
        'sku': 'MG8H4',
        'capacity': '256GB',
        'model': 'iPhone 17 Pro'
    },
    'iphone_17_pro_512gb_cosmic_orange': {
        'name': 'iPhone 17 Pro 512GB Kozmik Turuncu',
        'part_number': 'MG8M4TU/A',
        'sku': 'MG8M4',
        'capacity': '512GB',
        'model': 'iPhone 17 Pro'
    },
    'iphone_17_pro_max_256gb_cosmic_orange': {
        'name': 'iPhone 17 Pro Max 256GB Kozmik Turuncu',
        'part_number': 'MFYN4TU/A',
        'sku': 'MFYN4',
        'capacity': '256GB',
        'model': 'iPhone 17 Pro Max'
    },
    'iphone_17_pro_max_512gb_cosmic_orange': {
        'name': 'iPhone 17 Pro Max 512GB Kozmik Turuncu',
        'part_number': 'MFYR4TU/A',
        'sku': 'MFYR4',
        'capacity': '512GB',
        'model': 'iPhone 17 Pro Max'
    }
}

# Istanbul Apple Stores
STORES = {
    'bagdat_caddesi': {
        'name': 'Apple Bağdat Caddesi',
        'location': 'Kadıköy, İstanbul',
        'address': 'Bağdat Caddesi, No: 342, Caddebostan',
        'postal_code': '34728',
        'store_id': 'R724',
        'phone': '(0216) 468 01 00'
    },
    'zorlu_center': {
        'name': 'Apple Zorlu Center',
        'location': 'Beşiktaş, İstanbul',
        'address': 'Zorlu Center, Koru Sok. No: 2',
        'postal_code': '34340',
        'store_id': 'R725',
        'phone': '(0212) 708 37 00'
    },
    'akasya': {
        'name': 'Apple Akasya',
        'location': 'Üsküdar, İstanbul',
        'address': 'Akasya AVM, Acıbadem Mah, Çeçen Sok No: 25',
        'postal_code': '34660',
        'store_id': 'R726',
        'phone': '(0216) 250 71 00'
    }
}

def check_apple_store_stock(part_number, store_postal_code):
    """Check stock availability at Apple Store using location-based API"""
    try:
        url = f"https://www.apple.com/tr/shop/retail/pickup-message"
        params = {
            'pl': 'true',
            'parts.0': part_number,
            'location': store_postal_code
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('head', {}).get('status') == '200':
            body = data.get('body', {})
            stores = body.get('stores', [])
            
            # API returns all nearby stores, we need to find ours
            if stores and len(stores) > 0:
                # Return the first store (closest one)
                store = stores[0]
                parts_availability = store.get('partsAvailability', {})
                part_info = parts_availability.get(part_number, {})
                
                # Get the correct pickup display and label from messageTypes
                message_types = part_info.get('messageTypes', {})
                regular_message = message_types.get('regular', {})
                
                pickup_display = part_info.get('pickupDisplay', 'unavailable')
                store_pickup_quote = regular_message.get('storePickupQuote', 'Stok bilgisi alınamadı')
                
                return {
                    'available': pickup_display == 'available',
                    'pickup_display': pickup_display,
                    'store_pickup_label': store_pickup_quote,
                    'store_name': store.get('storeName', ''),
                    'store_number': store.get('storeNumber', ''),
                    'checked_at': datetime.now().isoformat()
                }
        
        return {
            'available': False,
            'pickup_display': 'unavailable',
            'store_pickup_label': 'Stok bilgisi alınamadı',
            'checked_at': datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            'available': False,
            'error': str(e),
            'store_pickup_label': f'Hata: {str(e)}',
            'checked_at': datetime.now().isoformat()
        }

@stock_bp.route('/check', methods=['POST'])
def check_stock():
    """Check stock for specified products and stores"""
    data = request.get_json()
    
    product_ids = data.get('products', list(PRODUCTS.keys()))
    store_ids = data.get('stores', list(STORES.keys()))
    
    results = []
    
    for product_id in product_ids:
        if product_id not in PRODUCTS:
            continue
            
        product = PRODUCTS[product_id]
        
        for store_id in store_ids:
            if store_id not in STORES:
                continue
                
            store = STORES[store_id]
            
            stock_info = check_apple_store_stock(
                product['part_number'],
                store['postal_code']
            )
            
            results.append({
                'product': {
                    'id': product_id,
                    'name': product['name'],
                    'part_number': product['part_number'],
                    'capacity': product['capacity'],
                    'model': product['model']
                },
                'store': {
                    'id': store_id,
                    'name': store['name'],
                    'location': store['location'],
                    'address': store['address'],
                    'phone': store['phone']
                },
                'stock': stock_info
            })
    
    return jsonify({
        'success': True,
        'results': results,
        'checked_at': datetime.now().isoformat()
    })

@stock_bp.route('/products', methods=['GET'])
def get_products():
    """Get list of available products"""
    return jsonify({
        'success': True,
        'products': PRODUCTS
    })

@stock_bp.route('/stores', methods=['GET'])
def get_stores():
    """Get list of available stores"""
    return jsonify({
        'success': True,
        'stores': STORES
    })
