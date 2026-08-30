import os
import uuid
import markdown as md_lib
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import Config
from models import (
    db, User, Category, Article, ChurchFather, ScriptureReference, Source, 
    ObjectionEntry, QuestionSubmission, Course, Lesson, Quiz, QuizQuestion, 
    CourseProgress, Certificate
)
from seed_data import seed_database
from seed_courses import seed_courses
from sqlalchemy import or_

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)
app.config.from_object(Config)

@app.template_filter('render_md')
def render_md_filter(text):
    if not text:
        return ""
    return md_lib.markdown(text, extensions=['fenced_code', 'tables', 'nl2br'])

# Initialize Extensions

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please sign in or create an account to submit your question to our apologetics team.'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Context Processor for Site-Wide Data
@app.context_processor
def inject_global_data():
    try:
        categories = Category.query.all()
    except Exception:
        categories = []
    return dict(all_categories=categories)

# Automatically create tables & seed database on app startup if running locally
if not os.environ.get('VERCEL'):
    with app.app_context():
        try:
            db.create_all()
            seed_database(app)
            seed_courses()
        except Exception as e:
            print(f"Startup DB init notice: {e}")

# ==================== PUBLIC ROUTES ====================

@app.route('/')
def index():
    featured_articles = Article.query.filter_by(status='Published', is_featured=True).limit(4).all()
    recent_articles = Article.query.filter_by(status='Published').order_by(Article.created_at.desc()).limit(6).all()
    categories = Category.query.all()
    fathers = ChurchFather.query.limit(4).all()
    objections = ObjectionEntry.query.limit(4).all()
    
    total_articles = Article.query.filter_by(status='Published').count()
    total_sources = Source.query.count()
    total_fathers = ChurchFather.query.count()

    return render_template(
        'index.html',
        featured_articles=featured_articles,
        recent_articles=recent_articles,
        categories=categories,
        fathers=fathers,
        objections=objections,
        total_articles=total_articles,
        total_sources=total_sources,
        total_fathers=total_fathers
    )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/apologetics')
def apologetics():
    category_slug = request.args.get('category')
    search_q = request.args.get('q', '').strip()
    
    query = Article.query.filter_by(status='Published')
    
    selected_category = None
    if category_slug:
        selected_category = Category.query.filter_by(slug=category_slug).first()
        if selected_category:
            query = query.filter_by(category_id=selected_category.id)
            
    if search_q:
        query = query.filter(
            or_(
                Article.title.ilike(f"%{search_q}%"),
                Article.question.ilike(f"%{search_q}%"),
                Article.short_answer.ilike(f"%{search_q}%")
            )
        )
        
    articles = query.order_by(Article.created_at.desc()).all()
    return render_template('apologetics.html', articles=articles, selected_category=selected_category, search_q=search_q)

@app.route('/category/<slug>')
def category_detail(slug):
    category = Category.query.filter_by(slug=slug).first_or_404()
    articles = Article.query.filter_by(category_id=category.id, status='Published').all()
    return render_template('apologetics.html', articles=articles, selected_category=category, search_q='')

@app.route('/article/<slug>')
def article_detail(slug):
    article = Article.query.filter_by(slug=slug, status='Published').first_or_404()
    related_articles = Article.query.filter(
        Article.category_id == article.category_id,
        Article.id != article.id,
        Article.status == 'Published'
    ).limit(3).all()
    
    return render_template('article_detail.html', article=article, related_articles=related_articles)

@app.route('/objections')
def objections():
    category_filter = request.args.get('category', 'all')
    search_q = request.args.get('q', '').strip()
    
    query = ObjectionEntry.query
    if search_q:
        query = query.filter(
            or_(
                ObjectionEntry.objection_text.ilike(f"%{search_q}%"),
                ObjectionEntry.short_rebuttal.ilike(f"%{search_q}%")
            )
        )
        
    objection_list = query.all()
    return render_template('objections.html', objections=objection_list, search_q=search_q, category_filter=category_filter)

@app.route('/bible-explorer')
def bible_explorer():
    search_q = request.args.get('q', '').strip()
    query = ScriptureReference.query
    
    if search_q:
        query = query.filter(
            or_(
                ScriptureReference.book.ilike(f"%{search_q}%"),
                ScriptureReference.passage_text.ilike(f"%{search_q}%"),
                ScriptureReference.catholic_interpretation.ilike(f"%{search_q}%")
            )
        )
        
    passages = query.all()
    return render_template('bible_explorer.html', passages=passages, search_q=search_q)

@app.route('/church-fathers')
def church_fathers():
    era_filter = request.args.get('era', 'all')
    search_q = request.args.get('q', '').strip()
    
    query = ChurchFather.query
    if era_filter != 'all':
        query = query.filter_by(era=era_filter)
        
    if search_q:
        query = query.filter(
            or_(
                ChurchFather.name.ilike(f"%{search_q}%"),
                ChurchFather.biography.ilike(f"%{search_q}%"),
                ChurchFather.major_writings.ilike(f"%{search_q}%")
            )
        )
        
    fathers_list = query.all()
    return render_template('church_fathers.html', fathers=fathers_list, search_q=search_q, era_filter=era_filter)

@app.route('/sources')
def sources():
    type_filter = request.args.get('type', 'all')
    search_q = request.args.get('q', '').strip()
    
    query = Source.query
    if type_filter != 'all':
        query = query.filter_by(source_type=type_filter)
        
    if search_q:
        query = query.filter(
            or_(
                Source.source_title.ilike(f"%{search_q}%"),
                Source.author.ilike(f"%{search_q}%"),
                Source.work_document.ilike(f"%{search_q}%")
            )
        )
        
    source_list = query.all()
    return render_template('sources.html', sources=source_list, search_q=search_q, type_filter=type_filter)


# ==================== REUSABLE COURSE SYSTEM ROUTES ====================

@app.route('/courses')
def courses():
    search_q = request.args.get('q', '').strip()
    category_filter = request.args.get('category', 'all')
    
    query = Course.query.filter_by(published=True)
    if search_q:
        query = query.filter(
            or_(
                Course.title.ilike(f"%{search_q}%"),
                Course.description.ilike(f"%{search_q}%")
            )
        )
    if category_filter != 'all':
        query = query.filter_by(category=category_filter)
        
    course_list = query.all()
    
    # Calculate user progress per course if logged in
    progress_map = {}
    if current_user.is_authenticated:
        for c in course_list:
            total_l = len(c.lessons)
            completed_l = CourseProgress.query.filter_by(user_id=current_user.id, course_id=c.id, completed=True).count()
            percent = int((completed_l / total_l * 100)) if total_l > 0 else 0
            progress_map[c.id] = {
                'completed_count': completed_l,
                'total_count': total_l,
                'percentage': percent
            }

    return render_template('courses.html', courses=course_list, search_q=search_q, category_filter=category_filter, progress_map=progress_map)


@app.route('/courses/<slug>')
def course_detail(slug):
    course = Course.query.filter_by(slug=slug, published=True).first_or_404()
    lessons = Lesson.query.filter_by(course_id=course.id, published=True).order_by(Lesson.lesson_number).all()
    
    completed_lesson_ids = set()
    user_certificate = None
    progress_percentage = 0

    if current_user.is_authenticated:
        completed_records = CourseProgress.query.filter_by(user_id=current_user.id, course_id=course.id, completed=True).all()
        completed_lesson_ids = set(r.lesson_id for r in completed_records)
        user_certificate = Certificate.query.filter_by(user_id=current_user.id, course_id=course.id).first()
        if len(lessons) > 0:
            progress_percentage = int((len(completed_lesson_ids) / len(lessons)) * 100)

    return render_template(
        'course_detail.html',
        course=course,
        lessons=lessons,
        completed_lesson_ids=completed_lesson_ids,
        user_certificate=user_certificate,
        progress_percentage=progress_percentage
    )


@app.route('/courses/<course_slug>/lessons/<lesson_slug>')
def lesson_view(course_slug, lesson_slug):
    course = Course.query.filter_by(slug=course_slug, published=True).first_or_404()
    lesson = Lesson.query.filter_by(course_id=course.id, slug=lesson_slug, published=True).first_or_404()
    all_lessons = Lesson.query.filter_by(course_id=course.id, published=True).order_by(Lesson.lesson_number).all()
    
    # Previous and Next Lessons
    prev_lesson = Lesson.query.filter_by(course_id=course.id, lesson_number=lesson.lesson_number - 1, published=True).first()
    next_lesson = Lesson.query.filter_by(course_id=course.id, lesson_number=lesson.lesson_number + 1, published=True).first()
    
    # Get Quiz
    quiz = Quiz.query.filter_by(lesson_id=lesson.id).first()
    
    # Check User Progress for this lesson
    user_progress = None
    if current_user.is_authenticated:
        user_progress = CourseProgress.query.filter_by(user_id=current_user.id, course_id=course.id, lesson_id=lesson.id).first()

    return render_template(
        'lesson_view.html',
        course=course,
        lesson=lesson,
        all_lessons=all_lessons,
        prev_lesson=prev_lesson,
        next_lesson=next_lesson,
        quiz=quiz,
        user_progress=user_progress
    )


@app.route('/courses/<course_slug>/lessons/<lesson_slug>/quiz', methods=['POST'])
@login_required
def submit_quiz(course_slug, lesson_slug):
    course = Course.query.filter_by(slug=course_slug, published=True).first_or_404()
    lesson = Lesson.query.filter_by(course_id=course.id, slug=lesson_slug, published=True).first_or_404()
    quiz = Quiz.query.filter_by(lesson_id=lesson.id).first_or_404()
    
    correct_count = 0
    total_questions = len(quiz.questions)
    answers_feedback = []

    for q in quiz.questions:
        user_answer = request.form.get(f'q_{q.id}')
        is_correct = (user_answer == q.correct_option)
        if is_correct:
            correct_count += 1
        answers_feedback.append({
            'question_id': q.id,
            'user_answer': user_answer,
            'correct_option': q.correct_option,
            'is_correct': is_correct,
            'explanation': q.explanation
        })
        
    score_percentage = int((correct_count / total_questions) * 100) if total_questions > 0 else 100
    passed = score_percentage >= quiz.passing_score

    # Record or update progress
    progress = CourseProgress.query.filter_by(user_id=current_user.id, course_id=course.id, lesson_id=lesson.id).first()
    if not progress:
        progress = CourseProgress(
            user_id=current_user.id,
            course_id=course.id,
            lesson_id=lesson.id
        )
        db.session.add(progress)

    progress.quiz_score = score_percentage
    if passed:
        progress.completed = True
        progress.quiz_passed = True
        progress.completed_at = datetime.utcnow()

    db.session.commit()

    # Check if all lessons in course are completed to auto-generate certificate!
    total_course_lessons = Lesson.query.filter_by(course_id=course.id, published=True).count()
    completed_course_lessons = CourseProgress.query.filter_by(user_id=current_user.id, course_id=course.id, completed=True).count()

    certificate_generated = False
    cert_id = None

    if total_course_lessons > 0 and completed_course_lessons >= total_course_lessons:
        cert = Certificate.query.filter_by(user_id=current_user.id, course_id=course.id).first()
        if not cert:
            cert_id = f"ARISE-CERT-2026-{uuid.uuid4().hex[:8].upper()}"
            cert = Certificate(
                certificate_id=cert_id,
                user_id=current_user.id,
                course_id=course.id,
                user_name=current_user.username,
                course_title=course.title
            )
            db.session.add(cert)
            db.session.commit()
            certificate_generated = True
        else:
            cert_id = cert.certificate_id

    if passed:
        flash(f"🎉 Congratulations! You passed the quiz with {score_percentage}%!", "success")
    else:
        flash(f"You scored {score_percentage}%. Passing score is {quiz.passing_score}%. Review the lesson and try again!", "warning")

    return render_template(
        'quiz_results.html',
        course=course,
        lesson=lesson,
        quiz=quiz,
        score_percentage=score_percentage,
        passed=passed,
        answers_feedback=answers_feedback,
        certificate_generated=certificate_generated,
        cert_id=cert_id
    )


@app.route('/my-learning')
@login_required
def my_learning():
    progress_records = CourseProgress.query.filter_by(user_id=current_user.id).all()
    user_certificates = Certificate.query.filter_by(user_id=current_user.id).all()
    
    # Organize progress by course
    enrolled_courses = Course.query.filter_by(published=True).all()
    user_courses_data = []

    for c in enrolled_courses:
        total_l = len(c.lessons)
        user_c_progress = [p for p in progress_records if p.course_id == c.id and p.completed]
        completed_cnt = len(user_c_progress)
        
        if completed_cnt > 0:
            percent = int((completed_cnt / total_l * 100)) if total_l > 0 else 0
            cert = next((crt for crt in user_certificates if crt.course_id == c.id), None)
            user_courses_data.append({
                'course': c,
                'total_lessons': total_l,
                'completed_lessons': completed_cnt,
                'percentage': percent,
                'certificate': cert
            })

    return render_template('my_learning.html', user_courses_data=user_courses_data, certificates=user_certificates)


@app.route('/certificate/<certificate_id>')
def view_certificate(certificate_id):
    cert = Certificate.query.filter_by(certificate_id=certificate_id).first_or_404()
    course = Course.query.get_or_404(cert.course_id)
    return render_template('certificate.html', cert=cert, course=course)


@app.route('/verify/<certificate_id>')
@app.route('/verify/')
def verify_certificate(certificate_id=None):
    if not certificate_id:
        certificate_id = request.args.get('certificate_id', '').strip()
    cert = Certificate.query.filter_by(certificate_id=certificate_id).first() if certificate_id else None
    return render_template('certificate_verify.html', cert=cert, searched_id=certificate_id)


# ==================== Q&A SUBMISSION & ACCOUNT ROUTES ====================

@app.route('/ask-apologist', methods=['GET', 'POST'])
@login_required
def ask_apologist():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        category_id = request.form.get('category_id')
        question_title = request.form.get('question_title')
        detailed_question = request.form.get('detailed_question')

        submission = QuestionSubmission(
            user_name=name or current_user.username,
            user_email=email or current_user.email,
            category_id=int(category_id) if category_id else None,
            question_title=question_title,
            detailed_question=detailed_question,
            status='Pending'
        )
        db.session.add(submission)
        db.session.commit()
        flash("Your question has been submitted to the ARISE apologetics team! We will review and provide a faithful Catholic response soon.", "success")
        return redirect(url_for('account'))

    return render_template('ask_apologist.html')


@app.route('/account')
@login_required
def account():
    my_questions = QuestionSubmission.query.filter_by(user_email=current_user.email).order_by(QuestionSubmission.created_at.desc()).all()
    user_certificates = Certificate.query.filter_by(user_id=current_user.id).all()
    return render_template('account.html', my_questions=my_questions, user_certificates=user_certificates)


# ==================== AUTHENTICATION ROUTES ====================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        email_or_user = request.form.get('email_or_user')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter(
            or_(User.email == email_or_user, User.username == email_or_user)
        ).first()

        if user and user.check_password(password):
            login_user(user, remember=remember)
            flash(f"Welcome back, {user.username}!", "success")
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash("Invalid credentials. Please verify your username/email and password.", "danger")

    return render_template('admin/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template('admin/register.html')

        if User.query.filter_by(username=username).first():
            flash("Username already exists. Please choose a different one.", "danger")
            return render_template('admin/register.html')

        if User.query.filter_by(email=email).first():
            flash("Email already registered. Please sign in instead.", "danger")
            return render_template('admin/register.html')

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash("Registration successful! Welcome to ARISE.", "success")
        return redirect(url_for('index'))

    return render_template('admin/register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been signed out.", "info")
    return redirect(url_for('index'))


# ==================== ADMIN MANAGEMENT ROUTES ====================

@app.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash("Unauthorized access. Admin privileges required.", "danger")
        return redirect(url_for('index'))
        
    total_articles = Article.query.count()
    total_categories = Category.query.count()
    total_questions = QuestionSubmission.query.count()
    pending_questions = QuestionSubmission.query.filter_by(status='Pending').count()
    total_courses = Course.query.count()
    
    return render_template(
        'admin/dashboard.html',
        total_articles=total_articles,
        total_categories=total_categories,
        total_questions=total_questions,
        pending_questions=pending_questions,
        total_courses=total_courses
    )


@app.route('/admin/questions')
@login_required
def admin_questions():
    if not current_user.is_admin:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('index'))
        
    status_filter = request.args.get('status', 'all')
    query = QuestionSubmission.query
    if status_filter != 'all':
        query = query.filter_by(status=status_filter)
        
    questions = query.order_by(QuestionSubmission.created_at.desc()).all()
    return render_template('admin/question_list.html', questions=questions, status_filter=status_filter)


@app.route('/admin/courses')
@login_required
def admin_courses():
    if not current_user.is_admin:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('index'))
    courses_list = Course.query.order_by(Course.created_at.desc()).all()
    return render_template('admin/admin_courses.html', courses=courses_list)


@app.route('/admin/courses/new', methods=['GET', 'POST'])
@login_required
def admin_course_new():
    if not current_user.is_admin:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        title = request.form.get('title')
        slug = request.form.get('slug')
        description = request.form.get('description')
        short_description = request.form.get('short_description')
        category = request.form.get('category', 'Catholic Formation')
        difficulty = request.form.get('difficulty', 'Intermediate')
        estimated_duration = request.form.get('estimated_duration', '10 Hours')
        
        new_course = Course(
            title=title,
            slug=slug,
            description=description,
            short_description=short_description,
            category=category,
            difficulty=difficulty,
            estimated_duration=estimated_duration,
            published=True
        )
        db.session.add(new_course)
        db.session.commit()
        flash(f"Course '{title}' created successfully!", "success")
        return redirect(url_for('admin_courses'))
        
    return render_template('admin/admin_course_edit.html', course=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
