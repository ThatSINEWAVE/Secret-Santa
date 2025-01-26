<div align="center">

# Secret Santa

A beautiful, interactive web application for organizing Secret Santa gift exchanges. Built with Flask and modern web technologies, this application provides a seamless and enjoyable experience for managing your holiday gift exchange.

</div>

## Features

- **Interactive UI**: Clean, modern interface with smooth animations and transitions
- **Real-time Updates**: Participant list updates automatically as selections are made
- **Festive Design**: Includes falling snowflakes, gradient backgrounds, and holiday-themed elements
- **Fair Selection**: Ensures random and unique gift assignments
- **Progress Tracking**: Visual indicators show which participants have already made their selections
- **Mobile Responsive**: Works seamlessly on both desktop and mobile devices

<div align="center">

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

</div>

## Technologies Used

- **Backend**: Python/Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with animations
- **Icons**: SVG icons for visual elements
- **Font**: Inter font family from Google Fonts

## 🎮 How to Use

1. Open the application in your browser
2. Select your name from the dropdown menu
3. Click the "Continue" button to draw your Secret Santa assignment
4. Your assignment will be displayed with a festive animation
5. Take a screenshot or note down your assignment
6. Keep it secret!

## Customization

You can customize the application by:

1. Modifying the participant list in `data.json`
2. Adjusting colors and animations in `styles.css`
3. Updating the UI elements in the HTML templates

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ThatSINEWAVE/secret-santa-2025.git
cd secret-santa-2025
```

2. Install dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

<div align="center">

## [Join my discord server](https://discord.gg/2nHHHBWNDw)

</div>

## Project Structure

```
secret-santa-2025/
├── app.py              # Flask application logic
├── data.json           # Participant and selection data
├── static/
│   └── styles.css      # Stylesheet with animations
├── templates/
│   ├── index.html      # Main page template
│   └── draw.html       # Selection result template
└── site-data/          # Favicon and site icons
```

## Reset Function

To reset all selections and start fresh:

1. Stop the application
2. Clear the "drawn" object in `data.json`
3. Restart the application

## Contributing
Contributions are welcome! If you find any bugs or have ideas for improvements, feel free to submit an issue or a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.