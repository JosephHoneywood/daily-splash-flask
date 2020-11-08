const span_day = document.getElementById('day');
const span_date = document.getElementById('date');
const span_month = document.getElementById('month');
const span_hour = document.getElementById('hour');
const span_min = document.getElementById('min');

const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

function render_time() {

    let d = new Date();
    let month = d.getMonth();
    let day = d.getDay();
    let date = d.getDate();
    let hour = d.getHours();
    let minutes = d.getMinutes();

    span_day.innerText = days[day];
    span_date.innerText = date;
    span_month.innerText = months[month];
    span_hour.innerText = hour;
    span_min.innerText = minutes;
};

render_time();

let interval = setInterval(render_time, 10000);



