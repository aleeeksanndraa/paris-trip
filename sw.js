// Offline support: the app, its data, fonts and the Leaflet library are kept on the phone.
// Map tiles you've already looked at are kept too; new areas need internet.
const APP = "paris-app-v5";
const TILES = "paris-tiles-v1";
const SHELL = ["./", "index.html", "data.js", "manifest.webmanifest", "icon-192.png", "icon-512.png", "icon-180.png",
  "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js",
  "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(APP).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => ![APP, TILES].includes(k)).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  // App files: try the network first so updates arrive, fall back to the saved copy.
  if (url.origin === location.origin) {
    e.respondWith(fetch(req).then(res => {
      const copy = res.clone(); caches.open(APP).then(c => c.put(req, copy)); return res;
    }).catch(() => caches.match(req).then(r => r || caches.match("index.html"))));
    return;
  }
  // Map tiles: saved copy first, refresh in the background.
  if (url.hostname === "tile.openstreetmap.org") {
    e.respondWith(caches.open(TILES).then(async c => {
      const hit = await c.match(req);
      const net = fetch(req).then(res => { if (res.ok) c.put(req, res.clone()); return res; }).catch(() => hit);
      return hit || net;
    }));
    return;
  }
  // Weather: network, with the app keeping its own last copy.
  if (url.hostname === "api.open-meteo.com") return;
  // Fonts and libraries: saved copy first.
  if (/fonts\.(googleapis|gstatic)\.com|cdnjs\.cloudflare\.com/.test(url.hostname)) {
    e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(res => {
      const copy = res.clone(); caches.open(APP).then(c => c.put(req, copy)); return res;
    })));
  }
});
