// ==================== MOBILE MENU ====================
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');
const navLinks = document.querySelectorAll('.nav-link');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
        document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
    });
}

// Close mobile menu when clicking on a link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        hamburger?.classList.remove('active');
        navMenu?.classList.remove('active');
        document.body.style.overflow = '';
    });
});

// Close mobile menu when clicking outside
document.addEventListener('click', (e) => {
    if (navMenu && hamburger && 
        !navMenu.contains(e.target) && 
        !hamburger.contains(e.target) &&
        navMenu.classList.contains('active')) {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
        document.body.style.overflow = '';
    }
});

// ==================== SMOOTH SCROLLING ====================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offset = 70;
            const targetPosition = target.offsetTop - offset;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ==================== NAVBAR SCROLL EFFECT ====================
const navbar = document.querySelector('.navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }

    lastScroll = currentScroll;
});

// ==================== ACTIVE NAV LINK ====================
function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');

    window.addEventListener('scroll', () => {
        const scrollY = window.pageYOffset;

        sections.forEach(section => {
            const sectionHeight = section.offsetHeight;
            const sectionTop = section.offsetTop - 100;
            const sectionId = section.getAttribute('id');
            const navLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);

            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                navLinks.forEach(link => link.classList.remove('active'));
                navLink?.classList.add('active');
            }
        });
    });
}

updateActiveNavLink();

// ==================== SCROLL TO TOP BUTTON ====================
function createScrollToTopButton() {
    if (document.querySelector('.scroll-top')) return;

    const scrollTop = document.createElement('div');
    scrollTop.className = 'scroll-top';
    scrollTop.innerHTML = '↑';
    document.body.appendChild(scrollTop);

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 400) {
            scrollTop.classList.add('show');
        } else {
            scrollTop.classList.remove('show');
        }
    });

    scrollTop.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

createScrollToTopButton();

// ==================== INTERSECTION OBSERVER ====================
function setupScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
            }
        });
    }, observerOptions);

    const elementsToAnimate = document.querySelectorAll('.timeline-card, .skill-category, .project-card, .contact-card-link');
    elementsToAnimate.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
}

setupScrollAnimations();

// ==================== PROFILE IMAGE ANIMATION ====================
function animateProfileImage() {
    const profileImg = document.querySelector('.profile-img');

    if (profileImg) {
        profileImg.addEventListener('mouseenter', () => {
            profileImg.style.animation = 'pulse 1s ease-in-out';
        });

        profileImg.addEventListener('animationend', () => {
            profileImg.style.animation = '';
        });
    }
}

animateProfileImage();

// ==================== PARALLAX EFFECT ====================
function setupParallax() {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        const heroContent = document.querySelector('.hero-content');
        const heroImage = document.querySelector('.hero-image');

        if (hero && scrolled < window.innerHeight) {
            if (heroContent) {
                heroContent.style.transform = `translateY(${scrolled * 0.2}px)`;
            }
            if (heroImage) {
                heroImage.style.transform = `translateY(${scrolled * 0.1}px)`;
            }
        }
    });
}

setupParallax();

// ==================== PROJECT CARDS HOVER EFFECT ====================
function setupProjectCards() {
    const projectCards = document.querySelectorAll('.project-card');

    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        });

        card.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;

            this.style.transform = `translateY(-8px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) rotateX(0) rotateY(0)';
        });
    });
}

setupProjectCards();

// ==================== SKILL ITEMS ANIMATION ====================
function animateSkills() {
    const skillItems = document.querySelectorAll('.skill-item');

    skillItems.forEach((skill, index) => {
        skill.style.animationDelay = `${index * 0.03}s`;

        skill.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)';
        });
    });
}

animateSkills();

// ==================== EMAIL COPY FUNCTIONALITY ====================
function setupEmailCopy() {
    const emailLinks = document.querySelectorAll('a[href^="mailto:"]');

    emailLinks.forEach(link => {
        link.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            const email = link.getAttribute('href').replace('mailto:', '');

            if (navigator.clipboard) {
                navigator.clipboard.writeText(email).then(() => {
                    showNotification('Email manzil nusxalandi!', 'success');
                }).catch(() => {
                    showNotification('Nusxalashda xatolik yuz berdi', 'error');
                });
            }
        });
    });
}

setupEmailCopy();

// ==================== NOTIFICATION SYSTEM ====================
function showNotification(message, type = 'success') {
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }

    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;

    notification.style.cssText = `
        position: fixed;
        top: 90px;
        right: 20px;
        background: ${type === 'success' ? 'linear-gradient(135deg, #3b82f6, #8b5cf6)' : 'linear-gradient(135deg, #ef4444, #dc2626)'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        font-weight: 600;
        z-index: 9999;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        animation: slideInRight 0.3s ease-out;
    `;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add notification animations CSS
const notificationStyles = document.createElement('style');
notificationStyles.textContent = `
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
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
`;
document.head.appendChild(notificationStyles);

// ==================== LAZY LOADING IMAGES ====================
function setupLazyLoading() {
    const images = document.querySelectorAll('img');

    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.style.opacity = '0';
                img.style.transition = 'opacity 0.5s ease';

                if (img.complete) {
                    img.style.opacity = '1';
                } else {
                    img.addEventListener('load', () => {
                        img.style.opacity = '1';
                    });
                }

                imageObserver.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

setupLazyLoading();

// ==================== EXTERNAL LINKS ====================
function setupExternalLinks() {
    const externalLinks = document.querySelectorAll('a[target="_blank"]');

    externalLinks.forEach(link => {
        link.setAttribute('rel', 'noopener noreferrer');
    });
}

setupExternalLinks();

// ==================== PERFORMANCE OPTIMIZATION ====================
function debounce(func, wait = 10) {
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

const debouncedScrollHandler = debounce(() => {
    // Scroll-dependent operations
}, 10);

window.addEventListener('scroll', debouncedScrollHandler);

// ==================== PAGE LOAD ANIMATION ====================
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';

    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);

    const preloader = document.querySelector('.preloader');
    if (preloader) {
        preloader.style.opacity = '0';
        setTimeout(() => preloader.remove(), 500);
    }
});

// ==================== KEYBOARD NAVIGATION ====================
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navMenu?.classList.contains('active')) {
        hamburger?.classList.remove('active');
        navMenu?.classList.remove('active');
        document.body.style.overflow = '';
    }
});

// ==================== EDUCATION & LANGUAGE ANIMATIONS ====================
function setupEducationLanguageAnimations() {
    const fadeElements = document.querySelectorAll('.education-column .timeline-card, .language-item');

    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    fadeElements.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
}

// ==================== LANGUAGE LEVEL PROGRESS ====================
function setupLanguageProgressBars() {
    const languageLevels = {
        'Beginner': 20,
        'Elementary': 40,
        'Pre-Intermediate': 55,
        'Intermediate': 70,
        'Advanced': 85,
        'Native': 100
    };

    document.querySelectorAll('.language-item').forEach(item => {
        const levelText = item.querySelector('.language-level')?.textContent?.trim();
        const levelPercent = languageLevels[levelText] || 0;

        const progressContainer = document.createElement('div');
        progressContainer.className = 'language-progress';

        const progressBar = document.createElement('div');
        progressBar.className = 'language-progress-bar';
        progressBar.style.width = '0%';

        progressContainer.appendChild(progressBar);
        item.appendChild(progressContainer);

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    progressBar.style.width = `${levelPercent}%`;
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        observer.observe(item);
    });
}

// ==================== INITIALIZE ALL FUNCTIONS ====================
document.addEventListener('DOMContentLoaded', () => {
    setupEducationLanguageAnimations();
    setupLanguageProgressBars();

    // Console welcome message
    console.log('%c👋 Assalomu alaykum! Portfolio saytimga xush kelibsiz!', 'color: #3b82f6; font-size: 20px; font-weight: bold; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);');
    console.log('%c🚀 Python Backend Developer', 'color: #8b5cf6; font-size: 16px; font-weight: 600;');
    console.log('%c💼 Portfolio loyihasi Django bilan yaratilgan', 'color: #10b981; font-size: 14px;');
    console.log('✅ Portfolio script successfully loaded!');
});

// ==================== TYPING EFFECT FOR HERO TITLE (OPTIONAL) ====================
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.textContent = '';

    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }

    type();
}

// Uncomment to enable typing effect
// const heroTitle = document.querySelector('.hero-title');
// if (heroTitle) {
//     const originalText = heroTitle.textContent;
//     typeWriter(heroTitle, originalText, 50);
// }

// ==================== SMOOTH REVEAL ON SCROLL ====================
function revealOnScroll() {
    const reveals = document.querySelectorAll('.fade-in');

    reveals.forEach(reveal => {
        const windowHeight = window.innerHeight;
        const revealTop = reveal.getBoundingClientRect().top;
        const revealPoint = 150;

        if (revealTop < windowHeight - revealPoint) {
            reveal.classList.add('show');
        }
    });
}

window.addEventListener('scroll', revealOnScroll);

// ==================== THEME TOGGLE (OPTIONAL) ====================
function createThemeToggle() {
    // Bu funksiyani kerak bo'lsa ishlatish mumkin
    const theme = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', theme);
}

// createThemeToggle();

// ==================== END OF SCRIPT ====================
console.log('📱 Mobile responsive: ✅');
console.log('🎨 Animations: ✅');
console.log('⚡ Performance optimized: ✅');
console.log('🔧 All features loaded successfully!');