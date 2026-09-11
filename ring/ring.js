/* The 5G Truth Webring — shared nav widget injected into #ring on each member site.
   Neutral retro strip so it reads the same on every era's theme. */
(function(){
  var RING=[
    {f:"cube-told-me-so.html",   t:"The Cube Told Me So"},
    {f:"bees-invented-5g.html",  t:"Bees Invented 5G"},
    {f:"held-toward-belgium.html",t:"Held Toward Belgium"},
    {f:"nans-wifi-guide.html",   t:"Nan's Wi-Fi Guide"},
    {f:"lewis-dot-mov.html",     t:"Lewis Dot Mov"},
    {f:"ramblers-lying.html",    t:"The Ramblers Are Lying"},
    {f:"big-candle.html",        t:"Big Candle ($WAX)"},
    {f:"silence-premium.html",   t:"Silence Premium Survivors"},
    {f:"spite-tower-13.html",    t:"Spite Tower 13 Fan Club"},
    {f:"rotisserie-nan.html",    t:"Rotisserie Nan Wellness"},
    {f:"conservatory-weather.html",t:"Conservatory Weather"},
    {f:"educated-stupid.html",   t:"Educated Stupid No More"},
    {f:"loo-standing-society.html",t:"The Loo Standing Society"},
    {f:"pyramids-5g.html",       t:"Pyramids Had 5G"},
    {f:"norfolk-mythology.html", t:"The Black Shuck Signal"},
    {f:"scouse-5g.html",         t:"The Scouse Signal Committee"},
    {f:"nazca-peru.html",        t:"Backpacking The Signal (Peru)"},
    {f:"hull.html",              t:"Hull: Our Own Signal"},
    {f:"coventry.html",          t:"Sent to Coventry"}
  ];
  var here=(location.pathname.split("/").pop())||"";
  var idx=0; for(var i=0;i<RING.length;i++){ if(RING[i].f===here){ idx=i; break; } }
  var prev=RING[(idx-1+RING.length)%RING.length];
  var next=RING[(idx+1)%RING.length];
  var rnd; do{ rnd=RING[Math.floor(Math.random()*RING.length)]; }while(rnd.f===here && RING.length>1);
  var el=document.getElementById("ring"); if(!el) return;
  el.innerHTML=
    '<div style="max-width:720px;margin:26px auto 8px;border:3px double #00cc44;background:#050505;color:#bfe;'+
    'font-family:\'Courier New\',monospace;font-size:12px;text-align:center;padding:10px;line-height:1.7;">'+
      '<div style="color:#ff5cd6;letter-spacing:2px;font-weight:bold;">◆ THE 5G TRUTH WEBRING ◆ member '+(idx+1)+' of '+RING.length+'</div>'+
      '<div style="margin-top:6px;">'+
        '<a href="'+prev.f+'" style="color:#5cf;">&laquo; '+prev.t+'</a>'+
        ' &nbsp;|&nbsp; <a href="'+rnd.f+'" style="color:#ffd94a;">RANDOM</a>'+
        ' &nbsp;|&nbsp; <a href="../webring.html" style="color:#9f9;">RING HUB</a>'+
        ' &nbsp;|&nbsp; <a href="'+next.f+'" style="color:#5cf;">'+next.t+' &raquo;</a>'+
      '</div>'+
      '<div style="margin-top:6px;color:#556;">a lovingly maintained ring of the internet\'s finest 5G truth sites &#8226; '+
        '<a href="../index.html" style="color:#8a8;">home</a></div>'+
    '</div>';
})();
