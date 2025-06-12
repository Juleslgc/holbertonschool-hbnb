# HBnB Project

## Project Structure

- `app/`: main folder containing the application code  
  - `api/`: contains the API endpoints, organized by version  
  - `models/`: contains the business logic classes (User, Place, Review, Amenity)  
  - `services/`: contains the facade to manage communication between layers  
  - `persistence/`: contains the in-memory repository to temporarily store objects  

- `run.py`: entry point to start the Flask application  
- `config.py`: application configuration (secret keys, debug mode, etc.)  
- `requirements.txt`: list of required Python packages  
- `README.md`: project documentation (this file)

## Installing Dependencies

To install the required packages, run the following command in your terminal:

```bash
pip install -r requirements.txt
