# University Study Room Occupancy Tracker

This project provides a complete system for monitoring and managing occupancy in university study rooms using computer vision, FastAPI, Docker, and Supabase.

## Features
- **Raspberry Pi Client:** Runs computer vision code to detect occupancy in study rooms and sends data to a central server.
- **FastAPI Server:** Receives occupancy data, validates it, and stores it in a Supabase PostgreSQL database.
- **Supabase Database:** Stores study room information, occupancy logs, and user accounts for secure access and management.
- **Dockerized Deployment:** FastAPI server runs in a Docker container for easy deployment and scalability.
- **Environment Security:** Sensitive credentials are managed via a `.env` file and not committed to source control.
- **User Management:** Supports authenticated access and account management for students and administrators.

## Technologies
- Python (Computer Vision, FastAPI)
- Docker & Docker Compose
- Supabase (PostgreSQL, Auth)
- PowerShell/Python scripts for testing and integration

## Setup & Usage
1. Set up Supabase and create required tables (`study_rooms`, `users`, etc.).
2. Configure your `.env` file with Supabase credentials.
3. Build and run the FastAPI server using Docker Compose:
   ```sh
   docker compose up --build
   ```
4. Use the Raspberry Pi client or test scripts to send occupancy data.
5. Manage and view data securely via Supabase.

## Security
- Do not commit your `.env` file or any secrets to source control.
- Enable Row Level Security (RLS) in Supabase for production and configure policies as needed.

## License
MIT
