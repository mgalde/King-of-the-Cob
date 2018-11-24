const app = document.getElementById('root');
const container2 = document.createElement('div');
container2.setAttribute('class', 'container2');
app.appendChild(container2);
var request = new XMLHttpRequest();

request.open('GET', 'http://127.0.0.1:8000/api/workhorse/Tasks/', true);
request.onload = function () {

// Begin accessing JSON data here
var data = JSON.parse(this.response);

if (request.status >= 200 && request.status < 400) {
data.forEach(task => {
  //console.log("Title: ", task.event);
  //console.log("Points: ", task.points);
  //console.log("Description: ", task.description);
  //console.log(task.url);
  //console.log(task.created_at);
  //console.log(task.id);
  const card = document.createElement('div');
  card.setAttribute('class', 'card');
  const h1 = document.createElement('h1');
  h1.textContent = "Task: " + task.event;
  const points = document.createElement('points');
  points.textContent = "Points: " + task.points;
  const description = document.createElement('description');
  description.textContent = "Description: " + task.description;
  const create_date = document.createElement('created_at');
  create_date.textContent = "Creation Date: " + task.created_at;
  container2.appendChild(card);
  card.appendChild(h1);
  card.appendChild(points);
  card.appendChild(description);
  card.appendChild(create_date);
});
} else {
console.log('error');
const errorMessage = document.createElement('marquee');
errorMessage.textContent = `Gah, it's not working!`;
app.appendChild(errorMessage);
}
}
request.send();
