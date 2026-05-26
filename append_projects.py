import re
import os

projects = [
    {
        "title": "PTSI Branch Support Portal",
        "category": "IT_TICKETING_SYSTEM",
        "status": "DEPLOYED",
        "stack": "FULL-STACK + CLOUD",
        "about": "A ticketing system for branch IT support requests within the Philippine Tuberculosis Society, designed to streamline issue resolution and minimize downtime across nationwide clinics.",
        "image": "IMAGES/works/ptsi_portal/ptsi_portal_1_1779768604237.png",
        "images": "[\"IMAGES/works/ptsi_portal/ptsi_portal_1_1779768604237.png\", \"IMAGES/works/ptsi_portal/ptsi_portal_2_1779768784774.png\", \"IMAGES/works/ptsi_portal/ptsi_portal_3_1779768907747.png\"]",
        "bg": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=1600"
    },
    {
        "title": "LVMH Cloud Service Desk",
        "category": "ENTERPRISE_TICKETING",
        "status": "DEPLOYED",
        "stack": "CLOUD_INFRASTRUCTURE",
        "about": "An enterprise ticketing platform for cloud infrastructure issues, serving LVMH global operations. Features automated routing and SLA tracking for zero-downtime mission-critical services.",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=800",
        "images": "[\"https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=800\"]",
        "bg": "https://images.unsplash.com/photo-1558655146-d09347e92766?auto=format&fit=crop&q=80&w=1600"
    },
    {
        "title": "Security Incident Response Tracker",
        "category": "SECURITY_MANAGEMENT",
        "status": "DEPLOYED",
        "stack": "CYBERSECURITY",
        "about": "A secure ticketing system built for the Lopez Group, managing and documenting physical and digital security incidents in compliance with strict enterprise standards.",
        "image": "https://images.unsplash.com/photo-1510511459019-5d01a80f00ed?auto=format&fit=crop&q=80&w=800",
        "images": "[\"https://images.unsplash.com/photo-1510511459019-5d01a80f00ed?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1510511459019-5d01a80f00ed?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1510511459019-5d01a80f00ed?auto=format&fit=crop&q=80&w=800\"]",
        "bg": "https://images.unsplash.com/photo-1614064641913-6b71a2ea4514?auto=format&fit=crop&q=80&w=1600"
    },
    {
        "title": "PTSI Medical Supply Inventory",
        "category": "INVENTORY_SYSTEM",
        "status": "ACTIVE",
        "stack": "NODEJS + MONGODB",
        "about": "A comprehensive system designed to track and forecast medical supplies and equipment levels across PTSI branches, utilizing predictive data analysis to prevent shortages.",
        "image": "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&q=80&w=800",
        "images": "[\"https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&q=80&w=800\"]",
        "bg": "https://images.unsplash.com/photo-1530497610245-94d3c16cda28?auto=format&fit=crop&q=80&w=1600"
    },
    {
        "title": "Global Cloud Asset Manager",
        "category": "ASSET_MANAGEMENT",
        "status": "DEPLOYED",
        "stack": "PYTHON + CLOUD",
        "about": "An advanced inventory hub managing thousands of hybrid cloud assets and server instances for Cloudterrain, ensuring optimal resource allocation and cost reduction.",
        "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=800",
        "images": "[\"https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=800\"]",
        "bg": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1600"
    },
    {
        "title": "Security Hardware Tracking",
        "category": "HARDWARE_INVENTORY",
        "status": "DEPLOYED",
        "stack": "SQL + FULL-STACK",
        "about": "An inventory system logging the lifecycle of surveillance cameras and biometric access control hardware across IBEST deployment sites.",
        "image": "https://images.unsplash.com/photo-1555664424-778a1e5e1b48?auto=format&fit=crop&q=80&w=800",
        "images": "[\"https://images.unsplash.com/photo-1555664424-778a1e5e1b48?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1555664424-778a1e5e1b48?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1555664424-778a1e5e1b48?auto=format&fit=crop&q=80&w=800\"]",
        "bg": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&q=80&w=1600"
    },
    {
        "title": "TB Patient Analytics Database",
        "category": "DATABASE_ANALYTICS",
        "status": "DEPLOYED",
        "stack": "DATA_ANALYSIS",
        "about": "A secure, HIPAA-compliant database platform built for PTSI to aggregate patient data, visualize treatment pipelines, and accelerate reporting workflows.",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800",
        "images": "[\"https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800\"]",
        "bg": "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?auto=format&fit=crop&q=80&w=1600"
    },
    {
        "title": "Distributed Telemetry DB",
        "category": "CLOUD_DATABASE",
        "status": "DEPLOYED",
        "stack": "SYSTEM_ENGINEERING",
        "about": "A highly-scalable database architecture capturing real-time telemetry from hybrid cloud infrastructures, built during my tenure as Senior System Engineer at Cloudterrain.",
        "image": "https://images.unsplash.com/photo-1666875753105-c63a6f3bdc86?auto=format&fit=crop&q=80&w=800",
        "images": "[\"https://images.unsplash.com/photo-1666875753105-c63a6f3bdc86?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1666875753105-c63a6f3bdc86?auto=format&fit=crop&q=80&w=800\", \"https://images.unsplash.com/photo-1666875753105-c63a6f3bdc86?auto=format&fit=crop&q=80&w=800\"]",
        "bg": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80&w=1600"
    }
]

# 1. Update index.html
html_additions = ""
for i, proj in enumerate(projects):
    idx = 7 + i
    num = str(idx + 1).zfill(2)
    html_additions += f'''
                <div class="work-item" data-index="{idx}">
                    <div class="work-item-inner">
                        <span class="work-num">[{num}]</span>
                        <div class="work-title-wrap">
                            <h3 class="work-title">{proj["title"]}</h3>
                            <span class="work-category">> {proj["category"]}</span>
                        </div>
                        <div class="work-hud-data">
                            <span>STATUS: <em>{proj["status"]}</em></span>
                            <span>STACK: <em>{proj["stack"]}</em></span>
                        </div>
                        <span class="work-arrow">→</span>
                    </div>
                    <div class="work-hover-img">
                        <img class="img-gray" src="{proj["image"].replace('w=800', 'w=600')}" alt="{proj["title"]}">
                        <img class="img-color" src="{proj["image"].replace('w=800', 'w=600')}" alt="{proj["title"]}">
                    </div>
                </div>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find the end of the work-list
marker = '<!-- End of Work List -->'
if marker not in html_content:
    # Need to insert right after the last work-item
    # It ends with </div></div></div> (work-item, work-list, container)
    # Let's find the closing tag of work-list.
    # We will search for '<div class="work-list">' and then the closing div.
    # Alternatively, just inject after data-index="6"
    pass

import re
match = re.search(r'(<div class="work-item" data-index="6">.*?</div>\s+</div>\s+)(</div>\s+</section>)', html_content, re.DOTALL)
if match:
    new_html = html_content[:match.end(1)] + html_additions + match.group(2)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("index.html updated successfully!")
else:
    print("Failed to find insertion point in index.html")

# 2. Update script.js
js_additions = ""
for proj in projects:
    js_additions += f'''    {{
        title: "{proj["title"]}",
        about: "{proj["about"]}",
        image: "{proj["image"]}",
        images: {proj["images"]},
        bg: "{proj["bg"]}",
        link: "#"
    }},
'''

with open('script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Inject into projectsData array
js_match = re.search(r'(link:\s*"#"\s*}\s*)];', js_content)
if js_match:
    new_js = js_content[:js_match.end(1)] + ",\n" + js_additions.rstrip(',\n') + "\n];" + js_content[js_match.end():]
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("script.js updated successfully!")
else:
    print("Failed to find projectsData array end in script.js")

