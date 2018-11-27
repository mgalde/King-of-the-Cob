const noteapp = document.getElementById('notes');
const container3 = document.createElement('div');
container3.setAttribute('class', 'container3');
noteapp.appendChild(container3);
var noterequest = new XMLHttpRequest();

noterequest.open('GET', 'http://127.0.0.1:8000/api/workhorse/Notes/', true);
noterequest.onload = function () {

// Begin accessing JSON data here
var data = JSON.parse(this.response);

if (noterequest.status >= 200 && noterequest.status < 400) {
data.forEach(note => {
  //console.log("Title: ", task.event);
  //console.log("Points: ", task.points);
  //console.log("Description: ", task.description);
  //console.log(task.url);
  //console.log(task.created_at);
  //console.log(task.id);
  const notecard = document.createElement('div');
  notecard.setAttribute('class', 'notecard');
  const h1 = document.createElement('h1');
  h1.textContent = "Note: " + note.title;
  const infograb = document.createElement('infograb');
  infograb.textContent = "Description: " + note.body;
  const create_date = document.createElement('created_at');
  create_date.textContent = "Creation Date: " + note.created_at;
  var a = document.createElement('a');
  var linkText = document.createTextNode("Info about this Note: " + note.id);
  a.appendChild(linkText);
  a.title = note.title;
  a.href = note.url;
  space = function () { return document.createElement( 'BR' ); }
  container3.appendChild(notecard);
  notecard.appendChild(h1);
  notecard.appendChild(space());
  notecard.appendChild(infograb);
  notecard.appendChild(space());
  notecard.appendChild(create_date);
  notecard.appendChild(space());
  notecard.appendChild(a);

});
} else {
console.log('error');
const errorMessage = document.createElement('marquee');
errorMessage.textContent = `Gah, notes are not working!`;
noteapp.appendChild(errorMessage);
}
}
noterequest.send();
