// Mobile Navigation Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');
const navLinks = document.querySelectorAll('.nav-link');

if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
        navMenu.classList.toggle('active');
    });

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
        });
    });
}

/* Smooth Scrolling */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#') return; // Skip links that are just '#'
        
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
            const navbarHeight = document.querySelector('.navbar')?.offsetHeight || 70;
            const targetTop = target.getBoundingClientRect().top + window.scrollY - navbarHeight;
            window.scrollTo({
                top: targetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Navbar Background on Scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(44, 62, 80, 0.95)';
        } else {
            navbar.style.background = 'var(--secondary-color)';
        }
    }
});

// Reveal Animation on Scroll
const revealObserverOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -50px 0px'
};

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
            revealObserver.unobserve(entry.target);
        }
    });
}, revealObserverOptions);

document.querySelectorAll('.reveal').forEach(el => {
    revealObserver.observe(el);
});


// Skill Bar Observer Options
const skillObserverOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

// Animate skill bars when visible
const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const skillFills = entry.target.querySelectorAll('.skill-fill');
            skillFills.forEach(fill => {
                const width = fill.style.width;
                fill.style.width = '0';
                setTimeout(() => {
                    fill.style.width = width;
                }, 100);
            });
            skillObserver.unobserve(entry.target);
        }
    });
}, skillObserverOptions);

const skillBars = document.querySelector('.skill-bars');
if (skillBars) {
    skillObserver.observe(skillBars);
}

// Form Submission
const contactForm = document.querySelector('#contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const submitBtn = document.getElementById('contact-submit');
        const feedback = document.getElementById('contact-feedback');

        // Clear previous feedback & errors
        feedback.className = 'contact-feedback';
        feedback.textContent = '';
        contactForm.querySelectorAll('.error').forEach(el => el.classList.remove('error'));

        // Basic validation
        let valid = true;
        const fields = contactForm.querySelectorAll('input[required], textarea[required]');
        fields.forEach(field => {
            if (!field.value.trim()) {
                field.classList.add('error');
                valid = false;
            }
        });

        const emailField = document.getElementById('contact-email');
        if (emailField && emailField.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailField.value)) {
            emailField.classList.add('error');
            valid = false;
        }

        if (!valid) {
            feedback.className = 'contact-feedback error';
            feedback.textContent = 'Please fill in all required fields correctly.';
            return;
        }

        // Loading state
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;

        // Simulate send (replace with real fetch/EmailJS/etc.)
        setTimeout(() => {
            submitBtn.classList.remove('loading');
            submitBtn.classList.add('sent');
            submitBtn.querySelector('.contact-submit-text').textContent = 'Message Sent!';
            submitBtn.querySelector('.contact-submit-icon').innerHTML = '<i class="fas fa-check"></i>';

            feedback.className = 'contact-feedback success';
            feedback.textContent = '✓ Your message has been sent. I\'ll get back to you within 24 hours.';

            contactForm.reset();

            // Reset button after a few seconds
            setTimeout(() => {
                submitBtn.classList.remove('sent');
                submitBtn.disabled = false;
                submitBtn.querySelector('.contact-submit-text').textContent = 'Send Message';
                submitBtn.querySelector('.contact-submit-icon').innerHTML = '<i class="fas fa-paper-plane"></i>';
            }, 4000);
        }, 1800);
    });

    // Remove error state on input
    contactForm.querySelectorAll('input, textarea').forEach(field => {
        field.addEventListener('input', () => field.classList.remove('error'));
    });
}

// Typing Animation for Professions
function initTyping() {
    const titleElement = document.querySelector('.typing-text');
    if (!titleElement) return;

    const titles = [
        'Full Stack Developer',
        'Web Developer',
        'AI-Powered Developer',
        'Business Solutions Expert'
    ];
    
    let titleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 150;

    function typeTitle() {
        const currentTitle = titles[titleIndex];
        
        if (isDeleting) {
            charIndex--;
            typingSpeed = 70;
        } else {
            charIndex++;
            typingSpeed = 150;
        }

        titleElement.innerHTML = currentTitle.substring(0, charIndex);

        if (!isDeleting && charIndex === currentTitle.length) {
            typingSpeed = 2500; // Longer pause at full word
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            titleIndex = (titleIndex + 1) % titles.length;
            typingSpeed = 500;
        }

        setTimeout(typeTitle, typingSpeed);
    }

    // Start after initial hero animations
    setTimeout(typeTitle, 2500);
}

// Robust start
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTyping);
} else {
    initTyping();
}

// Add active class to current nav link
window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('section');
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Parallax effect for hero section - REMOVED
// window.addEventListener('scroll', () => {
//     const hero = document.querySelector('.hero');
//     if (hero) {
//         const scrolled = window.pageYOffset;
//         hero.style.transform = `translateY(${scrolled * 0.5}px)`;
//     }
// });

// Hover effects are now handled efficiently in CSS via .project-card-inner

// Lazy loading for images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                img.classList.add('loaded');
                imageObserver.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img').forEach(img => {
        imageObserver.observe(img);
    });
}


// Project Modal Logic
const projectsData = [
    {
        title: "SaaS (brgyDesk)",
        about: "A comprehensive community management platform designed for local government units. Features automated document processing, resident records management, and real-time administrative dashboards.",
        image: "IMAGES/works/SaaS/0.png",
        images: ["IMAGES/works/SaaS/0.png", "IMAGES/works/SaaS/1.png", "IMAGES/works/SaaS/2.png", "IMAGES/works/SaaS/3.png", "IMAGES/works/SaaS/4.png", "IMAGES/works/SaaS/5.png"],
        bg: "https://images.unsplash.com/photo-1639322537228-f710d846310a?auto=format&fit=crop&q=80&w=1600",
        link: "#"
    },
    {
        title: "Time Logger System",
        about: "Enterprise attendance tracking solution with secure multi-factor authentication, GPS geolocation verification for field staff, and automated payroll integration.",
        image: "IMAGES/works/timelogger/1.png",
        images: ["IMAGES/works/timelogger/1.png", "IMAGES/works/timelogger/2.png"],
        bg: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1600",
        link: "#"
    },
    {
        title: "PTSI Website",
        about: "Modern corporate digital presence for PTSI. Focuses on high-performance architecture, responsive design, and professional brand storytelling.",
        image: "IMAGES/works/ptsi/1.png",
        images: ["IMAGES/works/ptsi/1.png", "IMAGES/works/ptsi/2.png", "IMAGES/works/ptsi/3.png", "IMAGES/works/ptsi/4.png", "IMAGES/works/ptsi/5.png"],
        bg: "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=1600",
        link: "#"
    },
    {
        title: "COCOSTUDIO Website",
        about: "Creative portfolio website for COCOSTUDIO. A visually-driven digital experience showcasing creative work with modern design and smooth interactions.",
        image: "IMAGES/works/cocostudio/cocostudio_1.png",
        images: [
            "IMAGES/works/cocostudio/cocostudio_1.png",
            "IMAGES/works/cocostudio/cocostudio_2.png",
            "IMAGES/works/cocostudio/cocostudio_3.png"
        ],
        bg: "IMAGES/works/cocostudio/cocostudio_1.png",
        link: "https://www.cocostudio.ph"
    },
    {
        title: "Company Intranet",
        about: "A secure, internal ecosystem for centralized employee collaboration, knowledge base management, and cross-departmental communication within a corporate environment.",
        image: "IMAGES/works/intranet/intranet.png",
        images: [
            "IMAGES/works/intranet/intranet.png",
            "IMAGES/works/intranet/intranet2.png",
            "IMAGES/works/intranet/intranet3.png"
        ],
        bg: "IMAGES/works/intranet/intranet.png",
        link: "#"
    },
    {
        title: "Paperless Automation",
        about: "Strategic digital transformation project that converted legacy manual processes into streamlined paperless workflows, increasing operational efficiency by over 40%.",
        image: "IMAGES/works/paperless/paperless1.png",
        images: [
            "IMAGES/works/paperless/paperless1.png",
            "IMAGES/works/paperless/paperless2.png",
            "IMAGES/works/paperless/paperless3.png"
        ],
        bg: "IMAGES/works/paperless/paperless1.png",
        link: "#"
    },
    {
        title: "Live Tracking & Analytics",
        about: "Real-time monitoring system featuring live count dashboards, asset tracking, and predictive analytics for operational logistics and security monitoring.",
        image: "IMAGES/works/livetracking/live1.png",
        images: [
            "IMAGES/works/livetracking/live1.png",
            "IMAGES/works/livetracking/live2.png",
            "IMAGES/works/livetracking/live3.png"
        ],
        bg: "IMAGES/works/livetracking/live1.png",
        link: "#"
    }
,
    {
        title: "PTSI Branch Support Portal",
        about: "A ticketing system for branch IT support requests within the Philippine Tuberculosis Society, designed to streamline issue resolution and minimize downtime across nationwide clinics.",
        image: "IMAGES/works/ptsi_portal/ptsi_portal_1_1779768604237.png",
        images: ["IMAGES/works/ptsi_portal/ptsi_portal_1_1779768604237.png", "IMAGES/works/ptsi_portal/ptsi_portal_2_1779768784774.png", "IMAGES/works/ptsi_portal/ptsi_portal_3_1779768907747.png"],
        bg: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1600",
        link: "#"
    },
    {
        title: "LVMH Cloud Service Desk",
        about: "An enterprise ticketing platform for cloud infrastructure issues, serving LVMH global operations. Features automated routing and SLA tracking for zero-downtime mission-critical services.",
        image: "IMAGES/works/lvmh/lvmh1.png",
        images: ["IMAGES/works/lvmh/lvmh1.png"],
        bg: "IMAGES/works/lvmh/lvmh1.png",
        link: "#"
    },
    {
        title: "Security Incident Response Tracker",
        about: "A secure ticketing system built for the Lopez Group, managing and documenting physical and digital security incidents in compliance with strict enterprise standards.",
        image: "IMAGES/works/ticketing/ticket1.png",
        images: [
            "IMAGES/works/ticketing/ticket1.png",
            "IMAGES/works/ticketing/ticket2.png",
            "IMAGES/works/ticketing/ticket3.png"
        ],
        bg: "IMAGES/works/ticketing/ticket1.png",
        link: "#"
    },
    {
        title: "TB Patient Analytics Database",
        about: "A secure, HIPAA-compliant database platform built for PTSI to aggregate patient data, visualize treatment pipelines, and accelerate reporting workflows.",
        image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800",
        images: ["https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800"],
        bg: "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&q=80&w=1600",
        link: "#"
    }
];

let currentProjIdx = 0;

function openProjectModal(idx) {
    currentProjIdx = idx;
    const modal = document.getElementById('project-modal');
    updateModalContent();
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeProjectModal() {
    const modal = document.getElementById('project-modal');
    modal.classList.remove('active');
    document.body.style.overflow = '';
}

function updateModalContent() {
    const data = projectsData[currentProjIdx];
    document.getElementById('modal-title').textContent = data.title;
    document.getElementById('modal-about').textContent = data.about;
    document.getElementById('modal-main-img').src = data.image;
    document.getElementById('modal-launch-link').href = data.link;
    document.getElementById('modal-curr-idx').textContent = currentProjIdx + 1;
    document.getElementById('modal-total-count').textContent = projectsData.length;

    // Set dynamic background photo on modal visual
    const modalVisual = document.querySelector('.modal-visual');
    if (modalVisual && data.bg) {
        modalVisual.style.backgroundImage = `url('${data.bg}')`;
        modalVisual.style.backgroundSize = 'cover';
        modalVisual.style.backgroundPosition = 'center';
    }

    // Populate gallery thumbnails if images array exists
    const gallery = document.getElementById('modal-gallery');
    if (gallery) {
        gallery.innerHTML = '';
        const imgs = data.images || [data.image];
        imgs.forEach((src, i) => {
            const thumb = document.createElement('img');
            thumb.src = src;
            thumb.alt = `${data.title} screenshot ${i + 1}`;
            thumb.className = 'modal-thumb' + (i === 0 ? ' active' : '');
            thumb.onclick = () => {
                const mainImg = document.getElementById('modal-main-img');
                mainImg.classList.add('switching');
                setTimeout(() => {
                    mainImg.src = src;
                    mainImg.onload = () => mainImg.classList.remove('switching');
                    setTimeout(() => mainImg.classList.remove('switching'), 600);
                    gallery.querySelectorAll('.modal-thumb').forEach(t => t.classList.remove('active'));
                    thumb.classList.add('active');
                }, 200);
            };
            gallery.appendChild(thumb);
        });
    }
}

function animateModalSwitch() {
    const content = document.querySelector('.modal-content');
    const visual = document.querySelector('.modal-visual');
    const details = document.querySelector('.modal-details');
    const mainImg = document.getElementById('modal-main-img');
    const targets = [content, visual, details, mainImg];
    targets.forEach(el => { if (el) el.classList.add('switching'); });
    setTimeout(() => {
        updateModalContent();
        requestAnimationFrame(() => {
            targets.forEach(el => { if (el) el.classList.remove('switching'); });
        });
    }, 200);
}

function nextProject() {
    currentProjIdx = (currentProjIdx + 1) % projectsData.length;
    animateModalSwitch();
}

function prevProject() {
    currentProjIdx = (currentProjIdx - 1 + projectsData.length) % projectsData.length;
    animateModalSwitch();
}

// Close modal on click outside
window.addEventListener('click', (e) => {
    const modal = document.getElementById('project-modal');
    if (e.target === modal) closeProjectModal();
});

// Attach click listeners to grid project cards
const gridCards = document.querySelectorAll('.projects-grid .project-card');
gridCards.forEach((card, idx) => {
    card.addEventListener('click', () => {
        if (typeof openProjectModal === 'function') {
            openProjectModal(idx);
        }
    });
});

// ─── Work List — Cursor Preview & Click to Open Modal ───
const workItems = document.querySelectorAll('.work-item');
const cursorPreview = document.getElementById('work-cursor-preview');
const cursorImg = document.getElementById('work-cursor-img');

let mouseX = 0, mouseY = 0;
let previewX = 0, previewY = 0;
let animFrame;

function animateCursor() {
    previewX += (mouseX - previewX) * 0.12;
    previewY += (mouseY - previewY) * 0.12;
    if (cursorPreview) {
        cursorPreview.style.left = (previewX - 160) + 'px';
        cursorPreview.style.top  = (previewY - 110) + 'px';
    }
    animFrame = requestAnimationFrame(animateCursor);
}
animateCursor();

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
});

workItems.forEach((item, idx) => {
    const data = projectsData[idx];
    if (!data) return;

    item.addEventListener('mouseenter', () => {
        if (cursorImg) cursorImg.src = data.image;
        if (cursorPreview) cursorPreview.classList.add('visible');
    });

    item.addEventListener('mouseleave', () => {
        if (cursorPreview) cursorPreview.classList.remove('visible');
    });

    item.addEventListener('click', () => {
        if (typeof openProjectModal === 'function') {
            openProjectModal(idx);
        }
    });
});

// ─── Hover Slideshow for Project Cards ───────────────────
gridCards.forEach((card, idx) => {
    const data = projectsData[idx];
    const imgContainer = card.querySelector('.project-image');
    if (!imgContainer || !data) return;

    const images = data.images || [data.image];

    // Build all slide images
    imgContainer.innerHTML = '';
    images.forEach((src, i) => {
        const img = document.createElement('img');
        img.src = src;
        img.alt = data.title;
        if (i === 0) img.classList.add('active-slide');
        imgContainer.appendChild(img);
    });

    let slideInterval = null;
    let currentSlide = 0;

    card.addEventListener('mouseenter', () => {
        if (images.length <= 1) return;
        slideInterval = setInterval(() => {
            const slides = imgContainer.querySelectorAll('img');
            slides[currentSlide].classList.remove('active-slide');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active-slide');
        }, 800);
    });

    card.addEventListener('mouseleave', () => {
        clearInterval(slideInterval);
        // Reset to first slide smoothly
        const slides = imgContainer.querySelectorAll('img');
        slides[currentSlide].classList.remove('active-slide');
        currentSlide = 0;
        slides[0].classList.add('active-slide');
    });
});


// Carousel logic removed; Recent Works now uses a standard CSS grid.

console.log('Portfolio loaded successfully!');

// ─── Cute Cyborg Gaze Tracking ───────────────────────────
(function() {
    // Track mouse globally
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;

    window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    // ── Hero cyborg (in .cute-cyborg-container) ──
    (function() {
        const pupils = document.querySelectorAll('.cute-cyborg-container .cyborg-eye-pupil');
        const reflections = document.querySelectorAll('.cute-cyborg-container .cyborg-eye-reflection');
        const cyborgContainer = document.querySelector('.cute-cyborg-container');

        if (!pupils.length || !cyborgContainer) return;

        let targetTX = 0, targetTY = 0, currentTX = 0, currentTY = 0;
        let faceX = 0, faceY = 0;

        function recalculate() {
            const rect = cyborgContainer.getBoundingClientRect();
            faceX = rect.left + rect.width / 2;
            faceY = rect.top + rect.height * 0.35;
        }

        window.addEventListener('resize', recalculate);
        window.addEventListener('scroll', recalculate, { passive: true });
        recalculate();
        setTimeout(recalculate, 500);

        function updateGaze() {
            const dx = mouseX - faceX;
            const dy = mouseY - faceY;
            const distance = Math.hypot(dx, dy);
            if (distance > 0) {
                const angle = Math.atan2(dy, dx);
                const scale = Math.min(6, distance / 40);
                targetTX = Math.cos(angle) * scale;
                targetTY = Math.sin(angle) * scale;
            } else {
                targetTX = 0; targetTY = 0;
            }
            currentTX += (targetTX - currentTX) * 0.15;
            currentTY += (targetTY - currentTY) * 0.15;
            pupils.forEach(p => p.style.transform = `translate(${currentTX}px, ${currentTY}px)`);
            reflections.forEach(r => r.style.transform = `translate(${currentTX * 0.7}px, ${currentTY * 0.7}px)`);
            requestAnimationFrame(updateGaze);
        }
        requestAnimationFrame(updateGaze);
    })();

    // ── Fixed HUD cyborgs (resume + projects panels) ──
    function initFixedCyborgGaze(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        const pupils     = container.querySelectorAll('.cyborg-eye-pupil');
        const reflections = container.querySelectorAll('.cyborg-eye-reflection');
        if (!pupils.length) return;

        let targetTX = 0, targetTY = 0, currentTX = 0, currentTY = 0;

        function getFacePos() {
            const svg = container.querySelector('.sticky-companion-bot');
            if (!svg) return { x: mouseX, y: mouseY };
            const rect = svg.getBoundingClientRect();
            return {
                x: rect.left + rect.width * 0.5,
                y: rect.top  + rect.height * 0.35
            };
        }

        function updateGaze() {
            // Only track when visible
            if (!container.classList.contains('visible')) {
                requestAnimationFrame(updateGaze);
                return;
            }
            const { x: faceX, y: faceY } = getFacePos();
            const dx = mouseX - faceX;
            const dy = mouseY - faceY;
            const distance = Math.hypot(dx, dy);
            if (distance > 0) {
                const angle = Math.atan2(dy, dx);
                const scale = Math.min(5, distance / 50);
                targetTX = Math.cos(angle) * scale;
                targetTY = Math.sin(angle) * scale;
            } else {
                targetTX = 0; targetTY = 0;
            }
            currentTX += (targetTX - currentTX) * 0.12;
            currentTY += (targetTY - currentTY) * 0.12;
            pupils.forEach(p => p.style.transform = `translate(${currentTX}px, ${currentTY}px)`);
            reflections.forEach(r => r.style.transform = `translate(${currentTX * 0.7}px, ${currentTY * 0.7}px)`);
            requestAnimationFrame(updateGaze);
        }
        requestAnimationFrame(updateGaze);
    }

    initFixedCyborgGaze('resume-cyborg-fixed');
    initFixedCyborgGaze('projects-cyborg-fixed');

})();


// Interactive Projects Slider Logic
(() => {
    const slider = document.getElementById('projects-slider');
    const track = document.getElementById('projects-track');
    
    if (!slider || !track) return;

    let isDown = false;
    let startX;
    let scrollLeft;
    
    // Physics variables
    let currentX = 0;
    let targetX = 0;
    let bounds = { max: 0, min: 0 };
    let reqId;

    const calculateBounds = () => {
        bounds.min = -(track.scrollWidth - slider.clientWidth + (window.innerWidth * 0.1));
        if (bounds.min > 0) bounds.min = 0;
    };

    window.addEventListener('resize', calculateBounds);
    // Initial calculate needs to wait for images/CSS to load
    setTimeout(calculateBounds, 500);

    const onPointerDown = (e) => {
        isDown = true;
        slider.style.cursor = 'grabbing';
        startX = e.pageX || (e.touches && e.touches[0].pageX);
        scrollLeft = targetX;
        
        // Prevent default only if mouse to avoid breaking scroll on mobile
        if(e.type === 'mousedown') e.preventDefault();
    };

    const onPointerUp = () => {
        isDown = false;
        slider.style.cursor = 'grab';
    };

    const onPointerMove = (e) => {
        if (!isDown) return;
        const x = e.pageX || (e.touches && e.touches[0].pageX);
        const walk = (x - startX) * 2; // Momentum multiplier
        targetX = scrollLeft + walk;
    };

    slider.addEventListener('mousedown', onPointerDown);
    slider.addEventListener('mouseleave', onPointerUp);
    slider.addEventListener('mouseup', onPointerUp);
    slider.addEventListener('mousemove', onPointerMove);

    slider.addEventListener('touchstart', onPointerDown, { passive: true });
    slider.addEventListener('touchend', onPointerUp);
    slider.addEventListener('touchmove', onPointerMove, { passive: true });

    // Render loop for smooth lerp
    const render = () => {
        // Enforce soft bounds
        if (targetX > bounds.max) targetX += (bounds.max - targetX) * 0.2;
        if (targetX < bounds.min) targetX += (bounds.min - targetX) * 0.2;

        // Lerp interpolation for buttery smoothness
        currentX += (targetX - currentX) * 0.08;

        // Force hardware acceleration with translate3d
        track.style.transform = `translate3d(${currentX}px, 0, 0)`;

        reqId = requestAnimationFrame(render);
    };

    render();
})();

// About Section Explore Logic
function resetAboutViews() {
    const views = ['about-default-view', 'about-explore-view', 'about-love-view', 'about-core-view', 'about-work-view'];
    views.forEach(id => {
        const el = document.getElementById(id);
        if(el) el.classList.remove('active-view');
    });
}

// Scroll to the top of the about section after a view switch
function scrollToAbout() {
    const aboutSection = document.getElementById('about');
    if (!aboutSection) return;
    const navbarHeight = document.querySelector('.navbar')?.offsetHeight || 70;
    const top = aboutSection.getBoundingClientRect().top + window.scrollY - navbarHeight;
    window.scrollTo({ top, behavior: 'smooth' });
}

function toggleExplore(event) {
    if(event) event.preventDefault();
    resetAboutViews();
    const exploreView = document.getElementById('about-explore-view');
    if(exploreView) exploreView.classList.add('active-view');
    scrollToAbout();
}

// Love view (carousel / scroller) logic
let currentLoveIdx = 0;
const loveTitles = [
    "CLEAN CODE",
    "CREATIVE DESIGN",
    "PROBLEM SOLVING",
    "AI & ROBOTICS",
    "SPEED & PERFORMANCE",
    "SHARING KNOWLEDGE",
    "MODULAR ARCHITECTURE",
    "MINIMALISM",
    "CONTINUOUS LEARNING",
    "GAME OF THRONES",
    "COLLABORATION",
    "GOOD FOOD",
    "TRAVELING",
    "MUSIC"
];

function updateLoveCarousel() {
    const track = document.getElementById('love-track');
    const titleEl = document.getElementById('love-title');
    if (!track || !titleEl) return;
    
    const items = track.querySelectorAll('.love-item-icon');
    const total = items.length;
    
    items.forEach((item, idx) => {
        let diff = idx - currentLoveIdx;
        if (diff > total / 2) diff -= total;
        if (diff < -total / 2) diff += total;
        
        const absDiff = Math.abs(diff);
        
        if (absDiff <= 3) {
            item.style.opacity = 1 - absDiff * 0.25;
            const xOffset = diff * 110;
            const scale = 1.3 - absDiff * 0.2;
            item.style.transform = `translateX(${xOffset}px) scale(${scale})`;
            item.style.pointerEvents = absDiff === 0 ? 'all' : 'none';
            if (absDiff === 0) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        } else {
            item.style.opacity = 0;
            item.style.transform = `translateX(${diff * 110}px) scale(0.5)`;
            item.style.pointerEvents = 'none';
            item.classList.remove('active');
        }
    });
    
    titleEl.textContent = `I LOVE ${loveTitles[currentLoveIdx]}`;
}

function prevLoveItem() {
    currentLoveIdx = (currentLoveIdx - 1 + loveTitles.length) % loveTitles.length;
    updateLoveCarousel();
}

function nextLoveItem() {
    currentLoveIdx = (currentLoveIdx + 1) % loveTitles.length;
    updateLoveCarousel();
}

function openLoveView() {
    resetAboutViews();
    const v = document.getElementById('about-love-view');
    if(v) v.classList.add('active-view');
    currentLoveIdx = 0;
    updateLoveCarousel();
    scrollToAbout();
}

function closeLoveView() {
    toggleExplore();
}

// Core view (slideshow) logic
function setCoreSlide(idx) {
    const slides = document.querySelectorAll('.core-slide');
    const dots = document.querySelectorAll('.slide-dot');
    slides.forEach((slide, i) => {
        if (i === idx) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });
    dots.forEach((dot, i) => {
        if (i === idx) {
            dot.classList.add('active');
        } else {
            dot.classList.remove('active');
        }
    });
}

function openCoreView() {
    resetAboutViews();
    const v = document.getElementById('about-core-view');
    if(v) v.classList.add('active-view');
    setCoreSlide(0);
    scrollToAbout();
}

function closeCoreView() {
    toggleExplore();
}

// Work view (equalizer and slides) logic
let currentWorkSlideIdx = 0;
const workSlides = [
    {
        title: "NEW MEDIA",
        desc: "My work crosses a broad range of categories in the digital space, both from a design and a technical perspective. I believe in using the right tools for the job.",
        activeBar: 0
    },
    {
        title: "SYSTEMS",
        desc: "Building robust backend microservices, automations, and APIs that scale. I enjoy designing architectures that can handle heavy lifting reliably.",
        activeBar: 1
    },
    {
        title: "DATABASES",
        desc: "Structuring efficient database schemas, query optimization, and secure data pipelines. Clean data relations are the bedrock of any solid application.",
        activeBar: 2
    },
    {
        title: "SECURITY",
        desc: "Implementing secure authentication mechanisms, threat modeling, and strict access controls to protect user data and resources.",
        activeBar: 3
    },
    {
        title: "AUTOMATION",
        desc: "Writing scripts and schedulers to eliminate manual overhead. Streamlining deployment pipelines and local environment configurations.",
        activeBar: 4
    }
];

function updateWorkSlides() {
    const titleEl = document.getElementById('work-slide-title');
    const descEl = document.getElementById('work-slide-desc');
    const bars = document.querySelectorAll('.data-equalizer .eq-bar');
    if (!titleEl || !descEl) return;
    
    const slide = workSlides[currentWorkSlideIdx];
    
    titleEl.style.opacity = 0;
    titleEl.style.transform = 'translateY(10px)';
    descEl.style.opacity = 0;
    descEl.style.transform = 'translateY(10px)';
    
    setTimeout(() => {
        titleEl.textContent = slide.title;
        descEl.textContent = slide.desc;
        titleEl.style.opacity = 1;
        titleEl.style.transform = 'translateY(0)';
        descEl.style.opacity = 1;
        descEl.style.transform = 'translateY(0)';
    }, 200);
    
    bars.forEach((bar, idx) => {
        if (idx === slide.activeBar) {
            bar.classList.add('active');
        } else {
            bar.classList.remove('active');
        }
    });
}

function prevWorkSlide() {
    currentWorkSlideIdx = (currentWorkSlideIdx - 1 + workSlides.length) % workSlides.length;
    updateWorkSlides();
}

function nextWorkSlide() {
    currentWorkSlideIdx = (currentWorkSlideIdx + 1) % workSlides.length;
    updateWorkSlides();
}

function openWorkView() {
    resetAboutViews();
    const v = document.getElementById('about-work-view');
    if(v) v.classList.add('active-view');
    currentWorkSlideIdx = 0;
    updateWorkSlides();
    scrollToAbout();
}

function closeWorkView() {
    toggleExplore();
}

// ── Services Section: Cover ↔ Detail Toggle ──────────────────────────────────

let svcCarouselIndex = 0;
const SVC_CARDS_PER_VIEW = 3; // cards visible at once

function openServicesView() {
    const cover  = document.getElementById('services-cover');
    const detail = document.getElementById('services-detail');
    if (!cover || !detail) return;

    cover.classList.add('hidden');
    detail.classList.add('visible');

    // Reset carousel to first position
    svcCarouselIndex = 0;
    _applySvcCarousel();

    // Scroll to services section top
    const servicesSection = document.getElementById('services');
    if (servicesSection) {
        const navbarHeight = document.querySelector('.navbar')?.offsetHeight || 70;
        const top = servicesSection.getBoundingClientRect().top + window.scrollY - navbarHeight;
        window.scrollTo({ top, behavior: 'smooth' });
    }
}

function closeServicesView() {
    const cover  = document.getElementById('services-cover');
    const detail = document.getElementById('services-detail');
    if (!cover || !detail) return;

    detail.classList.remove('visible');
    cover.classList.remove('hidden');
}

function moveSvcCarousel(dir) {
    const grid  = document.getElementById('svc-grid');
    if (!grid) return;

    const isMobile = window.innerWidth <= 968;
    const cardsPerView = isMobile ? 1 : SVC_CARDS_PER_VIEW;
    const totalCards = grid.children.length;
    const maxIndex   = Math.max(0, totalCards - cardsPerView);

    // Wrap around — loop from last back to first and vice versa
    if (dir > 0 && svcCarouselIndex >= maxIndex) {
        svcCarouselIndex = 0;
    } else if (dir < 0 && svcCarouselIndex <= 0) {
        svcCarouselIndex = maxIndex;
    } else {
        svcCarouselIndex += dir;
    }

    _applySvcCarousel();
}

function _applySvcCarousel() {
    const grid = document.getElementById('svc-grid');
    if (!grid) return;

    const isMobile = window.innerWidth <= 968;
    const cardsPerView = isMobile ? 1 : SVC_CARDS_PER_VIEW;
    const viewport = grid.parentElement; // .svc-carousel-viewport
    const viewportWidth = viewport.offsetWidth;
    const cardWidth = isMobile ? viewportWidth : viewportWidth / cardsPerView;
    const gap = isMobile ? 0 : 24;
    const offset = svcCarouselIndex * (cardWidth + gap);

    grid.style.transform = `translateX(-${offset}px)`;

    // Update nav button states
    const prevBtn = document.querySelector('.svc-carousel-nav.prev');
    const nextBtn = document.querySelector('.svc-carousel-nav.next');
    const totalCards = grid.children.length;
    const maxIndex = Math.max(0, totalCards - cardsPerView);

    if (prevBtn) prevBtn.style.opacity = svcCarouselIndex === 0 ? '0.3' : '1';
    if (nextBtn) nextBtn.style.opacity = svcCarouselIndex >= maxIndex ? '0.3' : '1';
}

// ── Mobile Hero Quote Ticker ──────────────────────────────────────────────────

(function () {
    const quotes = [
        '"I built a live TB patient tracking system and an HR attendance logger — giving organizations real-time visibility they never had before."',
        '"I built a full company intranet — centralizing internal tools, announcements, and workflows into one secure, organization-wide platform."',
        '"I launched a Barangay SaaS platform — residents request certificates online, officials process them digitally, billed monthly. Government, modernized."',
        '"I design and build interactive, professional websites — crafted to impress, convert, and represent your brand at its best."',
        '"I eliminated paper entirely — every internal request, approval, and workflow is now fully digital, automated, and trackable in real time."',
        '"I am your AI expert — tell me what you need and I\'ll build it. Faster delivery, smarter systems, and results that actually move your business forward."'
    ];

    let mqIdx = 0;
    let mqTimer = null;

    function initMobileTicker() {
        const textEl = document.getElementById('mq-text');
        const dotsEl = document.getElementById('mq-dots');
        if (!textEl || !dotsEl) return;

        // Only run on mobile
        if (window.innerWidth > 968) return;

        function setQuote(idx) {
            const dots = dotsEl.querySelectorAll('.mq-dot');

            // Fade out
            textEl.classList.add('fade-out');

            setTimeout(() => {
                textEl.textContent = quotes[idx];
                textEl.classList.remove('fade-out');
                textEl.classList.add('fade-in');

                // Force reflow then fade in
                requestAnimationFrame(() => {
                    requestAnimationFrame(() => {
                        textEl.classList.remove('fade-in');
                    });
                });

                // Update dots
                dots.forEach((d, i) => d.classList.toggle('active', i === idx));
            }, 400);
        }

        function advance() {
            mqIdx = (mqIdx + 1) % quotes.length;
            setQuote(mqIdx);
        }

        // Start auto-rotate every 4s
        mqTimer = setInterval(advance, 4000);

        // Allow tap to advance manually
        const ticker = document.getElementById('mobile-quote-ticker');
        if (ticker) {
            ticker.style.pointerEvents = 'all';
            ticker.addEventListener('click', () => {
                clearInterval(mqTimer);
                advance();
                mqTimer = setInterval(advance, 4000);
            });
        }
    }

    // Init after DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMobileTicker);
    } else {
        initMobileTicker();
    }
})();

// ── Solar System Planet-Pin Hover Animation ───────────────────────────────────

(function () {
    const skillLabels = [
        'JAVASCRIPT', 'PYTHON', 'REACT', 'NEXT.JS',
        'NODE.JS', 'TYPESCRIPT', 'MONGODB', 'SQL', 'DOCKER'
    ];

    let pinTimer      = null;
    let activePlanet  = null;   // the actual DOM element being tracked
    let trackingRaf   = null;   // requestAnimationFrame handle

    function initPlanetPins() {
        const svg       = document.getElementById('svc-solar-svg');
        const pin       = document.getElementById('planet-pin');
        const pinLabel  = document.getElementById('planet-pin-label');
        const orbitLabels = document.querySelectorAll('.svc-orbit-label');

        if (!svg || !pin || !pinLabel) return;

        const wrapper = svg.closest('.svc-orbital-wrapper') || svg.parentElement;

        // ── Continuously move pin to planet's current position ──
        function trackPin() {
            if (!activePlanet) return;

            const rect        = activePlanet.getBoundingClientRect();
            const wrapperRect = wrapper.getBoundingClientRect();

            // Centre of the planet relative to the wrapper
            const x = rect.left + rect.width  / 2 - wrapperRect.left;
            const y = rect.top  + rect.height / 2 - wrapperRect.top;

            pin.style.left = x + 'px';
            pin.style.top  = y + 'px';

            trackingRaf = requestAnimationFrame(trackPin);
        }

        function showPin(planetEl, idx) {
            activePlanet = planetEl;
            pinLabel.textContent = skillLabels[idx] || '';

            // Show + sprout
            pin.classList.add('visible');
            requestAnimationFrame(() => pin.classList.add('sprouting'));

            // Start live tracking
            cancelAnimationFrame(trackingRaf);
            trackPin();

            // Highlight orbit label
            orbitLabels.forEach((lbl, i) => lbl.classList.toggle('active', i === idx));

            // Highlight planet
            document.querySelectorAll('.svc-planet').forEach((p, i) => {
                p.classList.toggle('highlighted', i === idx);
            });
        }

        function hidePin() {
            activePlanet = null;
            cancelAnimationFrame(trackingRaf);

            pin.classList.remove('sprouting');
            setTimeout(() => pin.classList.remove('visible'), 350);

            orbitLabels.forEach((lbl, i) => lbl.classList.toggle('active', i === 0));
            document.querySelectorAll('.svc-planet').forEach(p => p.classList.remove('highlighted'));
        }

        // ── Attach hover + touch to each planet ──
        for (let i = 0; i < skillLabels.length; i++) {
            const planet = document.getElementById('planet-' + i);
            if (!planet) continue;

            planet.addEventListener('mouseenter', () => {
                clearTimeout(pinTimer);
                showPin(planet, i);
            });
            planet.addEventListener('mouseleave', () => {
                clearTimeout(pinTimer);
                pinTimer = setTimeout(hidePin, 200);
            });

            planet.addEventListener('touchstart', (e) => {
                e.preventDefault();
                clearTimeout(pinTimer);
                showPin(planet, i);
                pinTimer = setTimeout(hidePin, 2000);
            }, { passive: false });
        }

        // ── Orbit label clicks ──
        orbitLabels.forEach((lbl, i) => {
            lbl.addEventListener('click', () => {
                const planet = document.getElementById('planet-' + i);
                if (planet) {
                    clearTimeout(pinTimer);
                    showPin(planet, i);
                    pinTimer = setTimeout(hidePin, 2500);
                }
            });
        });

        // ── Auto-cycle when idle ──
        let autoCycleIdx = 0;
        const autoCycle = setInterval(() => {
            if (activePlanet !== null) return;   // user is hovering — skip

            const planet = document.getElementById('planet-' + autoCycleIdx);
            if (planet) {
                showPin(planet, autoCycleIdx);
                clearTimeout(pinTimer);
                pinTimer = setTimeout(hidePin, 1800);
            }
            autoCycleIdx = (autoCycleIdx + 1) % skillLabels.length;
        }, 2500);

        // Stop auto-cycle when cover hides
        const coverEl = document.getElementById('services-cover');
        if (coverEl) {
            new MutationObserver(() => {
                if (coverEl.classList.contains('hidden')) clearInterval(autoCycle);
            }).observe(coverEl, { attributes: true, attributeFilter: ['class'] });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initPlanetPins);
    } else {
        initPlanetPins();
    }
})();

// ── Sticky Cyborg Tour Guide — Dialog & Scan Animation ───────────────────────

(function () {

    // Section-specific rotating messages
    const sectionMessages = {
        resume: [
            'Scanning portfolio data...',
            '12 years of experience detected.',
            'Loading operation logs...',
            'System capabilities: ONLINE.',
            'Analyzing career trajectory...',
            'Enterprise deployments: confirmed.',
        ],
        services: [
            'Scanning service modules...',
            'Real projects. Real results.',
            'All systems operational.',
            'Select a service to explore.',
            'Built for scale and speed.',
            'AI-powered development: ACTIVE.',
        ],
        projects: [
            'Loading project archive...',
            'Click any project to explore.',
            'Real systems. Real impact.',
            'From SaaS to enterprise infra.',
            'Government. Healthcare. Cloud.',
            'Every project ships to production.',
        ]
    };

    let messageTimers = {};   // one interval per cyborg instance

    function startDialog(container, section) {
        const dialogBox  = container.querySelector('.cyborg-dialog-box, .cyborg-hud-panel');
        const dialogText = container.querySelector('.dialog-text');
        const bot        = container.querySelector('.cyborg-bot');

        if (!dialogBox || !dialogText) return;

        const messages = sectionMessages[section] || ['System online...'];
        let msgIdx = 0;

        // Show dialog immediately
        dialogBox.classList.add('active');

        // Rotate messages every 3.5s
        function showNextMessage() {
            dialogText.style.opacity = '0';
            dialogText.style.transform = 'translateY(4px)';

            setTimeout(() => {
                dialogText.textContent = messages[msgIdx];
                msgIdx = (msgIdx + 1) % messages.length;
                dialogText.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
                dialogText.style.opacity = '1';
                dialogText.style.transform = 'translateY(0)';
            }, 300);
        }

        // Set first message
        dialogText.textContent = messages[0];
        msgIdx = 1;

        // Clear any existing timer for this section
        if (messageTimers[section]) clearInterval(messageTimers[section]);
        messageTimers[section] = setInterval(showNextMessage, 3500);

        // Click bot to cycle message immediately
        if (bot && !bot._tourGuideWired) {
            bot._tourGuideWired = true;
            bot.addEventListener('click', () => showNextMessage());
        }
    }

    function stopDialog(container, section) {
        const dialogBox = container.querySelector('.cyborg-dialog-box, .cyborg-hud-panel');
        if (dialogBox) dialogBox.classList.remove('active');
        if (messageTimers[section]) {
            clearInterval(messageTimers[section]);
            delete messageTimers[section];
        }
    }

    function initCyborgTourGuides() {
        // Only observe cyborg instances that are IN the document flow (not fixed overlays)
        const instances = document.querySelectorAll('.cyborg-instance:not(.resume-cyborg-fixed)');
        if (!instances.length) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                const container = entry.target;
                const section   = container.dataset.section || 'resume';

                if (entry.isIntersecting) {
                    startDialog(container, section);
                } else {
                    stopDialog(container, section);
                }
            });
        }, {
            threshold: 0.3,
            rootMargin: '0px 0px -50px 0px'
        });

        instances.forEach(el => observer.observe(el));
    }

    // Expose to global scope so fixed panel observer can call them
    window.startDialog = startDialog;
    window.stopDialog  = stopDialog;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCyborgTourGuides);
    } else {
        initCyborgTourGuides();
    }

})();

// ── Resume & Projects Cyborg Fixed Panels — show/hide + dialog ───────────────

(function () {
    function isInView(el) {
        const rect = el.getBoundingClientRect();
        // Section must occupy at least 20% of the viewport height to count
        const visibleHeight = Math.min(rect.bottom, window.innerHeight) - Math.max(rect.top, 0);
        return visibleHeight > window.innerHeight * 0.2;
    }

    const pairs = [
        { sectionId: 'resume',   cyborgId: 'resume-cyborg-fixed' },
        { sectionId: 'projects', cyborgId: 'projects-cyborg-fixed' }
    ];

    // Sections that should HIDE the cyborg when they are in view
    const exclusions = ['services', 'about', 'contact'];

    function checkCyborgs() {
        // Check if any exclusion section is dominating the viewport
        const excludeActive = exclusions.some(id => {
            const el = document.getElementById(id);
            if (!el) return false;
            return isInView(el);
        });

        pairs.forEach(({ sectionId, cyborgId }) => {
            const section = document.getElementById(sectionId);
            const cyborg  = document.getElementById(cyborgId);
            if (!section || !cyborg) return;

            const inView = isInView(section) && !excludeActive;

            if (inView && !cyborg.classList.contains('visible')) {
                cyborg.classList.add('visible');
                window.startDialog && window.startDialog(cyborg, sectionId);
            } else if (!inView && cyborg.classList.contains('visible')) {
                cyborg.classList.remove('visible');
                window.stopDialog && window.stopDialog(cyborg, sectionId);
            }
        });
    }

    function init() {
        checkCyborgs();
        window.addEventListener('scroll', checkCyborgs, { passive: true });
        window.addEventListener('resize', checkCyborgs, { passive: true });
        setTimeout(checkCyborgs, 300);
        setTimeout(checkCyborgs, 800);
        setTimeout(checkCyborgs, 1500);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
