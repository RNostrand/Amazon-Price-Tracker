<h1 align="center">
  <a href="https://github.com/RNostrand/Amazon-Price-Tracker">
    <!-- Please provide path to your logo here -->
    <img src="docs/images/logo.svg" alt="Logo" height="100">
  </a>
</h1>

<div align="center">
  Amazon Price Tracker
  <br />
  <a href="#about"><strong>Explore the screenshots »</strong></a>
  <br />
  <br />
  <a href="https://github.com/RNostrand/Amazon-Price-Tracker/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/RNostrand/Amazon-Price-Tracker/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/RNostrand/Amazon-Price-Tracker/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
- [Project assistance](#project-assistance)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [Security](#security)
- [License](#license)

</details>

---

## About
Amazon Price Tracker is a web application written in Python and Flask which enables users to create a customizable list of products to track the price of and receive email notifications when one changes.

<details>
<summary>Screenshots</summary>
<br>

> **[?]**
> Please provide your screenshots here.

|                               Home Page                               |                               Login Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/screenshot.png" title="Home Page" width="100%"> | <img src="docs/images/screenshot.png" title="Login Page" width="100%"> |

</details>

### Built With
This application utilizes the following technologies: Python, Flask, SQLAlchemy, and WTForms.

## Getting Started

### Prerequisites
Please install Python and Pip as prerequisites for this project.

### Installation
To run this project locally, please follow these  steps:

1. Download this repo: `git clone https://github.com/RNostrand/Wildfire-Lookup.git`
2. Enter the repo folder: `cd Amazon-Price-Tracker`
3. Install the project requirments: `pip install -r requirements.txt`
4. Reference `.example-env` to create your own `.env` file. View the table below for descriptions of the variables.
5. Start the application: `python run.py`

<details>
<summary>Environment Variables</summary>
<br>

 <table>
  <tr>
    <th>Variable</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>EMAIL_USER</td>
    <td>Email address for the server to send emails from</td>
  </tr>
  <tr>
    <td>EMAIL_PASS</td>
    <td>Password for the server email address</td>
  </tr>
  <tr>
    <td>SECRET_KEY</td>
    <td>The secret key for your database. Can be any secure value</td>
  </tr>
  <tr>
    <td>SQLALCHEMY_DATABASE_URI</td>
    <td>URI to your server database</td>
  </tr>
  <tr>
    <td>PROXY</td>
    <td>The proxy to call Amazon from in your headers</td>
  </tr>
</table> 
</details>

## Usage
Users can register an account with an email and a password. Search for products and add them to your tracking list. When the price changes for an item, you will recieve an email notication alerting you of the change. 

## Roadmap

See the [open issues](https://github.com/RNostrand/Amazon-Price-Tracker/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/RNostrand/Amazon-Price-Tracker/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/RNostrand/Amazon-Price-Tracker/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/RNostrand/Amazon-Price-Tracker/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support
Reach out to the maintainer at one of the following places:

- [GitHub issues](https://github.com/RNostrand/Amazon-Price-Tracker/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)
- Contact options listed on [this GitHub profile](https://github.com/RNostrand)

## Project Assistance

If you want to say **thank you** or/and support active development of Amazon Price Tracker:

- Add a [GitHub Star](https://github.com/RNostrand/Amazon-Price-Tracker) to the project.

Together, we can make Amazon Price Tracker **better**!

## Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.


Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

The original setup of this repository is by [Ryan Nostrand](https://github.com/RNostrand).

For a full list of all authors and contributors, see [the contributors page](https://github.com/RNostrand/Amazon-Price-Tracker/contributors).

## Security

Amazon Price Tracker follows good practices of security, but 100% security cannot be assured.
Amazon Price Tracker is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.
