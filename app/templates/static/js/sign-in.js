async function signUpFormHandler(event) {
    event.preventDefault();

    const name = document.querySelector('#registration-form').value.trim();
    const email = document.querySelector('#email-registration').value.trim();
    const password = document.querySelector('#password-registration').value.trim();
  
    if (email && password) {
      const response = await fetch('/api/users/login', {
        method: 'post',
        body: JSON.stringify({
          name,
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

document.querySelector('.signup-form').addEventListener('submit', signUpFormHandler);
