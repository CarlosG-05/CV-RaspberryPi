import './Card.css';

export default function Card() {
    return (
            <div className="card-container">
                <div className="card-info">
                    <h1>Room 108</h1>
                    <h3>Occupancy: 5/10</h3>
                </div>
                <h1 className="room-state">Occupied</h1>
            </div>
        );
}
