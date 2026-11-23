import streamlit as st
from datetime import date

# PAGE CONFIGURATION
st.set_page_config(
    page_title="EventScout AI",
    page_icon="🚀",
    layout="wide"
)

# SAMPLE EVENT DATA FOR MVP DEMONSTRATION
events = [
    {
        "name": "AI Innovation Hackathon",
        "type": "Hackathon",
        "location": "Bangalore",
        "date": "2026-12-10",
        "deadline": "2026-12-05",
        "description": "Build innovative AI and machine learning solutions.",
        "link": "https://devpost.com/hackathons"
    },
    {
        "name": "Web Development Workshop",
        "type": "Workshop",
        "location": "Online",
        "date": "2026-12-15",
        "deadline": "2026-12-12",
        "description": "Learn modern web development technologies.",
        "link": "https://unstop.com"
    },
    {
        "name": "National Coding Competition",
        "type": "Competition",
        "location": "Chennai",
        "date": "2026-12-20",
        "deadline": "2026-12-15",
        "description": "Showcase programming and problem-solving skills.",
        "link": "https://unstop.com"
    },
    {
        "name": "Data Science Hackathon",
        "type": "Hackathon",
        "location": "Online",
        "date": "2026-12-25",
        "deadline": "2026-12-20",
        "description": "Explore data science and predictive analytics.",
        "link": "https://devpost.com/hackathons"
    },
    {
        "name": "Python Programming Workshop",
        "type": "Workshop",
        "location": "Bangalore",
        "date": "2027-01-05",
        "deadline": "2026-12-30",
        "description": "Improve Python programming and practical coding skills.",
        "link": "https://unstop.com"
    }
]

# HEADER
st.title("🚀 EventScout AI")
st.subheader("Discover Hackathons, Workshops & Competitions")

st.write(
    "An AI-assisted event discovery platform that helps students "
    "find opportunities based on their interests and location."
)

st.info(
    "MVP demonstration: The current listings are sample records, "
    "not verified live event announcements."
)

st.divider()

# SEARCH SECTION
st.header("🔍 Discover Events")

col1, col2 = st.columns(2)

with col1:
    search = st.text_input(
        "Search by keyword",
        placeholder="Example: AI, Python, coding..."
    )

with col2:
    location = st.selectbox(
        "Select Location",
        ["All", "Bangalore", "Chennai", "Online"]
    )

event_type = st.selectbox(
    "Select Event Type",
    ["All", "Hackathon", "Workshop", "Competition"]
)

# FILTER EVENTS
filtered_events = []

for event in events:

    matches_search = (
        search.lower() in (
            event["name"] + " " + event["description"]
        ).lower()
    )

    matches_location = (
        location == "All" or event["location"] == location
    )

    matches_type = (
        event_type == "All" or event["type"] == event_type
    )

    if matches_search and matches_location and matches_type:
        filtered_events.append(event)

# DISPLAY RESULTS
st.divider()

st.header("📋 Event Search Results")

st.write(f"Found {len(filtered_events)} matching events.")

if filtered_events:

    for event in filtered_events:

        with st.container(border=True):

            st.subheader("🎯 " + event["name"])

            st.write("**Event Type:**", event["type"])
            st.write("**Location:**", event["location"])
            st.write("**Event Date:**", event["date"])
            st.write("**Registration Deadline:**", event["deadline"])

            st.write("**Description:**", event["description"])

            # AI-STYLE SUMMARY
            st.markdown("### 🤖 Event Summary")

            summary = (
                f"{event['name']} is a {event['type'].lower()} "
                f"opportunity in {event['location']}. "
                f"It focuses on {event['description']} "
                f"Interested students should check the event "
                f"platform for further information."
            )

            st.success(summary)

            st.link_button(
                "Visit Event Platform 🔗",
                event["link"]
            )

else:
    st.warning("No matching events found. Try another search.")

# FOOTER
st.divider()

st.markdown(
    """
    ### About EventScout AI

    EventScout AI aims to simplify event discovery for students.

    **Key Features**
    - Natural-language keyword search
    - Location-based event filtering
    - Event information extraction (sample dataset in this MVP)
    - AI-style event summaries
    - Registration deadline highlights
    - External event platform links

    **Developed by Team NextGen Minds**
    wHACKiest 2026 | Track 2
    """
)
