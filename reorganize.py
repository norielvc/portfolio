from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

work_list = soup.find('div', id='work-list')
if work_list:
    # Find all work items anywhere in the document
    all_items = soup.find_all('div', class_='work-item')
    
    # Sort them by data-index
    all_items.sort(key=lambda x: int(x.get('data-index', 0)) if x.get('data-index') else 0)
    
    # Empty the work_list
    work_list.clear()
    
    # Append them back in order
    for item in all_items:
        # Extract removes it from its current position in the tree
        extracted = item.extract()
        work_list.append(extracted)

# Clean up duplicate modals
modals = soup.find_all('div', id='project-modal')
for i in range(1, len(modals)):
    modals[i].decompose()

# Clean up duplicate contact sections
contacts = soup.find_all('section', id='contact')
for i in range(len(contacts) - 1): # keep the last one, as it was properly appended
    contacts[i].decompose()

# Clean up duplicate footers
footers = soup.find_all('footer', class_='footer')
for i in range(len(footers) - 1):
    footers[i].decompose()

# Update project count
count_span = soup.find('span', class_='projects-count')
if count_span:
    count_span.string = '15'

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("index.html structure fixed!")
