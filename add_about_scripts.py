import os

js_code = """
// About Section Explore Logic
function resetAboutViews() {
    const views = ['about-default-view', 'about-explore-view', 'about-love-view', 'about-core-view', 'about-work-view'];
    views.forEach(id => {
        const el = document.getElementById(id);
        if(el) el.classList.remove('active-view');
    });
}

function toggleExplore(event) {
    if(event) event.preventDefault();
    resetAboutViews();
    const exploreView = document.getElementById('about-explore-view');
    if(exploreView) exploreView.classList.add('active-view');
}

function openLoveView() {
    resetAboutViews();
    const v = document.getElementById('about-love-view');
    if(v) v.classList.add('active-view');
}

function openCoreView() {
    resetAboutViews();
    const v = document.getElementById('about-core-view');
    if(v) v.classList.add('active-view');
}

function openWorkView() {
    resetAboutViews();
    const v = document.getElementById('about-work-view');
    if(v) v.classList.add('active-view');
}
"""

with open('script.js', 'a', encoding='utf-8') as f:
    f.write(js_code)

print("About scripts appended!")
