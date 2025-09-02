function uploadFile() {
  var fileInput = document.getElementById('file-upload');
  var formData = new FormData();
  formData.append("file", fileInput.files[0]);

  // Enviar el archivo al backend con fetch
    fetch('/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);  // Log para ver la respuesta del servidor
      alert("¡Archivo cargado exitosamente!");
    })
    .catch(error => console.error('Error al cargar el archivo:', error));
  }
