export async function login() {
  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  const response = await fetch('/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username,
      email,
    }),
  });
  // const data = await response.json();
  // if (data) {
  //   console.log(data)
  // }
  console.log(response.url)
  window.location.href = response.url || new URL('/');
}