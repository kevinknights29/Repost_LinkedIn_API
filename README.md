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

The goal of this project is to create a solution for extracting reposted posts from a LinkedIn user. As the LinkedIn API lacks direct support for this functionality, the project initially planned to utilize web scraping techniques. However, a Python library called `linkedin-api` was discovered, which bypasses the need for web scraping. This library enables the extraction of reposted posts without directly interacting with the LinkedIn API. However, it requires disabling two-factor authentication (2FA), posing potential security concerns.

### Current Results

By leveraging the `linkedin-api` package, reposted posts were successfully extracted.

![image](https://github.com/kevinknights29/Repost_LinkedIn_API/assets/74464814/28781824-e4e0-4c38-8453-b0520c54a188)

Check the code [here](main.py).

## Goals

- Develop a system capable of extracting reposted posts from a specified LinkedIn user efficiently and reliably.
- Ensure the system is scalable to handle large volumes of data.
- Maintain compatibility with LinkedIn's terms of service and data usage policies.
- Implement error-handling mechanisms to address any issues that may arise during the extraction process.

## Scope and Context

The scope of this project includes designing and implementing a solution to extract reposted posts from LinkedIn. Initially, web scraping techniques were considered due to the limitations of the LinkedIn API. However, with the discovery of the `linkedin-api` package, the focus shifted to utilizing this library. The context of this project revolves around the challenges posed by the LinkedIn API and the exploration of alternative solutions.

## System Design

The system design now involves the following components:

- Extraction of reposted posts using the `linkedin-api` package.
- Implementation of filtering logic to retrieve relevant content.

## Alternatives Considered

Various alternatives were considered before opting for the `linkedin-api` library:

- **Web Scraping**: Initially planned to utilize web scraping techniques due to the lack of support from the LinkedIn API.
- **Custom Solutions**: Explored the possibility of building a custom scraper, but deemed it less feasible due to time and resource constraints.

## Learning Logs

| Date     | Learning |
|----------|----------|
| 03-17-24 | UV has a fast environment setup time. |
| 03-17-24 | Even though Alpine images are lighter, it is hard to make them compatible with pre-commit. |
| 03-17-24 | To utilize LinkedIn's API, creating a LinkedIn Page and registering the application in the developer portal is necessary. |
| 03-17-24 | LinkedIn's API lacks support for an endpoint to retrieve user posts directly. |
| 03-17-24 | Web scraping appears to be the most viable approach for extracting reposted posts from a LinkedIn user. |
| 03-18-24 | Found a package called `linkedin-api` which circumvented the issues above. |
| 03-18-24 | `linkedin-api` works great, but it requires disabling 2FA for it to function, raising potential security concerns. |

## Resources

- [LinkedIn's Developer Portal](https://developer.linkedin.com/)
- [Associate an app with a LinkedIn Page](https://www.linkedin.com/help/linkedin/answer/a548360/)
- [Is it possible to get all LinkedIn Profile Posts with LinkedIn API](https://stackoverflow.com/questions/54625971/is-it-possible-to-get-all-linkedin-profile-posts-with-linkedin-api)
- [LinkedIn Consumer Solutions Platform](https://learn.microsoft.com/en-us/linkedin/consumer/)
- [Scraper API Documentation](https://www.scraperapi.com/documentation)
- [linkedin-api GitHub](https://github.com/tomquirk/linkedin-api)
- [linkedin-api PyPi](https://pypi.org/project/linkedin-api/)
