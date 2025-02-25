// service-worker.js
const CACHE_NAME = 'mymoney-cache-v1';
const urlsToCache = [
  '/',
  '/static/css/styles.css',
  '/static/python/main.py',
  '/static/js/brython.js',
  '/static/js/brython_stdlib.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});