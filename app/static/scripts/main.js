import './events.js';
import { login } from './form.js';
import { getPosts } from './posts.js';

window.onload = () => {
  const hamburger = document.querySelector('.hamburger');
  const overlay = document.querySelector('.overlay');
  const form = document.querySelector('form');
  if (form) {
    form.onsubmit = ((e) => {
      e.preventDefault();
      login();
    })
  }
  // if (window.location.href.includes('posts')) {
  //   getPosts();
  // }
  hamburger.onclick = () => {
    hamburger.classList.toggle('active');
    if (overlay) overlay.style.zIndex = 500;
    if (hamburger.classList.contains('active')) {
      overlay.classList.add('overlay-animate');
      overlay.classList.remove('overlay-animate-back');
      document.querySelector('.mobileMenu').style.display = 'block';
    } else {
      overlay.classList.remove('overlay-animate');
      overlay.classList.add('overlay-animate-back');
      document.querySelector('.mobileMenu').style.display = 'none';
    }
  };
  const links = document.querySelectorAll('header nav a');
  let stateArr = new Set();
  links.forEach((link, index) => {
    const nextURL = links[index + 1] ? links[index + 1].href : null;
    stateArr.add({ currentPage: link.href, url: nextURL });
    link.onclick = (e) => {
      // e.preventDefault();
      // window.history.pushState(Array.from(stateArr), null, nextURL);
      //     let new_state = { ...state, pageId: index, url: nextURL };
      //     window.history.replaceState(new_state, null, nextURL);
      //     console.log(window.history.state)
      //     console.log(e.state);
    }
  })
  console.log(window.history.state)
};