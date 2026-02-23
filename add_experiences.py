import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from core.models import Experience

def populate():
    # Clear existing to ensure clean state with correct sorting fields
    Experience.objects.all().delete()

    experiences = [
        {
            "company": "NSU HCI Design Inclusion and Access Lab",
            "title": "Research Assistant",
            "period": "2023 - 2024",
            "description": "As a Research Assistant at HCI DIAL, my team and I contributed to projects focused on refining user interfaces and enhancing user experience. I was actively involved in user studies and assisted in developing a wearable device to monitor health status. We aimed to harness technological advancements to support individuals living below the poverty line.",
            "start_year": 2023,
            "order": 10
        },
        {
            "company": "Spellbound - স্পেলবাউন্ড",
            "title": "Editorial Member",
            "period": "2020 - 2022",
            "description": "Spellbound, a Harry Potter magazine, was the online-based sole publication for Bengali Harry Potter enthusiasts. As an editorial team member, I contributed by ensuring the quality of the content, conducting peer reviews, and promoting the magazine alongside my fellow team members.",
            "start_year": 2020,
            "order": 5
        },
        {
            "company": "Manabu Bookstore",
            "title": "Co-Owner",
            "period": "2020 - 2022",
            "description": "Founded and ran a profitable online book-selling venture offering affordable, quality books; currently on break with plans to relaunch as a physical book café.",
            "start_year": 2020,
            "order": 4
        },
        {
            "company": "Notre Dame Science Club",
            "title": "President",
            "period": "2018 - 2019",
            "description": "Organized inter-college science and cultural festivals promoting innovation and collaboration.",
            "start_year": 2018,
            "order": 1
        },
        {
            "company": "SM Technology",
            "title": "AI Engineer",
            "period": "2022 - 2023",
            "description": "Specialized in developing and deploying large language models for specialized industrial applications.",
            "start_year": 2022,
            "order": 8
        },
        {
            "company": "Raim Laboratory",
            "title": "Jr. Software Engineer",
            "period": "2019 - 2020",
            "description": "Focused on backend development and system architecture design for scalable web applications.",
            "start_year": 2019,
            "order": 2
        }
    ]

    for exp_data in experiences:
        Experience.objects.create(
            company=exp_data["company"],
            title=exp_data["title"],
            period=exp_data["period"],
            description=exp_data["description"],
            start_year=exp_data["start_year"],
            order=exp_data["order"]
        )
    
    print("Experiences updated and sorted successfully!")

if __name__ == "__main__":
    populate()
