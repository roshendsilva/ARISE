/* ARISE Catholic Apologetics Platform Client Script
   Handles Dark Mode, Table of Contents scrolling, Citation generator, and UI helpers.
*/

document.addEventListener('DOMContentLoaded', () => {
  // 1. Dark Mode / Light Mode Persisted Toggle
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  const themeIcon = document.getElementById('theme-icon');
  const themeText = document.getElementById('theme-text');

  const currentTheme = localStorage.getItem('arise-theme') || 'light';
  applyTheme(currentTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(newTheme);
      localStorage.setItem('arise-theme', newTheme);
    });
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    if (themeIcon) {
      if (theme === 'dark') {
        themeIcon.className = 'bi bi-sun-fill text-warning me-1';
        if (themeText) themeText.textContent = 'Light Mode';
      } else {
        themeIcon.className = 'bi bi-moon-stars-fill me-1';
        if (themeText) themeText.textContent = 'Dark Mode';
      }
    }
  }

  // 2. Article Reading View - Table of Contents Active Link Highlight
  const tocLinks = document.querySelectorAll('.toc-list a');
  const sections = document.querySelectorAll('.scholarly-box, .article-section');

  if (tocLinks.length > 0 && sections.length > 0) {
    window.addEventListener('scroll', () => {
      let currentSectionId = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop - 120;
        if (window.scrollY >= sectionTop) {
          currentSectionId = section.getAttribute('id');
        }
      });

      tocLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSectionId}`) {
          link.classList.add('active');
        }
      });
    });
  }

  // 3. In-Article Quick Filter / Search
  const articleSearchInput = document.getElementById('article-search-input');
  if (articleSearchInput) {
    articleSearchInput.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase().trim();
      const boxes = document.querySelectorAll('.scholarly-box');
      boxes.forEach(box => {
        const text = box.textContent.toLowerCase();
        if (term === '' || text.includes(term)) {
          box.style.display = 'block';
        } else {
          box.style.display = 'none';
        }
      });
    });
  }
});

// 4. Citation Copy Modal Helper
function copyCitation(format, title, author, url) {
  let citation = '';
  const date = new Date().getFullYear();

  if (format === 'catholic') {
    citation = `ARISE Apologetics Library. "${title}." Catholic Theological Defense Series (${date}). Web. <${url}>`;
  } else if (format === 'mla') {
    citation = `ARISE Research Team. "${title}." ARISE Catholic Apologetics Platform, ${date}, ${url}.`;
  } else if (format === 'apa') {
    citation = `ARISE Platform. (${date}). ${title}. Retrieved from ${url}`;
  }

  navigator.clipboard.writeText(citation).then(() => {
    alert(`Copied ${format.toUpperCase()} Citation to clipboard:\n\n` + citation);
  }).catch(err => {
    console.error('Failed to copy citation: ', err);
  });
}

// 5. Share Article Helper
function shareArticle(title, url) {
  if (navigator.share) {
    navigator.share({
      title: title,
      text: `Read this Catholic theological defense on ARISE: ${title}`,
      url: url,
    }).catch(console.error);
  } else {
    navigator.clipboard.writeText(url).then(() => {
      alert('Article link copied to clipboard!');
    });
  }
}
