# __UML - Explanatory Notes__

## __High-Level Package Diagram__

### ___Presentation Layer___
<u>__Role:__</u>
Interface between the user and the system.

<u>__Content:__</u>
UserAPI, PlaceAPI, ReviewAPI, AmenityAPI: Services or access points for managing entities via REST/HTTP API calls.

Uses the __Facade Pattern__ to simplify access to business logic.

### ___Business Logic Layer___

<u>__Role:__</u>
Contains all business logic.

<u>__Content:__</u>
UserClass, PlaceClass, ReviewClass, AmenityClass: These are the main classes representing the entities with their methods and business rules.

Receives calls from the presentation layer and coordinates processing.

### ___Persistence Layer___

<u>__Role:__</u>
Manages communication with the database.

<u>__Content:__</u>
DatabaseAccess, an abstraction allowing CRUD operations (Create, Read, Update, Delete) to be performed.

This layer is isolated to facilitate maintenance, migrations, or storage system changes.

### ___Relationship between them___

| **Of**  |  **Worms**         | **Type of relationship** |
| :----------------- |:--------------------:| --------------:|
|  _PresentationLayer_ |   _BusinessLogicLayer_ | Facade Pattern |
| _BusinessLogicLayer_ | _PersistenceLayer_ |   Database Operations |

### ___Visual Representation of the High-Level Package Diagram___

![High-Level Package Diagram](/part1/High_Level_Package_Diagram.png)

## __Class Diagram for Business Logic Layer__

### ___UserClass___

<u>__Role:__</u>
Represents a system user who can create places and post reviews.

<u>__Key Attributes:__</u>

`id`: Unique identifier (UUID4, private)

`first_name`, `last_name`, `email`: Credentials

`password`: Password (private)

`admin`: Indicates whether the user is an administrator

`created_at`, `updated_at`: Creation and modification dates

<u>__Main Methods:__</u>

`create()`, `update()`, `delete()`: User management

`is_admin()`: Checks permissions

`get_id()`: Returns the user's ID

### ___PlaceClass___

<u>__Role:__</u>
Represents a place published by a user, with its contact information, description, and amenities.

<u>__Key Attributes:__</u>

`id`: Unique identifier (UUID4, private)

`title`, `description`, `price`: Accommodation data

`latitude`, `longitude`: Geographic location

`owner`: Owner ID (User)

`created_at`, `updated_at`: Time tracking

<u>__Main Methods:__</u>

`create()`, `update()`, `delete()`, `list()`: Location management

`get_id()`: Returns the location ID`

### ___ReviewClass___

<u>__Role:__</u>
Represents a review left by a user about a place.

<u>__Key Attributes:__</u>

`id`: Unique identifier (UUID4, private)

`place`, `user`: Associated identifiers

`comment`, `rating`: Content of the review

`created_at`, `updated_at`: History management

<u>__Main Methods:__</u>

`create()`, `update()`, `delete()`: Review management

`list_by_place()`: Filters reviews by place

`get_id()`: Returns the review ID

### ___AmenityClass___

<u>__Role:__</u>
Represents a piece of equipment or amenity associated with a location (Wi-Fi, air conditioning, etc.).

<u>__Key Attributes:__</u>

`id`: Unique identifier (UUID4, private)

`name`, `description`: Name and description of the equipment

`created_at`, `updated_at`: Tracking dates

<u>__Main Methods__</u>:

`create()`, `update()`, `delete()`, `list()`: Equipment management

`get_id()`: Returns the equipment ID`

### ___Place_AmenityClass___

<u>__Role:__</u>
The place_amenity table is used to model a many-to-many relationship between Place and Amenity objects.
It contains only two fields, which are foreign keys pointing to the identifiers of the related entities:

`place_id`: Place identifier, foreign key to places.id

`amenity_id`: Amenity identifier, foreign key to amenities.id

The table does not contain any business data or methods, it is only used to manage relationships between entities.

<u>__Thanks to this table:__</u>
A place can have multiple amenities (Wi-Fi, swimming pool, etc.)
An amenity can be shared between multiple places.

### ___Relationship between them___

| Relation                                    | Type         | Description                                                                                   |
| :------------------------------------------- | :------------: | ---------------------------------------------------------------------------------------------: |
| `UserClass "1" --> "0..*" ReviewClass`      | Association  | A user can write multiple reviews.                                                            |
| `UserClass "1" *-- "0..*" PlaceClass`       | Composition  | A user "owns" places. If the user is deleted, their places are deleted too.                  |
| `PlaceClass "1" *-- "0..*" ReviewClass`     | Composition  | A place can have multiple reviews. Reviews do not exist without their place.                 |
| `PlaceClass "1" --> "0..*" Place_AmenityClass` | Association  | A place can have multiple amenities.    |
| `Place_AmenityClass "0..*" --> "1" AmenityClass` | Association | The amenities can be in different locations. |

### ___Visual Representation of the Class Diagram___

![Class Diagram](/part1/Class_Diagram.png)

## ___User Registration Diagram___

This diagram models the process of registering a new user in the system. It includes all validations on the API and business logic side.

<u>__Detailed steps:__</u>

The user sends a POST request to /user with their information (email, password, name, etc.).

The API validates the structure of the request (validate_Format()).

If the fields are missing or poorly formatted → 400 Bad Request response.

<u>__If the structure is correct:__</u>

The API passes the data to the Business Logic layer for business validation.

If the email already exists → 400 Bad Request response.

<u>__If validation succeeds:__</u>

The business logic calls the database to register the user.

If a database error occurs → 500 Internal Server Error.

Otherwise → 201 Created with the user ID.

![Diagram User Registration](/part1/User_Registration.png)

## ___Place Creation Diagram___

This diagram represents the process of creating a new place by a user (often an administrator).

<u>__Detailed steps:__</u>

The user sends a POST request to /places with the listing information.

The API checks via business logic whether the user is an administrator.

If not, 403 Forbidden.

<u>__If the user is an administrator:__</u>

The API validates the data provided (validateRequest()).

If invalid data: 400 Bad Request.

<u>__If the data is valid:__</u>

The API calls the business logic to create the Place.

The logic saves the listing to the database.

If a database error occurs: 500 Internal Server Error.

Otherwise, success: 201 Created with the listing ID.

![Diagram Place Creation](/part1/Place_Creation.png)
![Diagram Place Creation](/part1/get_place.png)
![Diagram Place Creation](/part1/post_reviews.png)