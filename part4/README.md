# ___HBnB Project___

## ___Project Structure___

- `app/`: main folder containing the application code  
  - `api/`: contains the API endpoints, organized by version  
  - `models/`: contains the business logic classes (User, Place, Review, Amenity)  
  - `services/`: contains the facade to manage communication between layers  
  - `persistence/`: contains the in-memory repository to temporarily store objects  

- `run.py`: entry point to start the Flask application  
- `config.py`: application configuration (secret keys, debug mode, etc.)  
- `requirements.txt`: list of required Python packages  
- `README.md`: project documentation (this file)

## ___Installing Dependencies___

To install the required packages, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## ___Business Logic Layer___

The business logic layer is responsible for enforcing the business rules that govern the platform's operation. It is independent of the API (Flask) and database layers, allowing for greater modularity, testability, and code clarity.

### ___Entities and their responsibilities___

#### __User__  
Represents an individual registered on the platform.

_Attributes:_

- `id` (str): Unique identifier.

- `first_name` (str): First name (required, max. 50 characters).

- `last_name` (str): Last name (required, max. 50 characters).

- `email` (str): Unique and valid email address.

- `is_admin` (bool): Admin role (default: False).

- `created_at` / `updated_at` (datetime)

_Responsibilities:_

- Manage identity data.

- Verify email uniqueness and validity.

- Identify administrator users.

- Be associated with created locations and
reviews.

_Example of use:_

```python
user = User(
    id="u001",
    first_name="Alice",
    last_name="Dupont",
    email="alice@example.com"
)

print(user.email)        # alice@example.com
print(user.is_admin)     # False
```

#### __Place__  
Represents a property available for booking.

_Attributes:_

- `id` (str): Unique identifier.

- `title` (str): Title (required, max. 100 characters).

- `description` (str): Description of the property.

- `price` (float): Price per night (positive).

- `latitude` / `longitude` (float): Geographic coordinates.

- `owner` (User): Owner user.

- `created_at` / `updated_at` (datetime)

_Responsibilities:_

- Validate geographic coordinates and price.

- Be associated with a valid owner.

- Be listed, filtered, or rated.

_Example of use:_

```python
place = Place(
    id="p001",
    title="Cozy apartment in Paris",
    description="Ideal for a weekend.",
    price=120.0,
    latitude=48.8566,
    longitude=2.3522,
    owner=user
)

print(place.title)       # Cozy apartment in Paris
print(place.price)       # 120.0
```

#### __Review__  
Represents a user's rating of a place.

_Attributes:_

- `id` (str): Unique identifier.

- `text` (str): Content (required).

- `rating` (int): Rating between 1 and 5.

- `place` (Place): Location concerned.

- `user` (User): Author of the review.

- `created_at` / `updated_at` (datetime)

_Responsibilities:_

- Validate that the rating is between 1 and 5.

- Be connected to an existing user and place.

- Contribute to a place's reputation.

_Example of use:_

```python
review = Review(
    id="r001",
    text="Great stay, very clean.",
    rating=5,
    place=place,
    user=user
)

print(review.rating)         # 5
print(review.place.title)    # Cozy apartment in Paris
```
#### __Amenity__

Represents an item of equipment or service associated with a location (e.g., Wi-Fi, Parking, Pool).

_Attributes:_

- `id` (str): Unique identifier.

- `name` (str): Name of the item (required, max. 50 characters).

- `created_at` / `updated_at` (datetime)

_Responsibilities:_

- Be linked to one or more locations.

- Allows filtering of locations by equipment.

_Example of use:_

```python
wifi = Amenity(id="a001", name="Wi-Fi")

print(wifi.name)  # Wi-Fi
```
## ___Entity-Relationship Diagram___

_The diagram below represents the application's data model. It highlights the main entities, their attributes, and the relationships between them :_

- USER : Represents the application's users, with personal information such as first name, last name, email, password, and administrator status.

- PLACE : Designates the places offered, with a title, description, price, and geolocation (latitude and longitude).

- REVIEW : Allows users to leave reviews of places, with text and a rating.

- AMENITY : Groups the amenities or services associated with a place (Wi-Fi, parking, etc.).

_Relationships :_

- A user can create multiple places and leave multiple reviews.

- A place can receive multiple reviews and offer multiple amenities (and vice versa).

![Entity-Relationship Diagram](ER_Diagram.png)

## ___Simple Web client___

The Simple Web Client is a lightweight front-end application built using HTML, CSS, and JavaScript.  
It provides user authentication, browsing and filtering of places, and review submission functionality.

For more details, setup instructions, and usage, please check the [Simple Web Client README](/part4/base_files/README.md).

## ___Authors___

-[Vithushan Satkunanathan](https://github.com/Vitushan)  
-[Jules Ventura](https://github.com/Juleslgc)
