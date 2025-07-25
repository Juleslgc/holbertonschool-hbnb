/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/
let allPlaces = [];

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const priceFilter = document.getElementById('price-filter');
    const placeDetailSection = document.querySelector('.place-details');
    const reviewForm = document.getElementById('review-form');

    // If on the login page
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value;
            try {
                await loginUser(email, password);
            } catch (error) {
                alert('Error while connecting: ' + error.message);
            }
        });
    }
    // If on the index page
    else if (priceFilter) {
        checkAuthentication();
        priceFilter.addEventListener('change', (event) => {
            const selected = event.target.value;
            let filteredPlaces;

            if (selected === 'All') {
                filteredPlaces = allPlaces;
            } else {
                const maxPrice = parseInt(selected);
                filteredPlaces = allPlaces.filter(place => place.price <= maxPrice);
            }
            displayPlaces(filteredPlaces);
        });
    }
    // If on the place page
    else if (placeDetailSection) {
        const placeId = getPlaceIdFromURL();
        const token = getCookie('token');

        if (!placeId) {
            console.error('No place ID found');
            return;
        }
        const reviewSection = document.querySelector('.add-review');
        if (reviewSection) {
            if (token) {
                reviewSection.style.display = 'block';
            } else {
                reviewSection.style.display = 'none';
            }
        }
        fetchPlaceDetails(token, placeId);
    }
    // If on th review page
    else if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const token = getCookie('token');
            const placeId = getPlaceIdFromURL();
            const reviewText = document.getElementById('review').value.trim();
            const rating = parseInt(document.getElementById('rating').value);

            if (!reviewText || !rating) {
                alert('Please fill in all fields');
                return;
            }
            try {
                const response = await submitReview(token, placeId, reviewText, rating);
                await handleResponse(response, reviewForm);
            } catch (error) {
                console.error('Submission failed:', error);
                alert('An error occurred while submitting the review.');
            }
        });
    }
});

async function loginUser(email, password) {
    const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });

    if (response.ok) {
        const data = await response.json();
        // Store JWT token in cookie
        document.cookie = `token=${encodeURIComponent(data.access_token)}; path=/; SameSite=Lax`;
        // Redirect to main page
        window.location.href = 'index.html';
    } else {
        alert('Login failed: ' + response.statusText);
    }
}

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    // Show login link only if not authenticated
    if (!token) {
        if (loginLink) loginLink.style.display = 'block';
        console.log('No token found. Please login.');
        fetchPlaces(null);
    } else {
        if (loginLink) loginLink.style.display = 'none';
        console.log('Token found, fetching places...');
        fetchPlaces(token);// Fetch places if authenticated
    }
}

function getCookie(name) {
    // Retrieve a cookie value by name
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
        const [key, val] = cookie.split('=');
        if (key === name) return decodeURIComponent(val);
    }
    return null;
}

async function fetchPlaces(token) {
    // Send GET request to fetch all places with token
    try {
        const headers = { 'Content-Type': 'application/json' };
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }
        const response = await fetch('http://127.0.0.1:5000/api/v1/places/', {
            method: 'GET',
            headers: headers
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Places fetched:', data);
            allPlaces = data;
            displayPlaces(allPlaces);
        } else {
            console.error('HTTP Error:', response.status);
        }
    } catch (error) {
        console.error('Error fetching places:', error);
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return;

    placesList.innerHTML = '';// Clear existing content

    places.forEach(place => {
        console.log('Displaying place:', place);
        const placeCard = document.createElement('div');
        placeCard.classList.add('place-card');

        placeCard.innerHTML = `
            <h2>${place.title}</h2>
            <p>Price per night: $${place.price}</p>
            <a href="place.html?id=${place.id}" class="details-button">View Details</a>
        `;

        placesList.appendChild(placeCard);
    });
}

async function fetchPlaceDetails(token, placeId) {
    try {
        const headers = {
            'Content-Type': 'application/json'
        };
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }
        const response = await fetch(`http://127.0.0.1:5000/api/v1/places/${placeId}`, {
            method: 'GET',
            headers: headers
        });
        
        if (response.ok) {
            const place = await response.json();
            displayPlaceDetails(place);
        } else {
            console.error('Failed to fetch place details. Status:', response.status);

        }
    } catch (error) {
        console.error('Error fetching place details:', error);
    }
}

function displayPlaceDetails(place) {
    const infoSection = document.querySelector('.place-info');
    const reviewsContainer = document.querySelector('#reviews-container');

    // Display info place
    infoSection.innerHTML = `
        <h1>${place.title}</h1><br>
        <p><strong>Host:</strong> ${place.owner.first_name} ${place.owner.last_name}</p><br>
        <p><strong>Price per night:</strong> $${place.price}</p><br>
        <p><strong>Description:</strong> ${place.description}</p><br>
        <p><strong>Amenities:</strong> ${place.amenities.join(', ')}</p><br>
    `;

    // Display the reviews
    reviewsContainer.innerHTML = ''; // Empty the container

    if (place.reviews && place.reviews.length > 0) {
        place.reviews.forEach(r => {
            const review = document.createElement('div');
            review.classList.add('review-card');
            review.innerHTML = `
                <p><strong>${r.user}:</strong></p><br>
                <p>${r.text}</p><br>
                <p>Rating: ${'★'.repeat(r.rating)}${'☆'.repeat(5 - r.rating)}</p><br>
            `;
            reviewsContainer.appendChild(review);
        });
    } else {
        reviewsContainer.innerHTML = `<p>No reviews yet.</p>`;
    }
}

function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
}

async function submitReview(token, placeId, reviewText, rating) {
    return await fetch(`http://127.0.0.1:5000/api/v1/reviews`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            place_id: placeId,
            text: reviewText,
            rating: rating
        })
    });
}

async function handleResponse(response, form) {
    if (response.ok) {
        alert('Review submitted successfully!');
        form.reset();
    } else {
        try {
            const data = await response.json();
            alert(`Error: ${data.message || 'Failed to submit review.'}`);
        } catch (error) {
            alert('An unexpected error occurred.');
        }
    }
}