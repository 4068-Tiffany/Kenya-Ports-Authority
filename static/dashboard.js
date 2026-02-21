var map = L.map('map').setView([-1.286389, 36.817223], 12); // Nairobi

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

L.marker([-1.286389, 36.817223]).addTo(map)
  .bindPopup("Traffic HQ - Nairobi")
  .openPopup();
