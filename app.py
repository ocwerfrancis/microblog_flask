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
            "title": "Sunday Holy Mass",
            "time": "Sundays at 8:00 AM & 10:30 AM",
            "description": "Celebrate the Eucharist with worship, scripture, and a message of hope.",
        },
        {
            "title": "Daily Morning Mass",
            "time": "Monday–Friday at 6:30 AM",
            "description": "Start your day in prayer and thanksgiving with our weekday liturgy.",
        },
        {
            "title": "Healing & Intercession Mass",
            "time": "First Friday at 7:00 PM",
            "description": "A monthly service focused on healing prayer and community support.",
        },
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
        ministries=ministries,
        church_projects=church_projects,
    )


if __name__ == "__main__":
    app.run(debug=True)
