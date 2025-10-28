1. spent first bit trying to update securities to most current versions. 
    h11 was out of date, which also required httpcore to be updated
2. trying to fix deployment. set up new docker repo, added new login info for github. opened docker desktop
    realized I named the user token differently in github - fixed in yaml to match
    DOCKER_TOKEN was added under env variable - moved to env secret
    docker user is greghoff. github is greg-hoff. fixed push address so that docker is reached