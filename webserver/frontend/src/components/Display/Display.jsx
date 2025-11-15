import Card from '../Card/Card.jsx';

export default function Display(props) {

    return (
            <>
                {props.data.map(room_info =>
                    <Card
                        room_num={room_info.room_number}
                        current_occupancy={room_info.current_occupancy}
                        capacity={room_info.capacity}
                    />
                )}
            </>
        );
}
