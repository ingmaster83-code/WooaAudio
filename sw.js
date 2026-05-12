const CACHE_NAME = 'wooa-audio-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/css/style.css',
  '/js/pwa-install.js',
  '/audio-convert.html',
  '/video-to-audio.html',
  '/audio-trim.html',
  '/audio-merge.html',
  '/audio-volume.html',
  '/audio-fade.html',
  '/audio-speed.html',
  '/audio-waveform.html',
  '/audio-bpm.html',
  '/audio-info.html',
  '/audio-recorder.html',
  '/screen-audio.html',
  '/about.html',
  '/privacy.html',
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(res => {
        if (res && res.status === 200 && res.type === 'basic') {
          const clone = res.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(e.request, clone));
        }
        return res;
      }).catch(() => caches.match('/index.html'));
    })
  );
});
