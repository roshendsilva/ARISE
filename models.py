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

