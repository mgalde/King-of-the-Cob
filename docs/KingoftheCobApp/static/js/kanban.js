let instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/workhorse/Tasks/",
});

instance
  .get()
  .then(function(response) {
    let allStories = response.data;
    let todoStories = [];
    let reviewStories = [];
    let inprogressStories = [];
    let doneStories = [];
    let count = {
      started: 0,
      inProgress: 0
    }
    organizeStories(
      allStories,
      todoStories,
      reviewStories,
      inprogressStories,
      doneStories
    );
    displayStories(todoStories, reviewStories, inprogressStories, doneStories);

  })
  .catch(function(error) {
    console.log(error);
  });

  function organizeStories(
    allStories,
    todoStories,
    reviewStories,
    inprogressStories,
    doneStories
  ) {
    for (let i = 0; i < allStories.length; i++) {
      if (
        allStories[i].current_state === "unscheduled" ||
        allStories[i].current_state === "unstarted"
      )
      todoStories.push(allStories[i]);
      if (
        allStories[i].current_state === "started" ||
        allStories[i].current_state === "rejected"
      ) {
        inprogressStories.push(allStories[i]);
      }

      if (allStories[i].current_state === "finished") {
        reviewStories.push(allStories[i]);
      }
      if (
        allStories[i].current_state === "delivered" ||
        allStories[i].current_state === "accepted"
      )
      doneStories.push(allStories[i]);
    }
  }

  function displayStories(...storyColumns) {
      storyColumns.forEach(function(columns) {
        columns.forEach(function(story) {
          let storyUrl = story.url;
          let statusBadge = story.current_state;
          let estimate = story.points;
          let storyId = story.id;
          appendStory(story, storyUrl, statusBadge, estimate, storyId);
      });
    });
  }


function appendStory(story, storyUrl, statusBadge, estimate, storyId) {
  let storyType = story.event;
  if (estimate === undefined) estimate = "";
  $("div[data-accepts~='" + statusBadge + "']").append(
    "<div class='" + storyType + " card" + "' data-id='" + storyId + "'>" +
    "<a href='" + storyUrl + "'" + "target=" + "_blank" + ">" +
    "<p class=name>" + story.event + "</p></a>" +
    "<p class=details>" + story.description + "</p></a>" + "<br>" + "<br>" +
    "<p class='estimate'>"  + estimate + "</p>" +
    "<p class='status-badge " + statusBadge + "'>" + statusBadge + "</p>" +
    "</div>"
  );
}
