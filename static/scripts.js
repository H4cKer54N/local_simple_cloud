
var uploadModal = document.getElementById('uploadModal');

// When the user submits the form...
// When the user submits the form...
document.getElementById('uploadForm').addEventListener('submit', function(event) {
var filesInput = document.querySelector('input[type=file]');
if (filesInput.files.length == 0) {
    // Prevent form submission
    event.preventDefault();
    alert('No files selected');
} else {
    // Show the upload modal
    uploadModal.style.display = 'block';
}
});


function deleteFile(fileName) {
    if (confirm('Are you sure you want to delete this file?')) {
        fetch('/delete/' + fileName, { method: 'DELETE' })
            .then(response => {
                if (response.ok) {
                    alert('File deleted successfully');
                    location.reload();  // Reload the page to update the file list
                } else {
                    alert('Failed to delete file');
                }
            });
    }
}


// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
img.onclick = function(){
modal.style.display = "block";
modalImg.src = this.src;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
modal.style.display = "none";
}
