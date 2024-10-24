<a id="readme-top"></a>

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/crewan349/)

<h3 align="center">Concrete_Testing</h3>

  <p align="center">
    This is an application designed for the input of field and laboratory concrete quality control test results
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This app's primary purpose is to make it possible for field and laboratory workers to share and view concrete quality control test results. For this app to be useful to all, tests must be rounded to ASTM standards. 

### Built With

* [Visual Studio Code](https://code.visualstudio.com/)
* [ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/)
* [pandas](https://pandas.pydata.org/)

<!-- GETTING STARTED -->
## Getting Started

To run this program in its current form the program needs to be with python version 3.12.7, ttkbootstrap, and pandas 2.2.3 installed on the user’s system.

<!-- ROADMAP -->
## Roadmap

- [ ] Homepage: The homepage has 3 features from which the user can choose.
    - [ ] With the 3 buttons, the user can select whether to create a new sample, run a strength test, or check on an existing sample.
     

![MainMenu](/screenshots/MainMenu.png)
- [ ] New Sample: On the first page a user can input the data collected from a new sample.
    - [ ] Some checks and balances have been put in place to  ensure that the samples have the correct data input.
    - [ ] The four most common concrete tests are slump, temperature, air, and unit weight. This program requires an input that is rounded correctly.
        - [ ] A concrete slump can be 0 to 12 inches depending on the mix design. 
        - [ ] The air content of concrete is the amount of air in a concrete sample with the value rounded to the nearest tenth. Most concrete is around 4% to 8% if it is an air mix or 0% for a non-air mix.
        - [ ] The temperature of concrete is measured to the nearest whole number. However, a passing test is usually between 60 to 90 degrees.
        - [ ] The unit weight of concrete is usually between 130 and 150 lbs./ft^3 and this value is rounded to the nearest tenth.
         

![NewSample](/screenshots/NewSample.png)
- [ ] Strength Test: On this page, a user will see all the strength tests that still need to be run.
    - [ ] For an accurate measurement, a check was put in place to ensure the user was testing either a 4x8 or a 6x12 cylinder.
    - [ ] The strength is calculated for the user so all that remains is to input the load. This calculation is PSI so the input should be in pounds.
    - [ ] Most concrete is required to be above 4000 PSI. A 4x8 cylinder should be above 50210 pounds and a 6x12 cylinder should be above 112960 pounds.
     

![StrengthTest](/screenshots/StrengthTest.png)    
- [ ] Check Test: On the last page, the user may input a sample number to view all available information on that sample.


![CheckResults](/screenshots/CheckResults.png)

<!-- CONTACT -->
## Contact

Anthony Crew - CrewAN349@gmail.com

Project Link: [https://github.com/crewan349/Concrete_testing](https://github.com/crewan349/Concrete_testing)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
