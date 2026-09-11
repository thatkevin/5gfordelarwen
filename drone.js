/* ============================================================
   THE DRONE — ambient low hum for the pages beneath the waterline.
   Autoplay is blocked, so it's a toggle. Injects its own button.
   ============================================================ */
(function(){
  var d={ctx:null,nodes:[],master:null,on:false};
  function btnUpd(){
    var b=document.getElementById("dronebtn"); if(!b) return;
    b.innerHTML = d.on ? "&#9673; drone: on" : "&#9675; drone: off";
    b.style.color = d.on ? "#7fae7f" : "#3a5a3a";
  }
  function start(){
    try{
      var AC=window.AudioContext||window.webkitAudioContext; if(!AC) return;
      d.ctx=d.ctx||new AC();
      if(d.ctx.state==="suspended" && d.ctx.resume) d.ctx.resume();
      // iOS Safari: unlock audio with a 1-frame silent buffer inside the gesture
      try{ var ub=d.ctx.createBuffer(1,1,22050), us=d.ctx.createBufferSource(); us.buffer=ub; us.connect(d.ctx.destination); us.start(0); }catch(e){}
      var t=d.ctx.currentTime;
      var master=d.ctx.createGain();
      master.gain.setValueAtTime(0.0001,t);
      master.gain.linearRampToValueAtTime(0.06,t+3.5); // slow swell in
      master.connect(d.ctx.destination);
      // a low, slightly detuned chord = unease without melody
      var freqs=[55,55.4,82.4,110.3,164.7];
      var oscs=[];
      for(var i=0;i<freqs.length;i++){
        var o=d.ctx.createOscillator(); o.type="sine"; o.frequency.value=freqs[i];
        var og=d.ctx.createGain(); og.gain.value=(i>2?0.4:1.0);
        o.connect(og); og.connect(master); o.start(); oscs.push(o);
      }
      // very slow "breathing" LFO on the master level
      var lfo=d.ctx.createOscillator(); lfo.type="sine"; lfo.frequency.value=0.05;
      var lg=d.ctx.createGain(); lg.gain.value=0.025;
      lfo.connect(lg); lg.connect(master.gain); lfo.start();
      d.nodes=oscs.concat([lfo]); d.master=master; d.on=true;
      try{ localStorage.setItem("dalarwen_drone","on"); }catch(e){}
      btnUpd();
    }catch(e){}
  }
  function stop(){
    try{
      if(d.master&&d.ctx){ d.master.gain.linearRampToValueAtTime(0.0001,d.ctx.currentTime+0.8); }
      var arr=d.nodes;
      setTimeout(function(){ for(var i=0;i<arr.length;i++){ try{ arr[i].stop(); arr[i].disconnect(); }catch(e){} } },900);
    }catch(e){}
    d.nodes=[]; d.on=false;
    try{ localStorage.setItem("dalarwen_drone","off"); }catch(e){}
    btnUpd();
  }
  function toggle(){ if(d.on) stop(); else start(); }
  function inject(){
    if(document.getElementById("dronebtn")) return;
    var b=document.createElement("button");
    b.id="dronebtn"; b.type="button"; b.onclick=toggle;
    b.style.cssText="position:fixed;left:calc(10px + env(safe-area-inset-left));"+
      "bottom:calc(20px + env(safe-area-inset-bottom));z-index:2147483000;font-family:'Courier New',monospace;"+
      "font-size:13px;min-height:44px;background:#0a0a0a;color:#3a5a3a;border:1px solid #1f2a1f;padding:9px 13px;"+
      "cursor:pointer;letter-spacing:1px;touch-action:manipulation;-webkit-tap-highlight-color:transparent;-webkit-appearance:none;";
    document.body.appendChild(b);
    btnUpd();
  }
  if(document.body) inject(); else window.addEventListener("load",inject);
})();
