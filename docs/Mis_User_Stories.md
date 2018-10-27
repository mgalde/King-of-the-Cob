# Mis-User Stories

## Mis-User Story breakdown

* As a disgruntled developer, I want to be able to delete current work priorities so that no one knows what needs to be worked on and what work is coming up that still needs to be done.

  * Mitigation Criteria: A developer user will not have the ability to delete items from the product backlog as the access for deletion will be reserved for the SCRUM master to handle that administrative task. A developer will only have access to change backlog status. Additionally any changes by the developer will be logged as part of the update so that all users are aware which user enacted the change.

* As a external malicious user I want to be able to deny access to a teams project file to deny progress, delay productivity and to cause disruption of service.

  * Mitigation Criteria: King of the Cob will run as a de-centralized service away from the primary webhost as teams will be required to self-host the production server on there internal network. By simply making sure that the production server is not exposed to external connections the internal team should still have access within the defined network they have access to.  

* As a malicious SCRUM master I want to delete the progress of a team to delay progress, deny productivity and cause disruption to services.

  * Mitigation Criteria: A SCRUM master would be the admin level user for the interface and would have the capability to delete work, however the work is never truly deleted as the status is simply changed from active to inactive. The project will need to be purged from the database to be completely deleted from the service. 
