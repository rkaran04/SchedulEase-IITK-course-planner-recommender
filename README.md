# SchedulEase-IITK-course-planner-recommender

Welcome to **SchedulEase-IITK** (*Schedule with Ease IIT Kanpur*), a web application designed to simplify course timetable management. Whether you're dealing with course conflicts or trying to organize your schedule, this tool offers an intuitive interface to help you manage your academic life at IIT Kanpur.

## Description

**SchedulEase-IITK** is designed to help IIT Kanpur students efficiently create their academic schedules. It automatically navigates over 700+ courses from 20+ departments, ensuring that no selected courses clash. Built with a Flask backend, it offers comprehensive course coverage and simplifies the scheduling process, making it easy for students to avoid conflicts and create their ideal timetable.

**Motivation**: At IIT Kanpur, competitive programming can overshadow practical coding, creating an isolating environment. **SchedulEase-IITK** was developed as a side project to channel my passion for coding into something valuable for my peers, highlighting that coding is not just about competition but also creativity and problem-solving.


## Setup

### 1. Clone the repository
```bash
git clone https://github.com/rkaran04/SchedulEase-IITK-course-planner-recommender.git
```
It is optimised to run with debugging off on your local server, you can change by modiying [app.py](BACK_END/app.py)

### 2. Prepare Course CSV
Please follow the steps mentioned here to procure the course data from [here](Extract_course_data/README.md) and place it in the cloned repository

### 3. Update data (if needed)
```bash
bash update_data.sh
```
Run the above code to update the .json files

### 4. Run the Server
```bash
bash launch.sh
```
Run the above code to view the web-app work on `http://127.0.0.1:5000/` 

## Project Structure

```
SchedulEase-IITK  
├── ASSETS/  
├── BACK_END/  
├── Extract_course_data/  
├── FRONT_END/  
├── RECOMMENDATION/  
├── Course_schedule_from_pingala.csv    
├── updata_data.sh                      
├── launch.sh                           
└── README.md  

```
### Key Folders and Files

- **ASSETS/**: Contains `courses.json` and `details.json` for managing course data.
- **BACK_END/**: Handles core backend logic, including `app.py` and `course_schedule_manager.py`.
- **Extract_course_data/**: Contains scripts for converting course data from CSV to JSON format.
- **FRONT_END/**: Includes `index.html`, `styles.css`, and `scripts.js` for the frontend design and functionality.
- **RECOMMENDATION/**: Contains code for course recommendation based on user input.

