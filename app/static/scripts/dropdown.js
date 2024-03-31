

export function dropdown(Dropdown) {
  const ratingBtn = document.getElementById('ratingButton');
  const ratingMenu = document.getElementById('ratingDropdown');
  const ratingDD = new Dropdown(ratingMenu, ratingBtn);
  const cuisineBtn = document.getElementById('cuisineButton');
  const cuisineMenu = document.getElementById('cuisineDropdown');
  const cuisineDD = new Dropdown(cuisineMenu, cuisineBtn);
  const search = document.getElementById('searchForm');
  const cards = Array.from(document.querySelectorAll('.posts [id^=card-]'));
  console.log(cards)
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
  if (value !== 'All') {
    const filtered = arr.filter(item => item.dataset[dataSet].toLowerCase().includes(value.toLowerCase()));
    box.innerHTML = '';
    box.append(...filtered);
  } else {
    box.append(...arr);
  }
}
