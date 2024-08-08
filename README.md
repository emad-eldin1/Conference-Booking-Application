# Conference Booking Application

This is a Tkinter-based conference booking application that allows users to enter their personal details, submit the form, and view a list of users and available tickets. The application provides a graphical user interface (GUI) for booking conference tickets and displays relevant information.

## Features

- User registration form with fields for Name, Age, Email, Country, and Number of Tickets.
- Form validation and error handling.
- Display of successful booking information and available tickets.
- List of registered users and their booking details.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Ensure Python 3.x is installed on your system.
2. Clone this repository or download the source code.
3. Install any additional dependencies (if required).

## Usage

1. Open a terminal and navigate to the directory containing the application files.
2. Run the application using Python:

    ```bash
    python3 app.py
    ```

3. The application window will open. Enter the required details in the form and click "Submit" to book tickets.
4. View the list of users and available tickets in the output area of the application.

## Code Overview

### Main Application (`app.py`)

- **`ConferenceBookingApp` class**: Manages the Tkinter window and GUI components.
  - **`__init__`**: Initializes the application, sets up the window, and configures the grid layout.
  - **`create_widgets`**: Creates and places the GUI widgets such as labels, entry fields, and buttons.
  - **`bind_events`**: Binds the Enter key to the submit action.
  - **`submit`**: Handles form submission, validates input, calculates costs, and updates the output.
  - **`clear_inputs`**: Clears input fields after submission.
  - **`update_output`**: Updates the output text area with the list of users and available tickets.

### Data and Validation (`classes.py`)

- **`validateUserInput`**: Validates user input for correctness.
- **`checkOut`**: Calculates the total cost for the conference tickets.
- **`listOfUsers`**: Stores the list of registered users.
- **`conferenceTickets`**: Holds the number of tickets available for each country.
-----


## (Acknowledgements)

- Tkinter documentation and tutorials.
- Python community for support and resources.
--------
## Demo Video For The Application :  

<video controls src="Demo-video/Conference Booking Application (video-converter.com).mp4" title="Title"></video>