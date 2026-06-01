"""Custom interactive widgets for flagship chemistry web lessons.

INTERACTIVES maps a lesson page slug (the `<UU>-<LL>-<slug>` filename stem) to a
self-contained `.lab` HTML+JS block. build_web.py injects the block at the end of
that lesson's Investigate section. Each widget reuses the lab-notebook `.lab` /
`.lab-canvas` / `.lab-controls` / `.lab-readouts` classes from site.css.
"""
from __future__ import annotations

# Brand colours (match _assets/site.css tokens)
PURPLE = "#662e80"
BLUE = "#2ea3f2"
ORANGE = "#f37366"
INK = "#14141a"

# --- Gas laws: pressure–volume piston ------------------------------------
_GAS_PV = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="pv-svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-label="Gas piston">
      <rect x="120" y="20" width="220" height="320" fill="#f7f4ee" stroke="#14141a" stroke-width="3"/>
      <g id="pv-particles"></g>
      <rect id="pv-piston" x="120" y="60" width="220" height="20" fill="#662e80"/>
      <rect x="218" y="0" width="24" height="62" fill="#662e80"/>
      <line id="pv-bar" x1="430" y1="340" x2="430" y2="40" stroke="#2ea3f2" stroke-width="0"/>
      <text x="430" y="356" text-anchor="middle" font-family="Lora" font-size="13" fill="#14141a">pressure</text>
      <rect id="pv-gauge" x="410" y="40" width="40" height="300" fill="none" stroke="#c7c7cc" stroke-width="1.5"/>
      <rect id="pv-fill" x="410" y="340" width="40" height="0" fill="#2ea3f2" opacity="0.6"/>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <label style="font-family:var(--font-hand,inherit);">Volume
        <input id="pv-vol" type="range" min="1" max="10" step="0.5" value="6" style="width:180px;vertical-align:middle;">
      </label>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">Volume</span><span class="val" id="pv-v">6.0 L</span></div>
      <div class="readout-card"><span class="key">Pressure</span><span class="val accent" id="pv-p">100 kPa</span></div>
      <div class="readout-card"><span class="key">P × V (constant)</span><span class="val" id="pv-k">600</span></div>
    </div>
  </div>
</div>
<script>(function(){
  var K=600, svg=document.getElementById('pv-svg'), pg=document.getElementById('pv-particles');
  var piston=document.getElementById('pv-piston'), fill=document.getElementById('pv-fill');
  var TOP_MIN=40, TOP_MAX=300, parts=[];
  for(var i=0;i<24;i++){parts.push({x:130+Math.random()*200,fy:Math.random()});}
  function render(){
    var v=parseFloat(document.getElementById('pv-vol').value);
    var p=K/v;
    var top=TOP_MIN+(TOP_MAX-TOP_MIN)*(1-(v-1)/9);   // small V -> piston low -> taller gas? invert: large V -> more space
    top=20+ (10-v)/9*260;                            // V=10 -> top=20 (full), V=1 -> top=280 (compressed)
    piston.setAttribute('y',top);
    var gasTop=top+20, gasBot=340, h=gasBot-gasTop;
    pg.innerHTML='';
    parts.forEach(function(pt){
      var c=document.createElementNS('http://www.w3.org/2000/svg','circle');
      c.setAttribute('cx',pt.x); c.setAttribute('cy',gasTop+pt.fy*h);
      c.setAttribute('r',5); c.setAttribute('fill','#662e80');
      pg.appendChild(c);
    });
    var fh=300*(p/600);  if(fh>300)fh=300;
    fill.setAttribute('y',340-fh); fill.setAttribute('height',fh);
    document.getElementById('pv-v').textContent=v.toFixed(1)+' L';
    document.getElementById('pv-p').textContent=Math.round(p)+' kPa';
    document.getElementById('pv-k').textContent=Math.round(p*v);
  }
  document.getElementById('pv-vol').addEventListener('input',render); render();
})();</script>
<p style="margin-top:.6rem;"><em>Drag the slider.</em> Notice the product P × V stays the same — squeeze the gas into half the volume and the pressure doubles. That inverse relationship is what <strong>P₁V₁ = P₂V₂</strong> says.</p>
"""

# --- Acids & bases: titration --------------------------------------------
_TITRATION = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="ti-svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-label="Titration curve">
      <rect x="70" y="20" width="360" height="300" fill="#ffffff" stroke="#c7c7cc" stroke-width="1.5"/>
      <line x1="70" y1="170" x2="430" y2="170" stroke="#e5e5ea" stroke-width="1"/>
      <text x="60" y="25" text-anchor="end" font-family="JetBrains Mono" font-size="11" fill="#8a8a93">14</text>
      <text x="60" y="174" text-anchor="end" font-family="JetBrains Mono" font-size="11" fill="#8a8a93">7</text>
      <text x="60" y="320" text-anchor="end" font-family="JetBrains Mono" font-size="11" fill="#8a8a93">0</text>
      <path id="ti-path" d="" fill="none" stroke="#662e80" stroke-width="3"/>
      <circle id="ti-dot" cx="70" cy="318" r="6" fill="#f37366"/>
      <text x="250" y="345" text-anchor="middle" font-family="Lora" font-size="13" fill="#14141a">volume of base added (mL)</text>
      <!-- beaker -->
      <rect id="ti-beaker" x="500" y="150" width="90" height="150" rx="6" fill="#d8f0ff" stroke="#14141a" stroke-width="2.5"/>
      <text x="545" y="320" text-anchor="middle" font-family="Lora" font-size="12" fill="#14141a">solution</text>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <label>Base added
        <input id="ti-vol" type="range" min="0" max="50" step="1" value="0" style="width:200px;vertical-align:middle;">
      </label>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">Volume added</span><span class="val" id="ti-v">0 mL</span></div>
      <div class="readout-card"><span class="key">pH</span><span class="val accent" id="ti-ph">1.0</span></div>
      <div class="readout-card"><span class="key">Solution is</span><span class="val" id="ti-state">acidic</span></div>
    </div>
  </div>
</div>
<script>(function(){
  function pH(v){return 1+12/(1+Math.exp(-(v-25)*0.45));}
  function X(v){return 70+ (v/50)*360;}
  function Y(p){return 20+ (14-p)/14*300;}
  var path=document.getElementById('ti-path'), dot=document.getElementById('ti-dot'), beaker=document.getElementById('ti-beaker');
  function render(){
    var v=parseFloat(document.getElementById('ti-vol').value), p=pH(v);
    var d='M '+X(0)+' '+Y(pH(0));
    for(var t=0;t<=v;t+=1){ d+=' L '+X(t)+' '+Y(pH(t)); }
    path.setAttribute('d',d);
    dot.setAttribute('cx',X(v)); dot.setAttribute('cy',Y(p));
    // indicator colour: phenolphthalein-style (colourless acid -> pink base), via simple ramp
    var col = p<6 ? '#d8f0ff' : (p<8 ? '#eafbe7' : '#ffd6ec');
    beaker.setAttribute('fill',col);
    document.getElementById('ti-v').textContent=Math.round(v)+' mL';
    document.getElementById('ti-ph').textContent=p.toFixed(1);
    document.getElementById('ti-state').textContent = p<6.5?'acidic':(p<7.5?'neutral':'basic');
  }
  document.getElementById('ti-vol').addEventListener('input',render); render();
})();</script>
<p style="margin-top:.6rem;"><em>Add base drop by drop.</em> The pH barely moves at first, then leaps through the steep <strong>equivalence point</strong> near 25 mL — where moles of base equal moles of acid — and the indicator changes colour.</p>
"""

# --- Kinetics: potential-energy diagram ----------------------------------
_PE_DIAGRAM = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="pe-svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-label="Potential energy diagram">
      <line x1="70" y1="330" x2="610" y2="330" stroke="#14141a" stroke-width="1.5"/>
      <line x1="70" y1="20" x2="70" y2="330" stroke="#14141a" stroke-width="1.5"/>
      <text x="40" y="180" text-anchor="middle" font-family="Lora" font-size="13" fill="#14141a" transform="rotate(-90 40 180)">energy (kJ)</text>
      <text x="340" y="352" text-anchor="middle" font-family="Lora" font-size="13" fill="#14141a">reaction progress</text>
      <path id="pe-path" d="" fill="none" stroke="#662e80" stroke-width="3.5"/>
      <line id="pe-ea" x1="0" y1="0" x2="0" y2="0" stroke="#f37366" stroke-width="2" stroke-dasharray="5 4"/>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <label>Activation energy
        <input id="pe-ea-i" type="range" min="10" max="90" step="5" value="55" style="width:150px;vertical-align:middle;">
      </label>
      <label>&Delta;H
        <input id="pe-dh" type="range" min="-60" max="60" step="10" value="-30" style="width:150px;vertical-align:middle;">
      </label>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">Ea (forward)</span><span class="val accent" id="pe-eaf">55 kJ</span></div>
      <div class="readout-card"><span class="key">Ea (reverse)</span><span class="val" id="pe-ear">85 kJ</span></div>
      <div class="readout-card"><span class="key">&Delta;H</span><span class="val" id="pe-dhv">-30 kJ</span></div>
      <div class="readout-card"><span class="key">Reaction is</span><span class="val" id="pe-type">exothermic</span></div>
    </div>
  </div>
</div>
<script>(function(){
  function Y(e){return 330 - e*2.4;}   // 0..120 kJ -> 330..42 px
  var path=document.getElementById('pe-path'), eaLine=document.getElementById('pe-ea');
  function render(){
    var ea=parseFloat(document.getElementById('pe-ea-i').value);
    var dh=parseFloat(document.getElementById('pe-dh').value);
    var R=40, P=R+dh, peak=Math.max(R,P)+ea;
    var xr=130, xp=550, xt=340;
    var d='M '+xr+' '+Y(R)+' C '+(xr+90)+' '+Y(R)+' '+(xt-70)+' '+Y(peak)+' '+xt+' '+Y(peak)
         +' C '+(xt+70)+' '+Y(peak)+' '+(xp-90)+' '+Y(P)+' '+xp+' '+Y(P);
    path.setAttribute('d',d);
    eaLine.setAttribute('x1',xt); eaLine.setAttribute('y1',Y(R)); eaLine.setAttribute('x2',xt); eaLine.setAttribute('y2',Y(peak));
    document.getElementById('pe-eaf').textContent=ea+' kJ';
    document.getElementById('pe-ear').textContent=Math.round(peak-P)+' kJ';
    document.getElementById('pe-dhv').textContent=dh+' kJ';
    document.getElementById('pe-type').textContent = dh<0?'exothermic':(dh>0?'endothermic':'thermoneutral');
  }
  document.getElementById('pe-ea-i').addEventListener('input',render);
  document.getElementById('pe-dh').addEventListener('input',render); render();
})();</script>
<p style="margin-top:.6rem;"><em>Slide the activation energy and &Delta;H.</em> A lower hump means a faster reaction; a negative &Delta;H (products below reactants) releases energy — <strong>exothermic</strong>. The reverse activation energy is the gap from products back up to the peak.</p>
"""

INTERACTIVES = {
    "04-03-pressurevolume-relationship": _GAS_PV,
    "12-03-titration": _TITRATION,
    "11-03-potential-energy-diagrams": _PE_DIAGRAM,
}
