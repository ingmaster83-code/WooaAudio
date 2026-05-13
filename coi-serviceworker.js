// 더 이상 사용하지 않음 — 기존 등록 해제용 빈 서비스워커
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));
