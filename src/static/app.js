let currentLang = 'tr';

function switchLang(lang) {
    currentLang = lang;
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');

    document.querySelectorAll('[data-tr]').forEach(el => {
        el.textContent = el.getAttribute('data-' + lang);
    });
}

async function checkStock() {
    const btn = document.getElementById('checkBtn');
    btn.disabled = true;
    
    document.getElementById('manualResults').innerHTML = `
        <div class="loading">
            <div class="spinner"></div>
            <p>${currentLang === 'tr' ? 'Stok durumu kontrol ediliyor...' : 'Checking stock availability...'}</p>
        </div>
    `;

    try {
        const response = await fetch('/api/stock/check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        });

        const data = await response.json();
        displayResults(data.results, 'manualResults');
        
        showNotification(
            currentLang === 'tr' ? 'Stok kontrolü tamamlandı' : 'Stock check completed',
            'success'
        );
    } catch (error) {
        document.getElementById('manualResults').innerHTML = `
            <p style="color: #ef4444;">${currentLang === 'tr' ? 'Hata: ' : 'Error: '}${error.message}</p>
        `;
        showNotification(
            currentLang === 'tr' ? 'Stok kontrolü başarısız' : 'Stock check failed',
            'error'
        );
    } finally {
        btn.disabled = false;
    }
}

async function startScheduler() {
    const interval = document.getElementById('intervalInput').value;
    
    try {
        const response = await fetch('/api/scheduler/start', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ interval_minutes: parseInt(interval) })
        });

        const data = await response.json();
        
        if (data.success) {
            document.getElementById('startBtn').disabled = true;
            document.getElementById('stopBtn').disabled = false;
            updateSchedulerStatus();
            showNotification(data.message, 'success');
            
            // Start polling for results
            startPolling();
        } else {
            showNotification(data.message, 'error');
        }
    } catch (error) {
        showNotification(
            currentLang === 'tr' ? 'Zamanlayıcı başlatılamadı' : 'Failed to start scheduler',
            'error'
        );
    }
}

async function stopScheduler() {
    try {
        const response = await fetch('/api/scheduler/stop', {
            method: 'POST'
        });

        const data = await response.json();
        
        if (data.success) {
            document.getElementById('startBtn').disabled = false;
            document.getElementById('stopBtn').disabled = true;
            updateSchedulerStatus();
            showNotification(data.message, 'success');
            
            // Stop polling
            stopPolling();
        } else {
            showNotification(data.message, 'error');
        }
    } catch (error) {
        showNotification(
            currentLang === 'tr' ? 'Zamanlayıcı durdurulamadı' : 'Failed to stop scheduler',
            'error'
        );
    }
}

async function updateSchedulerStatus() {
    try {
        const response = await fetch('/api/scheduler/status');
        const data = await response.json();
        
        const status = data.status;
        const statusHtml = `
            <div style="margin-top: 20px; padding: 15px; background: #f9fafb; border-radius: 10px;">
                <p><strong>${currentLang === 'tr' ? 'Durum:' : 'Status:'}</strong> 
                    <span class="status-badge ${status.active ? 'status-active' : 'status-inactive'}">
                        ${status.active ? (currentLang === 'tr' ? 'Aktif' : 'Active') : (currentLang === 'tr' ? 'Pasif' : 'Inactive')}
                    </span>
                </p>
                ${status.active ? `
                    <p><strong>${currentLang === 'tr' ? 'Kontrol Aralığı:' : 'Check Interval:'}</strong> ${status.interval_minutes} ${currentLang === 'tr' ? 'dakika' : 'minutes'}</p>
                    <p><strong>${currentLang === 'tr' ? 'Son Kontrol:' : 'Last Check:'}</strong> ${status.last_check ? new Date(status.last_check).toLocaleString('tr-TR') : '-'}</p>
                    <p><strong>${currentLang === 'tr' ? 'Sonraki Kontrol:' : 'Next Check:'}</strong> ${status.next_check ? new Date(status.next_check).toLocaleString('tr-TR') : '-'}</p>
                ` : ''}
            </div>
        `;
        
        document.getElementById('schedulerStatus').innerHTML = statusHtml;
    } catch (error) {
        console.error('Failed to update scheduler status:', error);
    }
}

let pollingInterval;

function startPolling() {
    pollingInterval = setInterval(async () => {
        try {
            const response = await fetch('/api/scheduler/results');
            const data = await response.json();
            
            if (data.results && data.results.length > 0) {
                displayResults(data.results, 'schedulerResults');
                
                // Check for available stock and notify
                const availableItems = data.results.filter(r => r.stock.available);
                if (availableItems.length > 0) {
                    availableItems.forEach(item => {
                        showNotification(
                            `${currentLang === 'tr' ? 'Stokta!' : 'In Stock!'} ${item.product.name} - ${item.store.name}`,
                            'success'
                        );
                    });
                }
            }
            
            updateSchedulerStatus();
        } catch (error) {
            console.error('Polling error:', error);
        }
    }, 30000); // Poll every 30 seconds
}

function stopPolling() {
    if (pollingInterval) {
        clearInterval(pollingInterval);
        pollingInterval = null;
    }
}

function displayResults(results, containerId) {
    const container = document.getElementById(containerId);
    
    if (!results || results.length === 0) {
        container.innerHTML = `<p style="color: #666; text-align: center; padding: 20px;">${currentLang === 'tr' ? 'Henüz sonuç yok' : 'No results yet'}</p>`;
        return;
    }

    const html = `
        <div class="results-grid">
            ${results.map(result => `
                <div class="result-card ${result.stock.available ? 'available' : 'unavailable'}">
                    <h3>${result.product.name}</h3>
                    <div class="result-info">
                        <p><strong>${currentLang === 'tr' ? 'Mağaza:' : 'Store:'}</strong> ${result.store.name}</p>
                        <p><strong>${currentLang === 'tr' ? 'Lokasyon:' : 'Location:'}</strong> ${result.store.location}</p>
                        <p><strong>${currentLang === 'tr' ? 'Adres:' : 'Address:'}</strong> ${result.store.address}</p>
                        <p><strong>${currentLang === 'tr' ? 'Telefon:' : 'Phone:'}</strong> ${result.store.phone}</p>
                    </div>
                    <div class="stock-status ${result.stock.available ? 'stock-available' : 'stock-unavailable'}">
                        <span>${result.stock.available ? '✓' : '✗'}</span>
                        <span>${result.stock.store_pickup_label || (result.stock.available ? (currentLang === 'tr' ? 'Stokta var' : 'In stock') : (currentLang === 'tr' ? 'Stokta yok' : 'Out of stock'))}</span>
                    </div>
                    <p style="margin-top: 10px; font-size: 12px; color: #666;">
                        ${currentLang === 'tr' ? 'Kontrol zamanı:' : 'Checked at:'} ${new Date(result.stock.checked_at).toLocaleString('tr-TR')}
                    </p>
                </div>
            `).join('')}
        </div>
    `;
    
    container.innerHTML = html;
}

function showNotification(message, type) {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.innerHTML = `
        <p style="font-weight: 600; margin-bottom: 5px;">${type === 'success' ? '✓' : '✗'} ${message}</p>
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

// Initialize
updateSchedulerStatus();
