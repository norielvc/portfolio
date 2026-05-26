with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\styles.css', encoding='utf-8') as f:
    content = f.read()

content = content.replace('\r\n', '\n')

# Find the start of the corruption (the work responsive block that got garbled)
# and cut back to the clean work-nav-btn:hover closing brace
CUT_MARKER = '/* Responsive */\n@media (max-width: 1024px) {\n    .work-flex-layout {'

cut_pos = content.find(CUT_MARKER)
if cut_pos == -1:
    print("ERROR: cut marker not found")
    exit(1)

# Keep everything up to (not including) the marker
clean_base = content[:cut_pos]

# Append clean responsive block + full new services CSS
APPEND = '''/* Responsive */
@media (max-width: 1024px) {
    .work-flex-layout {
        flex-direction: column;
        text-align: center;
        gap: 40px;
    }
    .work-info-title { font-size: 3.5rem; }
    .work-slides-container p { margin: 0 auto 40px auto; }
    .work-nav-controls { justify-content: center; }
}

/* =========================================
   SERVICES SECTION — Two-State Design
   ========================================= */
section#services {
    background: #ffffff;
    color: #1a1a1a;
    overflow: hidden;
    position: relative;
}

.services-inner {
    position: relative;
    min-height: 600px;
    transition: min-height 0.7s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ---- Cover State ---- */
.services-cover {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 60px;
    padding: 100px 80px;
    max-width: 1300px;
    margin: 0 auto;
    opacity: 1;
    transform: translateY(0);
    transition: opacity 0.5s ease, transform 0.5s ease;
}

.services-cover.hidden {
    opacity: 0;
    transform: translateY(-30px);
    pointer-events: none;
    position: absolute;
    top: 0; left: 0; right: 0;
}

.svc-cover-text {
    flex: 1;
    max-width: 500px;
}

.svc-eyebrow {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 4px;
    color: #aaaaaa;
    margin-bottom: 16px;
    text-transform: uppercase;
}

.svc-cover-title {
    font-size: 5rem;
    font-weight: 900;
    line-height: 1;
    letter-spacing: -3px;
    color: #1a1a1a;
    margin-bottom: 24px;
}

.svc-cover-title em {
    font-style: italic;
    color: #888888;
    font-weight: 300;
}

.svc-cover-sub {
    font-size: 1.1rem;
    color: #666666;
    line-height: 1.6;
    margin-bottom: 40px;
    max-width: 380px;
}

.svc-explore-btn {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: #1a1a1a;
    color: #ffffff;
    border: none;
    padding: 16px 32px;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: inherit;
}

.svc-explore-btn:hover {
    background: #333333;
    transform: translateY(-3px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.15);
}

.svc-explore-btn svg {
    transition: transform 0.3s ease;
}

.svc-explore-btn:hover svg {
    transform: translate(3px, -3px);
}

/* ---- Orbital Visual ---- */
.svc-orbital-wrapper {
    flex: 1;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 520px;
}

.svc-orbital-svg {
    width: 100%;
    height: auto;
    overflow: visible;
}

.svc-sun {
    animation: svcSunPulse 3s ease-in-out infinite;
    transform-origin: 250px 180px;
}

.svc-sun-pulse {
    animation: svcSunPulse 3s ease-in-out infinite 0.5s;
    transform-origin: 250px 180px;
}

.svc-sun-pulse2 {
    animation: svcSunPulse 3s ease-in-out infinite 1s;
    transform-origin: 250px 180px;
}

@keyframes svcSunPulse {
    0%, 100% { opacity: 0.4; transform: scale(1); }
    50% { opacity: 0.9; transform: scale(1.1); }
}

.orb-ring-1  { animation: orbSpin 14s linear infinite; transform-origin: 250px 180px; }
.orb-ring-2  { animation: orbSpin 22s linear infinite; transform-origin: 250px 180px; }
.orb-ring-3  { animation: orbSpin 28s linear infinite reverse; transform-origin: 250px 180px; }
.orb-ring-1b { animation: orbSpin 18s linear infinite reverse; transform-origin: 250px 180px; }
.orb-ring-2b { animation: orbSpin 32s linear infinite; transform-origin: 250px 180px; }
.orb-ring-3b { animation: orbSpin 20s linear infinite; transform-origin: 250px 180px; }

@keyframes orbSpin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

.svc-orbit-labels {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-top: 24px;
}

.svc-orbit-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: #bbbbbb;
    padding: 6px 14px;
    border: 1px solid #e5e5e5;
    border-radius: 50px;
    transition: all 0.3s ease;
    cursor: default;
}

.svc-orbit-label.active {
    color: #ffffff;
    border-color: #1a1a1a;
    background: #1a1a1a;
}

/* ---- Detail (Card) State ---- */
.services-detail {
    padding: 80px 80px 100px;
    max-width: 1300px;
    margin: 0 auto;
    opacity: 0;
    transform: translateY(40px);
    pointer-events: none;
    position: absolute;
    top: 0; left: 0; right: 0;
    transition: opacity 0.5s ease 0.2s, transform 0.5s ease 0.2s;
}

.services-detail.visible {
    opacity: 1;
    transform: translateY(0);
    pointer-events: all;
    position: relative;
}

.svc-detail-header {
    display: flex;
    align-items: center;
    gap: 24px;
    margin-bottom: 60px;
}

.svc-back-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: none;
    border: 1px solid #e0e0e0;
    color: #1a1a1a;
    padding: 10px 20px;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    font-family: inherit;
}

.svc-back-btn:hover {
    background: #1a1a1a;
    color: #ffffff;
    border-color: #1a1a1a;
}

.svc-detail-title {
    font-size: 2.5rem;
    font-weight: 800;
    letter-spacing: -1px;
    color: #1a1a1a;
}

.svc-detail-title em {
    font-style: italic;
    color: #888888;
    font-weight: 300;
}

/* ---- Service Cards ---- */
.services-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}

.service-card {
    background: #ffffff;
    border: 1px solid #eeeeee;
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
    position: relative;
    overflow: hidden;
}

.service-card::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0%;
    height: 2px;
    background: #1a1a1a;
    transition: width 0.4s ease;
}

.service-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
    border-color: #d0d0d0;
}

.service-card:hover::after {
    width: 100%;
}

.service-icon {
    width: 80px;
    height: 80px;
    background: #f7f7f7;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 24px auto;
    transition: all 0.4s ease;
}

.service-card:hover .service-icon {
    background: #1a1a1a;
    transform: scale(1.08);
}

.service-card:hover .svc-icon-svg .icon-path {
    stroke: #ffffff;
}

.service-card:hover .svc-icon-svg .icon-dot {
    fill: #ffffff;
}

.svc-icon-svg {
    width: 38px;
    height: 38px;
}

.svc-icon-svg .icon-path {
    stroke: #1a1a1a;
    stroke-width: 2;
    fill: none;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 300;
    stroke-dashoffset: 300;
    transition: stroke 0.3s ease;
}

.svc-icon-svg .icon-dot {
    fill: #1a1a1a;
    transition: fill 0.3s ease;
}

.services-detail.visible .svc-icon-svg .icon-path {
    animation: svcIconDraw 2.8s ease-in-out infinite;
}

.services-detail.visible .service-card:nth-child(1) .icon-path { animation-delay: 0.0s; }
.services-detail.visible .service-card:nth-child(2) .icon-path { animation-delay: 0.2s; }
.services-detail.visible .service-card:nth-child(3) .icon-path { animation-delay: 0.4s; }
.services-detail.visible .service-card:nth-child(4) .icon-path { animation-delay: 0.6s; }
.services-detail.visible .service-card:nth-child(5) .icon-path { animation-delay: 0.8s; }
.services-detail.visible .service-card:nth-child(6) .icon-path { animation-delay: 1.0s; }

@keyframes svcIconDraw {
    0%   { stroke-dashoffset: 300; opacity: 0.3; }
    40%  { stroke-dashoffset: 0;   opacity: 1; }
    70%  { stroke-dashoffset: 0;   opacity: 1; }
    100% { stroke-dashoffset: 300; opacity: 0.3; }
}

.service-card h3 {
    font-size: 1.2rem;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 12px;
}

.service-card > p {
    color: #777777;
    font-size: 0.9rem;
    line-height: 1.6;
}

/* Responsive */
@media (max-width: 1024px) {
    .services-cover { flex-direction: column; padding: 60px 40px; gap: 40px; text-align: center; }
    .svc-cover-title { font-size: 3.5rem; }
    .services-grid { grid-template-columns: repeat(2, 1fr); }
    .services-detail { padding: 60px 40px 80px; }
}

@media (max-width: 640px) {
    .svc-cover-title { font-size: 2.5rem; letter-spacing: -1.5px; }
    .services-grid { grid-template-columns: 1fr; }
    .services-detail { padding: 40px 20px 60px; }
}
'''

new_content = clean_base + APPEND

with open(r'C:\Users\SCREENS\OneDrive\Desktop\PORTFOLIO\styles.css', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(new_content)

print(f"SUCCESS — File is now {len(new_content.splitlines())} lines")
