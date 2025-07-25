function fetchSeats() {
    fetch('/api/seats')
        .then(response => response.json())
        .then(data => {
            const grid = document.getElementById('seatGrid');
            grid.innerHTML = '';
            data.forEach(seat => {
                const btn = document.createElement('button');
                btn.className = 'btn btn-sm m-1 ' + (seat.is_available ? 'btn-success' : 'btn-danger');
                btn.textContent = seat.seat_number;
                btn.disabled = true;
                grid.appendChild(btn);
            });
        });
}
fetchSeats();
setInterval(fetchSeats, 15000);