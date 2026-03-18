
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from datetime import datetime
import sqlite3
import os

app = FastAPI()

# Set up templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE_URL = "sqlite:///./iot_smart_home.db"

# Initialize database
conn = sqlite3.connect('iot_smart_home.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    type TEXT NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS user_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    role TEXT NOT NULL
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS environment_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Seed data
cursor.execute("INSERT INTO devices (name, status, type) VALUES ('Thermostat', 'online', 'temperature')")
cursor.execute("INSERT INTO user_profiles (username, email, role) VALUES ('admin', 'admin@example.com', 'admin')")
cursor.execute("INSERT INTO environment_metrics (temperature, humidity) VALUES (22.5, 45.0)")
conn.commit()

# Models
class Device(BaseModel):
    id: int
    name: str
    status: str
    type: str

class UserProfile(BaseModel):
    id: int
    username: str
    email: str
    role: str

class EnvironmentMetric(BaseModel):
    id: int
    temperature: float
    humidity: float
    timestamp: datetime

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/devices", response_class=HTMLResponse)
async def read_devices(request):
    return templates.TemplateResponse("devices.html", {"request": request})

@app.get("/users", response_class=HTMLResponse)
async def read_users(request):
    return templates.TemplateResponse("users.html", {"request": request})

@app.get("/metrics", response_class=HTMLResponse)
async def read_metrics(request):
    return templates.TemplateResponse("metrics.html", {"request": request})

@app.get("/settings", response_class=HTMLResponse)
async def read_settings(request):
    return templates.TemplateResponse("settings.html", {"request": request})

# API Endpoints
@app.get("/api/devices", response_model=List[Device])
async def get_devices():
    cursor.execute("SELECT * FROM devices")
    devices = cursor.fetchall()
    return [Device(id=row[0], name=row[1], status=row[2], type=row[3]) for row in devices]

@app.post("/api/devices")
async def add_device(device: Device):
    cursor.execute("INSERT INTO devices (name, status, type) VALUES (?, ?, ?)", (device.name, device.status, device.type))
    conn.commit()
    return {"message": "Device added successfully"}

@app.get("/api/users", response_model=List[UserProfile])
async def get_users():
    cursor.execute("SELECT * FROM user_profiles")
    users = cursor.fetchall()
    return [UserProfile(id=row[0], username=row[1], email=row[2], role=row[3]) for row in users]

@app.get("/api/metrics", response_model=List[EnvironmentMetric])
async def get_metrics():
    cursor.execute("SELECT * FROM environment_metrics")
    metrics = cursor.fetchall()
    return [EnvironmentMetric(id=row[0], temperature=row[1], humidity=row[2], timestamp=row[3]) for row in metrics]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
