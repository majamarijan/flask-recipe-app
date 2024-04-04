

export function dropdown(Dropdown) {
  const ratingBtn = document.getElementById('ratingButton');
  const ratingMenu = document.getElementById('ratingDropdown');
  const ratingDD = new Dropdown(ratingMenu, ratingBtn);
  const cuisineBtn = document.getElementById('cuisineButton');
  const cuisineMenu = document.getElementById('cuisineDropdown');
  const cuisineDD = new Dropdown(cuisineMenu, cuisineBtn);
  const search = document.getElementById('searchForm');
  const cards = Array.from(document.querySelectorAll('.posts [id^=card-]'));
  const posts = document.querySelector('.posts');
  
  handleDropdown(ratingDD, ratingBtn, ratingMenu, cards, posts, 'rating');
  handleDropdown(cuisineDD, cuisineBtn, cuisineMenu, cards, posts, 'cuisine');
  handleSearchForm(search, cards, posts);

}

async function handleDropdown(ddown, btn, menu, cards, posts, dataSet) {
  ddown.updateOnToggle(() => {
    if (ddown.isVisible()) {
      menu.onclick = (e) => {
        btn.querySelector('span').innerText = e.target.innerText;
        filterResult(cards, posts, e.target.innerText, dataSet);
        ddown.hide();
      }
    }
  })
}

async function handleSearchForm(form, cards, posts) {
  form.oninput = (e) => {
    filterResult(cards, posts, e.target.value, 'name');
  }
}


function filterResult(arr, box, value, dataSet) {
  if (value !== 'All' && value !== '') {
    if (isNaN(value)) {
      const mapped = arr.map(item => item.dataset[dataSet].split(' '));
      const foundItems = mapped.map((x, index) => {
        const flt = x.filter(str => str.toLowerCase().startsWith(value.toLowerCase()))
        if (flt.length > 0) {
          return arr[index];
        }
      });
      const result = foundItems.filter(x => x !== undefined);
      if (result.length > 0) {
        box.innerHTML = '';
        box.append(...result);
      } else {
        box.innerHTML = '';
        box.append('No results found');
      }
    } else {
      const filtered = arr.filter(item => item.dataset[dataSet].includes(value));
      box.innerHTML = '';
      box.append(...filtered);
    }

  } else {
    box.innerHTML = ''
    box.append(...arr);
  }
}
