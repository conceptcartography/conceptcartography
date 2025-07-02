# Map Builder
<!-- GRAPH START -->

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


## 🗺️ Map 
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
<div id="data-builder-modal" style="display: none;">
  <div style="background: white; padding: 1rem; max-width: 900px; margin: 2rem auto; border-radius: 8px; box-shadow: 0 0 20px rgba(0,0,0,0.2);">
    <h3 style="margin-bottom: 0.5rem;">Concept Map Builder</h3>
    <p style="font-size: 0.9rem;">Add nodes and links using the tables below. Changes apply live.</p>

    <h4>🧠 Nodes</h4>
    <table id="nodes-table" style="width: 100%; border-collapse: collapse; margin-bottom: 1rem;">
      <thead>
        <tr>
          <th>ID</th>
          <th><button onclick="addNodeRow()">＋</button></th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>

    <h4>🔗 Links</h4>
    <table id="links-table" style="width: 100%; border-collapse: collapse;">
      <thead>
        <tr>
          <th>Source</th>
          <th>Target</th>
          <th>Type</th>
          <th><button onclick="addLinkRow()">＋</button></th>
        </tr>
      </thead>
      <tbody></tbody>
    </table>

    <div style="margin-top: 1rem;">
      <button onclick="loadDataFromBuilder()">Load Graph</button>
      <button onclick="closeDataBuilder()">Close</button>
    </div>
  </div>
</div>

<div id="graph-wrapper">
<div id="graph-controls">
  <input type="file" id="data-upload" accept=".json,.csv" />
  <button onclick="toggleDataBuilder()">Open Data Builder</button>
  <input type="text" id="search-box" list="concepts-list" placeholder="Search concept..." />
  <datalist id="concepts-list"></datalist>
  <button onclick="resetView()">Reset View</button>
  <button id="fullscreen-toggle" onclick="toggleFullScreen()">Full screen</button>
</div>
<div id="data-builder-modal" style="display: none;">
  <div style="background: white; padding: 1rem; max-width: 800px; margin: 2rem auto; border-radius: 8px; box-shadow: 0 0 20px rgba(0,0,0,0.2);">
    <h3>Edit Your Concept Map</h3>
    <textarea id="builder-textarea" style="width: 100%; height: 300px; font-family: monospace;"></textarea>
    <br />
    <button onclick="loadDataFromBuilder()">Load Data</button>
    <button onclick="closeDataBuilder()">Close</button>
  </div>
</div>


  <div id="graph-container"></div>
</div>



<script src="https://giscus.app/client.js"
        data-repo="natesheehan/conceptcartography"
        data-repo-id="R_kgDOPB5QiQ"
        data-category="General"
        data-category-id="DIC_kwDOPB5Qic4CsAxd"
        data-mapping="pathname"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="catppuccin_mocha"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>


<!-- Load the 3d-force-graph library and wait for it -->
<script>
  const forceGraphScript = document.createElement('script');
  forceGraphScript.src = 'https://unpkg.com/3d-force-graph';
  forceGraphScript.onload = () => {
    initGraph(); // call setup function only when the library is ready
    function toggleDataBuilder() {
  const modal = document.getElementById('data-builder-modal');
  modal.style.display = modal.style.display === 'none' ? 'block' : 'none';
}

function closeDataBuilder() {
  document.getElementById('data-builder-modal').style.display = 'none';
}
function loadDataFromBuilder() {
  const nodes = [];
  const links = [];

  // Read nodes
  document.querySelectorAll("#nodes-table tbody tr").forEach(tr => {
    const id = tr.querySelector("input").value.trim();
    if (id) nodes.push({ id });
  });

  // Read links
  document.querySelectorAll("#links-table tbody tr").forEach(tr => {
    const source = tr.querySelector('input[name="source"]').value.trim();
    const target = tr.querySelector('input[name="target"]').value.trim();
    const type = tr.querySelector('input[name="type"]').value.trim();
    if (source && target && type) {
      links.push({ source, target, type });
    }
  });

  renderGraph({ nodes, links });
  closeDataBuilder();
}
function toggleDataBuilder() {
  document.getElementById('data-builder-modal').style.display = 'block';
  // Clear tables on open
  document.querySelector("#nodes-table tbody").innerHTML = '';
  document.querySelector("#links-table tbody").innerHTML = '';
  addNodeRow(); addLinkRow();
}

function closeDataBuilder() {
  document.getElementById('data-builder-modal').style.display = 'none';
}

function addNodeRow(id = "") {
  const row = document.createElement("tr");
  row.innerHTML = `
    <td><input type="text" value="${id}" style="width: 100%;"></td>
    <td><button onclick="this.closest('tr').remove()">🗑️</button></td>
  `;
  document.querySelector("#nodes-table tbody").appendChild(row);
}

function addLinkRow(source = "", target = "", type = "") {
  const row = document.createElement("tr");
  row.innerHTML = `
    <td><input type="text" name="source" value="${source}" style="width: 100%;"></td>
    <td><input type="text" name="target" value="${target}" style="width: 100%;"></td>
    <td><input type="text" name="type" value="${type}" style="width: 100%;"></td>
    <td><button onclick="this.closest('tr').remove()">🗑️</button></td>
  `;
  document.querySelector("#links-table tbody").appendChild(row);
}

function loadDataFromBuilder() {
  try {
    const json = JSON.parse(document.getElementById('builder-textarea').value);
    renderGraph(json);
    closeDataBuilder();
  } catch (e) {
    alert("Invalid JSON");
  }
}

document.getElementById('data-upload').addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = () => {
    try {
      const content = reader.result;
      const json = file.name.endsWith('.csv') ? csvToJson(content) : JSON.parse(content);
      renderGraph(json);
    } catch (err) {
      alert("Error loading file: " + err.message);
    }
  };
  reader.readAsText(file);
});
function renderGraph(data) {
  const degreeMap = {};
  data.nodes.forEach(n => degreeMap[n.id.toLowerCase()] = 0);
  data.links.forEach(link => {
    const source = (link.source || '').toLowerCase();
    const target = (link.target || '').toLowerCase();
    if (degreeMap[source] !== undefined) degreeMap[source]++;
    if (degreeMap[target] !== undefined) degreeMap[target]++;
  });

  data.nodes.forEach(n => {
    const deg = degreeMap[n.id.toLowerCase()] || 1;
    n.val = Math.min(20, 1 + deg);
  });

  const datalist = document.getElementById('concepts-list');
  datalist.innerHTML = ''; // reset
  data.nodes.forEach(node => {
    const opt = document.createElement("option");
    opt.value = node.id;
    datalist.appendChild(opt);
  });

  const colorMap = {
    "type of": "blue", "part of": "green", "produces": "purple",
    "counteracts": "red", "similar to": "orange", "equivalent to": "gray",
    "distinct from": "lime", "depends on": "cyan"
  };

  Graph = ForceGraph3D()(document.getElementById('graph-container'))
    .graphData(data)
    .nodeLabel(node => node.id)
    .nodeColor(() => 'black')
    .nodeVal(node => node.val)
    .linkColor(link => colorMap[link.type?.toLowerCase().trim()] || 'gray')
    .linkWidth(1.5)
    .linkOpacity(0.8)
    .backgroundColor('#fdfdfd')
    .linkDirectionalParticles(5)
    .linkDirectionalParticleWidth(2)
    .linkDirectionalParticleColor(link => colorMap[link.type?.toLowerCase().trim()] || 'gray')
    .onNodeClick(node => {
      const slug = node.id.toLowerCase().replace(/\s+/g, '-');
      window.location.href = `/concepts/${slug}`;
    })
    .onBackgroundClick(() => Graph.zoomToFit(200));

  setTimeout(() => {
    const container = document.getElementById('graph-container');
    Graph.width(container.offsetWidth);
    Graph.height(container.offsetHeight);
    Graph.zoomToFit(400);
  }, 0);
}


function csvToJson(csvText) {
  const [header, ...lines] = csvText.trim().split('\n').map(line => line.split(','));
  const nodes = [];
  const links = [];
  for (const row of lines) {
    const entry = Object.fromEntries(header.map((k, i) => [k.trim(), row[i]?.trim() || ""]));
    if (entry["source"] && entry["target"] && entry["type"]) {
      links.push({ source: entry["source"], target: entry["target"], type: entry["type"] });
    }
    if (entry["id"]) {
      nodes.push({ id: entry["id"] });
    }
  }
  return { nodes, links };
}

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

document.getElementById('search-box').addEventListener('change', function () {
  focusOnConcept(this.value);
});


function toTitleCase(str) {
  return str.replace(/\w\S*/g, w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase());
}

function initGraph() {
// Always fetch the JSON from the /maps/ root, not from the page folder
const slugMatch = window.location.pathname.match(/\/maps\/([^\/]+)/);
const slug = slugMatch ? slugMatch[1] : '';
const jsonFile = `/conceptcartography/maps/${slug}.json`;

  fetch(jsonFile)
    .then(res => res.json())
    .then(data => renderGraph(data))
    .then(data => {
      // Count connections per node (degree)
      const degreeMap = {};
      data.nodes.forEach(n => degreeMap[n.id.toLowerCase()] = 0);
      data.links.forEach(link => {
        const source = (link.source || '').toLowerCase();
        const target = (link.target || '').toLowerCase();
        if (degreeMap[source] !== undefined) degreeMap[source]++;
        if (degreeMap[target] !== undefined) degreeMap[target]++;
      });

      // Add nodeVal for sizing
      data.nodes.forEach(n => {
        const deg = degreeMap[n.id.toLowerCase()] || 1;
        n.val = Math.min(20, 1 + deg); // size capped to 10 for clarity
      });

      // Add datalist for search
      const datalist = document.getElementById('concepts-list');
      data.nodes.forEach(node => {
        const opt = document.createElement("option");
        opt.value = node.id;
        datalist.appendChild(opt);
      });

      const colorMap = {
        "type of": "blue",
        "part of": "green",
        "produces": "purple",
        "counteracts": "red",
        "similar to": "orange",
        "equivalent to": "gray",
        "distinct from": "lime",
        "depends on": "cyan"
      };
      const normalize = str => (str || "").toLowerCase().trim();

      Graph = ForceGraph3D()(document.getElementById('graph-container'))
        .graphData(data)
        .nodeLabel(node => node.id)
        .nodeColor(() => 'black')
        .nodeVal(node => node.val) // <--- Set size based on val
        .linkColor(link => colorMap[normalize(link.type)] || 'green')
        .linkWidth(1.5)
        .linkOpacity(0.8)
        .backgroundColor('#fdfdfd')
        .linkDirectionalParticles(5)
        .linkDirectionalParticleWidth(2)
        .linkDirectionalParticleColor(link => colorMap[normalize(link.type)] || 'gray')
        .onNodeClick(node => {
          const slug = node.id.toLowerCase().replace(/\s+/g, '-');
          window.location.href = `/concepts/${slug}`;
        })
        .onBackgroundClick(() => Graph.zoomToFit(200));
        // Wait for layout and container to stabilize, then zoom and center the graph
setTimeout(() => {
  const container = document.getElementById('graph-container');
  Graph.width(container.offsetWidth);
  Graph.height(container.offsetHeight);
  Graph.zoomToFit(400);
}, 0); // Immediate timeout waits for next repaint

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
  if (!node) return;

  const distance = 100;
  const distRatio = 1 + distance / Math.hypot(node.x, node.y, node.z || 1);

  Graph.cameraPosition(
    {
      x: node.x * distRatio,
      y: node.y * distRatio,
      z: (node.z || 1) * distRatio
    },
    node,
    1000
  );

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
</script><!-- GRAPH END -->
