"# ProductCatlog" 

https://productcatlog-2-ho49.onrender.com/
# 🛍️ ChazeFashion - Product Catalog System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

ChazeFashion is a modern fashion product catalog built using Django. It allows fashion brands or retailers to manage, display, and organize their product offerings in an elegant and scalable way. It’s designed with extendibility and clean architecture in mind.

---

## 🚀 Features

- 🧾 **Product Listing:** Organized product display with categories and details
- 🖼️ **Media Management:** Upload and serve avatar and product images
- 🎨 **Custom Themes:** Easy theming with the `theme` and `templates` directories
- 🛠️ **Admin Panel:** Django admin for managing products and users
- 🔒 **User Profiles:** (Coming soon) User authentication and avatar management

---

## 🗂️ Project Structure

ChazeFashion/
├── catalog/ # Django app for catalog logic
├── media/avatars/ # Uploaded media files
├── templates/ # HTML templates
├── theme/ # Custom UI themes and styles
├── db.sqlite3 # SQLite database
├── manage.py # Django management script
├── requirements.txt # Python package requirements
└── README.md # Project documentation


```bash
git clone https://github.com/bhairava009/ProductCatlog.git
cd ProductCatlog
#######Set Up a Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
 ###Install Dependencies
bash
pip install -r requirements.txt

###Apply Migrations
python manage.py 
###Run the Development Server
python manage.py runserver
  

👨‍💻 Development Notes
Default database is SQLite for quick setup

Static/media files served locally during development

Recommended IDE: Visual Studio Code

📌 Future Enhancements (Ideas)
🔍 Product search and filtering

👥 User login/signup with social auth

📦 Inventory and stock tracking

🌐 API support (Django REST Framework)

🧪 Unit and integration tests

🤝 Contributing
Contributions are welcome! Feel free to open issues or pull requests if you’d like to collaborate.

🧑‍💻 Author
Bhairava009
GitHub: @bhairava009

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

Made with ❤️ using Django.


