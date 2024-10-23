<a id="readme-top"></a>

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/crewan349/)

<h3 align="center">Concrete_Testing</h3>

  <p align="center">
    This is an application designed to input field and lab concrete test results
    <br />
    <a href="https://github.com/crewan349/Concrete_testing"><strong>Explore the documents »</strong></a>
    <br />
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
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#roadmap">Road map</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The primary purpose for this app is to make it easier for field and laboratory workers to be able to share and view each other’s concrete test results. All tests need to be rounded to ASTM standards. 

### Built With

* [Visual Studio Code](https://code.visualstudio.com/)
* [ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/)
* [pandas](https://pandas.pydata.org/)

<!-- GETTING STARTED -->
## Getting Started

In order to run this program in its current form the program needs to be run through an IDE. With python version 3.12.7 and pandas 2.2.3 installed on the user’s system.

<!-- ROADMAP -->
## Road map

- [ ] Homepage: the homepage has 3 features that the user can choose from.
    - [ ] With the 3 buttons the user is able to select if they wish to create a new sample, run a strength test, or check on an existing sample.
![MainMenu](/screenshots/MainMenu.png)
- [ ] New Sample: on the first page a user may input the data that they have collected about a new sample.
    - [ ] Some checks and balances have been put in place to make sure that the samples have the correct data input.
    - [ ] The four most common concrete tests are slump, temperature, air, and unit weight. This program requires an input that is rounded correctly.
        - [ ] A concrete slump can be 0 to 12 inches depending on the mix design. 
        - [ ] The air content of concrete is the amount of air that is in a concrete sample and the value is rounded to nearest tent. Most concrete is around 4% to 8% if it is an air mix or 0% for a non-air mix.
        - [ ] The temperature of con concrete is measured to the nearest whole number, however a passing test is usually between 60 to 90 degrees.
        - [ ] The unit weight of concrete is usually between 130 and 150 lbs./ft^3 and this value is rounded to the nearest tenth.
![NewSample](/screenshots/NewSample.png)
- [ ] Strength Test: on this page a user will be able to see all of the strength tests that need to be run.
    - [ ] A check to make sure the user was testing a 4x8 or 6x12 was put in place for an accurate measurement.
    - [ ] The strength is calculated for the user so all they have to do is input the load. This calculation is PSI so the input should be in pounds.
    - [ ] Most concrete is required to be above 4000 PSI so for a 4x8 cylinder that would be above 50210 pounds and a 6x12 would be above 112960 pounds.
![StrengthTest](/screenshots/StrengthTest.png)    
- [ ] Check Test: on the last page the user may input a sample number to view all information on that sample.
![CheckResults](/screenshots/CheckResults.png)

<!-- CONTACT -->
## Contact

Anthony Crew - CrewAN349@gmail.com

Project Link: [https://github.com/crewan349/Concrete_testing](https://github.com/crewan349/Concrete_testing)

<p align="right">(<a href="#readme-top">back to top</a>)</p>