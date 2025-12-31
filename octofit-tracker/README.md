# OctoFit Tracker - Fitness Application

![OctoFit Tracker](docs/octofitapp-small.png)

A comprehensive fitness tracking application built for Mergington High School, featuring team-based competition between Marvel and DC superheroes!

## Features

- 👥 **Team Management**: Join Team Marvel or Team DC
- 📊 **Activity Tracking**: Log various workout types (running, walking, cycling, swimming, strength training, yoga, sports)
- 🏆 **Leaderboard**: Compete with other heroes for the top spot
- 💪 **Workout Suggestions**: Get personalized workout recommendations
- 📈 **Points System**: Earn points for every minute of activity

## Technology Stack

### Backend
- **Python 3.12** with Django 4.1.7
- **Django REST Framework** for API endpoints
- **SQLite** database
- **Django CORS Headers** for cross-origin requests

### Frontend
- **React.js** with React Router
- **Bootstrap 5** for styling
- **Responsive design** for mobile and desktop

## Getting Started

### Prerequisites

- Python 3.12+
- Node.js 20+ and npm
- Git

### Backend Setup

1. **Navigate to the backend directory**:
   ```bash
   cd octofit-tracker/backend
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Populate database with test data**:
   ```bash
   python manage.py populate_db
   ```

6. **Start the Django server**:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

The API will be available at `http://localhost:8000/api/`

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd octofit-tracker/frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the React development server**:
   ```bash
   npm start
   ```

The application will open at `http://localhost:3000`

## API Endpoints

- `GET /api/` - API root with endpoint list
- `GET /api/teams/` - List all teams
- `GET /api/profiles/` - List all user profiles
- `GET /api/activities/` - List all activities
- `GET /api/workouts/` - List workout suggestions
- `GET /api/leaderboard/?period=all_time` - Get leaderboard

## Test Data

The application comes pre-populated with 10 superheroes:

### Team Marvel
- Iron Man (Tony Stark) - @ironman
- Spider-Man (Peter Parker) - @spiderman
- Captain America (Steve Rogers) - @captainamerica
- Black Widow (Natasha Romanoff) - @blackwidow
- Thor (Thor Odinson) - @thor

### Team DC
- Superman (Clark Kent) - @superman
- Batman (Bruce Wayne) - @batman
- Wonder Woman (Diana Prince) - @wonderwoman
- The Flash (Barry Allen) - @flash
- Aquaman (Arthur Curry) - @aquaman

All test users have the password: `hero123`

## Development

### Running in GitHub Codespaces

This project is optimized for GitHub Codespaces:

1. The devcontainer is pre-configured with all dependencies
2. Ports 3000 (React) and 8000 (Django) are automatically forwarded
3. The backend automatically configures itself for Codespaces URLs

### Project Structure

```
octofit-tracker/
├── backend/
│   ├── octofit_tracker/        # Django project settings
│   ├── tracker/                # Main Django app
│   │   ├── models.py          # Database models
│   │   ├── serializers.py     # REST API serializers
│   │   ├── views.py           # API views
│   │   ├── admin.py           # Django admin config
│   │   └── management/        # Custom management commands
│   ├── manage.py
│   └── requirements.txt
└── frontend/
    ├── public/                 # Static files
    ├── src/
    │   ├── App.js             # Main React component with routing
    │   ├── App.css            # Application styles
    │   └── logo.png           # OctoFit logo
    └── package.json
```

## Contributing

This is an educational project for learning GitHub Copilot Agent Mode. Feel free to:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Credits

Built with ❤️ for Mergington High School by Paul Octo and the IT team.

Powered by GitHub Copilot Agent Mode.
