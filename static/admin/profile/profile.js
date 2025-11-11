// Sahifa yuklanganda animatsiyalar
document.addEventListener('DOMContentLoaded', function() {
    initAnimations();
    initInteractions();
    initTooltips();
});

// Animatsiyalarni ishga tushirish
function initAnimations() {
    const cards = document.querySelectorAll('.profile-card, .social-card, .info-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1
    });
    
    cards.forEach(card => {
        observer.observe(card);
    });
}

// Interaktiv funksiyalar
function initInteractions() {
    // Profil rasmiga hover effekti
    const profileAvatar = document.querySelector('.profile-avatar');
    if (profileAvatar) {
        profileAvatar.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1) rotate(5deg)';
        });
        
        profileAvatar.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotate(0deg)';
        });
    }
    
    // Info itemlarga hover effekti
    const infoItems = document.querySelectorAll('.info-item');
    infoItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.1)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.boxShadow = 'none';
        });
    });
    
    // Hujjat itemlarga click hodisasi
    const documentItems = document.querySelectorAll('.document-item');
    documentItems.forEach(item => {
        item.addEventListener('click', function(e) {
            if (!e.target.closest('.btn-download')) {
                const downloadBtn = this.querySelector('.btn-download');
                if (downloadBtn) {
                    downloadBtn.click();
                }
            }
        });
    });
    
    // Tugmalarga ripple effekti
    const buttons = document.querySelectorAll('.btn-action, .btn-download');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');
            
            this.appendChild(ripple);
            
            setTimeout(() => ripple.remove(), 600);
        });
    });
}

// Tooltip funksiyasi
function initTooltips() {
    const socialLinks = document.querySelectorAll('.social-link');
    
    socialLinks.forEach(link => {
        link.setAttribute('data-bs-toggle', 'tooltip');
        link.setAttribute('data-bs-placement', 'top');
        
        const icon = link.querySelector('i');
        if (icon.classList.contains('fa-telegram')) {
            link.setAttribute('title', 'Telegram orqali bog\'lanish');
        } else if (icon.classList.contains('fa-github')) {
            link.setAttribute('title', 'GitHub profilini ko\'rish');
        } else if (icon.classList.contains('fa-linkedin')) {
            link.setAttribute('title', 'LinkedIn profilini ko\'rish');
        }
    });
    
    // Bootstrap tooltiplarini ishga tushirish
    if (typeof bootstrap !== 'undefined') {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
}

// Statistikalarni animatsiyalash
function animateStats() {
    const statValues = document.querySelectorAll('.stat-value');
    
    statValues.forEach(stat => {
        const finalValue = parseInt(stat.textContent);
        let currentValue = 0;
        const increment = finalValue / 50;
        const duration = 1000;
        const stepTime = duration / 50;
        
        const counter = setInterval(() => {
            currentValue += increment;
            if (currentValue >= finalValue) {
                stat.textContent = finalValue;
                clearInterval(counter);
            } else {
                stat.textContent = Math.floor(currentValue);
            }
        }, stepTime);
    });
}

// Sahifa yuklanganda statistikalarni animatsiyalash
window.addEventListener('load', () => {
    setTimeout(animateStats, 300);
});

// Copy to clipboard funksiyasi
function copyToClipboard(text, element) {
    navigator.clipboard.writeText(text).then(() => {
        // Success notification
        showNotification('Nusxalandi!', 'success');
        
        // Visual feedback
        const originalText = element.innerHTML;
        element.innerHTML = '<i class="fas fa-check"></i> Nusxalandi';
        element.style.background = '#10b981';
        
        setTimeout(() => {
            element.innerHTML = originalText;
            element.style.background = '';
        }, 2000);
    }).catch(err => {
        showNotification('Xatolik yuz berdi', 'error');
    });
}

// Notification ko'rsatish
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : 'info-circle'}"></i>
        <span>${message}</span>
    `;
    
    // Notification stillar
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#10b981' : '#3b82f6'};
        color: white;
        padding: 15px 25px;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        display: flex;
        align-items: center;
        gap: 10px;
        z-index: 9999;
        animation: slideInRight 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Email va telefonga copy funksiyasi
document.addEventListener('DOMContentLoaded', function() {
    const emailItem = document.querySelector('.info-icon.email').closest('.info-item');
    const phoneItem = document.querySelector('.info-icon.phone').closest('.info-item');
    
    if (emailItem) {
        emailItem.style.cursor = 'pointer';
        emailItem.addEventListener('click', function() {
            const email = this.querySelector('p').textContent;
            copyToClipboard(email, this);
        });
    }
    
    if (phoneItem) {
        phoneItem.style.cursor = 'pointer';
        phoneItem.addEventListener('click', function() {
            const phone = this.querySelector('p').textContent;
            if (phone !== "Ko'rsatilmagan") {
                copyToClipboard(phone, this);
            }
        });
    }
});

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Lazy loading uchun
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            }
        });
    });
    
    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Console da chiroyli xabar
console.log('%c🚀 Admin Panel', 'color: #6366f1; font-size: 24px; font-weight: bold;');
console.log('%cProfil sahifasi muvaffaqiyatli yuklandi!', 'color: #10b981; font-size: 14px;');