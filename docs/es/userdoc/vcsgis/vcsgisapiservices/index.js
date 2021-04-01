window.onload = function() {
  // Build a system
  const ui = SwaggerUIBundle({
    url: "http://raw.githubusercontent.com/gvSIGAssociation/gvsig-desktop-docs/master/vcsgis/vcsgisapiservices.yaml",
    dom_id: '#swagger-ui',
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  })

  window.ui = ui
}
