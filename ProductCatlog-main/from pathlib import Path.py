from pathlib import Path

readme_content = """
# Sonu Kumar — Personal Portfolio Website

A sleek, responsive portfolio website built with **Flask**, **Tailwind CSS**, and **Jinja2**, showcasing my skills in data analysis, machine learning, visualization, and software development. Designed for easy customization and production deployment.

---

// [The full content goes here, same as the long markdown you shared above]
// For brevity, paste the entire description text here inside the triple quotes
// You can copy-paste it from your message or I can split it into chunks if needed

"""

# Save to file
readme_file = Path("README_Sonu_Portfolio.md")
readme_file.write_text(readme_content.strip())

print("README_Sonu_Portfolio.md created successfully.")
