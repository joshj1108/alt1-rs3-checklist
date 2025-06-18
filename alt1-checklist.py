from zipfile import ZipFile
from io import BytesIO

files = {
    "index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>RS3 Checklist</title>
  <link rel="stylesheet" href="styles.css">
  <script src="https://alt1.app/alt1lib.js"></script>
  <script>
    if (window.alt1) alt1.identifyAppUrl("./appconfig.json");
  </script>
</head>
<body>
  <h1>RS3 Checklist</h1>
  <div id="tabs">
    <button onclick="switchCategory('dailies')">Dailies</button>
    <button onclick="switchCategory('gathering')">Gathering</button>
    <button onclick="switchCategory('weeklies')">Weeklies</button>
    <button onclick="switchCategory('monthlies')">Monthlies</button>
    <button onclick="switchCategory('resources')">More Resources</button>
  </div>
  <div id="checklist"></div>
  <script src="app.js"></script>
</body>
</html>
''',
    "styles.css": '''body {
  font-family: Arial, sans-serif;
  background-color: #1e1e1e;
  color: white;
  padding: 20px;
}

#tabs {
  margin-bottom: 20px;
}

button {
  background-color: #333;
  color: white;
  border: none;
  padding: 10px;
  margin-right: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #555;
}

#checklist {
  margin-top: 20px;
}

.checklist-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.checklist-item input {
  margin-right: 10px;
}
''',
    "app.js": '''const categories = {
  dailies: ['Jack of Trades', 'Vis wax', 'Mine sandstone'],
  gathering: ['Crystal Tree', 'The Arc Contracts'],
  weeklies: ['Divine Locations', 'Sell to POF'],
  monthlies: ['Merchant ship'],
  resources: ['Alch Calc', 'Ports Calc', 'Rares Watchlist']
};

let currentCategory = 'dailies';

function switchCategory(category) {
  currentCategory = category;
  renderChecklist();
  loadProgress();
}

function renderChecklist() {
  const checklistDiv = document.getElementById('checklist');
  checklistDiv.innerHTML = '';

  categories[currentCategory].forEach(task => {
    const div = document.createElement('div');
    div.classList.add('checklist-item');

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.id = task;
    checkbox.onchange = saveProgress;

    const label = document.createElement('label');
    label.setAttribute('for', task);
    label.textContent = task;

    div.appendChild(checkbox);
    div.appendChild(label);
    checklistDiv.appendChild(div);
  });

  loadProgress();
}

function saveProgress() {
  const progress = {};
  document.querySelectorAll('.checklist-item input').forEach(input => {
    progress[input.id] = input.checked;
  });
  localStorage.setItem(currentCategory, JSON.stringify(progress));
}

function loadProgress() {
  const progress = JSON.parse(localStorage.getItem(currentCategory)) || {};
  document.querySelectorAll('.checklist-item input').forEach(input => {
    input.checked = progress[input.id] || false;
  });
}

// Initialize
renderChecklist();
''',
    "appconfig.json": '''{
  "name": "RS3 Daily Checklist",
  "description": "Checklists for RS3 dailies, weeklies, and more.",
  "author": "Your Name",
  "version": "1.0.0",
  "category": "Tools",
  "icon": "icon.png",
  "main": "index.html",
  "permissions": ["alt1"]
}
'''
}

with ZipFile("alt1-rs3-checklist.zip", "w") as zipf:
    for name, content in files.items():
        zipf.writestr(name, content)
