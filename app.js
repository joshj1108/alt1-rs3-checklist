const categories = {
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
