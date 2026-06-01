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

# --- Atomic concepts: Bohr-model builder ---------------------------------
_BOHR = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="bo-svg" width="420" height="360" viewBox="0 0 420 360" role="img" aria-label="Bohr model">
      <g id="bo-shells"></g>
      <circle cx="210" cy="180" r="30" fill="#662e80"/>
      <text id="bo-nuc" x="210" y="176" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="#fff">6p</text>
      <text id="bo-nuc2" x="210" y="192" text-anchor="middle" font-family="JetBrains Mono" font-size="12" fill="#fff">6n</text>
      <g id="bo-elec"></g>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <label>Atomic number (Z)
        <input id="bo-z" type="range" min="1" max="20" step="1" value="6" style="width:200px;vertical-align:middle;">
      </label>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">Element</span><span class="val accent" id="bo-sym">C</span></div>
      <div class="readout-card"><span class="key">Protons</span><span class="val" id="bo-p">6</span></div>
      <div class="readout-card"><span class="key">Neutrons</span><span class="val" id="bo-n">6</span></div>
      <div class="readout-card"><span class="key">Electrons</span><span class="val" id="bo-e">6</span></div>
    </div>
  </div>
</div>
<script>(function(){
  var SYM=['','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca'];
  var MASS=[0,1,4,7,9,11,12,14,16,19,20,23,24,27,28,31,32,35,40,39,40];
  var shellsG=document.getElementById('bo-shells'), elecG=document.getElementById('bo-elec');
  function fill(z){var caps=[2,8,8,2],out=[],r=z;for(var i=0;i<caps.length&&r>0;i++){var n=Math.min(caps[i],r);out.push(n);r-=n;}return out;}
  function render(){
    var z=parseInt(document.getElementById('bo-z').value,10), n=MASS[z]-z, sh=fill(z);
    document.getElementById('bo-nuc').textContent=z+'p';
    document.getElementById('bo-nuc2').textContent=n+'n';
    document.getElementById('bo-sym').textContent=SYM[z];
    document.getElementById('bo-p').textContent=z;
    document.getElementById('bo-n').textContent=n;
    document.getElementById('bo-e').textContent=z;
    shellsG.innerHTML=''; elecG.innerHTML='';
    sh.forEach(function(cnt,i){
      var rad=50+i*32, c=document.createElementNS('http://www.w3.org/2000/svg','circle');
      c.setAttribute('cx',210);c.setAttribute('cy',180);c.setAttribute('r',rad);
      c.setAttribute('fill','none');c.setAttribute('stroke','#c7c7cc');c.setAttribute('stroke-width','1.2');
      shellsG.appendChild(c);
      for(var k=0;k<cnt;k++){var a=2*Math.PI*k/cnt+i*0.4,
        e=document.createElementNS('http://www.w3.org/2000/svg','circle');
        e.setAttribute('cx',210+rad*Math.cos(a));e.setAttribute('cy',180+rad*Math.sin(a));
        e.setAttribute('r',6);e.setAttribute('fill','#2ea3f2');e.setAttribute('stroke','#14141a');e.setAttribute('stroke-width','1.2');
        elecG.appendChild(e);}
    });
  }
  document.getElementById('bo-z').addEventListener('input',render); render();
})();</script>
<p style="margin-top:.6rem;"><em>Slide the atomic number.</em> Protons (and the element's identity) change with Z; electrons fill shells 2, then 8, then 8. The neutron count here comes from each element's most common isotope.</p>
"""

# --- Nuclear: half-life decay --------------------------------------------
_HALFLIFE = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="hl-svg" width="640" height="340" viewBox="0 0 640 340" role="img" aria-label="Half-life decay curve">
      <line x1="60" y1="300" x2="610" y2="300" stroke="#14141a" stroke-width="1.5"/>
      <line x1="60" y1="20" x2="60" y2="300" stroke="#14141a" stroke-width="1.5"/>
      <text x="50" y="25" text-anchor="end" font-family="JetBrains Mono" font-size="11" fill="#8a8a93">100%</text>
      <text x="50" y="304" text-anchor="end" font-family="JetBrains Mono" font-size="11" fill="#8a8a93">0</text>
      <path id="hl-path" d="" fill="none" stroke="#662e80" stroke-width="3"/>
      <circle id="hl-dot" cx="60" cy="20" r="6" fill="#f37366"/>
      <text x="335" y="328" text-anchor="middle" font-family="Lora" font-size="13" fill="#14141a">half-lives elapsed</text>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <label>Half-lives elapsed
        <input id="hl-n" type="range" min="0" max="7" step="1" value="0" style="width:200px;vertical-align:middle;">
      </label>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">Half-lives</span><span class="val" id="hl-nv">0</span></div>
      <div class="readout-card"><span class="key">Remaining</span><span class="val accent" id="hl-pct">100%</span></div>
      <div class="readout-card"><span class="key">Fraction left</span><span class="val" id="hl-frac">1/1</span></div>
    </div>
  </div>
</div>
<script>(function(){
  function X(n){return 60+(n/7)*550;} function Y(p){return 300-(p/100)*280;}
  var path=document.getElementById('hl-path'), dot=document.getElementById('hl-dot');
  var d='M '+X(0)+' '+Y(100); for(var t=0;t<=7;t+=0.25){d+=' L '+X(t)+' '+Y(100*Math.pow(0.5,t));}
  path.setAttribute('d',d);
  function render(){
    var n=parseInt(document.getElementById('hl-n').value,10), pct=100*Math.pow(0.5,n);
    dot.setAttribute('cx',X(n)); dot.setAttribute('cy',Y(pct));
    document.getElementById('hl-nv').textContent=n;
    document.getElementById('hl-pct').textContent=(pct>=10?pct.toFixed(0):pct.toFixed(pct<1?2:1))+'%';
    document.getElementById('hl-frac').textContent='1/'+Math.pow(2,n);
  }
  document.getElementById('hl-n').addEventListener('input',render); render();
})();</script>
<p style="margin-top:.6rem;"><em>Step through half-lives.</em> Each half-life cuts the remaining radioactive sample in half — 100% → 50% → 25% → 12.5% … No matter how much you start with, the fraction left after <em>n</em> half-lives is always (½)ⁿ.</p>
"""

# --- Periodic table: trends across a period ------------------------------
_TRENDS = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="pt-svg" width="640" height="340" viewBox="0 0 640 340" role="img" aria-label="Periodic trend across period 3">
      <g id="pt-bars"></g>
      <text x="335" y="332" text-anchor="middle" font-family="Lora" font-size="13" fill="#14141a">Period 3:  Na → Ar  (left to right)</text>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <button id="pt-radius" class="primary" type="button">Atomic radius</button>
      <button id="pt-ie" type="button">Ionization energy</button>
      <button id="pt-en" type="button">Electronegativity</button>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">Trend</span><span class="val accent" id="pt-name">Atomic radius</span></div>
      <div class="readout-card"><span class="key">Across a period →</span><span class="val" id="pt-dir">decreases</span></div>
    </div>
  </div>
</div>
<script>(function(){
  var EL=['Na','Mg','Al','Si','P','S','Cl','Ar'];
  var DATA={radius:[186,160,143,117,110,104,99,71], ie:[496,738,578,786,1012,1000,1251,1521], en:[0.93,1.31,1.61,1.90,2.19,2.58,3.16,0]};
  var DIR={radius:'decreases', ie:'increases', en:'increases'};
  var NAME={radius:'Atomic radius', ie:'Ionization energy', en:'Electronegativity'};
  var bars=document.getElementById('pt-bars');
  function render(key){
    var vals=DATA[key], max=Math.max.apply(null,vals); bars.innerHTML='';
    EL.forEach(function(e,i){
      var h=(vals[i]/max)*240, x=70+i*68, y=290-h;
      var r=document.createElementNS('http://www.w3.org/2000/svg','rect');
      r.setAttribute('x',x);r.setAttribute('y',y);r.setAttribute('width',44);r.setAttribute('height',Math.max(h,0));
      r.setAttribute('fill', i%2? '#2ea3f2':'#662e80'); r.setAttribute('rx',3); bars.appendChild(r);
      var t=document.createElementNS('http://www.w3.org/2000/svg','text');
      t.setAttribute('x',x+22);t.setAttribute('y',308);t.setAttribute('text-anchor','middle');
      t.setAttribute('font-family','Lora');t.setAttribute('font-size','12');t.setAttribute('fill','#14141a');
      t.textContent=e; bars.appendChild(t);
    });
    document.getElementById('pt-name').textContent=NAME[key];
    document.getElementById('pt-dir').textContent=DIR[key];
    ['radius','ie','en'].forEach(function(k){document.getElementById('pt-'+k).classList.toggle('primary',k===key);});
  }
  document.getElementById('pt-radius').addEventListener('click',function(){render('radius');});
  document.getElementById('pt-ie').addEventListener('click',function(){render('ie');});
  document.getElementById('pt-en').addEventListener('click',function(){render('en');});
  render('radius');
})();</script>
<p style="margin-top:.6rem;"><em>Switch the trend.</em> Across a period, atomic radius <strong>decreases</strong> while ionization energy and electronegativity <strong>increase</strong> — the growing nuclear charge pulls the same outer shell in tighter. (Argon has no electronegativity value; noble gases don't bond.)</p>
"""

# --- Solutions: solubility curve -----------------------------------------
_SOLUBILITY = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="so-svg" width="640" height="340" viewBox="0 0 640 340" role="img" aria-label="Solubility curve">
      <line x1="60" y1="300" x2="610" y2="300" stroke="#14141a" stroke-width="1.5"/>
      <line x1="60" y1="20" x2="60" y2="300" stroke="#14141a" stroke-width="1.5"/>
      <path id="so-path" d="" fill="none" stroke="#662e80" stroke-width="3"/>
      <circle id="so-dot" cx="60" cy="300" r="6" fill="#f37366"/>
      <text x="335" y="328" text-anchor="middle" font-family="Lora" font-size="13" fill="#14141a">temperature (°C)</text>
      <text x="20" y="160" text-anchor="middle" font-family="Lora" font-size="12" fill="#14141a" transform="rotate(-90 20 160)">solubility (g / 100 g)</text>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <label>Temperature
        <input id="so-t" type="range" min="0" max="100" step="5" value="20" style="width:200px;vertical-align:middle;">
      </label>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">Temperature</span><span class="val" id="so-tv">20 °C</span></div>
      <div class="readout-card"><span class="key">KNO₃ solubility</span><span class="val accent" id="so-sv">59 g</span></div>
      <div class="readout-card"><span class="key">per</span><span class="val">100 g H₂O</span></div>
    </div>
  </div>
</div>
<script>(function(){
  function S(t){return 13+2.3*t;}
  function X(t){return 60+(t/100)*550;} function Y(s){return 300-(s/250)*280;}
  var path=document.getElementById('so-path'), dot=document.getElementById('so-dot');
  var d='M '+X(0)+' '+Y(S(0)); for(var t=0;t<=100;t+=5){d+=' L '+X(t)+' '+Y(S(t));}
  path.setAttribute('d',d);
  function render(){
    var t=parseFloat(document.getElementById('so-t').value), s=S(t);
    dot.setAttribute('cx',X(t)); dot.setAttribute('cy',Y(s));
    document.getElementById('so-tv').textContent=Math.round(t)+' °C';
    document.getElementById('so-sv').textContent=Math.round(s)+' g';
  }
  document.getElementById('so-t').addEventListener('input',render); render();
})();</script>
<p style="margin-top:.6rem;"><em>Raise the temperature.</em> For most solids like KNO₃, solubility climbs steeply as the water heats up — hot water dissolves far more solute. Reading this curve is exactly the skill the solubility tables test.</p>
"""

# --- Acids & bases: pH scale ---------------------------------------------
_PHSCALE = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="ph-svg" width="640" height="260" viewBox="0 0 640 260" role="img" aria-label="pH scale">
      <defs><linearGradient id="ph-grad" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0" stop-color="#d7263d"/><stop offset="0.3" stop-color="#f37366"/>
        <stop offset="0.5" stop-color="#4caf50"/><stop offset="0.7" stop-color="#2ea3f2"/>
        <stop offset="1" stop-color="#662e80"/></linearGradient></defs>
      <rect x="40" y="60" width="560" height="40" fill="url(#ph-grad)" stroke="#14141a" stroke-width="1.5" rx="4"/>
      <g id="ph-ticks"></g>
      <polygon id="ph-mark" points="0,105 -8,128 8,128" fill="#14141a"/>
      <circle id="ph-beaker" cx="320" cy="205" r="36" fill="#4caf50" stroke="#14141a" stroke-width="2.5"/>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <label>pH
        <input id="ph-i" type="range" min="0" max="14" step="1" value="7" style="width:220px;vertical-align:middle;">
      </label>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">pH</span><span class="val accent" id="ph-v">7</span></div>
      <div class="readout-card"><span class="key">[H⁺] (mol/L)</span><span class="val" id="ph-h">1×10⁻⁷</span></div>
      <div class="readout-card"><span class="key">Solution is</span><span class="val" id="ph-state">neutral</span></div>
    </div>
  </div>
</div>
<script>(function(){
  var ticks=document.getElementById('ph-ticks');
  for(var i=0;i<=14;i++){var x=40+(i/14)*560,
    t=document.createElementNS('http://www.w3.org/2000/svg','text');
    t.setAttribute('x',x);t.setAttribute('y',120);t.setAttribute('text-anchor','middle');
    t.setAttribute('font-family','JetBrains Mono');t.setAttribute('font-size','11');t.setAttribute('fill','#14141a');
    t.textContent=i; ticks.appendChild(t);}
  var SUP={'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'};
  function sup(n){return String(n).split('').map(function(c){return SUP[c]||c;}).join('');}
  var mark=document.getElementById('ph-mark'), beaker=document.getElementById('ph-beaker');
  function colour(p){return p<3?'#d7263d':p<6?'#f37366':p<8?'#4caf50':p<11?'#2ea3f2':'#662e80';}
  function render(){
    var p=parseInt(document.getElementById('ph-i').value,10), x=40+(p/14)*560;
    mark.setAttribute('transform','translate('+x+',0)');
    beaker.setAttribute('fill',colour(p));
    document.getElementById('ph-v').textContent=p;
    document.getElementById('ph-h').textContent='1×10⁻'+sup(p);
    document.getElementById('ph-state').textContent=p<7?'acidic':p>7?'basic':'neutral';
  }
  document.getElementById('ph-i').addEventListener('input',render); render();
})();</script>
<p style="margin-top:.6rem;"><em>Slide the pH.</em> Each step <em>down</em> the scale means ten times more H⁺ ions — pH 3 is ten times more acidic than pH 4. Seven is neutral; below is acidic, above is basic.</p>
"""

# --- Heat & energy: heating-curve tracer ---------------------------------
_HEATCURVE = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="hc-svg" width="640" height="340" viewBox="0 0 640 340" role="img" aria-label="Heating curve">
      <line x1="60" y1="300" x2="610" y2="300" stroke="#14141a" stroke-width="1.5"/>
      <line x1="60" y1="20" x2="60" y2="300" stroke="#14141a" stroke-width="1.5"/>
      <path id="hc-path" d="" fill="none" stroke="#662e80" stroke-width="3"/>
      <circle id="hc-dot" cx="60" cy="280" r="6" fill="#f37366"/>
      <text x="335" y="328" text-anchor="middle" font-family="Lora" font-size="13" fill="#14141a">heat added →</text>
      <text x="20" y="160" text-anchor="middle" font-family="Lora" font-size="12" fill="#14141a" transform="rotate(-90 20 160)">temperature (°C)</text>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <label>Heat added
        <input id="hc-q" type="range" min="0" max="100" step="2" value="0" style="width:220px;vertical-align:middle;">
      </label>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">Temperature</span><span class="val accent" id="hc-temp">-20 °C</span></div>
      <div class="readout-card"><span class="key">Phase</span><span class="val" id="hc-phase">solid</span></div>
    </div>
  </div>
</div>
<script>(function(){
  function temp(q){ if(q<10)return -20+(q/10)*20; if(q<30)return 0; if(q<55)return (q-30)/25*100; if(q<85)return 100; return 100+(q-85)/15*20; }
  function phase(q){ if(q<10)return'solid'; if(q<30)return'melting (solid + liquid)'; if(q<55)return'liquid'; if(q<85)return'boiling (liquid + gas)'; return'gas'; }
  function X(q){return 60+(q/100)*550;} function Y(t){return 300-((t+20)/140)*280;}
  var path=document.getElementById('hc-path'), dot=document.getElementById('hc-dot');
  var d='M '+X(0)+' '+Y(temp(0)); for(var q=0;q<=100;q+=2){d+=' L '+X(q)+' '+Y(temp(q));}
  path.setAttribute('d',d);
  function render(){
    var q=parseFloat(document.getElementById('hc-q').value), t=temp(q);
    dot.setAttribute('cx',X(q)); dot.setAttribute('cy',Y(t));
    document.getElementById('hc-temp').textContent=Math.round(t)+' °C';
    document.getElementById('hc-phase').textContent=phase(q);
  }
  document.getElementById('hc-q').addEventListener('input',render); render();
})();</script>
<p style="margin-top:.6rem;"><em>Add heat.</em> Temperature rises through the solid, liquid, and gas regions — but flattens at the melting and boiling plateaus, where the added energy breaks attractions between particles instead of raising the temperature.</p>
"""

# --- Physical behavior: states of matter ---------------------------------
_STATES = """
<div class="lab" data-interactive="true">
  <div class="lab-canvas">
    <svg id="st-svg" width="420" height="320" viewBox="0 0 420 320" role="img" aria-label="States of matter">
      <rect x="60" y="40" width="300" height="240" fill="#f7f4ee" stroke="#14141a" stroke-width="2.5"/>
      <g id="st-parts"></g>
    </svg>
  </div>
  <div class="lab-controls">
    <div class="button-bar">
      <label>Temperature
        <input id="st-t" type="range" min="0" max="100" step="1" value="10" style="width:220px;vertical-align:middle;">
      </label>
    </div>
    <div class="lab-readouts">
      <div class="readout-card"><span class="key">State</span><span class="val accent" id="st-state">solid</span></div>
      <div class="readout-card"><span class="key">Particles</span><span class="val" id="st-desc">packed, vibrating</span></div>
    </div>
  </div>
</div>
<script>(function(){
  var g=document.getElementById('st-parts');
  function render(){
    var t=parseFloat(document.getElementById('st-t').value);
    var state=t<33?'solid':t<66?'liquid':'gas';
    var desc=t<33?'packed in a fixed lattice':t<66?'close but sliding past each other':'far apart, moving fast and freely';
    g.innerHTML=''; var pts=[];
    if(state==='solid'){ for(var r=0;r<5;r++)for(var c=0;c<6;c++)pts.push([95+c*44,75+r*44]); }
    else if(state==='liquid'){ for(var i=0;i<26;i++){var col=i%6,row=Math.floor(i/6);pts.push([90+col*44+(row%2?16:0),150+row*40]);} }
    else { var seed=7; for(var i=0;i<22;i++){ seed=(seed*9301+49297)%233280; var rx=seed/233280; seed=(seed*9301+49297)%233280; var ry=seed/233280; pts.push([85+rx*250,60+ry*195]); } }
    pts.forEach(function(p){var c=document.createElementNS('http://www.w3.org/2000/svg','circle');
      c.setAttribute('cx',p[0]);c.setAttribute('cy',p[1]);c.setAttribute('r',10);
      c.setAttribute('fill','#662e80');c.setAttribute('stroke','#14141a');c.setAttribute('stroke-width','1.2');g.appendChild(c);});
    document.getElementById('st-state').textContent=state;
    document.getElementById('st-desc').textContent=desc;
  }
  document.getElementById('st-t').addEventListener('input',render); render();
})();</script>
<p style="margin-top:.6rem;"><em>Heat it up.</em> As temperature rises, particles gain kinetic energy: a rigid <strong>solid</strong> lattice loosens into a <strong>liquid</strong> that flows, then spreads into a <strong>gas</strong> that fills its container.</p>
"""

INTERACTIVES = {
    "04-03-pressurevolume-relationship": _GAS_PV,
    "12-03-titration": _TITRATION,
    "11-03-potential-energy-diagrams": _PE_DIAGRAM,
    "05-02-determining-number-of-subatomic-particles": _BOHR,
    "06-03-half-life": _HALFLIFE,
    "07-05-periodic-trends": _TRENDS,
    "10-03-using-solubility-tables": _SOLUBILITY,
    "12-05-ph-and-indicators": _PHSCALE,
    "03-01-heating-and-cooling-curves": _HEATCURVE,
    "02-02-states-of-matter-and-phase-changes": _STATES,
}
