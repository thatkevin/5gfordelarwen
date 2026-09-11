/* Dalarwen 5G — offline service worker.
   Pre-caches the whole site so it runs with no internet (ironically, for Dalarwen).
   Bump CACHE when content changes to force an update on next online visit. */
var CACHE = "dalarwen-offline-v8";
var ASSETS = [
  "./",
  "404.html",
  "about-dalarwen.html",
  "above.html",
  "adventure.html",
  "arcade.html",
  "bees.html",
  "careers.html",
  "clifftop-caravans.html",
  "credits.html",
  "downloads.html",
  "faq.html",
  "free-up-lewis.html",
  "guestbook.html",
  "index.html",
  "infinite-walks.html",
  "isamsj.html",
  "jencorp.html",
  "keep-dalarwen-dark.html",
  "lewis.html",
  "manifesto.html",
  "matrix.html",
  "men-of-harlech.html",
  "org-chart.html",
  "patwa.html",
  "radiation.html",
  "sam.html",
  "signal-test.html",
  "sitemap.html",
  "static.html",
  "the-corridor.html",
  "the-cube.html",
  "the-division.html",
  "the-quiet.html",
  "towers.html",
  "tv-licence.html",
  "webring.html",
  "ring/bees-invented-5g.html",
  "ring/big-candle.html",
  "ring/conservatory-weather.html",
  "ring/coventry.html",
  "ring/cube-told-me-so.html",
  "ring/educated-stupid.html",
  "ring/electric-sheep-paper.html",
  "ring/held-toward-belgium.html",
  "ring/hull.html",
  "ring/lewis-dot-mov.html",
  "ring/loo-standing-society.html",
  "ring/nans-wifi-guide.html",
  "ring/nazca-peru.html",
  "ring/norfolk-mythology.html",
  "ring/pyramids-5g.html",
  "ring/ramblers-lying.html",
  "ring/rotisserie-nan.html",
  "ring/scouse-5g.html",
  "ring/silence-premium.html",
  "ring/spite-tower-13.html",
  "downloads/merger-presentation.html",
  "retro.css",
  "retro.js",
  "dark.css",
  "drone.js",
  "gate.js",
  "ring/ring.js",
  "favicon.svg",
  "favicon.ico",
  "favicon-32.png",
  "apple-touch-icon.png",
  "icon-192.png",
  "icon-512.png",
  "manifest.webmanifest",
  "assets/alien.gif",
  "assets/bee.gif",
  "assets/construction.gif",
  "assets/cube3d.gif",
  "assets/dancer.gif",
  "assets/email.gif",
  "assets/fire_bar.gif",
  "assets/flame.gif",
  "assets/globe.gif",
  "assets/heart.gif",
  "assets/loading.gif",
  "assets/newblink.gif",
  "assets/radiation.gif",
  "assets/signal_waves.gif",
  "assets/spin5g.gif",
  "assets/star.gif",
  "assets/stars.gif",
  "assets/tower.gif",
  "game-art/win1.png",
  "game-art/win2.png",
  "game-art/win3.png",
  "game-art/win4.png",
  "game-art/win5.png"
];
self.addEventListener("install", function(e){
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function(c){
    return Promise.all(ASSETS.map(function(u){
      return c.add(new Request(u, {cache:"reload"})).catch(function(){ });
    }));
  }));
});
self.addEventListener("activate", function(e){
  e.waitUntil(caches.keys().then(function(keys){
    return Promise.all(keys.map(function(k){ if(k!==CACHE) return caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});
self.addEventListener("fetch", function(e){
  if(e.request.method!=="GET") return;
  var url=new URL(e.request.url);
  if(url.origin!==location.origin) return;
  e.respondWith(
    caches.match(e.request, {ignoreSearch:true}).then(function(hit){
      if(hit) return hit;
      return fetch(e.request).then(function(net){
        try{ var copy=net.clone(); caches.open(CACHE).then(function(c){ c.put(e.request, copy); }); }catch(err){}
        return net;
      }).catch(function(){
        if(e.request.mode==="navigate") return caches.match("index.html", {ignoreSearch:true});
        return new Response("", {status:504, statusText:"offline"});
      });
    })
  );
});
