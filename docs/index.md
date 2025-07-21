# 
<h1 style="
  font-size: 1.75rem;
  text-align: center;
  margin-bottom: 2rem;
  font-weight: 600;
  color: var(--md-typeset-color, #333);
">Concept Cartography</h1>
<img src="assets/homelogo.gif" style="border:black 9px solid;height:400px;width:600px;display:block;margin:auto;">

# Our Community 

<div id="contributors" style="
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 1.5rem;
  justify-items: center;
  align-items: center;
  padding: 1rem;
  border-radius: 10px;
  background-color: rgba(240, 240, 240, 0.4);
  max-width: 800px;
  margin: 0 auto;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
">


</div>

<script>
  const repo = "natesheehan/conceptcartography";

  fetch(`https://api.github.com/repos/${repo}/contributors`)
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("contributors");
      container.innerHTML = data.map(user => `
        <a href="${user.html_url}" target="_blank" title="${user.login}" style="
          display: flex;
          flex-direction: column;
          align-items: center;
          text-decoration: none;
          color: inherit;
          transition: transform 0.2s ease, box-shadow 0.2s ease;
          border-radius: 8px;
          padding: 0.5rem;
        " onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 4px 12px rgba(0,0,0,0.08)'"
          onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='none'">
          <img src="${user.avatar_url}&s=96" alt="${user.login}" style="
            width: 64px;
            height: 64px;
            border-radius: 50%;
            border: 1px solid #ccc;
            object-fit: cover;
            margin-bottom: 0.5rem;
            transition: box-shadow 0.3s ease;
          ">
          <span style="
            font-size: 0.8rem;
            font-weight: 500;
            text-align: center;
          ">${user.login}</span>
        </a>
      `).join('');
    })
    .catch(err => {
      document.getElementById("contributors").innerHTML = "<p style='text-align: center; color: #888;'>Failed to load contributors.</p>";
      console.error(err);
    });
</script>
