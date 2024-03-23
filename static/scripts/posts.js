export async function getPosts() {
  const response = await fetch('http://127.0.0.1:5000/api/posts?limit=10');
  const data = await response.json();
  const recepies = data.recipes;
  console.log(recepies);
  const posts = document.querySelector('.posts');
}
