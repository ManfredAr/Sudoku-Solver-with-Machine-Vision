document.addEventListener('DOMContentLoaded', function() {
    const processImageButton = document.getElementById('processImage');
    processImageButton.addEventListener('click', function() {
        const inputElement = document.getElementById('imageUpload');
        const selectedFile = inputElement.files[0];

        if (selectedFile) {
            const formData = new FormData();
            formData.append('image', selectedFile);

            const xhr = new XMLHttpRequest();
            xhr.open('POST', 'uploadImage/');
            xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));

            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        console.log('Success');
                        console.log(xhr.responseText);
                    } else {
                        console.error('Request failed:', xhr.status);
 
                    }
                }
            };

            xhr.send(formData);
        } else {
            alert('Please select an image to solve');
        }
    });
});