# Epistemic Diversity


## ❔ Description
Who and what is included or excluded in knowledge practice? How does that matter both for what and how we know, and for recognition, equity, and justice? These are topics at the forefront of fields like feminist epistemology, critical race studies, social epistemology, political epistemology, indigenous studies, science and technology studies, and philosophy of science.

The map makes visible some of the intertwined political and epistemic dimensions of knowledge creation and sharing discussed in this literature. Like all maps, this one is a single perspective on a complicated terrain. It is non-exhaustive. It connects ideas, rather than citations. It aims to give a sense for the diversity of voices and areas where these topics come up, while acknowledging that there is so much more to see and do between and beyond the points we depict.

You can use this map to navigate the conceptual space, trace conceptual lineages and interrelations, and explore definitions and references. Take it as a starting point, a piece of equipment for orienting your thinking. At the same time, we hope that the map will preserve some disorientation: that it will raise questions, disrupt standard narratives, and create a sense of discomfort at its own inadequacy.

This map was created based primarily on readings from an interdisciplinary, international, online reading group, beginning in mid-2024. We thank everyone who came along and shared their insights and ideas and contributed to a series of enlightening and provocative discussions.

<style>
#graph-wrapper {
  max-width: 100vw;
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
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 99999; /* Make sure it’s above the sidebar */
  background: #ffffff;
  margin: 0;
  padding: 0;
}

#graph-wrapper.fullscreen canvas,
#graph-wrapper.fullscreen #graph-container {
  width: 100vw !important;
  height: 100vh !important;
  margin: 0;
  padding: 0;
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
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(6px);
  font-size: 0.85em;
  text-align: center;
  padding: 0.6rem 1rem;
  border-top: 1px solid #ccc;
  z-index: 999;
}


#search-box {
  background: white;
  font-family: inherit;
}

datalist option {
  font-size: 0.9rem;
}
.legend-item {
  cursor: pointer;
  padding: 0 4px;
  border-bottom: 2px solid transparent;
  transition: all 0.2s ease;
}

.legend-item:hover {
  border-bottom: 2px solid currentColor;
}

.legend-item.active {
  font-weight: bold;
  border-bottom: 2px solid currentColor;
}
.icon-btn {
  position: relative;
  background-color: #f5f5f5;
  color: #333;
  border: 1px solid #ccc;
  border-radius: 50%;
  width: 42px;
  height: 42px;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
}

.icon-btn:hover {
  background-color: #e8e8e8;
  transform: scale(1.1);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.icon-btn:active {
  background-color: #ddd;
  transform: scale(0.95);
}

.icon-btn i {
  pointer-events: none;
}

/* Tooltip styling */
.icon-btn::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: -1.8rem;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(60, 60, 60, 0.9);
  color: #fff;
  padding: 4px 8px;
  font-size: 0.8rem;
  border-radius: 4px;
  opacity: 0;
  pointer-events: none;
  white-space: nowrap;
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.icon-btn:hover::after {
  opacity: 1;
  transform: translateX(-50%) translateY(4px);
}
#concept-details {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: clamp(300px, 28%, 400px);
  max-height: 85vh;
  overflow-y: auto;
  overflow-x: hidden;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  font-family: "Inter", sans-serif;
  color: #374151;
  display: none;
  z-index: 1000;
  transition: all 0.3s ease, transform 0.3s ease;
}

#concept-details h3 {
  margin-top: 0;
  font-size: 1.5rem;
  font-weight: 700;
  color: #1f2937;
  border-bottom: 2px solid #e5e7eb;
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
}

#concept-details section {
  margin-bottom: 1.2rem;
}

#concept-details section strong {
  display: block;
  margin-bottom: 0.6rem;
  color: #111827;
  font-weight: 600;
}

#concept-details p {
  margin: 0.4rem 0;
  line-height: 1.6;
  color: #4b5563;
}

.relation-pill {
  display: inline-block;
  background-color: #6b7280;
  color: #fff;
  padding: 0.35rem 0.75rem;
  margin: 0.2rem;
  border-radius: 999px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.2s ease;
}

.relation-pill:hover {
  background-color: #4b5563;
  transform: scale(1.05);
}
.tabs {
  display: flex;
  flex-wrap: wrap; /* allow wrapping on small screens */
  border-bottom: 2px solid #e5e7eb;
  margin-bottom: 1rem;
  gap: 0.4rem; /* spacing between buttons */
  overflow-x: auto; /* horizontal scroll on overflow */
  -webkit-overflow-scrolling: touch; /* smooth on iOS */
}

.tab-btn {
  flex: 1 1 auto; /* grow and shrink as needed */
  min-width: 100px; /* prevent too small buttons */
  text-align: center;
  background: none;
  border: none;
  border-bottom: 3px solid transparent;
  padding: 0.6rem 1rem;
  font-weight: 600;
  color: #4b5563;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap; /* prevent text wrapping */
}

.tab-btn.active {
  color: #1a202c;
  border-color: #3182ce;
}

.tab-btn:hover {
  background-color: #f1f5f9;
}

.tab-content {
  display: none;
}

.tab-content.active {
  display: block;
}



}

</style>


## 🗺️ Map 

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<div id="graph-wrapper">
<div id="graph-controls">
  <input type="text" id="search-box" list="concepts-list" placeholder="Search concept..." />
  <datalist id="concepts-list"></datalist>

  <!-- Reset View Button -->
  <button class="icon-btn" onclick="resetView()" data-tooltip="Reset View">
    <i class="fas fa-undo-alt"></i>
  </button>

  <!-- Fullscreen Toggle Button -->
  <button class="icon-btn" id="fullscreen-toggle" onclick="toggleFullScreen()" data-tooltip="Toggle Fullscreen">
    <i class="fas fa-expand-arrows-alt" id="fullscreen-icon"></i>
  </button>

  <!-- Random Concept Button -->
  <button class="icon-btn" onclick="jumpToRandomConcept()" data-tooltip="Jump to Random Concept">
    <i class="fas fa-random"></i>
  </button>
</div>



  <div id="graph-container"></div>
<div id="concept-details">
  <h3 id="details-title"></h3>
  <div class="tabs">
    <button class="tab-btn active" onclick="showTab(event, 'definition-tab')">📖 Definitions</button>
    <button class="tab-btn" onclick="showTab(event, 'references-tab')">📚 References</button>
    <button class="tab-btn" onclick="showTab(event, 'relations-tab')">🔗 Related</button>
  </div>
  <div id="definition-tab" class="tab-content active">
    <p id="details-definition"></p>
  </div>
  <div id="references-tab" class="tab-content">
    <p id="details-references"></p>
  </div>
  <div id="relations-tab" class="tab-content">
    <div id="details-relations"></div>
  </div>
  <p style="margin-top:1rem;"><a id="details-link" href="#" target="_blank" style="color:#007acc;">🔗 View full concept →</a></p>
</div>


<div id="graph-legend">
  <strong>Relation types (click to filter):</strong><br>
  <span class="legend-item" data-type="type of" style="color: blue;">Type of</span>, 
  <span class="legend-item" data-type="part of" style="color: green;">Part of</span>, 
  <span class="legend-item" data-type="produces" style="color: purple;">Produces</span>, 
  <span class="legend-item" data-type="counteracts" style="color: red;">Counteracts</span>, 
  <span class="legend-item" data-type="similar to" style="color: orange;">Similar to</span>, 
  <span class="legend-item" data-type="equivalent to" style="color: gray;">Equivalent to</span>, 
  <span class="legend-item" data-type="distinct from" style="color: black;">Distinct from</span>, 
  <span class="legend-item" data-type="depends on" style="color: cyan;">Depends on</span>
</div>

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

function showTab(evt, tabId) {
  // Hide all tab contents
  document.querySelectorAll('.tab-content').forEach(tab => {
    tab.classList.remove('active');
  });

  // Deactivate all tab buttons
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.remove('active');
  });

  // Activate the clicked tab
  document.getElementById(tabId).classList.add('active');
  evt.currentTarget.classList.add('active');
}


function jumpToRandomConcept() {
  if (!Graph) return;

  const nodes = Graph.graphData().nodes;
  if (nodes.length === 0) return;

  const randomNode = nodes[Math.floor(Math.random() * nodes.length)];
  highlightNode(randomNode);
}


function showModal(contentHTML) {
  // Create backdrop
  const backdrop = document.createElement('div');
  backdrop.style.position = 'fixed';
  backdrop.style.top = '0';
  backdrop.style.left = '0';
  backdrop.style.width = '100vw';
  backdrop.style.height = '100vh';
  backdrop.style.background = 'rgba(0, 0, 0, 0.6)';
  backdrop.style.display = 'flex';
  backdrop.style.justifyContent = 'center';
  backdrop.style.alignItems = 'center';
  backdrop.style.zIndex = '10000';

  // Create modal
  const modal = document.createElement('div');
  modal.style.background = '#fff';
  modal.style.borderRadius = '8px';
  modal.style.boxShadow = '0 10px 40px rgba(0, 0, 0, 0.3)';
  modal.style.maxWidth = '90vw';
  modal.style.maxHeight = '80vh';
  modal.style.overflowY = 'auto';
  modal.innerHTML = contentHTML;

  // Close button
  const closeBtn = document.createElement('button');
  closeBtn.innerText = 'Close';
  closeBtn.style.display = 'block';
  closeBtn.style.margin = '1rem auto 0';
  closeBtn.style.padding = '0.5rem 1rem';
  closeBtn.style.border = '1px solid #ccc';
  closeBtn.style.background = 'black';
  closeBtn.style.borderRadius = '4px';
  closeBtn.style.cursor = 'pointer';
  closeBtn.onclick = () => backdrop.remove();

  modal.appendChild(closeBtn);
  backdrop.appendChild(modal);
  backdrop.onclick = e => {
    if (e.target === backdrop) backdrop.remove();
  };
  document.body.appendChild(backdrop);
}


function toTitleCase(str) {
  return str.replace(/\w\S*/g, w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase());
}

function initGraph() {
  fetch('../../assets/graph.json')
    .then(res => res.json())
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
  .backgroundColor('#fdf6e3') // warm, creamy canvas like fabric
  .nodeColor(() => '#dc2626') // deep red “stitch knots”
  .nodeOpacity(1)             // flat, solid like thread
  .nodeRelSize(3.5)           // small like embroidery knots
  .linkColor(link => colorMap[normalize(link.type)] || '#7f5539') // earthy thread colours
  .linkOpacity(0.9)           // strong thread appearance
  .linkWidth(3)               // thick like embroidery floss
  .linkCurveRotation(() => Math.PI / 6) // more natural thread curvature
  .nodeVal(node => node.val)
  .nodeLabel(node => node.title || node.id)
  .linkDirectionalArrowLength(0) // no arrows
  .linkDirectionalArrowRelPos(0);


let activeFilters = new Set();

document.querySelectorAll('.legend-item').forEach(item => {
  item.addEventListener('click', () => {
    const type = item.dataset.type.toLowerCase();

    if (activeFilters.has(type)) {
      activeFilters.delete(type);
      item.classList.remove('active');
    } else {
      activeFilters.add(type);
      item.classList.add('active');
    }

    updateGraphFilters();
  });
});

function updateGraphFilters() {
  const links = Graph.graphData().links;

  if (activeFilters.size === 0) {
    // Show all links if no filters
    Graph.linkVisibility(() => true);
    Graph.nodeVisibility(() => true);
    return;
  }

  // Filter links and nodes based on active relation types
  const visibleLinks = links.filter(link => activeFilters.has((link.type || '').toLowerCase()));
  const visibleNodes = new Set();

  visibleLinks.forEach(link => {
    visibleNodes.add(link.source.id);
    visibleNodes.add(link.target.id);
  });

  Graph.linkVisibility(link => activeFilters.has((link.type || '').toLowerCase()));
  Graph.nodeVisibility(node => visibleNodes.has(node.id));
}

Graph.onNodeClick(node => {
  highlightNode(node);
});
Graph.onBackgroundClick(() => {
  // Reset node and link colors
  Graph.nodeColor(() => '#3b3b3b'); // Default grey for nodes
  Graph.linkColor(() => '#cccccc'); // Default light grey for links

  // Hide the details panel
  document.getElementById('concept-details').style.display = 'none';


});


      
        // Wait for layout and container to stabilize, then zoom and center the graph
setTimeout(() => {
  const container = document.getElementById('graph-container');
  Graph.width(container.offsetWidth);
  Graph.height(container.offsetHeight);
  Graph.zoomToFit(400);
}, 0); // Immediate timeout waits for next repaint

    });
}

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/\s+/g, '-')         // replace spaces with hyphens
    .replace(/[^\w\-]+/g, '')     // remove non-word chars
    .replace(/\-\-+/g, '-')       // collapse multiple hyphens
    .replace(/^-+/, '')           // trim leading hyphens
    .replace(/-+$/, '');          // trim trailing hyphens
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

  // Force redraw of canvas at fullscreen size
  setTimeout(() => {
    Graph.width(window.innerWidth);
    Graph.height(window.innerHeight);
  }, 100); // Delay ensures DOM fully updated

  const icon = document.getElementById('fullscreen-icon');
if (isFullscreen) {
  icon.classList.remove('fa-expand-arrows-alt');
  icon.classList.add('fa-compress-arrows-alt');
} else {
  icon.classList.remove('fa-compress-arrows-alt');
  icon.classList.add('fa-expand-arrows-alt');
}

}

function focusOnConcept(query) {
  if (!Graph || !query.trim()) return;

  const normalized = query.toLowerCase().trim();
  const node = Graph.graphData().nodes.find(n => n.id.toLowerCase() === normalized)
             || Graph.graphData().nodes.find(n => n.id.toLowerCase().includes(normalized));

  if (node) {
    // Trigger the same behaviour as clicking on a node
    highlightNode(node);

    // Reset the search box
    document.getElementById('search-box').value = '';
  }
}

function highlightNode(node) {
  if (!node) return;

  // Highlight node and its neighbors
  const neighbors = new Set();
  const links = Graph.graphData().links;

const relatedConceptsMap = new Map();

links.forEach(link => {
  const neighborId = link.source.id === node.id ? link.target.id : (link.target.id === node.id ? link.source.id : null);
  if (neighborId && !relatedConceptsMap.has(neighborId)) {
    neighbors.add(neighborId);
    relatedConceptsMap.set(neighborId, {
      id: neighborId,
      title: link.source.id === node.id ? link.target.title || link.target.id : link.source.title || link.source.id,
      type: link.type
    });
  }
});

const relatedConcepts = Array.from(relatedConceptsMap.values());

  // Update node colors
  Graph.nodeColor(n => {
    if (n.id === node.id) return '#facc15'; // Highlight clicked node
    if (neighbors.has(n.id)) return '#38bdf8'; // Blue for neighbors
    return '#3b3b3b'; // Default grey
  });

  // Update link colors
  Graph.linkColor(link => {
    if (link.source.id === node.id || link.target.id === node.id) {
      return '#f87171'; // Red for connected links
    }
    return '#cccccc'; // Default light grey
  });

  // Zoom camera to node
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

  // Generate related concepts HTML
  // Generate related concepts buttons under the title
const relatedButtonsHTML = relatedConcepts.length > 0
  ? `<div style="margin-top: 0.6rem; margin-bottom: 1rem; display: flex; flex-wrap: wrap; gap: 0.4rem;">
        ${relatedConcepts.map(concept => `
          <button class="relation-pill" style="
            background-color: ${getRelationColor(concept.type)};
            color: #fff;
            padding: 0.35rem 0.75rem;
            border: none;
            border-radius: 999px;
            font-size: 0.85rem;
            cursor: pointer;
            transition: transform 0.2s ease;"
            onclick="focusOnConcept('${concept.id}')"
            title="Relation: ${toTitleCase(concept.type)}">
            ${concept.title}
          </button>
        `).join('')}
     </div>`
  : '';

document.getElementById('details-title').innerHTML = `
  ${node.title}
  ${relatedButtonsHTML}
`;


  // Update details panel
  // Update the popup content without wiping the tab structure
document.getElementById('details-title').innerText = node.title;

// Clean definition text
const cleanDefinition = (node.definition || "")
  .replace(/^>\s*/gm, "")
  .trim();
document.getElementById('details-definition').innerText = cleanDefinition || "No definition available.";

// References
document.getElementById('details-references').innerHTML = node.reference
  ? node.reference.replace(/(https?:\/\/\S+)/g, '<a href="$1" target="_blank">$1</a>')
  : "No references.";

// Related Concepts
document.getElementById('details-relations').innerHTML = relatedConcepts.length > 0
  ? `<div style="display:flex;flex-wrap:wrap;gap:0.4rem;margin-top:0.4rem;">
        ${relatedConcepts.map(concept => `
          <span class="relation-pill" style="
            background-color: ${getRelationColor(concept.type)};
            color: white;
            padding: 0.3rem 0.6rem;
            border-radius: 999px;
            font-size: 0.85rem;
            cursor: pointer;
            white-space: nowrap;"
            onclick="focusOnConcept('${concept.id}')"
            title="${toTitleCase(concept.type)}">
            ${concept.title}
          </span>
        `).join('')}
      </div>`
  : '<em>No related concepts.</em>';

// Link to full concept
document.getElementById('details-link').href = `../../concepts/${slugify(node.id)}`;

// Show popup
document.getElementById('concept-details').style.display = 'block';

// Reset tabs to first tab
document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
document.querySelector('.tab-btn').classList.add('active');
document.querySelector('.tab-content').classList.add('active');

}
function getRelationColor(type) {
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
  return colorMap[(type || '').toLowerCase()] || "#888";
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

<!-- Load the 3d-force-graph library and wait for it -->
<script>
  const forceGraphScript = document.createElement('script');
  forceGraphScript.src = 'https://unpkg.com/3d-force-graph';
  forceGraphScript.onload = () => {
    initGraph(); // call setup function only when the library is ready
  };
  
  document.head.appendChild(forceGraphScript);
</script>

## ✍️ Authors
Rose Trappes, Nathanael Sheehan, Rena Alcalay 


