import os
import markdown as md_lib
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import Config
from models import (
    db, User, Category, Article, ChurchFather, ScriptureReference, Source, ObjectionEntry, 
    QuestionSubmission, Course, CourseModule, Lesson, LessonSource, Quiz, QuizQuestion, 
    QuizOption, QuizAttempt, LessonProgress, CourseProgress, FinalAssessment, 
    FinalAssessmentQuestion, FinalAssessmentOption, FinalAssessmentAttempt, Certificate
)
from seed_data import seed_database
from seed_courses import seed_courses_data
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
            seed_courses_data(app)
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
        
    scriptures = query.all()
    return render_template('bible_explorer.html', scriptures=scriptures, search_q=search_q)

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
        
    fathers = query.all()
    return render_template('church_fathers.html', fathers=fathers, era_filter=era_filter, search_q=search_q)

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
    return render_template('sources.html', sources=source_list, type_filter=type_filter, search_q=search_q)

@app.route('/search')
def global_search():
    q = request.args.get('q', '').strip()
    if not q:
        return redirect(url_for('index'))
        
    articles = Article.query.filter(
        Article.status == 'Published',
        or_(
            Article.title.ilike(f"%{q}%"),
            Article.question.ilike(f"%{q}%"),
            Article.short_answer.ilike(f"%{q}%"),
            Article.catholic_teaching.ilike(f"%{q}%")
        )
    ).all()
    
    scriptures = ScriptureReference.query.filter(
        or_(
            ScriptureReference.book.ilike(f"%{q}%"),
            ScriptureReference.passage_text.ilike(f"%{q}%"),
            ScriptureReference.catholic_interpretation.ilike(f"%{q}%")
        )
    ).all()

    fathers = ChurchFather.query.filter(
        or_(
            ChurchFather.name.ilike(f"%{q}%"),
            ChurchFather.biography.ilike(f"%{q}%")
        )
    ).all()

    objections = ObjectionEntry.query.filter(
        or_(
            ObjectionEntry.objection_text.ilike(f"%{q}%"),
            ObjectionEntry.short_rebuttal.ilike(f"%{q}%")
        )
    ).all()

    sources = Source.query.filter(
        or_(
            Source.source_title.ilike(f"%{q}%"),
            Source.work_document.ilike(f"%{q}%")
        )
    ).all()

    return render_template(
        'search.html',
        q=q,
        articles=articles,
        scriptures=scriptures,
        fathers=fathers,
        objections=objections,
        sources=sources
    )

# ==================== AUTHENTICATION & ACCOUNT ROUTES ====================

@app.route('/login', methods=['GET', 'POST'])
@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin_dashboard'))
        return redirect(url_for('account'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            if user.is_admin:
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('account'))
        else:
            flash('Invalid email or password. Please check your credentials.', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('account'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        if not username or not email or not password:
            flash('Please fill in all required fields.', 'danger')
        elif password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('An account with this email address already exists.', 'warning')
        elif User.query.filter_by(username=username).first():
            flash('Username is already taken. Please choose another.', 'warning')
        else:
            new_user = User(username=username, email=email, is_admin=False)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            flash('Welcome to ARISE! Your research account has been created.', 'success')
            return redirect(url_for('account'))

    return render_template('register.html')

@app.route('/logout')
@app.route('/admin/logout')
@login_required
def logout():
    logout_user()
    flash('You have been signed out.', 'info')
    return redirect(url_for('index'))

@app.route('/account')
@login_required
def account():
    user_questions = QuestionSubmission.query.filter_by(user_email=current_user.email).order_by(QuestionSubmission.created_at.desc()).all()
    return render_template('account.html', user_questions=user_questions)

# ==================== ADMIN ROUTES ====================

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    total_articles = Article.query.count()
    published_articles = Article.query.filter_by(status='Published').count()
    draft_articles = Article.query.filter_by(status='Draft').count()
    total_categories = Category.query.count()
    total_sources = Source.query.count()
    
    recent_articles = Article.query.order_by(Article.created_at.desc()).limit(5).all()

    return render_template(
        'admin/dashboard.html',
        total_articles=total_articles,
        published_articles=published_articles,
        draft_articles=draft_articles,
        total_categories=total_categories,
        total_sources=total_sources,
        recent_articles=recent_articles
    )

@app.route('/admin/articles')
@login_required
def admin_articles():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template('admin/article_list.html', articles=articles)

@app.route('/admin/article/new', methods=['GET', 'POST'])
@login_required
def admin_article_new():
    categories = Category.query.all()
    if request.method == 'POST':
        title = request.form.get('title')
        slug = request.form.get('slug') or title.lower().replace(' ', '-').replace('?', '').replace(',', '')
        category_id = request.form.get('category_id')
        question = request.form.get('question')
        what_protestants_believe = request.form.get('what_protestants_believe')
        short_answer = request.form.get('short_answer')
        catholic_teaching = request.form.get('catholic_teaching')
        biblical_evidence = request.form.get('biblical_evidence')
        objection = request.form.get('objection')
        catholic_response = request.form.get('catholic_response')
        early_church_evidence = request.form.get('early_church_evidence')
        catechism_text = request.form.get('catechism_text')
        historical_documents = request.form.get('historical_documents')
        conclusion = request.form.get('conclusion')
        status = request.form.get('status', 'Published')
        is_featured = True if request.form.get('is_featured') else False

        article = Article(
            title=title,
            slug=slug,
            category_id=category_id,
            question=question,
            what_protestants_believe=what_protestants_believe,
            short_answer=short_answer,
            catholic_teaching=catholic_teaching,
            biblical_evidence=biblical_evidence,
            objection=objection,
            catholic_response=catholic_response,
            early_church_evidence=early_church_evidence,
            catechism_text=catechism_text,
            historical_documents=historical_documents,
            conclusion=conclusion,
            status=status,
            is_featured=is_featured
        )
        db.session.add(article)
        db.session.commit()
        flash('Article created successfully!', 'success')
        return redirect(url_for('admin_articles'))

    return render_template('admin/article_form.html', article=None, categories=categories)

@app.route('/admin/article/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def admin_article_edit(id):
    article = Article.query.get_or_404(id)
    categories = Category.query.all()
    if request.method == 'POST':
        article.title = request.form.get('title')
        article.slug = request.form.get('slug')
        article.category_id = request.form.get('category_id')
        article.question = request.form.get('question')
        article.what_protestants_believe = request.form.get('what_protestants_believe')
        article.short_answer = request.form.get('short_answer')
        article.catholic_teaching = request.form.get('catholic_teaching')
        article.biblical_evidence = request.form.get('biblical_evidence')
        article.objection = request.form.get('objection')
        article.catholic_response = request.form.get('catholic_response')
        article.early_church_evidence = request.form.get('early_church_evidence')
        article.catechism_text = request.form.get('catechism_text')
        article.historical_documents = request.form.get('historical_documents')
        article.conclusion = request.form.get('conclusion')
        article.status = request.form.get('status')
        article.is_featured = True if request.form.get('is_featured') else False

        db.session.commit()
        flash('Article updated successfully!', 'success')
        return redirect(url_for('admin_articles'))

    return render_template('admin/article_form.html', article=article, categories=categories)

@app.route('/admin/article/<int:id>/delete', methods=['POST'])
@login_required
def admin_article_delete(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash('Article deleted successfully.', 'info')
    return redirect(url_for('admin_articles'))

@app.route('/admin/categories', methods=['GET', 'POST'])
@login_required
def admin_categories():
    if request.method == 'POST':
        name = request.form.get('name')
        slug = request.form.get('slug') or name.lower().replace(' ', '-')
        description = request.form.get('description')
        overview = request.form.get('overview')
        icon = request.form.get('icon', 'bi-book')

        cat = Category(name=name, slug=slug, description=description, overview=overview, icon=icon)
        db.session.add(cat)
        db.session.commit()
        flash('Category created successfully!', 'success')
        return redirect(url_for('admin_categories'))

    categories = Category.query.all()
    return render_template('admin/category_list.html', categories=categories)


# ==================== ASK AN APOLOGIST ROUTES ====================

@app.route('/ask-an-apologist', methods=['GET', 'POST'])
@login_required
def ask_apologist():
    # If logged in as Admin, redirect directly to Question Inbox to view & answer user questions
    if current_user.is_authenticated and getattr(current_user, 'is_admin', False) and request.args.get('view') != 'public' and request.method == 'GET':
        return redirect(url_for('admin_questions'))

    submitted_submission = None
    matched_articles = []
    
    if request.method == 'POST':
        user_name = request.form.get('user_name', '').strip()
        user_email = request.form.get('user_email', '').strip()
        category_id = request.form.get('category_id')
        question_title = request.form.get('question_title', '').strip()
        detailed_question = request.form.get('detailed_question', '').strip()

        if user_name and user_email and question_title and detailed_question:
            # Search database for instant answer synthesis
            query_terms = [t for t in (question_title + " " + detailed_question).split() if len(t) > 3]
            filters = []
            for term in query_terms[:5]:
                filters.append(Article.title.ilike(f"%{term}%"))
                filters.append(Article.question.ilike(f"%{term}%"))
                filters.append(Article.short_answer.ilike(f"%{term}%"))
            
            if filters:
                matched_articles = Article.query.filter(Article.status == 'Published', or_(*filters)).limit(3).all()

            ai_synthesis = ""
            if matched_articles:
                ai_synthesis = f"**Instant Research Synthesis from ARISE Vault:**\n\nBased on your query, we found {len(matched_articles)} primary theological defenses in our repository:\n\n"
                for art in matched_articles:
                    ai_synthesis += f"- **[{art.title}]({url_for('article_detail', slug=art.slug)})**: {art.short_answer[:220]}...\n\n"
            else:
                ai_synthesis = "Thank you for submitting your question! Our apologetics team will review your query and provide a detailed answer based on Sacred Scripture, Church Fathers, and Magisterial decrees."

            submission = QuestionSubmission(
                user_name=user_name,
                user_email=user_email,
                category_id=int(category_id) if category_id and category_id.isdigit() else None,
                question_title=question_title,
                detailed_question=detailed_question,
                status='Pending',
                ai_synthesized_answer=ai_synthesis
            )
            db.session.add(submission)
            db.session.commit()
            
            submitted_submission = submission
            flash('Your question has been submitted to the ARISE Apologetics Team! See instant evidence matches below.', 'success')

    categories = Category.query.all()
    answered_questions = QuestionSubmission.query.filter(
        QuestionSubmission.status.in_(['Answered', 'Published'])
    ).order_by(QuestionSubmission.answered_at.desc(), QuestionSubmission.created_at.desc()).all()

    return render_template(
        'ask_apologist.html',
        categories=categories,
        answered_questions=answered_questions,
        submitted_submission=submitted_submission,
        matched_articles=matched_articles
    )


@app.route('/api/instant-answer', methods=['POST'])
def api_instant_answer():
    data = request.get_json() or {}
    query = data.get('query', '').strip()
    if not query or len(query) < 3:
        return jsonify({"results": []})

    terms = [t for t in query.split() if len(t) > 2]
    filters = []
    for term in terms[:4]:
        filters.append(Article.title.ilike(f"%{term}%"))
        filters.append(Article.question.ilike(f"%{term}%"))
        filters.append(Article.short_answer.ilike(f"%{term}%"))
        filters.append(Article.catholic_teaching.ilike(f"%{term}%"))

    articles = Article.query.filter(Article.status == 'Published', or_(*filters)).limit(4).all()
    results = []
    for a in articles:
        results.append({
            "title": a.title,
            "slug": a.slug,
            "url": url_for('article_detail', slug=a.slug),
            "short_answer": a.short_answer[:160] + "..." if len(a.short_answer) > 160 else a.short_answer
        })

    return jsonify({"results": results})


@app.route('/admin/questions')
@login_required
def admin_questions():
    status_filter = request.args.get('status')
    if status_filter:
        questions = QuestionSubmission.query.filter_by(status=status_filter).order_by(QuestionSubmission.created_at.desc()).all()
    else:
        questions = QuestionSubmission.query.order_by(QuestionSubmission.created_at.desc()).all()
    
    return render_template('admin/question_inbox.html', questions=questions, current_status=status_filter)


@app.route('/admin/questions/<int:id>/answer', methods=['POST'])
@login_required
def admin_answer_question(id):
    question = QuestionSubmission.query.get_or_404(id)
    answer = request.form.get('official_answer', '').strip()
    status = request.form.get('status', 'Published')
    
    question.official_answer = answer
    question.status = status
    question.answered_at = datetime.utcnow()
    db.session.commit()
    
    flash('Question answered successfully!', 'success')
    return redirect(url_for('admin_questions'))


@app.route('/admin/questions/<int:id>/delete', methods=['POST'])
@login_required
def admin_delete_question(id):
    question = QuestionSubmission.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    flash('Question deleted successfully.', 'info')
    return redirect(url_for('admin_questions'))


# ==============================================================================
# COURSE PLATFORM PUBLIC ROUTES
# ==============================================================================

@app.route('/courses')
def courses():
    search_query = request.args.get('q', '').strip()
    difficulty_filter = request.args.get('difficulty', 'all').strip()
    category_filter = request.args.get('category', 'all').strip()

    query = Course.query.filter_by(status='Published')

    if search_query:
        query = query.filter(or_(
            Course.title.ilike(f'%{search_query}%'),
            Course.short_description.ilike(f'%{search_query}%'),
            Course.category_name.ilike(f'%{search_query}%')
        ))

    if difficulty_filter and difficulty_filter != 'all':
        query = query.filter_by(difficulty=difficulty_filter)

    if category_filter and category_filter != 'all':
        query = query.filter_by(category_name=category_filter)

    all_courses = query.order_by(Course.created_at.desc()).all()

    # User progress mapping if authenticated
    user_progress_map = {}
    if current_user.is_authenticated:
        enrollments = CourseProgress.query.filter_by(user_id=current_user.id).all()
        for e in enrollments:
            user_progress_map[e.course_id] = e.progress_percentage

    return render_template(
        'courses.html', 
        courses=all_courses, 
        user_progress_map=user_progress_map,
        search_query=search_query,
        difficulty_filter=difficulty_filter,
        category_filter=category_filter
    )


@app.route('/courses/<slug>')
def course_detail(slug):
    course = Course.query.filter_by(slug=slug, status='Published').first_or_404()
    
    total_lessons = len(course.lessons)

    user_course_progress = None
    completed_lesson_ids = set()
    first_uncompleted_lesson = None

    if current_user.is_authenticated:
        user_course_progress = CourseProgress.query.filter_by(user_id=current_user.id, course_id=course.id).first()
        progress_records = LessonProgress.query.filter_by(user_id=current_user.id, completed=True).all()
        completed_lesson_ids = set(pr.lesson_id for pr in progress_records)

    sorted_lessons = sorted(course.lessons, key=lambda l: l.lesson_number)
    for les in sorted_lessons:
        if les.id not in completed_lesson_ids:
            first_uncompleted_lesson = les
            break

    if not first_uncompleted_lesson and sorted_lessons:
        first_uncompleted_lesson = sorted_lessons[0]

    return render_template(
        'course_detail.html',
        course=course,
        total_lessons=total_lessons,
        user_course_progress=user_course_progress,
        completed_lesson_ids=completed_lesson_ids,
        first_uncompleted_lesson=first_uncompleted_lesson
    )


@app.route('/courses/<course_slug>/lesson/<lesson_slug>')
def lesson_view(course_slug, lesson_slug):
    course = Course.query.filter_by(slug=course_slug, status='Published').first_or_404()
    lesson = Lesson.query.filter_by(course_id=course.id, slug=lesson_slug).first_or_404()

    ordered_lessons = sorted(course.lessons, key=lambda l: l.lesson_number)
    
    current_index = -1
    for idx, l in enumerate(ordered_lessons):
        if l.id == lesson.id:
            current_index = idx
            break

    prev_lesson = ordered_lessons[current_index - 1] if current_index > 0 else None
    next_lesson = ordered_lessons[current_index + 1] if current_index < len(ordered_lessons) - 1 else None

    is_completed = False
    quiz_attempt = None

    if current_user.is_authenticated:
        prog = LessonProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson.id).first()
        if prog:
            is_completed = prog.completed

        if lesson.quizzes:
            quiz_obj = lesson.quizzes[0]
            quiz_attempt = QuizAttempt.query.filter_by(user_id=current_user.id, quiz_id=quiz_obj.id).order_by(QuizAttempt.attempted_at.desc()).first()

        # Update last viewed lesson in CourseProgress
        cp = CourseProgress.query.filter_by(user_id=current_user.id, course_id=course.id).first()
        if not cp:
            cp = CourseProgress(user_id=current_user.id, course_id=course.id, progress_percentage=0)
            db.session.add(cp)
        cp.last_lesson_id = lesson.id
        db.session.commit()

    return render_template(
        'lesson_view.html',
        course=course,
        lesson=lesson,
        prev_lesson=prev_lesson,
        next_lesson=next_lesson,
        is_completed=is_completed,
        quiz_attempt=quiz_attempt
    )


@app.route('/courses/<course_slug>/lesson/<lesson_slug>/mark-complete', methods=['POST'])
@login_required
def mark_lesson_complete(course_slug, lesson_slug):
    course = Course.query.filter_by(slug=course_slug).first_or_404()
    lesson = Lesson.query.filter_by(course_id=course.id, slug=lesson_slug).first_or_404()

    prog = LessonProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson.id).first()
    if not prog:
        prog = LessonProgress(user_id=current_user.id, lesson_id=lesson.id)
        db.session.add(prog)

    prog.completed = True
    prog.completed_at = datetime.utcnow()
    db.session.commit()

    # Recalculate CourseProgress
    total_lessons = len(course.lessons)
    if total_lessons > 0:
        completed_count = LessonProgress.query.filter(
            LessonProgress.user_id == current_user.id,
            LessonProgress.lesson_id.in_([l.id for l in course.lessons]),
            LessonProgress.completed == True
        ).count()

        percent = int((completed_count / total_lessons) * 100)
        
        cp = CourseProgress.query.filter_by(user_id=current_user.id, course_id=course.id).first()
        if not cp:
            cp = CourseProgress(user_id=current_user.id, course_id=course.id)
            db.session.add(cp)

        cp.progress_percentage = percent
        if percent >= 100:
            cp.completed = True
            cp.completed_at = datetime.utcnow()

        db.session.commit()

    flash(f"Lesson '{lesson.title}' marked as complete!", "success")

    ordered_lessons = sorted(course.lessons, key=lambda l: l.lesson_number)
    next_les = None
    for idx, l in enumerate(ordered_lessons):
        if l.id == lesson.id and idx < len(ordered_lessons) - 1:
            next_les = ordered_lessons[idx + 1]
            break

    if next_les:
        return redirect(url_for('lesson_view', course_slug=course.slug, lesson_slug=next_les.slug))
    
    if course.final_assessments:
        return redirect(url_for('take_final_assessment', course_slug=course.slug))
    
    return redirect(url_for('course_detail', slug=course.slug))


@app.route('/courses/<course_slug>/lesson/<lesson_slug>/quiz-submit', methods=['POST'])
@login_required
def quiz_submit(course_slug, lesson_slug):
    course = Course.query.filter_by(slug=course_slug).first_or_404()
    lesson = Lesson.query.filter_by(course_id=course.id, slug=lesson_slug).first_or_404()

    if not lesson.quizzes:
        return jsonify({'error': 'No quiz available for this lesson'}), 400

    quiz = lesson.quizzes[0]
    total_questions = len(quiz.questions)
    if total_questions == 0:
        return jsonify({'score': 100, 'passed': True})

    correct_count = 0
    feedback = {}

    for question in quiz.questions:
        selected_option_id = request.form.get(f'question_{question.id}')
        is_correct = False

        correct_option = QuizOption.query.filter_by(question_id=question.id, is_correct=True).first()
        correct_option_id = correct_option.id if correct_option else None

        if selected_option_id and correct_option_id and int(selected_option_id) == correct_option_id:
            correct_count += 1
            is_correct = True

        feedback[question.id] = {
            'is_correct': is_correct,
            'correct_option_id': correct_option_id,
            'explanation': question.explanation or ''
        }

    score_percentage = int((correct_count / total_questions) * 100)
    passed = (score_percentage >= quiz.passing_percentage)

    attempt = QuizAttempt(
        user_id=current_user.id,
        quiz_id=quiz.id,
        score_percentage=score_percentage,
        passed=passed,
        attempted_at=datetime.utcnow()
    )
    db.session.add(attempt)

    if passed:
        prog = LessonProgress.query.filter_by(user_id=current_user.id, lesson_id=lesson.id).first()
        if not prog:
            prog = LessonProgress(user_id=current_user.id, lesson_id=lesson.id)
            db.session.add(prog)

        prog.quiz_passed = True
        prog.completed = True
        prog.completed_at = datetime.utcnow()

    db.session.commit()

    total_lessons = len(course.lessons)
    if total_lessons > 0:
        completed_count = LessonProgress.query.filter(
            LessonProgress.user_id == current_user.id,
            LessonProgress.lesson_id.in_([l.id for l in course.lessons]),
            LessonProgress.completed == True
        ).count()

        percent = int((completed_count / total_lessons) * 100)
        cp = CourseProgress.query.filter_by(user_id=current_user.id, course_id=course.id).first()
        if not cp:
            cp = CourseProgress(user_id=current_user.id, course_id=course.id)
            db.session.add(cp)

        cp.progress_percentage = percent
        if percent >= 100:
            cp.completed = True
            cp.completed_at = datetime.utcnow()

        db.session.commit()

    return jsonify({
        'score': score_percentage,
        'passed': passed,
        'passing_percentage': quiz.passing_percentage,
        'feedback': feedback
    })


@app.route('/courses/<course_slug>/assessment', methods=['GET', 'POST'])
@login_required
def take_final_assessment(course_slug):
    course = Course.query.filter_by(slug=course_slug, status='Published').first_or_404()
    
    if not course.final_assessments:
        flash("No final assessment configured for this course yet.", "info")
        return redirect(url_for('course_detail', slug=course.slug))

    assessment = course.final_assessments[0]

    if request.method == 'POST':
        total_questions = len(assessment.questions)
        correct_count = 0

        for question in assessment.questions:
            selected_opt_id = request.form.get(f'question_{question.id}')
            correct_opt = FinalAssessmentOption.query.filter_by(question_id=question.id, is_correct=True).first()

            if selected_opt_id and correct_opt and int(selected_opt_id) == correct_opt.id:
                correct_count += 1

        score_percentage = int((correct_count / total_questions) * 100) if total_questions > 0 else 100
        passed = (score_percentage >= assessment.passing_percentage)

        attempt = FinalAssessmentAttempt(
            user_id=current_user.id,
            assessment_id=assessment.id,
            score_percentage=score_percentage,
            passed=passed,
            attempted_at=datetime.utcnow()
        )
        db.session.add(attempt)
        db.session.commit()

        if passed:
            existing_cert = Certificate.query.filter_by(user_id=current_user.id, course_id=course.id).first()
            if not existing_cert:
                import random
                import string
                unique_hex = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
                cert_id = f"ARISE-2026-{unique_hex}"
                
                cert = Certificate(
                    certificate_id=cert_id,
                    user_id=current_user.id,
                    course_id=course.id,
                    student_name=current_user.username,
                    course_title=course.title,
                    completion_date=datetime.utcnow(),
                    instructor_signature=course.instructor_name or "Roshen D'silva, Founder"
                )
                db.session.add(cert)

            cp = CourseProgress.query.filter_by(user_id=current_user.id, course_id=course.id).first()
            if not cp:
                cp = CourseProgress(user_id=current_user.id, course_id=course.id)
                db.session.add(cp)

            cp.progress_percentage = 100
            cp.completed = True
            cp.completed_at = datetime.utcnow()
            db.session.commit()

            flash(f"Congratulations! You passed the assessment with {score_percentage}%!", "success")
            return redirect(url_for('view_certificate', course_slug=course.slug))
        else:
            flash(f"You scored {score_percentage}%. The passing threshold is {assessment.passing_percentage}%. Review the lessons and try again!", "warning")

    return render_template('final_assessment.html', course=course, assessment=assessment)


@app.route('/courses/<course_slug>/certificate')
@login_required
def view_certificate(course_slug):
    course = Course.query.filter_by(slug=course_slug).first_or_404()
    cert = Certificate.query.filter_by(user_id=current_user.id, course_id=course.id).first()

    if not cert:
        flash("You have not earned a certificate for this course yet. Complete all lessons and pass the final assessment!", "warning")
        return redirect(url_for('course_detail', slug=course.slug))

    return render_template('certificate.html', cert=cert, course=course)


@app.route('/certificate/verify/<certificate_id>')
def verify_certificate(certificate_id):
    cert = Certificate.query.filter_by(certificate_id=certificate_id.upper().strip()).first()
    return render_template('certificate_verify.html', cert=cert, queried_id=certificate_id)


@app.route('/my-learning')
@login_required
def my_learning():
    enrollments = CourseProgress.query.filter_by(user_id=current_user.id).all()
    certificates = Certificate.query.filter_by(user_id=current_user.id).order_by(Certificate.completion_date.desc()).all()
    return render_template('my_learning.html', enrollments=enrollments, certificates=certificates)


# ==============================================================================
# ADMIN COURSE MANAGEMENT ROUTES
# ==============================================================================

@app.route('/admin/courses')
@login_required
def admin_courses():
    if not current_user.is_admin:
        flash("Admin access required.", "danger")
        return redirect(url_for('index'))
    courses_list = Course.query.order_by(Course.created_at.desc()).all()
    return render_template('admin/admin_courses.html', courses=courses_list)


@app.route('/admin/courses/new', methods=['GET', 'POST'])
@login_required
def admin_course_new():
    if not current_user.is_admin:
        flash("Admin access required.", "danger")
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        slug = request.form.get('slug', '').strip() or title.lower().replace(' ', '-')
        short_description = request.form.get('short_description', '').strip()
        full_description = request.form.get('full_description', '').strip()
        thumbnail_icon = request.form.get('thumbnail_icon', 'bi-journal-bookmark-fill').strip()
        instructor_name = request.form.get('instructor_name', "ARISE Faculty").strip()
        difficulty = request.form.get('difficulty', 'Beginner').strip()
        category_name = request.form.get('category_name', 'Catholic Apologetics').strip()
        estimated_completion_time = request.form.get('estimated_completion_time', '3 Hours').strip()
        learning_objectives = request.form.get('learning_objectives', '').strip()
        status = request.form.get('status', 'Published').strip()

        new_course = Course(
            title=title,
            slug=slug,
            short_description=short_description,
            full_description=full_description,
            thumbnail_icon=thumbnail_icon,
            instructor_name=instructor_name,
            difficulty=difficulty,
            category_name=category_name,
            estimated_completion_time=estimated_completion_time,
            learning_objectives=learning_objectives,
            status=status
        )
        db.session.add(new_course)
        db.session.commit()

        flash(f"Course '{title}' created successfully!", "success")
        return redirect(url_for('admin_courses'))

    return render_template('admin/admin_course_edit.html', course=None)


@app.route('/admin/courses/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def admin_course_edit(id):
    if not current_user.is_admin:
        flash("Admin access required.", "danger")
        return redirect(url_for('index'))

    course = Course.query.get_or_404(id)

    if request.method == 'POST':
        course.title = request.form.get('title', '').strip()
        course.slug = request.form.get('slug', '').strip() or course.title.lower().replace(' ', '-')
        course.short_description = request.form.get('short_description', '').strip()
        course.full_description = request.form.get('full_description', '').strip()
        course.thumbnail_icon = request.form.get('thumbnail_icon', 'bi-journal-bookmark-fill').strip()
        course.instructor_name = request.form.get('instructor_name', "ARISE Faculty").strip()
        course.difficulty = request.form.get('difficulty', 'Beginner').strip()
        course.category_name = request.form.get('category_name', 'Catholic Apologetics').strip()
        course.estimated_completion_time = request.form.get('estimated_completion_time', '3 Hours').strip()
        course.learning_objectives = request.form.get('learning_objectives', '').strip()
        course.status = request.form.get('status', 'Published').strip()

        db.session.commit()
        flash(f"Course '{course.title}' updated successfully!", "success")
        return redirect(url_for('admin_courses'))

    return render_template('admin/admin_course_edit.html', course=course)


@app.route('/admin/courses/<int:id>/delete', methods=['POST'])
@login_required
def admin_course_delete(id):
    if not current_user.is_admin:
        flash("Admin access required.", "danger")
        return redirect(url_for('index'))

    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash(f"Course '{course.title}' deleted.", "info")
    return redirect(url_for('admin_courses'))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    print(f"Starting ARISE Catholic Apologetics Platform on http://127.0.0.1:{port}")
    app.run(host='127.0.0.1', port=port, debug=True)

