// ============================================
// DASHBOARD JAVASCRIPT - Modern Admin Panel
// ============================================

document.addEventListener('DOMContentLoaded', function() {

    // ============================================
    // 1. SIDEBAR TOGGLE (Mobile)
    // ============================================
    const menuToggle = document.getElementById('menuToggle');
    const sidebar = document.getElementById('sidebar');

    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', function() {
            sidebar.classList.toggle('active');

            // Backdrop qo'shish (mobile uchun)
            if (sidebar.classList.contains('active')) {
                createBackdrop();
            } else {
                removeBackdrop();
            }
        });
    }

    function createBackdrop() {
        const backdrop = document.createElement('div');
        backdrop.className = 'sidebar-backdrop';
        backdrop.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 999;
            animation: fadeIn 0.3s ease;
        `;

        backdrop.addEventListener('click', function() {
            sidebar.classList.remove('active');
            removeBackdrop();
        });

        document.body.appendChild(backdrop);
    }

    function removeBackdrop() {
        const backdrop = document.querySelector('.sidebar-backdrop');
        if (backdrop) {
            backdrop.remove();
        }
    }

    // Window resize da backdrop o'chirish
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('active');
            removeBackdrop();
        }
    });


    // ============================================
    // 2. THEME TOGGLE (Dark/Light Mode)
    // ============================================
    const themeToggle = document.getElementById('themeToggle');
    const body = document.body;

    // LocalStorage dan theme'ni olish
    const currentTheme = localStorage.getItem('theme') || 'light';

    // Sahifa yuklanganda theme'ni o'rnatish
    if (currentTheme === 'dark') {
        body.classList.add('dark-theme');
        updateThemeIcon('sun');
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            body.classList.toggle('dark-theme');

            // Theme'ni saqlash
            if (body.classList.contains('dark-theme')) {
                localStorage.setItem('theme', 'dark');
                updateThemeIcon('sun');
                showNotification('Qorong\'i rejim yoqildi', 'success');
            } else {
                localStorage.setItem('theme', 'light');
                updateThemeIcon('moon');
                showNotification('Yorug\' rejim yoqildi', 'success');
            }
        });
    }

    function updateThemeIcon(icon) {
        const iconElement = themeToggle.querySelector('i');
        if (iconElement) {
            iconElement.className = icon === 'sun' ? 'fas fa-sun' : 'fas fa-moon';
        }
    }


    // ============================================
    // 3. ACTIVE MENU ITEM
    // ============================================
    const navItems = document.querySelectorAll('.nav-item');
    const currentPath = window.location.pathname;

    navItems.forEach(item => {
        const href = item.getAttribute('href');

        // Active klassni olib tashlash
        item.classList.remove('active');

        // Joriy sahifaga mos kelsa active qo'shish
        if (href && currentPath.includes(href) && href !== '/') {
            item.classList.add('active');
        }

        // Hover effect
        item.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s ease';
        });
    });


    // ============================================
    // 4. STAT CARDS ANIMATION
    // ============================================
    const statCards = document.querySelectorAll('.stat-card');

    // Intersection Observer - ko'ringanda animate qilish
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 100);

                // Raqamlarni animate qilish
                animateNumber(entry.target);
            }
        });
    }, observerOptions);

    statCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        observer.observe(card);
    });

    // Raqamlarni animate qilish funksiyasi
    function animateNumber(card) {
        const numberElement = card.querySelector('.stat-number');
        if (!numberElement) return;

        const finalNumber = parseInt(numberElement.textContent) || 0;
        const duration = 1000; // 1 soniya
        const steps = 50;
        const increment = finalNumber / steps;
        let current = 0;

        const timer = setInterval(() => {
            current += increment;
            if (current >= finalNumber) {
                numberElement.textContent = finalNumber;
                clearInterval(timer);
            } else {
                numberElement.textContent = Math.floor(current);
            }
        }, duration / steps);
    }


    // ============================================
    // 5. NOTIFICATION SYSTEM
    // ============================================
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: white;
            padding: 15px 20px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            z-index: 10000;
            display: flex;
            align-items: center;
            gap: 12px;
            animation: slideInRight 0.3s ease;
            max-width: 350px;
        `;

        const colors = {
            success: '#10b981',
            error: '#ef4444',
            warning: '#f59e0b',
            info: '#3b82f6'
        };

        const icons = {
            success: 'fa-check-circle',
            error: 'fa-times-circle',
            warning: 'fa-exclamation-triangle',
            info: 'fa-info-circle'
        };

        notification.innerHTML = `
            <i class="fas ${icons[type]}" style="color: ${colors[type]}; font-size: 24px;"></i>
            <span style="flex: 1; color: #333;">${message}</span>
            <button onclick="this.parentElement.remove()" style="background: none; border: none; cursor: pointer; font-size: 18px; color: #999;">
                <i class="fas fa-times"></i>
            </button>
        `;

        document.body.appendChild(notification);

        // 5 soniyadan keyin o'chirish
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 5000);
    }

    // CSS animation qo'shish
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from {
                transform: translateX(400px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        @keyframes slideOutRight {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(400px);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);


    // ============================================
    // 6. SMOOTH SCROLL
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
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


    // ============================================
    // 7. LOADING STATE
    // ============================================
    const links = document.querySelectorAll('a:not([target="_blank"])');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.getAttribute('href') && !this.getAttribute('href').startsWith('#')) {
                // Loading indicator ko'rsatish
                showLoadingIndicator();
            }
        });
    });

    function showLoadingIndicator() {
        const loader = document.createElement('div');
        loader.id = 'pageLoader';
        loader.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            z-index: 99999;
            animation: loadingBar 1s ease-in-out infinite;
        `;

        document.body.appendChild(loader);
    }

    const loadingStyle = document.createElement('style');
    loadingStyle.textContent = `
        @keyframes loadingBar {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
    `;
    document.head.appendChild(loadingStyle);


    // ============================================
    // 8. TOOLTIP
    // ============================================
    const tooltipElements = document.querySelectorAll('[data-tooltip]');

    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'custom-tooltip';
            tooltip.textContent = this.getAttribute('data-tooltip');
            tooltip.style.cssText = `
                position: absolute;
                background: #333;
                color: white;
                padding: 8px 12px;
                border-radius: 6px;
                font-size: 13px;
                z-index: 10000;
                pointer-events: none;
                white-space: nowrap;
            `;

            document.body.appendChild(tooltip);

            const rect = this.getBoundingClientRect();
            tooltip.style.top = (rect.top - tooltip.offsetHeight - 10) + 'px';
            tooltip.style.left = (rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2)) + 'px';

            this.addEventListener('mouseleave', function() {
                tooltip.remove();
            }, { once: true });
        });
    });


    // ============================================
    // 9. SEARCH FUNCTIONALITY (Agar kerak bo'lsa)
    // ============================================
    const searchInput = document.getElementById('searchInput');

    if (searchInput) {
        let searchTimeout;

        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);

            searchTimeout = setTimeout(() => {
                const query = this.value.toLowerCase();

                // Bu yerda AJAX search qilishingiz mumkin
                console.log('Qidiruv:', query);

                // Misol: stat cards ni filtrlash
                statCards.forEach(card => {
                    const text = card.textContent.toLowerCase();
                    if (text.includes(query)) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }, 300);
        });
    }


    // ============================================
    // 10. KEYBOARD SHORTCUTS
    // ============================================
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + K - Qidiruv
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            if (searchInput) {
                searchInput.focus();
            }
        }

        // Ctrl/Cmd + B - Sidebar toggle
        if ((e.ctrlKey || e.metaKey) && e.key === 'b') {
            e.preventDefault();
            if (sidebar) {
                sidebar.classList.toggle('active');
            }
        }

        // Esc - Sidebar yopish
        if (e.key === 'Escape') {
            if (sidebar && sidebar.classList.contains('active')) {
                sidebar.classList.remove('active');
                removeBackdrop();
            }
        }
    });


    // ============================================
    // 11. PAGE VISIBILITY (Tab change detection)
    // ============================================
    document.addEventListener('visibilitychange', function() {
        if (document.hidden) {
            console.log('Foydalanuvchi boshqa tabga o\'tdi');
        } else {
            console.log('Foydalanuvchi qaytib keldi');
            // Malumotlarni yangilash mumkin
        }
    });


    // ============================================
    // 12. CONSOLE LOG (Development mode)
    // ============================================
    console.log('%c Dashboard Loaded! ', 'background: #6366f1; color: white; padding: 10px 20px; border-radius: 5px; font-size: 16px; font-weight: bold;');
    console.log('%c Version: 1.0.0 ', 'color: #8b5cf6; font-size: 12px;');

});


// ============================================
// UTILITY FUNCTIONS
// ============================================

// Vaqtni formatlash
function formatTime(date) {
    return new Intl.DateTimeFormat('uz-UZ', {
        hour: '2-digit',
        minute: '2-digit'
    }).format(date);
}

// Sanani formatlash
function formatDate(date) {
    return new Intl.DateTimeFormat('uz-UZ', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(date);
}

// Raqamni formatlash
function formatNumber(num) {
    return new Intl.NumberFormat('uz-UZ').format(num);
}

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}