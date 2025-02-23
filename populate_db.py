from events.models import Event, Participant, Category
import os
import django
from faker import Faker
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_management.settings')
django.setup()

# Import models after Django setup

# Function to populate the database


def populate_db():
    fake = Faker()

    # Create Categories
    categories = [Category.objects.create(
        name=fake.word().capitalize(),
        description=fake.sentence()
    ) for _ in range(5)]
    print(f"Created {len(categories)} categories.")

    # Create Events
    events = [Event.objects.create(
        name=fake.sentence(nb_words=3).replace('.', ''),
        description=fake.paragraph(),
        date=fake.date_this_year(),
        time=fake.time(),
        location=fake.city(),
        category=random.choice(categories)
    ) for _ in range(10)]
    print(f"Created {len(events)} events.")

    # Create Participants
    participants = [Participant.objects.create(
        name=fake.name(),
        email=fake.unique.email()
    ) for _ in range(15)]
    print(f"Created {len(participants)} participants.")

    # Assign Participants to Events (Many-to-Many)
    for participant in participants:
        # Assign each participant to 1-5 events
        assigned_events = random.sample(events, random.randint(1, 5))
        participant.event.set(assigned_events)

    print("Assigned participants to events.")
    print("Database populated successfully!")


# Run the function
if __name__ == "__main__":
    populate_db()
