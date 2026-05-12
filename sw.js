const CACHE_NAME = 'wooa-audio-v2';
const STATIC_ASSETS = [
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
  '/about.html',
  '/privacy.html',
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(STATIC_ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// COOP/COEP 헤더 주입 - FFmpeg.wasm SharedArrayBuffer 활성화
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;

  e.respondWith(
    fetch(e.request).then(resp => {
      // 헤더 추가가 필요한 응답에만 적용
      const newHeaders = new Headers(resp.headers);
      newHeaders.set('Cross-Origin-Opener-Policy', 'same-origin');
      newHeaders.set('Cross-Origin-Embedder-Policy', 'require-corp');

      return new Response(resp.body, {
        status: resp.status,
        statusText: resp.statusText,
        headers: newHeaders,
      });
    }).catch(() => {
      // 네트워크 실패 시 캐시에서
      return caches.match(e.request).then(cached => cached || caches.match('/index.html'));
    })
  );
});
