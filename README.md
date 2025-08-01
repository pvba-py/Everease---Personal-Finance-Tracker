# EverEase - Personal Finance Tracker

A simple and intuitive personal finance tracker built with Flask. Manage budgets, track expenses, view summaries, and handle loan management with a clean, responsive web interface.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Team Members](#team-members)
- [Contributing](#contributing)
- [License](#license)

## Features

### **Dashboard & Home**
- Personalized welcome screen
- Budget overview and status tracking
- Quick navigation to all features

### **Budget Management**
- Set monthly/weekly budgets
- Real-time budget vs. expenses comparison
- Budget status indicators (Within Budget/Over Budget)

### **Expense Tracking**
- Add expenses with descriptions and amounts
- Categorized expense management
- Input validation and error handling

### **Financial Summary**
- Comprehensive expense reports
- Total spending calculations
- Budget performance analysis

### **Budget Monitoring**
- Real-time budget exceeded alerts
- Spending pattern insights
- Financial health indicators

### **Loan Management**
- Track loan amounts
- Due date reminders
- Loan status overview

### **User Authentication**
- Secure login system
- Session management
- Multi-user support

## Demo

Check out the [Everease Output.pdf](./Everease%20Output.pdf) file in this repository to see screenshots of the application in action, including all features and user interfaces.

## Technologies Used

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3
- **Styling**: Custom CSS with gradient backgrounds and animations
- **Session Management**: Flask Sessions
- **Data Storage**: In-memory data structures (Python dictionaries)

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/pvba-py/Everease---Personal-Finance-Tracker.git
   cd everease
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - Use the demo credentials to log in

## Usage

### Getting Started

1. **Login**: Use one of the demo accounts to access the application
2. **Set Budget**: First-time users are prompted to set a budget
3. **Add Expenses**: Start tracking your expenses with descriptions and amounts
4. **Monitor Progress**: View your spending against your budget in real-time
5. **Review Summary**: Check comprehensive reports of your financial activity

### Demo Credentials

The application comes with demo user accounts for testing:
- Username: `demo_user` | Password: `demo123`
- Username: `test_user` | Password: `test123`
- Username: `john_doe` | Password: `password`
- Username: `jane_smith` | Password: `12345`

### Navigation Flow

```
Login → Set Budget → Home Dashboard
  ↓
Home → Add Expense / View Summary / Check Budget / Loan Management
  ↓
Logout
```

## Project Structure

```
everease/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Everease Output.pdf   # Application screenshots/demo
├── README.md             # Project documentation
│
├── static/
│   └── styles.css        # Custom CSS styling
│
└── templates/
    ├── main.html         # Landing page
    ├── login.html        # User authentication
    ├── home.html         # Main dashboard
    ├── set_budget.html   # Budget setting interface
    ├── add_expense.html  # Expense entry form
    ├── view_summary.html # Financial summary display
    ├── check_budget.html # Budget status checker
    └── loan_management.html # Loan tracking interface
```

## Key Features Breakdown

### **User Interface**
- Modern gradient backgrounds
- Responsive design for all devices
- Smooth animations and transitions
- Clean, intuitive navigation

### **Security Features**
- Session-based authentication
- Input validation and sanitization
- Error handling and user feedback
- Secure password management

### **Responsive Design**
- Mobile-friendly interface
- Tablet and desktop optimization
- Cross-browser compatibility
- Accessible design principles

### **Performance**
- Lightweight Flask framework
- Efficient data handling
- Fast page load times
- Minimal resource usage

## Screenshots

View the complete application walkthrough in the `Everease Output.pdf` file, which includes:
- Login interface
- Dashboard overview
- Budget setting process
- Expense tracking workflow
- Summary reports
- Loan management features

## Team Members

This project was developed as part of **Gelectra** at **GITAM University, Hyderabad** as a collaborative team effort.

**PVB Adithya** (Team Leader)
- Email: vprata2@gitam.in / adithya.vprata@gmail.com  
- GitHub: [pvba-py](https://github.com/pvba-py)  
- LinkedIn: [pvba](https://www.linkedin.com/in/pvba)

**Jay Varma**  
- Email: jmandapa@gitam.in / jayasimhavarma0401@gmail.com  
- GitHub: [Jayvarma04](https://github.com/Jayvarma04)  
- LinkedIn: [jayvarma04](https://www.linkedin.com/in/jayvarma04)

**HariPriya Paturi**
- GitHub: [HariPriya-Paturi](https://github.com/HariPriya-Paturi)

**Kamalini P**
- GitHub: [Kamalini12](https://github.com/Kamalini12)
- LinkedIn: [kamalinipemmasani](https://www.linkedin.com/in/kamalinipemmasani/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Export data to CSV/Excel
- [ ] Monthly/yearly expense reports
- [ ] Expense categories and tags
- [ ] Budget alerts via email
- [ ] Multi-currency support
- [ ] Data visualization with charts
- [ ] Mobile app development

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to reach out or open an issue in this repository.

---

**Star this repository if you find it helpful!**

Built with Flask and Python
