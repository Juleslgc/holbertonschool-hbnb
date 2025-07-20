/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/


document.addEventListener('DOMContentLoaded', () => {
    /* DO SOMETHING */
    const login = document.getElementById('login-form');
    if (login) {
      login.addEventListener('submit', async (event) => {
        event.preventDefault();

      if (!login.checkValidity()) {
        login.reportValidity()
        return;
      }

      });
    }
  });