function uploadFile() {
  var fileInput = document.getElementById('file-upload');
  var formData = new FormData();
  formData.append("file", fileInput.files[0]);

  fetch('/upload', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);  
    })
    .catch(error => console.error('Error al cargar el archivo:', error));
}
