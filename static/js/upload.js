// static/js/upload.js

document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById('id_image');
    const previewContainer = document.getElementById('preview-images-container');
    const successMessage = document.getElementById('success-message');

    fileInput.addEventListener('change', function () {
        previewContainer.innerHTML = ''; // Clear previous previews
        const files = this.files;

        if (files.length > 4) {
            alert('شما نمی‌توانید بیشتر از 4 عکس بارگذاری کنید.');
            fileInput.value = ''; // Clear the input
            return;
        }

        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const reader = new FileReader();

            reader.onload = function (e) {
                const col = document.createElement('div');
                col.classList.add('col-md-3');
                const img = document.createElement('img');
                img.src = e.target.result;
                img.classList.add('img-thumbnail');
                img.style.maxWidth = '100%';
                col.appendChild(img);
                previewContainer.appendChild(col);
            };

            reader.readAsDataURL(file);
        }
    });

    // Display the success message for a few seconds and then hide it
    if (successMessage) {
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 3000); // Hide the message after 3 seconds
    }
});
