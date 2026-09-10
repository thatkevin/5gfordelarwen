/* ============================================================
   DALARWEN 5G LIBERATION FRONT ⸻ THE DOORSTEP
   A cosmetic "for pals only" password gate. NOT real security:
   this is a static public site, the password lives in this file.
   Load this in <head> BEFORE the page renders.
   ============================================================ */
(function(){
  var PW="ISAMSJ";
  var KEY="dalarwen_unlocked";
  try{ if(sessionStorage.getItem(KEY)==="1") return; }catch(e){}

  // Hide the page until the gate is ready (avoids a flash of content).
  var hide=document.createElement("style");
  hide.id="dgateHide";
  hide.textContent="body{visibility:hidden!important}#dgate,#dgate *{visibility:visible!important}";
  (document.head||document.documentElement).appendChild(hide);

  function unlock(){
    try{ sessionStorage.setItem(KEY,"1"); }catch(e){}
    var g=document.getElementById("dgate"); if(g&&g.parentNode) g.parentNode.removeChild(g);
    var h=document.getElementById("dgateHide"); if(h&&h.parentNode) h.parentNode.removeChild(h);
    document.body.style.visibility="";
  }

  function build(){
    var g=document.createElement("div");
    g.id="dgate";
    g.style.cssText="position:fixed;top:0;left:0;right:0;bottom:0;z-index:2147483647;"+
      "background:#000000 url('assets/stars.gif') repeat;display:flex;"+
      "align-items:center;justify-content:center;text-align:center;font-family:'Times New Roman',serif;";
    g.innerHTML =
      '<div style="border:6px ridge #FF00FF;background:#0A0016;padding:22px 26px;max-width:460px;box-shadow:0 0 40px #FF00FF;">'+
        '<div style="font-size:40px;line-height:1;">&#128274;</div>'+
        '<div style="font-family:Impact,\'Arial Black\',sans-serif;font-size:30px;color:#00FF00;letter-spacing:1px;margin:8px 0;">RESTRICTED AREA</div>'+
        '<div style="font-family:Impact,\'Arial Black\',sans-serif;font-size:20px;color:#00FFFF;margin-bottom:4px;">FOR PALS ONLY</div>'+
        '<div style="font-family:\'Comic Sans MS\',cursive;font-size:14px;color:#FFFFFF;margin:10px 0 10px;">'+
          'The Cube guards the truth of Dalarwen.<br>Speak the password, pal.</div>'+
        '<div style="font-family:\'Comic Sans MS\',cursive;font-size:13px;color:#FFCC00;margin:0 0 14px;border:1px dashed #FFCC00;padding:6px;">'+
          '&#128161; <b>HINT:</b> the mega-corp that owns us all.<br>'+
          '<span style="color:#00FFFF;">(you know the one. close enough counts.)</span></div>'+
        '<input id="dgatepw" type="password" autocomplete="off" placeholder="PASSWORD" '+
          'style="width:78%;font-family:\'Courier New\',monospace;font-size:20px;text-align:center;'+
          'background:#001100;color:#00FF00;border:3px inset #00FF00;padding:8px;letter-spacing:4px;">'+
        '<div style="margin-top:14px;">'+
          '<button id="dgatego" style="font-family:Impact,\'Arial Black\',sans-serif;font-size:20px;color:#000;'+
          'background:#00FF00;border:4px outset #00FF00;padding:8px 18px;cursor:pointer;">&#128225; ENTER THE TRUTH</button>'+
        '</div>'+
        '<div id="dgateerr" style="font-family:\'Comic Sans MS\',cursive;font-size:14px;color:#FF0033;font-weight:bold;min-height:20px;margin-top:12px;"></div>'+
        '<div style="font-family:\'Times New Roman\',serif;font-size:11px;color:#888;margin-top:10px;">'+
          '(psst &#11835; it is a joke among pals. this doorstep is cosmetic, not real security.)</div>'+
      '</div>';
    document.body.appendChild(g);

    var input=document.getElementById("dgatepw");
    var err=document.getElementById("dgateerr");
    var tries=0;
    function norm(s){ return String(s||"").toUpperCase().replace(/[^A-Z0-9]/g,""); }
    function lev(a,b){
      var m=a.length,n=b.length,i,j,d=[];
      for(i=0;i<=m;i++) d[i]=[i];
      for(j=0;j<=n;j++) d[0][j]=j;
      for(i=1;i<=m;i++) for(j=1;j<=n;j++)
        d[i][j]=Math.min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+(a.charAt(i-1)===b.charAt(j-1)?0:1));
      return d[m][n];
    }
    function closeEnough(v){
      var t=norm(PW), x=norm(v);
      if(!x) return false;
      if(x===t) return true;                       // exact (any case/punctuation)
      if(x.indexOf(t)>=0 || (x.length>=4 && t.indexOf(x)>=0)) return true; // contains / prefix
      return lev(x,t)<=2;                           // a couple of typos are fine
    }
    function attempt(){
      var v=(input.value||"").trim();
      if(closeEnough(v)){ unlock(); return; }
      tries++;
      var msgs=[
        "&#10060; ACCESS DENIED. The Cube rejects you.",
        "&#10060; STILL WRONG. Have you tried the hill?",
        "&#10060; NO. The bees do not recognise you.",
        "&#10060; DENIED. Hold your guess toward Belgium and try again."
      ];
      err.innerHTML=msgs[Math.min(tries-1,msgs.length-1)];
      input.value="";
      // a little 90s shake
      var box=g.firstChild;
      box.style.transition="transform 0.05s";
      var n=0, iv=setInterval(function(){ box.style.transform="translateX("+((n%2)?6:-6)+"px)"; if(++n>6){ clearInterval(iv); box.style.transform=""; } },50);
      input.focus();
    }
    document.getElementById("dgatego").onclick=attempt;
    input.addEventListener("keydown",function(e){ if((e.key||"")==="Enter"||e.keyCode===13){ e.preventDefault(); attempt(); } });
    input.focus();
  }

  if(document.body) build();
  else document.addEventListener("DOMContentLoaded",build);
})();
