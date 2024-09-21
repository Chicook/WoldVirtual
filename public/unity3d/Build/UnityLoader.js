/* UnityLoader.js */
(function() {
  var UnityLoader = {
    instantiate: function(containerId, buildUrl) {
      var container = document.getElementById(containerId);
      if (!container) {
        console.error('Container not found:', containerId);
        return;
      }

      var script = document.createElement('script');
      script.src = buildUrl;
      script.onload = function() {
        console.log('Unity build loaded:', buildUrl);
      };
      script.onerror = function() {
        console.error('Failed to load Unity build:', buildUrl);
      };

      container.appendChild(script);
    }
  };

  window.UnityLoader = UnityLoader;
})();
