---
hide:
  - navigation
  - toc
  - feedback
---

<!-- Page title for SEO/accessibility; visually hidden -->
<h1 class="sr-only">k0rdent API documentation</h1>

<!-- Page-specific CSS -->
<style>
  /* Remove default margins so ReDoc can use full height */
  .md-main__inner { margin-top: 0 !important; }
  .md-content { margin-top: 0 !important; }
  html, body { height: 100%; }

  /* Hide the header palette toggle (light/dark switch) on THIS page only */
  .md-header__option[data-md-component="palette"],
  form[data-md-component="palette"] {
    display: none !important;
  }

  /* Full-bleed page width */
  .md-header .md-grid,
  .md-main .md-grid,
  .md-footer .md-grid {
    max-width: none;
  }

  /* Remove content padding so ReDoc can span edge-to-edge */
  .md-content,
  .md-content__inner {
    margin: 0 !important;
    padding: 0 !important;
  }

  /* Hide footer (prevents the ugly overlap) */
  .md-footer { display: none !important; }

  /* Ensure sidebars never appear */
  .md-sidebar--primary,
  .md-sidebar--secondary {
    display: none !important;
  }

  /* ReDoc canvas */
  #redoc-container {
    min-height: 100vh;
    height: 100vh;
  }

  /* Smallify function-name headers for small screens */
  #redoc-container h2 { font-size: 1.3em !important; }

/* ReDoc sidebar: allow long operation names to wrap */
.redoc-wrap .menu-content,
.redoc-wrap .menu-content .menu-item,
.redoc-wrap .menu-content .menu-item .label,
.redoc-wrap .menu-content .operation-name,
.redoc-wrap .menu-content .section-item {
  white-space: normal !important;
  word-break: break-word;
  overflow-wrap: anywhere;
}

</style>

<!-- Force light theme on THIS page only (non-persistent) -->
<script>
  (function () {
    function forceLight() {
      document.body.setAttribute("data-md-color-scheme", "default");
      document.body.setAttribute("data-md-color-primary", "indigo");
      document.body.setAttribute("data-md-color-accent", "indigo");
      // Reflect "light" radio without touching localStorage
      var light = document.querySelector('input.md-option#\\_\\_palette_0');
      if (light) light.checked = true;
    }
    forceLight();
    document.addEventListener("DOMContentLoaded", forceLight);
  })();
</script>

<!-- ReDoc mount -->
<div id="redoc-container"></div>

<!-- ReDoc bundle -->
<script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>

<!-- Initialize ReDoc with a robust spec URL (so this script works for all versions) and take control of panel relative widths -->
<script>
  (function () {
    var specUrl = new URL("../openapi/k0rdent-api-main.json", window.location.href).pathname;

    Redoc.init(specUrl, {
      scrollYOffset: 0,
      theme: {
        /* widen the left menu (default ~260px) */
        sidebar: { width: '320px' },        // try 320–360px

        /* make the right examples panel narrower */
        rightPanel: { width: '30%' }        // try 28–34%
      }
    }, document.getElementById("redoc-container"));
  })();
</script>






