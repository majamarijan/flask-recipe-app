window.onresize = (e) => {
  if (window.innerWidth >= 720) {
    document.querySelector('.overlay').classList.remove('overlay-animate');
    document.querySelector('.overlay').classList.add('overlay-animate-back');
    // document.querySelector('.content').style.filter = 'none';
    document.querySelector('.hamburger').classList.remove('active');
  }
}

