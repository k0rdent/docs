// docs/javascripts/plausible-loader.js
(function () {
  // Prevent duplicate loads
  if (window.__plausibleLoaded) return;
  window.__plausibleLoaded = true;

  // Create the script tag Plausible provided
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://plausible.io/js/pa-6S0x1KqBcDkAQ6nmjTKTl.js'; // your pa-… URL
  s.onload = function () {
    // Initialize exactly as their snippet does
    window.plausible = window.plausible || function () {
      (plausible.q = plausible.q || []).push(arguments);
    };
    plausible.init = plausible.init || function (opts) {
      plausible.o = opts || {};
    };
    plausible.init(); // use server-side config baked into pa-… script
  };

  document.head.appendChild(s);
})();
