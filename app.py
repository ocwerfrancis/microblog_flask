from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


@app.route("/")
def home():
    mass_programs = [
        {
            "title": "Sunday Masses",
            "time": "7:00 AM (English), 8:30 AM (Luganda), 10:00 AM (English), 5:00 PM (English)",
            "description": "Join us for any of our four Sunday celebrations.",
        },
        {
            "title": "Daily Masses",
            "time": "Monday–Friday: 6:30 AM & 6:30 PM · Saturday: 7:00 AM",
            "description": "Daily Eucharistic celebrations through the week.",
        },
    ]

    thursday_program = [
        "Mass - 6:30 AM",
        "Adoration",
        "Benediction",
        "Catechesis - 5:00 PM",
        "Mass - 6:30 PM",
    ]

    ministries = [
        {
            "name": "Children's Ministry",
            "summary": "Safe and engaging classes where kids discover Jesus through stories and activities.",
        },
        {
            "name": "Worship Team",
            "summary": "Musicians and vocalists leading heartfelt worship every week.",
        },
        {
            "name": "Community Outreach",
            "summary": "Serving our city through care packages, local partnerships, and volunteer days.",
        },
    ]

    church_projects = [
        {
            "name": "Food Pantry Expansion",
            "status": "Ongoing",
            "summary": "Expanding storage and volunteer capacity to support more families each month.",
        },
        {
            "name": "Youth Learning Center",
            "status": "Phase 1 Complete",
            "summary": "Creating a modern space for after-school mentoring, tutoring, and discipleship.",
        },
        {
            "name": "Community Health Outreach",
            "status": "Launching Soon",
            "summary": "Partnering with local professionals for health screenings and wellness awareness.",
        },
    ]

    return render_template(
        "index.html",
        mass_programs=mass_programs,
        thursday_program=thursday_program,
        ministries=ministries,
        church_projects=church_projects,
    )


if __name__ == "__main__":
    app.run(debug=True)
