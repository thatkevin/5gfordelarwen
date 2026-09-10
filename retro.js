/* ============================================================
   DALARWEN 5G LIBERATION FRONT ⸻ SHARED SCRIPTS
   Countdown, nav, guestbook, petition, odometer, matrix rain,
   the spinny circle of despair, and assorted nonsense.
   ============================================================ */

/* ---------- shared NAV + FOOTER injection ---------- */
var PAGES = [
  ["index.html","HOME"],
  ["the-cube.html","THE CUBE"],
  ["towers.html","15 TOWERS"],
  ["radiation.html","RADIATION"],
  ["lewis.html","LEWIS HQ"],
  ["manifesto.html","MANIFESTO"],
  ["keep-dalarwen-dark.html","KEEP IT DARK"],
  ["arcade.html","ARCADE"],
  ["signal-test.html","SIGNAL TEST"],
  ["bees.html","THE BEES"],
  ["patwa.html","INNA PATWA"],
  ["faq.html","F.A.Q."],
  ["downloads.html","DOWNLOADS"],
  ["matrix.html","THE MATRIX"],
  ["guestbook.html","GUESTBOOK"],
  ["webring.html","WEBRING"]
];
function currentPage(){
  var p = location.pathname.split("/").pop();
  return (p==="" ? "index.html" : p);
}
function buildNav(){
  var el=document.getElementById("navbar"); if(!el) return;
  var here=currentPage(), html="";
  for(var i=0;i<PAGES.length;i++){
    var cls = PAGES[i][0]===here ? ' class="here"' : '';
    html += '<a href="'+PAGES[i][0]+'"'+cls+'>'+PAGES[i][1]+'</a>';
  }
  el.innerHTML=html;
}

/* ---------- COUNTDOWN to New Year ---------- */
function pad(n){ n=""+n; return n.length<2?"0"+n:n; }
function startCountdown(id){
  var el=document.getElementById(id); if(!el) return;
  function tick(){
    var now=new Date();
    var target=new Date(now.getFullYear()+1,0,1,0,0,0);
    var diff=target-now;
    var d=Math.floor(diff/86400000);
    var h=Math.floor((diff%86400000)/3600000);
    var m=Math.floor((diff%3600000)/60000);
    var s=Math.floor((diff%60000)/1000);
    el.innerHTML=d+"d "+pad(h)+":"+pad(m)+":"+pad(s);
  }
  tick(); setInterval(tick,1000);
}

/* ---------- localStorage helpers ---------- */
function lsGet(k,def){ try{ var v=localStorage.getItem(k); return v===null?def:v; }catch(e){ return def; } }
function lsSet(k,v){ try{ localStorage.setItem(k,v); }catch(e){} }

/* ---------- PETITION counter ---------- */
var PETITION_SEED=1447;
function renderPetition(){
  var extra=parseInt(lsGet("delarwen_signed","0"),10)||0;
  var total=PETITION_SEED+extra;
  var c=document.getElementById("sigcount"); if(c) c.innerHTML=total.toLocaleString();
  var pct=Math.min(99,3+Math.floor(total/40));
  var bar=document.getElementById("grw"); if(bar) bar.style.width=pct+"%";
  var gp=document.getElementById("grpct"); if(gp) gp.innerHTML=pct+"%";
  return total;
}
var PETITION_MSGS=[
  "THE CUBE ACKNOWLEDGES YOUR COURAGE. 14 towers to go... no wait, still 15. Always 15.",
  "SIGNAL DETECTED IN YOUR SOUL. Lewis felt that.",
  "A BEE JUST SMILED. You did that.",
  "THE OFFLINE INDUSTRIAL COMPLEX TREMBLES.",
  "Spotify heard you. It played one (1) second before buffering. PROGRESS."
];
function signPetition(){
  var extra=(parseInt(lsGet("delarwen_signed","0"),10)||0)+1;
  lsSet("delarwen_signed",""+extra);
  renderPetition();
  var t=document.getElementById("thanks");
  if(t) t.innerHTML=PETITION_MSGS[extra%PETITION_MSGS.length];
  var b=document.getElementById("signbtn");
  if(b) b.value=" DEMAND AGAIN (THE CUBE ALLOWS IT) ";
}
function spreadSignal(){
  var url=location.href.replace(/[^\/]*$/,"index.html");
  var text="I demand 15 (FIFTEEN) 5G towers for DALARWEN. Zero bars. Zero mercy. "+url;
  if(navigator.share){ navigator.share({title:"15 TOWERS FOR DALARWEN",text:text,url:url}); }
  else if(navigator.clipboard){ navigator.clipboard.writeText(text);
    var t=document.getElementById("thanks"); if(t) t.innerHTML="THE SIGNAL IS COPIED. NOW SPREAD IT."; }
}

/* ---------- VISITOR ODOMETER ---------- */
function initOdometer(id,base){
  var el=document.getElementById(id||"odometer"); if(!el) return;
  base=base||133700;
  var v=parseInt(lsGet("delarwen_visits","0"),10)||0;
  v+=1; lsSet("delarwen_visits",""+v);
  var shown=base+v, str=""+shown;
  while(str.length<7) str="0"+str;
  el.innerHTML=str;
}

/* ---------- GUESTBOOK (localStorage) ---------- */
var GUESTBOOK_SEED=[
  {name:"L3WIS_ONLINE",loc:"The Attic (still zero bars)",msg:"i cannot even SEE this message. i posted it from the hill. FIFTEEN TOWERS NOW. i have things to POST."},
  {name:"BeeQueen_Dalarwen",loc:"The Hive (zero bars, obviously)",msg:"we invented 5G. give us our frequency back. buzz buzz. <3"},
  {name:"xX_TruthSeeker_Xx",loc:"On the hill, facing Belgium",msg:"finally a site that GETS IT. the cube is real. i have seen the four corners. all zero. ALL of them."},
  {name:"nan",loc:"Kitchen (zero bars)",msg:"how do i turn the wifi on. the little man on the phone said i need a tower. i want 15."},
  {name:"SpotifyStreamer99",loc:"The Loo (zero, even standing on the cistern)",msg:"downgraded to Silence Premium. this is my villain origin story."}
];
function loadGuestbook(){
  var raw=lsGet("delarwen_guestbook",null);
  if(raw){ try{ return JSON.parse(raw); }catch(e){} }
  return GUESTBOOK_SEED.slice();
}
function saveGuestbook(arr){ lsSet("delarwen_guestbook",JSON.stringify(arr)); }
function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
function renderGuestbook(){
  var el=document.getElementById("gbentries"); if(!el) return;
  var arr=loadGuestbook(), html="";
  for(var i=0;i<arr.length;i++){
    var e=arr[i];
    html += '<table border="2" cellpadding="6" width="100%" bordercolor="#00FF00" style="margin-bottom:10px;background:#001400;">'+
      '<tr><td><font face="Arial Black" size="3" color="#00FFFF">&#9733; '+esc(e.name)+'</font>'+
      ' <font face="Times New Roman" size="2" color="#888">signing in from <i>'+esc(e.loc||"an undisclosed dead zone")+'</i></font><br>'+
      '<font face="Comic Sans MS" size="3" color="#FFFFFF">'+esc(e.msg)+'</font></td></tr></table>';
  }
  el.innerHTML=html;
  var c=document.getElementById("gbcount"); if(c) c.innerHTML=arr.length;
}
function submitGuestbook(){
  var n=document.getElementById("gbname").value.trim()||"Anonymous Coward";
  var l=document.getElementById("gbloc").value.trim();
  var m=document.getElementById("gbmsg").value.trim();
  if(!m){ alert("THE CUBE DEMANDS A MESSAGE. Say something about the towers."); return; }
  var arr=loadGuestbook();
  arr.unshift({name:n,loc:l,msg:m});
  if(arr.length>200) arr=arr.slice(0,200);
  saveGuestbook(arr);
  renderGuestbook();
  document.getElementById("gbmsg").value="";
  var s=document.getElementById("gbstatus");
  if(s) s.innerHTML="&#9989; SIGNED. Your truth is now etched into the localStorage of eternity.";
}

/* ---------- MATRIX RAIN (5G edition) ---------- */
function startMatrix(canvasId){
  var cv=document.getElementById(canvasId); if(!cv||!cv.getContext) return;
  var ctx=cv.getContext("2d");
  function size(){ cv.width=cv.clientWidth; cv.height=cv.clientHeight; }
  size(); window.addEventListener("resize",size);
  var glyphs="5G0110001010TOWERDALARWENｱｲｳｴｵﾊﾋﾌ01#@$%▲△●○◇◆∎".split("");
  var fs=16, cols=Math.floor(cv.width/fs), drops=[];
  for(var i=0;i<cols;i++) drops[i]=Math.random()*-40;
  function draw(){
    ctx.fillStyle="rgba(0,0,0,0.08)"; ctx.fillRect(0,0,cv.width,cv.height);
    ctx.font=fs+"px monospace";
    for(var i=0;i<drops.length;i++){
      var ch=glyphs[Math.floor(Math.random()*glyphs.length)];
      var x=i*fs, y=drops[i]*fs;
      ctx.fillStyle= Math.random()<0.02 ? "#FFFFFF" : "#00FF66";
      ctx.fillText(ch,x,y);
      if(y>cv.height && Math.random()>0.975) drops[i]=0;
      drops[i]++;
    }
  }
  setInterval(draw,55);
}

/* ---------- FAKE TERMINAL typewriter ---------- */
function typeTerminal(id,lines,done){
  var el=document.getElementById(id); if(!el) return;
  var li=0,ci=0;
  function step(){
    if(li>=lines.length){ if(done) done(); return; }
    var full=lines[li];
    el.innerHTML = el.innerHTML.replace(/<span class="cur">.*?<\/span>/,"");
    el.innerHTML += full.charAt(ci);
    ci++;
    if(ci>=full.length){ el.innerHTML+="\n"; li++; ci=0; setTimeout(step,300); }
    else setTimeout(step,18+Math.random()*40);
  }
  step();
}

/* ---------- easter eggs ----------
   - type "5" five times: MAXIMUM 5G
   - type the corp's name anywhere: a door opens
*/
function armEasterEggs(){
  var fives=0, buf="";
  document.addEventListener("keydown",function(e){
    var k=e.key||String.fromCharCode(e.keyCode);
    // 5x5
    if(k==="5"){ fives++; if(fives>=5){ document.body.style.animation="shim 0.4s linear infinite";
      alert("MAXIMUM 5G ACHIEVED. ALL FIFTEEN TOWERS ARE NOW THEORETICALLY HUMMING."); fives=0; } }
    else fives=0;
    // secret word buffer
    if(k&&k.length===1){ buf=(buf+k).toUpperCase().slice(-12); }
    if(buf.indexOf("ISAMSJ")>=0){ buf=""; location.href="isamsj.html"; }
    if(buf.indexOf("JENCORP")>=0){ buf=""; location.href="jencorp.html"; }
  });
}

/* A near-invisible portal, injected at the foot of every loud page.
   Dark-on-dark. It is always there. It is always watching. */
function injectPortal(){
  if(document.getElementById("thedoor")) return;
  var a=document.createElement("a");
  a.id="thedoor"; a.href="static.html"; a.title="";
  a.innerHTML="&#9642;"; // a small square
  a.style.cssText="display:block;text-align:center;color:#0a0a0a;background:#000;"+
    "text-decoration:none;font-size:14px;padding:10px 0;letter-spacing:2px;";
  a.onmouseover=function(){ this.style.color="#1a0000"; };
  a.onmouseout=function(){ this.style.color="#0a0a0a"; };
  document.body.appendChild(a);
}

/* Secret: click the visitor odometer five times to reveal a hidden link. */
function armOdometerSecret(){
  var el=document.getElementById("odometer"); if(!el) return;
  var n=0;
  el.style.cursor="pointer";
  el.addEventListener("click",function(){
    n++;
    if(n===5){
      var d=document.createElement("div");
      d.style.cssText="margin:8px auto;font-family:'Courier New',monospace;font-size:12px;color:#330000;";
      d.innerHTML='<a href="static.html" style="color:#440000;">&#9608;&#9608;&#9608;&#9608;&#9608; there is a channel between the bars &#9608;&#9608;&#9608;&#9608;&#9608;</a>';
      el.parentNode.appendChild(d);
    }
  });
}

/* ---------- SVG helpers ---------- */
var SVGNS="http://www.w3.org/2000/svg";
function svgEl(tag,attrs){
  var e=document.createElementNS(SVGNS,tag);
  for(var k in attrs){ e.setAttribute(k,attrs[k]); }
  return e;
}

/* Animated SVG "SIGNAL PROPAGATION MATRIX" ⸻ a heatmap that pulses. */
function buildSignalMatrix(id,rows,cols){
  var host=document.getElementById(id); if(!host) return;
  rows=rows||10; cols=cols||16;
  var cell=26, gap=3, pad=6;
  var W=pad*2+cols*(cell+gap)-gap, H=pad*2+rows*(cell+gap)-gap;
  var svg=svgEl("svg",{viewBox:"0 0 "+W+" "+H,width:"100%",preserveAspectRatio:"xMidYMid meet",
    style:"background:#000;border:3px inset #00FF00;max-width:720px;"});
  var rects=[];
  for(var r=0;r<rows;r++){ for(var c=0;c<cols;c++){
    var x=pad+c*(cell+gap), y=pad+r*(cell+gap);
    var rc=svgEl("rect",{x:x,y:y,width:cell,height:cell,rx:3,fill:"#031a03",stroke:"#032a03","stroke-width":1});
    rc._r=r; rc._c=c; svg.appendChild(rc); rects.push(rc);
  }}
  host.innerHTML=""; host.appendChild(svg);
  var palette=["#001400","#003300","#006600","#00AA00","#00FF00","#66FF66","#CCFFCC","#00FFFF","#FF00FF"];
  var t=0, cx=cols/2, cy=rows/2;
  function frame(){
    t+=0.18;
    // moving source(s) ⸻ three "towers" orbit and radiate
    var srcs=[
      [cx+Math.cos(t)*cols*0.35, cy+Math.sin(t*0.9)*rows*0.4],
      [cols*0.2+Math.sin(t*1.3)*2, rows*0.5+Math.cos(t)*2],
      [cols*0.85, rows*0.3+Math.sin(t*0.7)*rows*0.3]
    ];
    for(var i=0;i<rects.length;i++){
      var rc=rects[i], best=0;
      for(var s=0;s<srcs.length;s++){
        var dx=rc._c-srcs[s][0], dy=rc._r-srcs[s][1];
        var d=Math.sqrt(dx*dx+dy*dy);
        var wave=Math.max(0, Math.cos(d*0.8 - t*2)) * Math.max(0,1-d/9);
        if(wave>best) best=wave;
      }
      var idx=Math.min(palette.length-1, Math.floor(best*palette.length));
      rc.setAttribute("fill", best<0.04 ? "#031a03" : palette[idx]);
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}

/* Interactive SVG tower-coverage map for towers.html */
function buildTowerMap(id){
  var host=document.getElementById(id); if(!host) return;
  var W=520,H=380;
  var svg=svgEl("svg",{viewBox:"0 0 "+W+" "+H,width:"100%",preserveAspectRatio:"xMidYMid meet",
    style:"background:#010a01;border:4px ridge #00FF00;max-width:640px;"});
  // terrain grid
  for(var gx=0;gx<=W;gx+=40) svg.appendChild(svgEl("line",{x1:gx,y1:0,x2:gx,y2:H,stroke:"#062a06","stroke-width":1}));
  for(var gy=0;gy<=H;gy+=40) svg.appendChild(svgEl("line",{x1:0,y1:gy,x2:W,y2:gy,stroke:"#062a06","stroke-width":1}));
  // the house
  var hx=W/2-24, hy=H/2-18;
  var house=svgEl("rect",{x:hx,y:hy,width:48,height:36,fill:"#221100",stroke:"#FFCC00","stroke-width":2});
  var roof=svgEl("polygon",{points:(hx-4)+","+hy+" "+(hx+52)+","+hy+" "+(W/2)+","+(hy-22),fill:"#552200",stroke:"#FFCC00","stroke-width":2});
  var label=svgEl("text",{x:W/2,y:hy+58,fill:"#FFCC00","font-family":"Arial Black","font-size":12,"text-anchor":"middle"});
  label.textContent="DALARWEN";
  // 15 tower slots in a ring + inner ring
  var towers=[];
  function addTower(px,py,n){
    var cov=svgEl("circle",{cx:px,cy:py,r:0,fill:"rgba(0,255,120,0.10)",stroke:"#00FF66","stroke-width":1,"stroke-dasharray":"4 3"});
    var pulse=svgEl("circle",{cx:px,cy:py,r:6,fill:"none",stroke:"#00FFFF","stroke-width":2,opacity:0});
    var mast=svgEl("polygon",{points:(px-6)+","+(py+8)+" "+(px+6)+","+(py+8)+" "+px+","+(py-10),fill:"#888",stroke:"#0f0","stroke-width":1});
    var num=svgEl("text",{x:px,y:py+20,fill:"#00FF00","font-family":"monospace","font-size":10,"text-anchor":"middle"});
    num.textContent=n; cov.style.opacity=0.001;
    svg.appendChild(cov); svg.appendChild(pulse); svg.appendChild(mast); svg.appendChild(num);
    towers.push({cov:cov,pulse:pulse,px:px,py:py,on:false,r:0});
  }
  var i=0;
  for(var a=0;a<10;a++){ // outer ring 10
    var ang=a/10*2*Math.PI, px=W/2+Math.cos(ang)*210, py=H/2+Math.sin(ang)*150;
    px=Math.max(20,Math.min(W-20,px)); py=Math.max(20,Math.min(H-20,py));
    addTower(px,py,++i);
  }
  for(var b=0;b<5;b++){ // inner ring 5
    var ang2=b/5*2*Math.PI+0.3, px2=W/2+Math.cos(ang2)*95, py2=H/2+Math.sin(ang2)*70;
    addTower(px2,py2,++i);
  }
  svg.appendChild(roof); svg.appendChild(house); svg.appendChild(label);
  host.innerHTML=""; host.appendChild(svg);

  var built=0;
  var counter=document.getElementById("towerbuilt");
  var msg=document.getElementById("towermsg");
  function updateCoverage(){
    var pct=Math.min(100,Math.round(built/15*100));
    if(counter) counter.innerHTML=built+" / 15";
    var barsEl=document.getElementById("towerbars");
    if(barsEl) barsEl.innerHTML=(built===0?"NO SIGNAL":(built<15?"&#128246;".repeat(Math.min(5,Math.ceil(built/3))):"&#128246;&#128246;&#128246;&#128246;&#128246; LOSSLESS"));
    if(msg){
      if(built===0) msg.innerHTML="Dalarwen sits in total darkness. Build a tower.";
      else if(built<15) msg.innerHTML="Coverage growing... "+(15-built)+" tower(s) until the grid is COMPLETE.";
      else msg.innerHTML="&#127881; THE GRID IS COMPLETE. LEWIS IS BROADCASTING. THE BEES ARE DANCING. &#127881;";
    }
  }
  // animate coverage rings
  function anim(){
    for(var k=0;k<towers.length;k++){
      var tw=towers[k];
      if(tw.on){
        var target=70;
        tw.r += (target-tw.r)*0.08;
        tw.cov.setAttribute("r",tw.r);
        tw.cov.style.opacity=0.14;
      }
    }
    requestAnimationFrame(anim);
  }
  requestAnimationFrame(anim);
  // build on click (or auto via button)
  window.buildOneTower=function(){
    for(var k=0;k<towers.length;k++){
      if(!towers[k].on){ towers[k].on=true; built++; updateCoverage(); return; }
    }
    updateCoverage();
  };
  window.buildAllTowers=function(){ for(var k=0;k<towers.length;k++){ if(!towers[k].on){towers[k].on=true;built++;} } updateCoverage(); };
  window.resetTowers=function(){ for(var k=0;k<towers.length;k++){ towers[k].on=false; towers[k].r=0; towers[k].cov.setAttribute("r",0);} built=0; updateCoverage(); };
  updateCoverage();
}

/* ---------- boot ---------- */
window.addEventListener("load",function(){
  buildNav();
  armEasterEggs();
  armOdometerSecret();
  injectPortal();
});
