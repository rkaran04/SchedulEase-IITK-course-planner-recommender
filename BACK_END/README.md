
# BACK_END Folder

The **BACK_END** folder contains core scripts for managing the application's functionality.

## Files
- **`app.py`**: Main application script for backend operations and routing.
- **`course_schedule_manager.py`**: Manages course scheduling logic, including processing times and dates.

## Clash Detection Logic
A key feature of this project is the **clash detection system**, which prevents class overlaps in a student's schedule.

### How It Works
1. **Time Segmentation**: Each day is divided into **15-minute segments**, with a total of **52 segments**.
2. **Binary Representation**: Courses are represented as **52-bit integers**—each bit indicates whether a class is scheduled.
3. **Detecting Clashes**: 
   - **Bitwise AND** checks for overlaps (results in 0 = no clash).
   - **Bitwise OR** compiles schedules into one combined view.

### Benefits
- **Efficiency**: Fast binary operations handle multiple courses with ease.
- **Simplicity**: Compact encoding reduces complexity in storage and processing.
- **Scalability**: Works seamlessly as the number of courses increases.

### Real-World Application
This system allows you to select courses confidently, immediately alerting you to any time conflicts while generating a comprehensive daily schedule.

## Functions in `course_schedule_manager.py`
- **`extract_last_bracket_content(course_name)`**: Extracts content from the last brackets of a course name.
- **`get_class_string(arr)`**: Formats class schedule data into a specific string format.
- **`get_schedule(course)`**: Retrieves the complete schedule for a specific course.
- **`get_available_courses(selected_courses)`**: Returns courses that don’t conflict with selected ones.

## API Endpoints
- **Fetch Course Schedule**: 
  - **Endpoint:** `/API/schedule/<course>`
  - **Method:** `GET`
  
- **Available Courses**: 
  - **Endpoint:** `/API/available`
  - **Method:** `GET`
  - **Parameters:** `courses[]` - List of selected courses.

### Serving Static and Asset Files
- Static files (HTML, CSS, JS) are served from the **FRONT_END** directory, while assets like images are served from **ASSETS**.

> **Note**: Each file contains sample test cases under `if __name__ == "__main__":` for developer reference.
