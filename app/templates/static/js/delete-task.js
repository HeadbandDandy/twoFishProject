async function deleteTaskHandler(event) {
    event.preventDefault();
  
    const id = window.location.toString().split('/')[
      window.location.toString().split('/').length - 1
    ];
    const response = await fetch(`/api/todos/${id}`, {
      method: 'DELETE'
    });
  
    if (response.ok) {
      document.location.replace('/index/');
    } else {
      alert(response.statusText);
    }
  }
  
  document.querySelector('.delete-btn').addEventListener('click', deleteTaskHandler);