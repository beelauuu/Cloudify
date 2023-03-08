const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

menu.addEventListener('click', function() {
  menu.classList.toggle('is-active');
  menuLinks.classList.toggle('active');
});

function downloadImage(url) {
  // Get the image URL
  const imageUrl = url;
  // Create a link element
  const link = document.createElement('a');
  // Set the link element's href to the image URL
  link.href = imageUrl;
  // Set the link element's download attribute to the desired file name
  link.download = 'image-name';
  // Append the link element to the document
  document.body.appendChild(link);
  // Click the link element to trigger the download
  link.click();
  // Remove the link element from the document
  document.body.removeChild(link);
}