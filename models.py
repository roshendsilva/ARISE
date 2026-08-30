from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    slug = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    overview = db.Column(db.Text, nullable=True) # Detailed "About [Topic]" introduction
    icon = db.Column(db.String(50), default='bi-book')

    articles = db.relationship('Article', backref='category', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Category {self.name}>'


class ChurchFather(db.Model):
    __tablename__ = 'church_fathers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    era = db.Column(db.String(50), nullable=False) # Apostolic, Early Apologist, Later Father
    dates = db.Column(db.String(80), nullable=True) # e.g. "c. 35 - c. 99 AD"
    location = db.Column(db.String(100), nullable=True) # e.g. "Rome", "Antioch", "Hippo"
    biography = db.Column(db.Text, nullable=True)
    major_writings = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<ChurchFather {self.name}>'


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), nullable=False, unique=True)
    
    # 8-Section Scholarly Apologetic Schema
    question = db.Column(db.Text, nullable=False)
    what_protestants_believe = db.Column(db.Text, nullable=True)
    short_answer = db.Column(db.Text, nullable=False)
    catholic_teaching = db.Column(db.Text, nullable=False)
    
    biblical_evidence = db.Column(db.Text, nullable=True)
    objection = db.Column(db.Text, nullable=True)
    catholic_response = db.Column(db.Text, nullable=True)
    early_church_evidence = db.Column(db.Text, nullable=True)
    catechism_text = db.Column(db.Text, nullable=True)
    historical_documents = db.Column(db.Text, nullable=True)
    conclusion = db.Column(db.Text, nullable=True)
    
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    status = db.Column(db.String(20), default='Published') # Draft, Published, Archived
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    scripture_references = db.relationship('ScriptureReference', backref='article', lazy=True, cascade="all, delete-orphan")
    sources = db.relationship('Source', backref='article', lazy=True, cascade="all, delete-orphan")
    objections = db.relationship('ObjectionEntry', backref='article', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Article {self.title}>'


class ScriptureReference(db.Model):
    __tablename__ = 'scripture_references'

    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(80), nullable=False)
    chapter = db.Column(db.Integer, nullable=False)
    verse_start = db.Column(db.Integer, nullable=False)
    verse_end = db.Column(db.Integer, nullable=True)
    passage_text = db.Column(db.Text, nullable=False)
    catholic_interpretation = db.Column(db.Text, nullable=True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=True)

    @property
    def citation(self):
        if self.verse_end and self.verse_end != self.verse_start:
            return f"{self.book} {self.chapter}:{self.verse_start}-{self.verse_end}"
        return f"{self.book} {self.chapter}:{self.verse_start}"

    def __repr__(self):
        return f'<ScriptureReference {self.citation}>'


class Source(db.Model):
    __tablename__ = 'sources'

    id = db.Column(db.Integer, primary_key=True)
    source_title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(120), nullable=True)
    date_period = db.Column(db.String(80), nullable=True) # e.g., "110 AD", "1545-1563 AD", "1992"
    work_document = db.Column(db.String(200), nullable=True) # e.g., "Letter to the Smyrnaeans", "Decree on Justification"
    section_ref = db.Column(db.String(100), nullable=True) # e.g., "Chapter 8", "CCC 1374", "Session 6, Canon 9"
    url = db.Column(db.String(300), nullable=True)
    source_type = db.Column(db.String(50), nullable=False) # Scripture, Catechism, Church Father, Ecumenical Council, Magisterial Document, Historical Source
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=True)

    def __repr__(self):
        return f'<Source {self.source_title}>'


class ObjectionEntry(db.Model):
    __tablename__ = 'objection_entries'

    id = db.Column(db.Integer, primary_key=True)
    objection_text = db.Column(db.Text, nullable=False)
    short_rebuttal = db.Column(db.Text, nullable=False)
    worship_vs_veneration_note = db.Column(db.Text, nullable=True) # Clarification of Latria vs Dulia/Hyperdulia or theological definitions
    related_article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=True)

    def __repr__(self):
        return f'<ObjectionEntry {self.objection_text[:30]}>'


class QuestionSubmission(db.Model):
    __tablename__ = 'question_submissions'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(120), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    question_title = db.Column(db.String(255), nullable=False)
    detailed_question = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending') # Pending, Answered, Published
    official_answer = db.Column(db.Text, nullable=True)
    ai_synthesized_answer = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    answered_at = db.Column(db.DateTime, nullable=True)

    category = db.relationship('Category', backref='questions', lazy=True)

    def __repr__(self):
        return f'<QuestionSubmission {self.question_title[:30]}>'


# ==============================================================================
# COURSE & LEARNING PLATFORM MODELS
# ==============================================================================

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), nullable=False, unique=True)
    short_description = db.Column(db.Text, nullable=False)
    full_description = db.Column(db.Text, nullable=False)
    thumbnail_icon = db.Column(db.String(100), default='bi-journal-bookmark-fill')
    image_url = db.Column(db.String(300), nullable=True)
    instructor_name = db.Column(db.String(120), default="ARISE Theological Faculty")
    difficulty = db.Column(db.String(50), default="Beginner") # Beginner, Intermediate, Advanced
    category_name = db.Column(db.String(100), default="Catholic Apologetics")
    estimated_completion_time = db.Column(db.String(80), default="3 Hours")
    learning_objectives = db.Column(db.Text, nullable=True) # Multiline text
    status = db.Column(db.String(20), default='Published') # Draft, Published, Archived
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    modules = db.relationship('CourseModule', backref='course', lazy=True, cascade="all, delete-orphan", order_by="CourseModule.order")
    lessons = db.relationship('Lesson', backref='course', lazy=True, cascade="all, delete-orphan", order_by="Lesson.lesson_number")
    final_assessments = db.relationship('FinalAssessment', backref='course', lazy=True, cascade="all, delete-orphan")
    certificates = db.relationship('Certificate', backref='course', lazy=True, cascade="all, delete-orphan")
    enrollments = db.relationship('CourseProgress', backref='course', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Course {self.title}>'


class CourseModule(db.Model):
    __tablename__ = 'course_modules'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    order = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    lessons = db.relationship('Lesson', backref='module', lazy=True, cascade="all, delete-orphan", order_by="Lesson.order")

    def __repr__(self):
        return f'<CourseModule {self.title}>'


class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey('course_modules.id'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=True) # Optional link to existing article!
    
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), nullable=False)
    lesson_number = db.Column(db.Integer, nullable=False)
    order = db.Column(db.Integer, default=1)
    estimated_reading_time = db.Column(db.String(50), default="10 min")
    
    # 7-Part Apologetics Lesson Schema
    main_content = db.Column(db.Text, nullable=False)
    catholic_claim = db.Column(db.Text, nullable=True)
    biblical_evidence = db.Column(db.Text, nullable=True)
    historical_evidence = db.Column(db.Text, nullable=True)
    catholic_teaching = db.Column(db.Text, nullable=True)
    common_objection = db.Column(db.Text, nullable=True)
    catholic_response = db.Column(db.Text, nullable=True)
    further_reading = db.Column(db.Text, nullable=True)
    
    status = db.Column(db.String(20), default='Published')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sources = db.relationship('LessonSource', backref='lesson', lazy=True, cascade="all, delete-orphan")
    quizzes = db.relationship('Quiz', backref='lesson', lazy=True, cascade="all, delete-orphan")
    progress_records = db.relationship('LessonProgress', backref='lesson', lazy=True, cascade="all, delete-orphan")

    linked_article = db.relationship('Article', foreign_keys=[article_id])

    def __repr__(self):
        return f'<Lesson {self.title}>'


class LessonSource(db.Model):
    __tablename__ = 'lesson_sources'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(120), nullable=True)
    date_period = db.Column(db.String(80), nullable=True)
    work_document = db.Column(db.String(200), nullable=True)
    section_ref = db.Column(db.String(100), nullable=True)
    url = db.Column(db.String(300), nullable=True)
    source_type = db.Column(db.String(50), default='Scripture') # Scripture, Catechism, Church Father, Ecumenical Council, Papal Document, Academic

    def __repr__(self):
        return f'<LessonSource {self.title}>'


class Quiz(db.Model):
    __tablename__ = 'quizzes'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    title = db.Column(db.String(200), default="Lesson Quiz")
    passing_percentage = db.Column(db.Integer, default=70)

    questions = db.relationship('QuizQuestion', backref='quiz', lazy=True, cascade="all, delete-orphan", order_by="QuizQuestion.order")
    attempts = db.relationship('QuizAttempt', backref='quiz', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Quiz for Lesson {self.lesson_id}>'


class QuizQuestion(db.Model):
    __tablename__ = 'quiz_questions'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(50), default='multiple_choice') # multiple_choice, true_false
    explanation = db.Column(db.Text, nullable=True)
    order = db.Column(db.Integer, default=1)

    options = db.relationship('QuizOption', backref='question', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<QuizQuestion {self.question_text[:30]}>'


class QuizOption(db.Model):
    __tablename__ = 'quiz_options'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('quiz_questions.id'), nullable=False)
    option_text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<QuizOption {self.option_text[:30]}>'


class QuizAttempt(db.Model):
    __tablename__ = 'quiz_attempts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    score_percentage = db.Column(db.Integer, nullable=False)
    passed = db.Column(db.Boolean, default=False)
    attempted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<QuizAttempt User {self.user_id} Score {self.score_percentage}%>'


class LessonProgress(db.Model):
    __tablename__ = 'lesson_progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    quiz_passed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    user = db.relationship('User', backref='lesson_progress_records')

    def __repr__(self):
        return f'<LessonProgress User {self.user_id} Lesson {self.lesson_id} Done:{self.completed}>'


class CourseProgress(db.Model):
    __tablename__ = 'course_progress'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    progress_percentage = db.Column(db.Integer, default=0)
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, nullable=True)
    last_lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=True)

    user = db.relationship('User', backref='course_enrollments')
    last_lesson = db.relationship('Lesson', foreign_keys=[last_lesson_id])

    def __repr__(self):
        return f'<CourseProgress User {self.user_id} Course {self.course_id} {self.progress_percentage}%>'


class FinalAssessment(db.Model):
    __tablename__ = 'final_assessments'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    title = db.Column(db.String(200), default="Final Course Assessment")
    description = db.Column(db.Text, nullable=True)
    passing_percentage = db.Column(db.Integer, default=70)
    total_questions = db.Column(db.Integer, default=10)

    questions = db.relationship('FinalAssessmentQuestion', backref='assessment', lazy=True, cascade="all, delete-orphan")
    attempts = db.relationship('FinalAssessmentAttempt', backref='assessment', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<FinalAssessment Course {self.course_id}>'


class FinalAssessmentQuestion(db.Model):
    __tablename__ = 'final_assessment_questions'

    id = db.Column(db.Integer, primary_key=True)
    assessment_id = db.Column(db.Integer, db.ForeignKey('final_assessments.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(50), default='multiple_choice')
    explanation = db.Column(db.Text, nullable=True)
    order = db.Column(db.Integer, default=1)

    options = db.relationship('FinalAssessmentOption', backref='question', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<FinalAssessmentQuestion {self.question_text[:30]}>'


class FinalAssessmentOption(db.Model):
    __tablename__ = 'final_assessment_options'

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('final_assessment_questions.id'), nullable=False)
    option_text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<FinalAssessmentOption {self.option_text[:30]}>'


class FinalAssessmentAttempt(db.Model):
    __tablename__ = 'final_assessment_attempts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    assessment_id = db.Column(db.Integer, db.ForeignKey('final_assessments.id'), nullable=False)
    score_percentage = db.Column(db.Integer, nullable=False)
    passed = db.Column(db.Boolean, default=False)
    attempted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<FinalAssessmentAttempt User {self.user_id} Score {self.score_percentage}%>'


class Certificate(db.Model):
    __tablename__ = 'certificates'

    id = db.Column(db.Integer, primary_key=True)
    certificate_id = db.Column(db.String(100), unique=True, nullable=False) # e.g. ARISE-2026-X8F9A
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    student_name = db.Column(db.String(120), nullable=False)
    course_title = db.Column(db.String(200), nullable=False)
    completion_date = db.Column(db.DateTime, default=datetime.utcnow)
    instructor_signature = db.Column(db.String(120), default="Roshen D'silva, Lead Apologist")
    disclaimer = db.Column(db.Text, default="This certificate recognizes the successful completion of an educational course offered by Arise. It is not an academic degree, government qualification, or ecclesiastical credential.")

    user = db.relationship('User', backref='certificates')

    def __repr__(self):
        return f'<Certificate {self.certificate_id}>'
