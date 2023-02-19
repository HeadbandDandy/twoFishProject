async function loginFormHandler(event) {
    event.preventDefault();
  
    const email = document.querySelector('#email-input').value.trim();
    const password = document.querySelector('#password-input').value.trim();
  
    if (email && password) {
      const response = await fetch('/api/users/login', {
        method: 'post',
        body: JSON.stringify({
          email,
          password
        }),
        headers: { 'Content-Type': 'application/json' }
      });
  
      if (response.ok) {
        document.location.replace('/index/');
      } else {
        alert(response.statusText);
      }
    }
  }

document.querySelector('.signin-form').addEventListener('submit', loginFormHandler);
