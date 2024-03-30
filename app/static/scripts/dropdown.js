

export function dropdown(Dropdown) {
  const ratingBtn = document.getElementById('ratingButton');
  const ratingMenu = document.getElementById('ratingDropdown');
  const ratingDD = new Dropdown(ratingMenu, ratingBtn);
  const cuisineBtn = document.getElementById('cuisineButton');
  const cuisineMenu = document.getElementById('cuisineDropdown');
  const cuisineDD = new Dropdown(cuisineMenu, cuisineBtn);


  handleDropdown(ratingDD, ratingBtn, ratingMenu);
  handleDropdown(cuisineDD, cuisineBtn, cuisineMenu);

}

function handleDropdown(ddown, btn, menu) {
  ddown.updateOnToggle(() => {
    if (ddown.isVisible()) {
      menu.onclick = (e) => {
        btn.querySelector('span').innerText = e.target.innerText;

        ddown.hide();
      }
    }
  })
}

