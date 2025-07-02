# About us

<div style="display: flex; gap: 1rem; flex-wrap: wrap; justify-content: center; margin-bottom: 2rem;">
  <img src="img/mod1.jpg" alt="Moderator 1" width="150" />
  <img src="img/mod2.jpg" alt="Moderator 2" width="150" />
  <img src="img/mod3.jpg" alt="Moderator 3" width="150" />
</div>

# Contributors

<div id="contributors">

</div>

<script>
  const repo = "natesheehan/conceptcartography"; // ← Replace this with your actual repo

  fetch(`https://api.github.com/repos/${repo}/contributors`)
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("contributors");
      container.innerHTML = "<ul>" + data.map(user =>
        `<li><a href="${user.html_url}" target="_blank">${user.login}</a> — ${user.contributions} commits</li>`
      ).join('') + "</ul>";
    })
    .catch(err => {
      document.getElementById("contributors").innerText = "Failed to load contributors.";
      console.error(err);
    });
</script>
