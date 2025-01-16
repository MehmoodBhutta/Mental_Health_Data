# Mental Health in Tech Survey Dashboard

## Project Overview
This project is a **Flask-based web application** that visualizes survey data on mental health in the tech industry. The app leverages Python libraries like Pandas and Plotly to analyze and display interactive visualizations, making the data easy to explore and understand.

## Features
- **Data Upload**: Users can upload survey data in CSV format.
- **Interactive Visualizations**: Includes bar charts, pie charts, and more, created using Plotly.
- **User-Friendly Interface**: Simple and intuitive design for ease of use.

## Tools and Technologies
- **Flask**: Backend framework for web development.
- **Pandas**: Data manipulation and analysis.
- **Plotly**: Interactive data visualization.
- **HTML/CSS**: Frontend styling and layout.

## How to Run the Project
### Prerequisites
- Python 3.8 or later
- Pip (Python package manager)

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/mental-health-dashboard.git
   cd mental-health-dashboard
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the App**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

## File Structure
```
mental-health-dashboard/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── base.html          # Base layout
│   ├── index.html         # Home page
├── static/                # Static files (CSS, JS, images)
├── data/                  # Folder for uploaded data
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## How to Use
1. Launch the app locally using the instructions above.
2. Upload a CSV file containing survey data.
3. Explore the interactive visualizations generated from the data.

## Example Dataset
You can find an example dataset used for testing in the `data/` folder.

## Future Enhancements
- Add user authentication.
- Integrate more data visualization options.
- Deploy the application online.

## Contributing
Contributions are welcome! Feel free to fork the repository and create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, feel free to reach out to [your email/LinkedIn profile].
