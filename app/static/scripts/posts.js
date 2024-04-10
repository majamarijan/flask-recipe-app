export async function getPosts() {
  const posts = await fetch('http://localhost:5000/posts');
  const data = await posts.json();
  return data
}
