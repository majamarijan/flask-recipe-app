export async function hamburgerMenu() {
  const hamburger = document.querySelector('.hamburger');
  const overlay = document.querySelector('.overlay');
  hamburger.onclick = () => {
    hamburger.classList.toggle('active');
    if (hamburger.classList.contains('active')) {
      overlay.style.zIndex = 1000;
      overlay.classList.add('overlay-animate');
      overlay.classList.remove('overlay-animate-back');
      document.querySelector('.mobileMenu').style.display = 'block';
      overlay.style.contentVisibility = 'visible';
      document.querySelector('.mobileMenu').style.zIndex = 1500;
      document.querySelector('.mobileMenu ul').style.zIndex = 2000;
    } else {
      overlay.classList.remove('overlay-animate');
      overlay.classList.add('overlay-animate-back');
      document.querySelector('.mobileMenu').style.display = 'none';
    }
  };
}
