import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import logo from './logo.png';

const API_BASE_URL = process.env.REACT_APP_CODESPACE_NAME
  ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev`
  : 'http://localhost:8000';

function Navigation() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
      <div className="container">
        <Link className="navbar-brand d-flex align-items-center" to="/">
          <img src={logo} alt="OctoFit Tracker" height="40" className="me-2" />
          <span>OctoFit Tracker</span>
        </Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/activities">Activities</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/workouts">Workouts</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/teams">Teams</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

function Home() {
  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-md-12 text-center">
          <img src={logo} alt="OctoFit Tracker" className="mb-4" style={{maxWidth: '300px'}} />
          <h1 className="display-4">Welcome to OctoFit Tracker</h1>
          <p className="lead">Track your fitness journey with your favorite superheroes!</p>
          <p className="text-muted">Join Team Marvel or Team DC and compete to become the ultimate fitness champion.</p>
          <div className="mt-4">
            <Link to="/leaderboard" className="btn btn-primary btn-lg me-3">View Leaderboard</Link>
            <Link to="/activities" className="btn btn-outline-primary btn-lg">Log Activity</Link>
          </div>
        </div>
      </div>
      <div className="row mt-5">
        <div className="col-md-4 text-center">
          <div className="card h-100">
            <div className="card-body">
              <h3>🏆 Compete</h3>
              <p>Join a team and compete with your friends in fitness challenges</p>
            </div>
          </div>
        </div>
        <div className="col-md-4 text-center">
          <div className="card h-100">
            <div className="card-body">
              <h3>💪 Track</h3>
              <p>Log your workouts and watch your points grow</p>
            </div>
          </div>
        </div>
        <div className="col-md-4 text-center">
          <div className="card h-100">
            <div className="card-body">
              <h3>🎯 Achieve</h3>
              <p>Get personalized workout recommendations</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function Leaderboard() {
  const [leaders, setLeaders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/leaderboard/?period=all_time`)
      .then(res => res.json())
      .then(data => {
        setLeaders(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching leaderboard:', err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="container mt-5 text-center"><div className="spinner-border" role="status"></div></div>;
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">🏆 All-Time Leaderboard</h2>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>Rank</th>
              <th>Hero Name</th>
              <th>Username</th>
              <th>Team</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
            {leaders.map((leader, index) => (
              <tr key={leader.id}>
                <td className="fw-bold">#{leader.rank}</td>
                <td>{leader.hero_name}</td>
                <td>{leader.username}</td>
                <td>
                  <span className={`badge ${leader.team_name === 'Team Marvel' ? 'bg-danger' : 'bg-info'}`}>
                    {leader.team_name}
                  </span>
                </td>
                <td className="fw-bold">{leader.points} pts</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/activities/`)
      .then(res => res.json())
      .then(data => {
        setActivities(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching activities:', err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="container mt-5 text-center"><div className="spinner-border" role="status"></div></div>;
  }

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    });
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">📊 Recent Activities</h2>
      <div className="row">
        {activities.slice(0, 12).map((activity) => (
          <div key={activity.id} className="col-md-6 col-lg-4 mb-4">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{activity.username}</h5>
                <h6 className="card-subtitle mb-2 text-muted">{activity.activity_type}</h6>
                <p className="card-text">
                  <strong>Duration:</strong> {activity.duration_minutes} min<br/>
                  {activity.distance_km && <><strong>Distance:</strong> {activity.distance_km} km<br/></>}
                  {activity.calories_burned && <><strong>Calories:</strong> {activity.calories_burned}<br/></>}
                  <strong>Points:</strong> {activity.points_earned}
                </p>
                <p className="card-text"><small className="text-muted">{formatDate(activity.activity_date)}</small></p>
                {activity.notes && <p className="card-text fst-italic">"{activity.notes}"</p>}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/workouts/`)
      .then(res => res.json())
      .then(data => {
        setWorkouts(data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching workouts:', err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="container mt-5 text-center"><div className="spinner-border" role="status"></div></div>;
  }

  const getDifficultyBadge = (difficulty) => {
    const colors = {
      beginner: 'success',
      intermediate: 'warning',
      advanced: 'danger'
    };
    return colors[difficulty] || 'secondary';
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">💪 Workout Suggestions</h2>
      <div className="row">
        {workouts.map((workout) => (
          <div key={workout.id} className="col-md-6 mb-4">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{workout.title}</h5>
                <div className="mb-2">
                  <span className={`badge bg-${getDifficultyBadge(workout.difficulty)} me-2`}>
                    {workout.difficulty}
                  </span>
                  <span className="badge bg-secondary">{workout.activity_type}</span>
                  <span className="badge bg-info ms-2">{workout.duration_minutes} min</span>
                </div>
                <p className="card-text">{workout.description}</p>
                <h6 className="mt-3">Instructions:</h6>
                <pre className="bg-light p-3 rounded" style={{fontSize: '0.9rem', whiteSpace: 'pre-wrap'}}>
                  {workout.instructions}
                </pre>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function Teams() {
  const [teams, setTeams] = useState([]);
  const [profiles, setProfiles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      fetch(`${API_BASE_URL}/api/teams/`).then(res => res.json()),
      fetch(`${API_BASE_URL}/api/profiles/`).then(res => res.json())
    ])
      .then(([teamsData, profilesData]) => {
        setTeams(teamsData);
        setProfiles(profilesData);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching teams:', err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="container mt-5 text-center"><div className="spinner-border" role="status"></div></div>;
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">👥 Teams</h2>
      {teams.map((team) => {
        const teamMembers = profiles.filter(p => p.team === team.id);
        return (
          <div key={team.id} className="card mb-4">
            <div className="card-header bg-primary text-white">
              <h4 className="mb-0">{team.name}</h4>
            </div>
            <div className="card-body">
              <p className="lead">{team.description}</p>
              <h5>Members ({teamMembers.length}):</h5>
              <div className="row">
                {teamMembers.map((member) => (
                  <div key={member.id} className="col-md-4 mb-3">
                    <div className="card">
                      <div className="card-body">
                        <h6 className="card-title">{member.hero_name}</h6>
                        <p className="card-text">
                          <small className="text-muted">@{member.user.username}</small><br/>
                          <strong>{member.total_points} points</strong>
                        </p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/teams" element={<Teams />} />
        </Routes>
        <footer className="bg-light text-center text-muted py-4 mt-5">
          <div className="container">
            <p className="mb-0">© 2025 OctoFit Tracker - Built with ❤️ for Mergington High School</p>
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;
