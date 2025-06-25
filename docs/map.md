# Concept Network Map

<style>
/* Main graph container wrapper */
#graph-wrapper {
  max-width: 1000px;
  margin: 0 auto;
  position: relative;
  transition: all 0.3s ease;
  overflow: hidden;
}

/* Force canvas to stay within the page content width */
#graph-wrapper canvas {
  max-width: 50%;
  height: 50% !important;
  display: block;
  margin: 0 auto;
}

/* Graph rendering space */
#graph-container {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  background: white;

  transition: all 0.3s ease;
  overflow: hidden;
}

/* Fullscreen wrapper mode */
#graph-wrapper.fullscreen {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  z-index: 9999;
  background: var(--md-default-bg-color);
}

/* Fullscreen canvas */
#graph-wrapper.fullscreen canvas,
#graph-wrapper.fullscreen #graph-container {
  width: 100vw !important;
  height: 100vh !important;
  border-radius: 0;
  box-shadow: none;
}

/* Controls and legend styling remains the same */
#graph-controls {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 1rem;
}
#graph-wrapper.fullscreen #graph-controls {
  position: absolute;
  top: 1rem;
  left: 1rem;
  z-index: 10000;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(4px);
  border-radius: 6px;
  padding: 0.5rem;
}
#graph-controls button,
#graph-controls select {
  padding: 0.5em 1em;
  font-size: 0.9em;
  cursor: pointer;
}
#graph-legend {
  font-size: 0.85em;
  padding: 0.5rem 1rem;
  background: var(--md-code-bg-color);
  border-radius: 6px;
  margin-top: 1rem;
}
</style>



<div id="graph-legend">
  <strong>Relation types (edge colors):</strong><br>
  <span style="color: blue;">Type of</span>, 
  <span style="color: green;">Part of</span>, 
  <span style="color: purple;">Produces</span>, 
  <span style="color: red;">Counteracts</span>, 
  <span style="color: orange;">Similar to</span>, 
  <span style="color: gray;">Equivalent to</span>, 
  <span style="color: black;">Distinct from</span>, 
  <span style="color: cyan;">Depends on</span>
</div>

<div id="graph-wrapper">

  <div id="graph-container">
    <div id="graph-controls">
    <button onclick="resetView()">Reset View</button>
    <button onclick="toggleRotate()">Toggle Auto-Rotate</button>
    <button id="fullscreen-toggle" onclick="toggleFullScreen()">Enter Full Screen</button>
    <select id="focus-select" onchange="focusNode(this.value)">
      <option value="">Focus on a concept...</option>
    </select>
  </div></div>
</div>





<!-- Load the 3d-force-graph library and wait for it -->
<script>
  const forceGraphScript = document.createElement('script');
  forceGraphScript.src = 'https://unpkg.com/3d-force-graph';
  forceGraphScript.onload = () => {
    initGraph(); // call setup function only when the library is ready
  };
  document.head.appendChild(forceGraphScript);
</script>

<script>
let Graph;
let autoRotate = false;

function initGraph() {
  fetch('../assets/graph.json')
    .then(res => res.json())
    .then(data => {
      const colorMap = {
        "Type of": "blue",
        "Part of": "green",
        "Produces": "purple",
        "Counteracts": "red",
        "Similar to": "orange",
        "Equivalent to": "gray",
        "Distinct from": "black",
        "Depends on": "cyan"
      };

      // Populate dropdown
      const select = document.getElementById('focus-select');
      data.nodes.forEach(node => {
        const opt = document.createElement("option");
        opt.value = node.id;
        opt.innerText = node.id;
        select.appendChild(opt);
      });

      Graph = ForceGraph3D()(document.getElementById('graph-container'))
        .graphData(data)
        .nodeLabel(node => node.id)
        .nodeAutoColorBy('id')
        .linkLabel(link => `${link.type}`)
        .linkColor(link => colorMap[link.type] || 'gray')
        .linkWidth(2)
        .linkDirectionalParticles(4)
        .linkDirectionalParticleWidth(2.5)
        .linkColor(link => colorMap[link.type] || 'gray')
        .linkOpacity(0.6)
        .linkWidth(2)
        .linkDirectionalParticles(3)
        .linkDirectionalParticleColor(link => colorMap[link.type] || 'gray')
        .linkDirectionalParticleWidth(1.5)

        .onNodeClick(node => {
          const slug = node.id.toLowerCase().replace(/\s+/g, '-');
          window.location.href = `/concepts/${slug}`;
        })
        .onBackgroundClick(() => Graph.zoomToFit(400));
    });
}

function resetView() {
  Graph && Graph.zoomToFit(400);
}

function toggleRotate() {
  autoRotate = !autoRotate;
  Graph.controls().autoRotate = autoRotate;
  Graph.controls().autoRotateSpeed = 1.2;
}

function toggleFullScreen() {
  const wrapper = document.getElementById('graph-wrapper');
  const button = document.getElementById('fullscreen-toggle');
  const isFullscreen = wrapper.classList.toggle('fullscreen');

  Graph.width(isFullscreen ? window.innerWidth : wrapper.offsetWidth);
  Graph.height(isFullscreen ? window.innerHeight : 600);

  button.innerText = isFullscreen ? "Exit Full Screen" : "Enter Full Screen";
}

// Handle ESC to exit fullscreen
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    const wrapper = document.getElementById('graph-wrapper');
    const button = document.getElementById('fullscreen-toggle');
    if (wrapper.classList.contains('fullscreen')) {
      wrapper.classList.remove('fullscreen');
      Graph.width(wrapper.offsetWidth);
      Graph.height(600);
      button.innerText = "Enter Full Screen";
    }
  }
});


function focusNode(name) {
  const node = Graph.graphData().nodes.find(n => n.id === name);
  if (node) {
    Graph.centerAt(node.x, node.y, 1000);
    Graph.zoom(5, 1000);
  }
}
</script>
