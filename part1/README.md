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

### ___Relationship between them___

| Relation                                    | Type         | Description                                                                                   |
| :------------------------------------------- | :------------: | ---------------------------------------------------------------------------------------------: |
| `UserClass "1" --> "0..*" ReviewClass`      | Association  | A user can write multiple reviews.                                                            |
| `UserClass "1" *-- "0..*" PlaceClass`       | Composition  | A user "owns" places. If the user is deleted, their places are deleted too.                  |
| `PlaceClass "1" *-- "0..*" ReviewClass`     | Composition  | A place can have multiple reviews. Reviews do not exist without their place.                 |
| `PlaceClass "0..*" o-- "0..*" AmenityClass` | Aggregation  | A place can have multiple amenities. The amenities can be in different locations.               |

### ___Visual Representation of the Class Diagram___

![Class Diagram](/part1/Class_Diagram.png)