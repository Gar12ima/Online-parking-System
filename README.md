# Online-parking-System

# Car Parking Management System 🚗🅿️

This is a GUI-based Car Parking Management System built using Python and Tkinter, integrated with MySQL for database operations. It supports user registration, login, vehicle slot allocation, and viewing parking status, and it includes a Naive Bayes model for demonstration or future prediction integration.

## 🛠️ Features

- **Login & Registration**: Simple user interface for account creation and authentication.
- **Slot Booking**: Users can book parking slots with vehicle details.
- **Slot Visualization**: View currently occupied parking slots with images.
- **Machine Learning**: Naive Bayes classifier included for possible predictive analysis or demo.
- **MySQL Database Integration**: Stores user credentials and parking data.

## 📁 Project Structure

```
├── carparking.py           # Slot visualization
├── Connection.py           # MySQL database connection
├── login.py                # Login UI logic
├── new user.py             # Registration UI logic
├── newuser_support.py      # Backend logic for new user registration
├── start.py                # Initial start screen with navigation
├── start_support.py        # Navigation logic for login/register/exit
├── welcome.py              # Post-login car entry interface
├── welcome_suport.py       # Slot entry and display logic
├── naive_bayes.py          # Naive Bayes demo with data.csv
└── README.md               # Project documentation
```

## 🧑‍💻 Prerequisites

- Python 3.x
- MySQL Server
- Required Python Libraries:
  ```bash
  pip install tkinter easygui mysql-connector-python pandas numpy matplotlib scikit-learn Pillow
  ```

## 🗃️ Database Setup

Ensure your MySQL server is running and create a database named `carparking_python`. Inside it, create these tables:

```sql
CREATE TABLE reg (
  user_nm VARCHAR(50),
  password VARCHAR(50),
  email VARCHAR(50),
  mobile VARCHAR(15)
);

CREATE TABLE carpark (
  car_no VARCHAR(20),
  name VARCHAR(50),
  mobile VARCHAR(15),
  slot_no VARCHAR(10)
);

CREATE TABLE carsloat (
  IDd VARCHAR(10),
  photo VARCHAR(100)
);
```

Also, place your car images (e.g., `1.jpg`, `2.jpg`) in an accessible path as used in `carparking.py`.

## ▶️ How to Run

1. Launch the application using:
   ```bash
   python start.py
   ```

2. Use the GUI to register, login, book a slot, or view parking status.

3. Run the Naive Bayes demo with:
   ```bash
   python naive_bayes.py
   ```

## 🔒 Credentials (Default for Testing)

- Username: (register your own using the UI)
- Password: (same as above)

## 📌 Notes

- GUI was created using the PAGE GUI builder.
- Designed for learning and demonstration purposes.
- Ensure paths to images in the code match your system's directory structure.

## 📷 Screenshots
![Screenshot 2025-05-27 121147](https://github.com/user-attachments/assets/c3b051e1-258b-4251-9dfb-3ac852ee106b)
![Screenshot 2025-05-27 121200](https://github.com/user-attachments/assets/66fa9ac4-7aaa-479c-bbf6-6e3e8fb05193)
![Screenshot 2025-05-27 121212](https://github.com/user-attachments/assets/73fc3ba1-4fad-45ed-ae84-37c9e510c6f4)
![Screenshot 2025-05-27 121222](https://github.com/user-attachments/assets/44d20add-7c5b-4e9c-9c73-2907e780da95)
![Screenshot 2025-05-27 121232](https://github.com/user-attachments/assets/aaac76db-bad4-43df-bde6-208d68055a2b)

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

## 🙋‍♀️ Author

Garima Mishra
