import os
import sys

# Add root directory to sys.path
sys.path.append(r"c:\Users\joyce evangeline\OneDrive\Desktop\Apologetics")

from models import db, Course, Lesson, Quiz, QuizQuestion
from scratch.build_course_1_data import course_1_data

# Reusable registry of courses for the Arise Courses Platform.
# Future courses (e.g. Marian Dogmas, Sacraments, Early Christianity) will simply be registered in this list!
COURSES_REGISTRY = [
    course_1_data
]

def seed_courses(app=None):
    print("Starting Reusable Arise Course Platform Seeding...", flush=True)

    for c_data in COURSES_REGISTRY:
        course = Course.query.filter_by(slug=c_data["slug"]).first()
        if not course:
            course = Course(
                title=c_data["title"],
                slug=c_data["slug"],
                description=c_data["description"],
                short_description=c_data.get("short_description", ""),
                thumbnail=c_data.get("thumbnail", "images/logo.jpg"),
                instructor=c_data.get("instructor", "Roshen D'silva"),
                category=c_data.get("category", "Catholic Formation"),
                difficulty=c_data.get("difficulty", "Intermediate"),
                estimated_duration=c_data.get("estimated_duration", "10 Hours"),
                published=c_data.get("published", True)
            )
            db.session.add(course)
            db.session.commit()
            print(f"Created Course: '{course.title}' (ID: {course.id})", flush=True)
        else:
            print(f"Course '{course.title}' already exists.", flush=True)

        # Seed lessons and quizzes
        for l_data in c_data.get("lessons", []):
            lesson = Lesson.query.filter_by(course_id=course.id, slug=l_data["slug"]).first()
            if not lesson:
                lesson = Lesson(
                    course_id=course.id,
                    title=l_data["title"],
                    slug=l_data["slug"],
                    lesson_number=l_data["lesson_number"],
                    introduction=l_data.get("introduction", ""),
                    content=l_data["content"],
                    learning_objectives=l_data.get("learning_objectives", ""),
                    key_takeaways=l_data.get("key_takeaways", ""),
                    scripture_references=l_data.get("scripture_references", ""),
                    sources=l_data.get("sources", ""),
                    estimated_reading_time=l_data.get("estimated_reading_time", "35 mins"),
                    published=True
                )
                db.session.add(lesson)
                db.session.commit()
                print(f"  + Added Lesson #{lesson.lesson_number}: '{lesson.title}'", flush=True)
            else:
                # Update content if existing
                lesson.content = l_data["content"]
                lesson.learning_objectives = l_data.get("learning_objectives", "")
                lesson.key_takeaways = l_data.get("key_takeaways", "")
                lesson.scripture_references = l_data.get("scripture_references", "")
                lesson.sources = l_data.get("sources", "")
                db.session.commit()

            # Seed Quiz & QuizQuestions
            quiz = Quiz.query.filter_by(lesson_id=lesson.id).first()
            if not quiz:
                quiz = Quiz(
                    lesson_id=lesson.id,
                    title=l_data.get("quiz_title", f"Quiz: {lesson.title}"),
                    passing_score=70
                )
                db.session.add(quiz)
                db.session.commit()

            # Questions
            for q_item in l_data.get("questions", []):
                existing_q = QuizQuestion.query.filter_by(quiz_id=quiz.id, question_text=q_item["question"]).first()
                if not existing_q:
                    q_obj = QuizQuestion(
                        quiz_id=quiz.id,
                        question_text=q_item["question"],
                        option_a=q_item["options"]["A"],
                        option_b=q_item["options"]["B"],
                        option_c=q_item["options"]["C"],
                        option_d=q_item["options"]["D"],
                        correct_option=q_item["correct"],
                        explanation=q_item.get("explanation", "")
                    )
                    db.session.add(q_obj)
            db.session.commit()

    print("SUCCESS: Finished seeding all courses and lessons in registry!", flush=True)

if __name__ == '__main__':
    from app import app
    with app.app_context():
        seed_courses()
