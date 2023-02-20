async function taskHandler(event) {
    event.preventDefault();
  
    const descr = document.querySelector('input[name="descr"]').value;
  
    const response = await fetch(`/api/todos`, {
      method: 'POST',
      body: JSON.stringify({
        descr
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    });
  
    if (response.ok) {
      document.location.replace('/index');
    } else {
      alert(response.statusText);
    }
  }
  
  document.querySelector('.task-form').addEventListener('submit', taskHandler);
  