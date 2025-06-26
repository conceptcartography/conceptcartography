# Diversity Network Map

This map was created based primarily on readings from an interdisciplinary, international, online reading group, beginning in mid-2024. We thank everyone who came along and shared their insights and ideas and contributed to a series of enlightening and provocative discussions.
<style>
#graph-wrapper {
  max-width: 1000px;
  margin: 0 auto;
  position: relative;
  transition: all 0.3s ease;
  overflow: hidden;
}

#graph-wrapper canvas {
  max-width: 100%;
  height: auto !important;
  display: block;
  margin: 0 auto;
}

#graph-container {
  width: 100%;
  height: 600px;
  background: #fafafa;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}

#graph-wrapper.fullscreen {
  position: fixed;
  top: 0; left: 0;
  width: 100vw; height: 100vh;
  z-index: 9999;
  background: #ffffff;
}

#graph-wrapper.fullscreen canvas,
#graph-wrapper.fullscreen #graph-container {
  width: 100vw !important;
  height: 100vh !important;
  border-radius: 0;
  box-shadow: none;
}
#graph-controls {
  position: absolute;
  top: 1rem;
  left: 1rem;
  z-index: 1000;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(8px);
  padding: 0.8rem 1rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
  align-items: center;
  max-width: 95vw;
}

#graph-controls input[type="text"] {
  flex: 1;
  min-width: 180px;
  padding: 0.4rem 0.75rem;
  font-size: 0.95rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  transition: border-color 0.2s ease;
}

#graph-controls input[type="text"]:focus {
  outline: none;
  border-color: #007acc;
  box-shadow: 0 0 0 2px rgba(0, 122, 204, 0.2);
}

#graph-controls button {
  background-color: #f5f5f5;
  color: #333;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 0.9rem;
  padding: 0.4rem 0.9rem;
  cursor: pointer;
  transition: background-color 0.2s ease, box-shadow 0.2s ease;
}

#graph-controls button:hover {
  background-color: #e8e8e8;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
}

#graph-controls button:active {
  background-color: #ddd;
}

#graph-legend {
  font-size: 0.85em;
  padding: 0.5rem 1rem;
  background: var(--md-code-bg-color);
  border-radius: 6px;
  margin-top: 1rem;
}

#search-box {
  background: white;
  font-family: inherit;
}

datalist option {
  font-size: 0.9rem;
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
<div id="graph-controls">
  <input type="text" id="search-box" list="concepts-list" placeholder="Search concept..." />
<datalist id="concepts-list"></datalist>
  <button onclick="resetView()">Reset View</button>
  <button onclick="toggleRotate()">Rotate</button>
  <button id="fullscreen-toggle" onclick="toggleFullScreen()">Full screen</button>
</div>

  <div id="graph-container"></div>
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
let allNodes = [];



document.getElementById('search-box').addEventListener('keydown', function(e) {
  if (e.key === 'Enter') {
    focusOnConcept(this.value);
  }
});


function initGraph() {
  fetch('../../assets/graph.json')
    .then(res => res.json())
    .then(data => {
      allNodes = data.nodes;
      const datalist = document.getElementById('concepts-list');
data.nodes.forEach(node => {
  const opt = document.createElement("option");
  opt.value = node.id;
  datalist.appendChild(opt);
});
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

      Graph = ForceGraph3D()(document.getElementById('graph-container'))
        .graphData(data)
        .nodeLabel(node => node.id)
        .nodeColor(() => '#3b3b3b')
        .linkColor(link => colorMap[link.type] || 'green')
        .linkWidth(2.5)
        .linkOpacity(0.8)
        .backgroundColor('#fdfdfd')
        .linkDirectionalParticles(2)
        .linkDirectionalParticleWidth(2)
        .linkDirectionalParticleColor(link => colorMap[link.type] || 'gray')
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
  button.innerText = isFullscreen ? "Exit Full Screen" : "Full Screen";
}

function focusOnConcept(query) {
  if (!Graph || !query) return;

  const normalized = query.toLowerCase().trim();
  const node = Graph.graphData().nodes.find(n => n.id.toLowerCase() === normalized);

  if (node) {
    highlightNode(node);
  } else {
    const partial = Graph.graphData().nodes.find(n => n.id.toLowerCase().includes(normalized));
    if (partial) {
      highlightNode(partial);
    }
  }
}

function highlightNode(node) {
  Graph.centerAt(node.x, node.y, 1000);
  Graph.zoom(5, 1000);

  const originalColor = '#3b3b3b';
  const highlightColor = '#facc15'; // bright yellow

  const nodeColorFn = n => n.id === node.id ? highlightColor : originalColor;
  Graph.nodeColor(nodeColorFn);

  setTimeout(() => {
    Graph.nodeColor(() => originalColor);
  }, 2000);
}



// Escape to exit full screen
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    const wrapper = document.getElementById('graph-wrapper');
    const button = document.getElementById('fullscreen-toggle');
    if (wrapper.classList.contains('fullscreen')) {
      wrapper.classList.remove('fullscreen');
      Graph.width(wrapper.offsetWidth);
      Graph.height(600);
      button.innerText = "Full Screen";
    }
  }
});
</script>