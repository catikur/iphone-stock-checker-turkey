"""Scheduler routes for automated stock checking"""
from flask import Blueprint, jsonify, request
from datetime import datetime
import threading
import time

scheduler_bp = Blueprint('scheduler', __name__)

# Global scheduler state
scheduler_state = {
    'active': False,
    'interval_minutes': 30,
    'last_check': None,
    'next_check': None,
    'thread': None,
    'results': []
}

def scheduled_check_worker():
    """Background worker for scheduled stock checks"""
    from src.routes.stock import check_apple_store_stock, PRODUCTS, STORES
    
    while scheduler_state['active']:
        try:
            results = []
            
            # Check all products at all stores
            for product_id, product in PRODUCTS.items():
                for store_id, store in STORES.items():
                    stock_info = check_apple_store_stock(
                        product['part_number'],
                        store['store_id']
                    )
                    
                    result = {
                        'product': {
                            'id': product_id,
                            'name': product['name'],
                            'part_number': product['part_number']
                        },
                        'store': {
                            'id': store_id,
                            'name': store['name'],
                            'location': store['location']
                        },
                        'stock': stock_info
                    }
                    
                    results.append(result)
                    
                    # If stock is available, add to notifications
                    if stock_info.get('available'):
                        result['notification'] = True
            
            scheduler_state['results'] = results
            scheduler_state['last_check'] = datetime.now().isoformat()
            
            # Calculate next check time
            next_check_time = datetime.now().timestamp() + (scheduler_state['interval_minutes'] * 60)
            scheduler_state['next_check'] = datetime.fromtimestamp(next_check_time).isoformat()
            
        except Exception as e:
            print(f"Scheduler error: {e}")
        
        # Wait for the specified interval
        time.sleep(scheduler_state['interval_minutes'] * 60)

@scheduler_bp.route('/start', methods=['POST'])
def start_scheduler():
    """Start the automated stock checking scheduler"""
    data = request.get_json() or {}
    
    if scheduler_state['active']:
        return jsonify({
            'success': False,
            'message': 'Zamanlayıcı zaten çalışıyor'
        }), 400
    
    # Set interval (default 30 minutes)
    interval = data.get('interval_minutes', 30)
    if interval < 5:
        return jsonify({
            'success': False,
            'message': 'Minimum kontrol aralığı 5 dakikadır'
        }), 400
    
    scheduler_state['interval_minutes'] = interval
    scheduler_state['active'] = True
    
    # Start background thread
    thread = threading.Thread(target=scheduled_check_worker, daemon=True)
    thread.start()
    scheduler_state['thread'] = thread
    
    return jsonify({
        'success': True,
        'message': 'Zamanlayıcı başlatıldı',
        'interval_minutes': interval
    })

@scheduler_bp.route('/stop', methods=['POST'])
def stop_scheduler():
    """Stop the automated stock checking scheduler"""
    if not scheduler_state['active']:
        return jsonify({
            'success': False,
            'message': 'Zamanlayıcı zaten durdurulmuş'
        }), 400
    
    scheduler_state['active'] = False
    scheduler_state['thread'] = None
    
    return jsonify({
        'success': True,
        'message': 'Zamanlayıcı durduruldu'
    })

@scheduler_bp.route('/status', methods=['GET'])
def get_status():
    """Get current scheduler status"""
    return jsonify({
        'success': True,
        'status': {
            'active': scheduler_state['active'],
            'interval_minutes': scheduler_state['interval_minutes'],
            'last_check': scheduler_state['last_check'],
            'next_check': scheduler_state['next_check']
        }
    })

@scheduler_bp.route('/results', methods=['GET'])
def get_results():
    """Get latest stock check results"""
    return jsonify({
        'success': True,
        'results': scheduler_state['results'],
        'last_check': scheduler_state['last_check']
    })

@scheduler_bp.route('/config', methods=['POST'])
def update_config():
    """Update scheduler configuration"""
    data = request.get_json()
    
    interval = data.get('interval_minutes')
    if interval and interval >= 5:
        scheduler_state['interval_minutes'] = interval
        
        return jsonify({
            'success': True,
            'message': 'Ayarlar güncellendi',
            'interval_minutes': interval
        })
    
    return jsonify({
        'success': False,
        'message': 'Geçersiz ayarlar'
    }), 400
