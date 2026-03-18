# IoT Smart Home Dashboard

## Overview
The IoT Smart Home Dashboard is a comprehensive web application designed to provide users with the ability to monitor and manage their smart home devices efficiently. Built with FastAPI, this dashboard offers a seamless interface to interact with various IoT devices, track environmental metrics, and manage user profiles. This project is ideal for homeowners, IoT enthusiasts, and developers looking to integrate and control multiple smart devices from a single, user-friendly platform. The dashboard not only simplifies device management but also provides insights into environmental data, making it a valuable tool for smart home automation.

## Features
- **Device Management**: Easily add, view, and control IoT devices, ensuring they are always online and functioning correctly.
- **User Profiles**: Manage user accounts and roles, providing secure access and control over the smart home environment.
- **Environmental Metrics**: Monitor real-time data on temperature and humidity, helping users maintain optimal home conditions.
- **Responsive Design**: Utilizes Bootstrap for a responsive and visually appealing user interface that works on all devices.
- **FastAPI Backend**: A robust backend that ensures fast and reliable data processing and API management.
- **SQLite Database**: Stores device, user, and environmental data securely and efficiently.
- **Template Rendering**: Dynamic HTML rendering using Jinja2 templates for a seamless user experience.

## Tech Stack
| Component        | Technology  |
|------------------|-------------|
| Backend Framework| FastAPI     |
| Web Server       | Uvicorn     |
| Templating       | Jinja2      |
| Database         | SQLite      |
| Frontend Styling | Bootstrap   |
| Language         | Python 3.11+|

## Architecture
The IoT Smart Home Dashboard is structured to separate concerns between the frontend and backend. The FastAPI backend serves HTML pages rendered with Jinja2 templates and provides RESTful API endpoints for data interaction. The SQLite database is used to store and manage data for devices, user profiles, and environmental metrics.

```plaintext
+-------------------+
|  Frontend (HTML)  |
+-------------------+
         |
         v
+-------------------+
| FastAPI Backend   |
+-------------------+
         |
         v
+-------------------+
| SQLite Database   |
+-------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iot-smart-home-dashboard-auto.git
   cd iot-smart-home-dashboard-auto
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the SQLite database:
   ```bash
   python app.py
   ```

### Running the Application
Start the application using Uvicorn:
```bash
uvicorn app:app --reload
```
Visit the dashboard at `http://localhost:8000`.

## API Endpoints
| Method | Path           | Description                                     |
|--------|----------------|-------------------------------------------------|
| GET    | `/`            | Render the main dashboard page.                 |
| GET    | `/devices`     | Render the devices management page.             |
| GET    | `/users`       | Render the user profiles page.                  |
| GET    | `/metrics`     | Render the environmental metrics page.          |
| GET    | `/settings`    | Render the settings page.                       |
| GET    | `/api/devices` | Retrieve a list of all devices.                 |
| POST   | `/api/devices` | Add a new device to the system.                 |
| GET    | `/api/users`   | Retrieve a list of all user profiles.           |
| GET    | `/api/metrics` | Retrieve a list of all environmental metrics.   |

## Project Structure
```plaintext
.
├── Dockerfile                  # Docker configuration file
├── app.py                      # Main application code
├── requirements.txt            # Python dependencies
├── start.sh                    # Shell script to start the application
├── static/
│   └── css/
│       └── bootstrap.min.css   # Bootstrap CSS for styling
├── templates/
│   ├── dashboard.html          # Dashboard page template
│   ├── devices.html            # Devices management page template
│   ├── metrics.html            # Environmental metrics page template
│   ├── settings.html           # Settings page template
│   └── users.html              # User profiles page template
```

## Screenshots
*Screenshots of the application would be placed here to showcase the UI and features.*

## Docker Deployment
To deploy the application using Docker, use the following commands:

1. Build the Docker image:
   ```bash
   docker build -t iot-smart-home-dashboard .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 iot-smart-home-dashboard
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.
