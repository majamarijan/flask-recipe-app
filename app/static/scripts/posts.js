async function getPosts() {
  const posts = await fetch('http://localhost:5000/api/posts');
  const data = await posts.json();
  return data
}

export async function renderPosts() {
  const posts = document.querySelector('.posts');
  console.log('render')
  posts.innerHTML = 'loading...';
  getPosts().then(data => {
    posts.innerHTML = '';
    data.map(post=> {
      posts.insertAdjacentHTML('beforeend', generateCards(post))
    })
  })
}

function generateCards(post) {
  const card =`<a href="/posts/post/${post.id}" id="card-${post.id}" data-name="${post.name}"
				data-rating="${post.rating}"
					data-cuisine="${post.cuisine}">
				<div class="card">
					<div class="card-image">
						<img src="${post.thumbnail}" alt="${post.name}" width='150' height='150'>
						<ul class="tags">
              ${renderTags(post.tags)}
						</ul>
						<h3 class="post-name">${post.name}</h3>
					</div>
					<div class="card-body">
						<div class="card-title">
							<span>Cuisine: ${post.cuisine}</span>
						</div>
						<div class="card-info">
							<span><i class="fa-solid fa-stopwatch"></i>20min</span>
							<span><i class="fa-solid fa-utensils"></i>15min</span>
							<span><i class="fa-solid fa-bowl-food"></i>4</span>
							<span
								><i class="fa-solid fa-fire-flame-curved"></i
								>${post.caloriesPerServing}</span
							>
							<span><i class="fa-solid fa-star"></i>${post.rating}</span>
						</div>
					</div>
				</div>
			</a>`
    return card;
}

function renderTags(tags) {
  return tags.map(tag => {
    if(tags.indexOf(tag) == 0) {
      return `<li>${tag}</li>`
    } else {
      return `<li>| ${tag}</li>`
    }
  }).join('')
}