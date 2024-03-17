# Repost_LinkedIn_API

This project aims to extract the posts a given user has reposted from LinkedIn.

## Topics

1. [Overview](#overview)
2. [Goals](#goals)
3. [Scope and Context](#scope-and-context)
4. [System Design](#system-design)
5. [Alternatives Considered](#alternatives-considered)
6. [Learning Logs](#learning-logs)
7. [Resources](#resources)

---

## Overview

The goal of this project is to create a solution for extracting reposted posts from a LinkedIn user. As the LinkedIn API lacks direct support for this functionality, the project will utilize web scraping techniques. A web scraping service such as Scraper API will be employed due to its robust proxy and user-friendly API.

## Goals

- Develop a system capable of extracting reposted posts from a specified LinkedIn user efficiently and reliably.
- Ensure the system is scalable to handle large volumes of data.
- Maintain compatibility with LinkedIn's terms of service and data usage policies.
- Implement error-handling mechanisms to address any issues that may arise during the scraping process.

## Scope and Context

The scope of this project includes designing and implementing a solution to extract reposted posts from LinkedIn using web scraping techniques. It involves selecting an appropriate web scraping service, developing scripts to interact with the service's API, and integrating the solution into the desired application or workflow.

The context of this project revolves around the limitations of the LinkedIn API, which does not offer a direct endpoint for retrieving reposted posts from a user's profile. Therefore, web scraping emerges as a viable alternative for accessing this data.

## System Design

The system design will involve the following components:

1. **Scraper API Integration**: Utilize Scraper API to facilitate web scraping of LinkedIn profiles.
2. **Data Extraction Scripts**: Develop scripts to extract reposted posts from LinkedIn profiles using the Scraper API.
3. **Error Handling Mechanisms**: Implement mechanisms to handle errors gracefully, such as retries, logging, and alerts.
4. **Scalability Considerations**: Design the system to scale efficiently, considering factors such as concurrent requests and resource utilization.

## Alternatives Considered

Various alternatives were considered before opting for web scraping as the solution:

- **LinkedIn API**: Investigated the use of LinkedIn's official API, but found that it lacks support for retrieving reposted posts from user profiles.
- **Custom Solutions**: Explored the possibility of building a custom scraper, but deemed it less feasible due to time and resource constraints.

## Learning Logs

| Date     | Learning |
|----------|----------|
| 03-17-24 | UV has a fast environment setup time. |
| 03-17-24 | Even though Alpine images are lighter, it is hard to make them compatible with pre-commit. |
| 03-17-24 | To utilize LinkedIn's API, creating a LinkedIn Page and registering the application in the developer portal is necessary. |
| 03-17-24 | LinkedIn's API lacks support for an endpoint to retrieve user posts directly. |
| 03-17-24 | Web scraping appears to be the most viable approach for extracting reposted posts from a LinkedIn user. |

## Resources

- [LinkedIn's Developer Portal](https://developer.linkedin.com/)
- [Associate an app with a LinkedIn Page](https://www.linkedin.com/help/linkedin/answer/a548360/)
- [Is it possible to get all LinkedIn Profile Posts with LinkedIn API](https://stackoverflow.com/questions/54625971/is-it-possible-to-get-all-linkedin-profile-posts-with-linkedin-api)
- [LinkedIn Consumer Solutions Platform](https://learn.microsoft.com/en-us/linkedin/consumer/)
- [Scraper API Documentation](https://www.scraperapi.com/documentation)
