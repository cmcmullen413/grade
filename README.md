[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/cmcmullen413/grade">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Grade</h3>

  <p align="center">
    Git remade in rust
    <br />
    <a href="https://github.com/cmcmullen413/grade/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/cmcmullen413/grade/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

Grade, or "git remade", is a git remake in the rust language.
It implements (or will implement) all the basic features of git
and strives to be functionally similar.

The test suite for this project is written in Python to make my life easier
and tests simpler and more readable.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Rust][Rust-Lang.org]][Rust-url]
* [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
To build and use grade yourself, ensure you have [Rust (1.96.0+)][Rust-url] installed,
as well as Cargo (which should included when you install Rust)

### Installation
1. Clone the repository
    ```bash
   git clone https://github.com/cmcmullen413/grade.git
   cd grade
   ```
2. Build the project
    ```bash
   cargo build --release
   ```
3. The compiled binary will be located in the 'target/release/' directory.
   This file will need to be either:
   - Moved into the project folder that you want to version control (for simple testing and tomfoolery)
   - or
   - Added to you system PATH variable (to be used as a regular program just like git)

In the future, if time allows, I plan to create installers that will do this process automatically

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Grade is used in the same way git is in the command line, with only minor differences in command names.
The program does include automatic translation of git commands however,
so 'grade commit' has the same functionality as 'grade submit'
For a quick guide to convert git terms into the correct grade term, see [git_dictionary.txt](./git_dictionary.txt)  
The currently implemented features are:  
- None

For the complete list of grade functionality for your current build, use the -h or --help flag.  
  ```bash
  grade --help
  ```
This also works for specific commands
  ```bash
  grade command -h
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Snapshots
- [ ] Branches
- [ ] Branch Names
- [ ] Tags
- [ ] Distribution
- [ ] Merges
- [ ] Rewriting History
- [ ] Staging
- [ ] Diffs
- [ ] Eliminating Duplication
- [ ] Compressing Blobs

See the [open issues](https://github.com/cmcmullen413/grade/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Caleb McMullen - cmcmullen413@gmail.com

Project Link: [https://github.com/cmcmullen413/grade](https://github.com/cmcmullen413/grade)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/cmcmullen413/grade.svg?style=for-the-badge
[contributors-url]: https://github.com/cmcmullen413/grade/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cmcmullen413/grade.svg?style=for-the-badge
[forks-url]: https://github.com/cmcmullen413/grade/network/members
[stars-shield]: https://img.shields.io/github/stars/cmcmullen413/grade.svg?style=for-the-badge
[stars-url]: https://github.com/cmcmullen413/grade/stargazers
[issues-shield]: https://img.shields.io/github/issues/cmcmullen413/grade.svg?style=for-the-badge
[issues-url]: https://github.com/cmcmullen413/grade/issues
[license-shield]: https://img.shields.io/github/license/cmcmullen413/grade.svg?style=for-the-badge
[license-url]: https://github.com/cmcmullen413/grade/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/caleb-mcmullen-102953265
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Rust-Lang.org]: https://img.shields.io/badge/Rust-%23000000.svg?e&logo=rust&logoColor=white
[Rust-url]: https://rust-lang.org
[Python.org]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
[Python-url]: https://rust-python.org