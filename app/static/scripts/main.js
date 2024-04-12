import './events.js';
import { login } from './form.js';
import { Dropdown } from 'https://esm.sh/flowbite';
import { dropdown } from './dropdown.js';
import { hamburgerMenu } from './hamburger.js';
import { renderPosts} from './posts.js'

window.onload = () => {
  const form = document.querySelector('form');

  if(window.innerWidth < 720) {
    hamburgerMenu();
  }

  if (form) {
    form.onsubmit = ((e) => {
      e.preventDefault();
      login();
    })
  }
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

  if (window.location.href.includes('posts')) {
    dropdown(Dropdown);
    // renderPosts()
  }
};