$(function () {
  // Sidebar toggle behavior
  $('#sidebarCollapse').on('click', function () {
    $('#sidebar, #content').toggleClass('active');
  });
});

// success alerts
function subBtn() {
  alert("پیام شما با موفقیت ارسال شد.");
}

function forgetBtn() {
  alert("ایمیل بازیابی برای شما ارسال شد.");
}

function resetBtn() {
  alert("رمز عبور با موفقیت بازیابی شد.");
}

// project
function toggleImages(id) {
  var rows = document.getElementsByClassName('image-row');
  var boxes = document.getElementsByClassName('box');

  for (var i = 0; i < rows.length; i++) {
      if (rows[i].id === id) {
          rows[i].style.display = rows[i].style.display === 'none' || rows[i].style.display === '' ? 'block' : 'none';
      } else {
          rows[i].style.display = 'none';
      }
  }

  for (var j = 0; j < boxes.length; j++) {
      if (boxes[j].onclick.toString().includes(id)) {
          boxes[j].classList.toggle('active-box');
      } else {
          boxes[j].classList.remove('active-box');
      }
  }
}


function openLightbox(src) {
  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightbox-img');
  lightboxImg.src = src;
  lightbox.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  var lightbox = document.getElementById('lightbox');
  lightbox.style.display = 'none';
  document.body.style.overflow = 'auto';
}

