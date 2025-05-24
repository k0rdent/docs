document.addEventListener('DOMContentLoaded', function() {
    // The theme's JavaScript will run first and set up the repository for the second badge
    
    // Find all repository links
    const repoLinks = document.querySelectorAll('a.md-source[data-md-component="source"]');
    
    // If we have more than one, set up the first one with the correct repository info
    if (repoLinks.length >= 1) {
      const repoInfo = document.getElementById('repo-info');
      if (repoInfo) {
        const repoName = repoInfo.getAttribute('data-repo-name');
        const repoUrl = repoInfo.getAttribute('data-repo-url');
        
        // Set first badge to show KCM data
        repoLinks[0].href = repoUrl;
        
        // Fix repository name
        const repoNameEl = repoLinks[0].querySelector('.md-source__repository');
        if (repoNameEl) {
          repoNameEl.textContent = repoName;
        }
        
        // Remove facts that might have been added already
        const facts = repoLinks[0].querySelector('.md-source__facts');
        if (facts) {
          facts.innerHTML = '';
        }
        
        // Now call the GitHub API for KCM stats
        fetch('https://api.github.com/repos/k0rdent/kcm')
          .then(response => response.json())
          .then(data => {
            // Create or get facts container
            let factsDiv = facts || document.createElement('div');
            if (!facts) {
              factsDiv.className = 'md-source__facts';
              repoLinks[0].appendChild(factsDiv);
            }
            
            // Create star fact
            const starFact = document.createElement('div');
            starFact.className = 'md-source__fact';
            starFact.textContent = data.stargazers_count;
            factsDiv.appendChild(starFact);
            
            // Create fork fact
            const forkFact = document.createElement('div');
            forkFact.className = 'md-source__fact';
            forkFact.textContent = data.forks_count;
            factsDiv.appendChild(forkFact);
          });
      }
    }
  });