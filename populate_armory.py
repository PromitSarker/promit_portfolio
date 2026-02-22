import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from core.models import SkillPillar, SkillCategory, Skill

def populate():
    # Clear existing to avoid duplicates in demo
    SkillPillar.objects.all().delete()
    SkillCategory.objects.all().delete()
    Skill.objects.all().delete()

    pillars = [
        {
            "name": "FOUNDATIONS",
            "subtitle": "CORE ENGINEERING",
            "categories": [
                {"name": "PYTHON", "skills": ["DJANGO", "FASTAPI", "DRF"]},
                {"name": "GIT", "skills": ["GITHUB", "GITLAB CI"]},
                {"name": "DATA", "skills": ["POSTGRES", "MONGODB", "SQL"]},
            ]
        },
        {
            "name": "INTELLIGENCE",
            "subtitle": "MODEL ARCHITECTURE",
            "categories": [
                {"name": "ML / DL", "skills": ["PYTORCH", "SCIKIT-LEARN", "TENSORFLOW"]},
                {"name": "LLM TUNING", "skills": ["LORA", "QLORA", "PEFT"]},
                {"name": "AGENTS", "skills": ["LANGCHAIN", "N8N", "MCP"]},
            ]
        },
        {
            "name": "INFRASTRUCTURE",
            "subtitle": "DEPLOYMENT & RAG",
            "categories": [
                {"name": "OPS", "skills": ["DOCKER", "KUBERNETES", "AWS"]},
                {"name": "RAG", "skills": ["RAG", "VECTOR EMBEDDINGS"]},
                {"name": "VECTOR DB", "skills": ["CHROMADB", "FAISS", "PINECONE"]},
            ]
        }
    ]

    for i, p_data in enumerate(pillars):
        pillar = SkillPillar.objects.create(
            name=p_data["name"],
            subtitle=p_data["subtitle"],
            order=i
        )
        for j, c_data in enumerate(p_data["categories"]):
            category = SkillCategory.objects.create(
                pillar=pillar,
                name=c_data["name"],
                order=j
            )
            for k, s_name in enumerate(c_data["skills"]):
                Skill.objects.create(
                    category=category,
                    name=s_name,
                    order=k
                )
    
    print("Armory populated successfully!")

if __name__ == "__main__":
    populate()
