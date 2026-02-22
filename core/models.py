from django.db import models

class PortfolioProfile(models.Model):
    name = models.CharField(max_length=100, default="Promit Sarker")
    hero_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    hero_subtitle = models.CharField(max_length=200, default="Est. MMXXIV • Artificial Intelligence")
    hero_title = models.CharField(max_length=200, default="THE INTERSECTION OF <br> <span class='italic text-gold'>WISDOM</span> & CODE")
    hero_tagline = models.TextField(default="Architecting the next generation of artificial intelligence with the precision of classical geometry.")
    
    philosophy_title = models.CharField(max_length=200, default="Ethics & Architecture")
    philosophy_intro = models.TextField(default="My approach to development is rooted in the belief that reason should be as ethical as it is efficient.")
    
    projects_title = models.CharField(max_length=200, default="Selected Works")
    armory_title = models.CharField(max_length=200, default="The Armory")
    armory_tagline = models.CharField(max_length=500, default="An architectural repository of technical proficiencies tailored for intelligent systems.")
    publications_title = models.CharField(max_length=200, default="Publications")
    chronology_title = models.CharField(max_length=200, default="Chronology")
    chronicles_title = models.CharField(max_length=200, default="The Chronicles")
    chronicles_subtitle = models.CharField(max_length=200, default="Scrolls")
    
    experience_label = models.CharField(max_length=100, default="I. Praxis (Experience)")
    education_label = models.CharField(max_length=100, default="II. Formation (Education)")
    
    contact_title = models.CharField(max_length=200, default="Initiate Dialogue")
    contact_subtitle = models.TextField(default='"The Universe is change; our life is what our thoughts make it."')
    
    email = models.EmailField(default="promitsrkr@gmail.com")
    linkedin_url = models.URLField(default="https://linkedin.com/in/promitsarker")
    github_url = models.URLField(default="https://github.com/PromitSarker")
    resume_url = models.URLField(blank=True, null=True, help_text="Link to your PDF resume")
    
    def __str__(self):
        return f"{self.name}'s Profile"

class SkillPillar(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. FOUNDATIONS")
    subtitle = models.CharField(max_length=100, help_text="e.g. CORE ENGINEERING")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class PhilosophyTrait(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text="FontAwesome class, e.g., fa-compass")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Store tags as a plain text string (comma-separated)
    tags = models.TextField(help_text="Comma-separated tags, e.g. Python,Django,ML")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    imageUrl = models.URLField(blank=True, null=True, help_text="Fallback URL if no image is uploaded")
    url = models.URLField(help_text="Link to project, e.g., GitHub or live demo")  # new field

    def get_tags(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=300)
    abstract = models.TextField()
    venue = models.CharField(max_length=100, help_text="e.g. NeurIPS 2023")
    volume = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. Volume XXIV")
    authors = models.CharField(max_length=200, default="M. Aurelius, et al.")
    pdf_url = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default="The Algorithm")
    excerpt = models.TextField()
    date = models.DateField()
    imageUrl = models.URLField()
    url = models.URLField(help_text="Link to full blog post, e.g., Medium URL")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order', '-date']

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    period = models.CharField(max_length=100, help_text="e.g., 2023 - Present")
    description = models.TextField()
    order = models.IntegerField(default=0, help_text="Higher number comes first")

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    period = models.CharField(max_length=100, help_text="e.g., 2016 – 2018")
    description = models.TextField()
    order = models.IntegerField(default=0, help_text="Higher number comes first")

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return f"{self.degree} at {self.institution}"


class SkillCategory(models.Model):
    pillar = models.ForeignKey(SkillPillar, related_name='categories', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return f"{self.name} ({self.pillar.name if self.pillar else 'No Pillar'})"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
