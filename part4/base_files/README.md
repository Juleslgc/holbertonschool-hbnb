# HBnB - Simple Web Client

This project represents the **web client** side of the HBnB Evolution rental application. It allows users to:

- Log in via an authentication form.
- View a list of available rental places with price filtering.
- View detailed information for a selected place.
- Read and submit reviews for each place (only when logged in).

---

## Main Features

### 1. Authentication

- Login form with email and password.
- JWT token management stored in cookies to secure requests.
- Conditional display of the review submission form based on authentication status.

### 2. Places List

- Dynamic display of all places fetched from the API.
- Filtering places by price through a dropdown menu.
- Summary display with title, price, and link to details.

### 3. Place Details

- Display full information: title, description, host, price, amenities.
- List of existing reviews.
- Review submission form (visible only if logged in).

---

## Technologies Used

- **HTML / CSS**: page structure and styling.
- **Vanilla JavaScript**: DOM manipulation, API calls, authentication handling.
- **REST API**: communication with the backend via `fetch`.

---

## Code Structure

- `index.html`: main page with the list of places.
- `place.html`: details page for a single place.
- `login.html`: login page.
- `scripts.js`: shared JavaScript logic for multiple pages.
- `styles.css`: shared CSS styles.

---

## Notes

- JWT token is stored and managed in cookies.
- API base URL: `http://127.0.0.1:5000/api/v1`.
- Review form only shows if the user is authenticated.
- Network errors are shown in console or as alerts.

---

## Getting Started

1. Clone this repository and serve it on a local web server (e.g., VSCode Live Server).
2. Open `index.html` in a modern web browser.
3. Log in with an existing user account or create one via the backend.
4. Browse, filter, and view places.
5. Add reviews to places if logged in.

---

Feel free to contribute or ask questions!

