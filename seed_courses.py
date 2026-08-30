import os
import sys
import psycopg2
import urllib.parse

# Add root directory to sys.path
sys.path.append(r"c:\Users\joyce evangeline\OneDrive\Desktop\Apologetics")

from config import Config
from scratch.build_all_rich_articles import generate_lesson_1, generate_lesson_2, generate_lesson_3, generate_lesson_4, generate_lesson_5, generate_lesson_6, generate_lesson_7, generate_lesson_8, generate_lesson_9, generate_lesson_10

print("Updating Course Database Schema on Supabase PostgreSQL...", flush=True)

u = urllib.parse.urlparse(Config.SQLALCHEMY_DATABASE_URI)
password = urllib.parse.unquote(u.password) if u.password else "Roshen@2026"

conn = psycopg2.connect(
    dbname=u.path[1:].split('?')[0],
    user=u.username,
    password=password,
    host=u.hostname,
    port=6543,
    sslmode='require'
)
conn.autocommit = True
cursor = conn.cursor()

print("Dropping existing course tables if necessary...", flush=True)

cursor.execute("""
DROP TABLE IF EXISTS user_course_progress CASCADE;
DROP TABLE IF EXISTS user_lesson_progress CASCADE;
DROP TABLE IF EXISTS course_assessment_questions CASCADE;
DROP TABLE IF EXISTS lesson_quizzes CASCADE;
DROP TABLE IF EXISTS lessons CASCADE;
DROP TABLE IF EXISTS courses CASCADE;

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    slug VARCHAR(200) NOT NULL UNIQUE,
    description TEXT NOT NULL,
    overview TEXT,
    level VARCHAR(50) DEFAULT 'Beginner / Intermediate',
    is_published BOOLEAN DEFAULT TRUE,
    passing_score INT DEFAULT 70,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE,
    module_number INT DEFAULT 1,
    lesson_number INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    slug VARCHAR(200) NOT NULL UNIQUE,
    estimated_time VARCHAR(50) DEFAULT '45 mins',
    learning_objectives TEXT,
    content TEXT NOT NULL,
    key_points TEXT,
    reflection_questions TEXT,
    primary_sources TEXT,
    secondary_sources TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE lesson_quizzes (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_option VARCHAR(1) NOT NULL,
    explanation TEXT
);

CREATE TABLE course_assessment_questions (
    id SERIAL PRIMARY KEY,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_option VARCHAR(1) NOT NULL,
    explanation TEXT
);

CREATE TABLE user_lesson_progress (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    completed BOOLEAN DEFAULT FALSE,
    quiz_score INT,
    completed_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE user_course_progress (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE,
    is_completed BOOLEAN DEFAULT FALSE,
    final_score INT,
    certificate_id VARCHAR(64) UNIQUE,
    completed_at TIMESTAMP
);
""")

print("Database schema created successfully!", flush=True)

# Insert main course
cursor.execute("""
    INSERT INTO courses (title, slug, description, overview, level, is_published, passing_score)
    VALUES (
        'Understanding the Catholic Church',
        'understanding-the-catholic-church',
        'A rigorous 10-lesson formation course on ecclesiology, biblical authority, apostolic succession, papacy, early Church history, sacraments, and apologetic defense of the Catholic Faith.',
        '### Course Overview\n\nWelcome to **Understanding the Catholic Church**—an academic and faithful Catholic formation course designed to give believers and honest seekers a comprehensive mastery of Catholic doctrine, Church history, Sacred Scripture, and Sacred Tradition.\n\nEvery lesson provides long-form educational analysis, biblical exegesis, patristic testimony, magisterial definitions, and systematic responses to major objections.',
        'Beginner / Intermediate',
        TRUE,
        70
    ) RETURNING id;
""")
course_id = cursor.fetchone()[0]
print(f"Course ID: {course_id}", flush=True)

# Generate all 10 long-form lessons (4,000+ words each)
lessons_data = [
    generate_lesson_1(),
    generate_lesson_2(),
    generate_lesson_3(),
    generate_lesson_4(),
    generate_lesson_5(),
    generate_lesson_6(),
    generate_lesson_7(),
    generate_lesson_8(),
    generate_lesson_9(),
    generate_lesson_10(),
]

for l in lessons_data:
    cursor.execute("""
        INSERT INTO lessons (course_id, module_number, lesson_number, title, slug, estimated_time, learning_objectives, content, key_points, reflection_questions, primary_sources, secondary_sources)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """, (
        course_id, l["module_number"], l["lesson_number"], l["title"], l["slug"],
        l["estimated_time"], l["learning_objectives"], l["content"], l["key_points"],
        l["reflection_questions"], l["primary_sources"], l["secondary_sources"]
    ))
    lesson_id = cursor.fetchone()[0]

    # Populate 5 Quiz questions per lesson
    quizzes = l.get("quizzes", [])
    for q in quizzes:
        cursor.execute("""
            INSERT INTO lesson_quizzes (lesson_id, question, option_a, option_b, option_c, option_d, correct_option, explanation)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """, (
            lesson_id, q["question"], q["option_a"], q["option_b"], q["option_c"], q["option_d"],
            q["correct_option"], q["explanation"]
        ))

    print(f"Seeded Lesson {l['lesson_number']}: {l['title']} (Content length: {len(l['content'])} chars / ~{len(l['content'].split())} words)", flush=True)

# Seed 30 Final Assessment Questions for Course
final_questions = [
    {"question": "What is the Greek word 'Ekklesia' used in the Septuagint and New Testament to mean?", "option_a": "An informal fellowship", "option_b": "The assembly of God's covenant people called out", "option_c": "A physical temple building", "option_d": "A private prayer gathering", "correct_option": "B", "explanation": "Ekklesia signifies the assembly of God's covenant people called together by God."},
    {"question": "Which Church Father first used the term 'Catholic Church' in writing around 110 AD?", "option_a": "St. Clement of Rome", "option_b": "St. Justin Martyr", "option_c": "St. Ignatius of Antioch", "option_d": "St. Augustine", "correct_option": "C", "explanation": "St. Ignatius of Antioch wrote in Letter to the Smyrnaeans 8:2: 'Where Jesus Christ is, there is the Catholic Church.'"},
    {"question": "What does Matthew 16:18-19 reveal about Church leadership?", "option_a": "Jesus established no visible structure", "option_b": "Jesus gave Peter the keys of the Kingdom of Heaven and supreme authority to bind and loose", "option_c": "Jesus made all disciples equal in rank with no head", "option_d": "Jesus appointed John as chief apostle", "correct_option": "B", "explanation": "Jesus explicitly names Simon as Peter (Rock) and confers the keys of the kingdom and binding/loosing authority upon him."},
    {"question": "What Old Testament passage provides the royal dynastic background for the 'Keys of the Kingdom'?", "option_a": "Genesis 12:1-3", "option_b": "Isaiah 22:20-22", "option_c": "Exodus 20:1-17", "option_d": "Psalm 110:1-4", "correct_option": "B", "explanation": "Isaiah 22:20-22 describes Eliakim receiving the key of the house of David as chief steward/prime minister over the Davidic Kingdom."},
    {"question": "What are the Four Marks of the Church declared in the Nicene Creed (381 AD)?", "option_a": "Faithful, Loving, Pure, Universal", "option_b": "One, Holy, Catholic, Apostolic", "option_c": "Scriptural, Sacramental, Spiritual, Charitable", "option_d": "Global, Ancient, Traditional, Orthodox", "correct_option": "B", "explanation": "The Nicene-Constantinopolitan Creed solemnly professes: 'I believe in One, Holy, Catholic, and Apostolic Church.'"},
    {"question": "Which Latin phrase represents the Protestant doctrine that Scripture alone is the sole infallible rule of faith?", "option_a": "Sola Fide", "option_b": "Sola Scriptura", "option_c": "Sola Gratia", "option_d": "Solus Christus", "correct_option": "B", "explanation": "Sola Scriptura asserts that Scripture alone is the only infallible authority, rejecting Sacred Tradition and Magisterial authority."},
    {"question": "Which NT passage commands believers to hold fast to the traditions handed down, whether by word of mouth or by letter?", "option_a": "2 Thessalonians 2:15", "option_b": "Romans 3:28", "option_c": "Galatians 1:8", "option_d": "Hebrews 11:1", "correct_option": "A", "explanation": "2 Thessalonians 2:15 commands: 'Stand firm and hold to the traditions which you were taught by us, whether by word of mouth or by letter.'"},
    {"question": "What is the Catholic Magisterium?", "option_a": "The academic theology faculty", "option_b": "The living, teaching authority of the Church exercised by the Pope and Bishops in communion with him", "option_c": "A advisory committee of lay scholars", "option_d": "The private conscience of individual believers", "correct_option": "B", "explanation": "The Magisterium is the living teaching office of the Church entrusted with authentically interpreting the Word of God."},
    {"question": "How did the early Church determine the Canon of Sacred Scripture in the 4th century?", "option_a": "By individual private inspiration", "option_b": "Through Catholic regional councils at Rome (382), Hippo (393), and Carthage (397, 419)", "option_c": "The Bible fell fully bound from heaven", "option_d": "Emperor Constantine dictated the books at Nicaea", "correct_option": "B", "explanation": "The Catholic Church defined the 73-book canon of Scripture through regional councils under Pope St. Damasus I in the late 4th century."},
    {"question": "What is Apostolic Succession?", "option_a": "The unbroken lineage of validly ordained bishops extending from the Apostles to today", "option_b": "The belief that anyone reading the Bible succeeds the Apostles", "option_c": "A political succession of Christian emperors", "option_d": "The automatic inheritance of faith through bloodlines", "correct_option": "A", "explanation": "Apostolic succession is the continuous line of episcopal ordination handed down from the Apostles through the laying on of hands."},
    {"question": "Which early Church Father wrote 'Against Heresies' (c. 180 AD) giving the line of Roman Bishops from Peter to Eleutherius?", "option_a": "St. Irenaeus of Lyons", "option_b": "St. Cyprian of Carthage", "option_c": "St. Augustine", "option_d": "St. Athanasius", "correct_option": "A", "explanation": "St. Irenaeus traced the succession of Roman bishops to demonstrate apostolic truth against Gnostic heresies."},
    {"question": "What does 1 Timothy 4:14 teach regarding episcopal/priestly ordination?", "option_a": "Ordination occurs through popular election", "option_b": "Grace is conferred through the laying on of hands by the council of elders", "option_c": "Ordination is purely a human title without spiritual effect", "option_d": "Anyone can ordain themselves", "correct_option": "B", "explanation": "1 Timothy 4:14 speaks of the spiritual gift imparted through the laying on of hands (presbyterion)."},
    {"question": "What dogmatic definition of Papal Infallibility was solemnly defined at Vatican Council I (1870)?", "option_a": "The Pope can never make a moral mistake or sin", "option_b": "The Pope is infallible when defining ex cathedra a doctrine of faith or morals for the whole Church", "option_c": "Every opinion of the Pope is automatically infallible", "option_d": "The Pope acts as a secular ruler over nations", "correct_option": "B", "explanation": "Vatican I defined that when speaking ex cathedra as Pastor and Teacher of all Christians, the Pope possesses divine assistance in defining doctrine of faith or morals."},
    {"question": "What did St. Cyprian of Carthage teach regarding unity with Peter's See (c. 251 AD)?", "option_a": "The Chair of Peter is the source of Church unity", "option_b": "Rome has no special primacy among churches", "option_c": "The papacy was invented by Roman emperors", "option_d": "Churches should operate as isolated independent assemblies", "correct_option": "A", "explanation": "St. Cyprian affirmed in 'On the Unity of the Catholic Church' that Christ founded the Church upon Peter to manifest unity."},
    {"question": "Which early Christian document from c. 90-100 AD reflects liturgical instructions, baptism, and moral teaching?", "option_a": "The Didache (Teaching of the Twelve Apostles)", "option_b": "The Summa Theologiae", "option_c": "The Synod of Whitby", "option_d": "The Vulgate", "correct_option": "A", "explanation": "The Didache is one of the earliest post-apostolic writings detailing early Christian worship, baptism, and moral instruction."},
    {"question": "What does 1 Peter 3:21 explicitly say about Baptism?", "option_a": "Baptism is merely an outward symbol", "option_b": "Baptism now saves you, not as a removal of dirt but as an appeal to God for a good conscience", "option_c": "Baptism is unnecessary for salvation", "option_d": "Only adults may be baptized", "correct_option": "B", "explanation": "1 Peter 3:21 states: 'Baptism, which corresponds to this, now saves you.'"},
    {"question": "What does the Catholic Church teach regarding Transubstantiation in the Eucharist?", "option_a": "The bread and wine remain unchanged and are only symbolic", "option_b": "The whole substance of bread and wine is changed into the Body, Blood, Soul, and Divinity of Jesus Christ", "option_c": "Christ's body coexists alongside physical bread (Consubstantiation)", "option_d": "The Eucharist only becomes Christ inside the believer's mind", "correct_option": "B", "explanation": "Transubstantiation defined by Trent affirms the complete conversion of substance into the real Body and Blood of Christ while accidents remain."},
    {"question": "What NT passage establishes the Sacrament of Reconciliation / Penance?", "option_a": "John 20:21-23", "option_b": "Romans 10:9", "option_c": "1 Corinthians 13:1", "option_d": "Hebrews 11:6", "correct_option": "A", "explanation": "In John 20:22-23, Jesus breathed on the Apostles and said: 'If you forgive the sins of any, they are forgiven; if you withhold forgiveness, it is withheld.'"},
    {"question": "Which New Testament letter explicitly commands calling the presbyters/priests for the Anointing of the Sick?", "option_a": "James 5:14-15", "option_b": "1 Peter 5:1-2", "option_c": "Galatians 6:1", "option_d": "Revelation 22:1", "correct_option": "A", "explanation": "James 5:14-15: 'Is any among you sick? Let him call for the elders (presbyters) of the Church, and let them pray over him, anointing him with oil.'"},
    {"question": "What does the Catholic Church teach regarding the Sacrament of Matrimony?", "option_a": "It is a temporary legal contract dissolvable by civil divorce", "option_b": "It is a valid, indissoluble sacramental covenant instituted by God between one man and one woman", "option_c": "It was created in the Middle Ages for land ownership", "option_d": "It is inferior to non-sacramental union", "correct_option": "B", "explanation": "Catholic doctrine affirms that valid, consummated sacramental marriage is indissoluble, as taught by Christ in Matthew 19:6."},
    {"question": "Do Catholics worship Mary or the Saints?", "option_a": "Yes, Catholics worship saints as divine beings", "option_b": "No, Catholics offer Latria (worship) to God alone, and Dulia/Hyperdulia (veneration/honor) to Saints and Mary", "option_c": "Catholics consider Mary equal to God the Father", "option_d": "Catholics worship statues of saints", "correct_option": "B", "explanation": "Catholic theology makes a strict distinction between Latria (sacrificial adoration owed to God alone) and Dulia/Hyperdulia (honor and veneration)."},
    {"question": "What is the biblical basis for asking Saints in Heaven to pray for us (Intercession)?", "option_a": "Revelation 5:8 and 8:3-4 showing the prayers of the saints offered like incense before God", "option_b": "Statue worship in Leviticus", "option_c": "There is no biblical basis", "option_d": "Reincarnation passages", "correct_option": "A", "explanation": "Revelation 5:8 depicts the elders in heaven holding golden bowls of incense, which are the prayers of the holy ones (saints)."},
    {"question": "What is Purgatory according to Catholic teaching?", "option_a": "A second chance for unrepentant sinners in hell", "option_b": "The final purification of the elect before entering the perfection of Heaven", "option_c": "A place of permanent punishment created in the 12th century", "option_d": "An invention of Greek mythology", "correct_option": "B", "explanation": "CCC 1030 defines Purgatory as the final purification of those who die in God's grace and friendship to achieve the holiness necessary for heaven."},
    {"question": "What Old Testament passage demonstrates prayer and sacrifice for the deceased?", "option_a": "2 Maccabees 12:44-45", "option_b": "Genesis 1:1", "option_c": "Ecclesiastes 3:1", "option_d": "Job 1:1", "correct_option": "A", "explanation": "2 Maccabees 12:44-45 records Judas Maccabeus offering expiatory sacrifices for the fallen dead that they might be delivered from sin."},
    {"question": "Why is Mary called 'Theotokos' (Mother of God)?", "option_a": "Because she created the Divine nature of God", "option_b": "Because Jesus is one Divine Person with two natures, and Mary gave birth to Jesus who is true God", "option_c": "Because she is older than God", "option_d": "It is an unofficial popular title", "correct_option": "B", "explanation": "The Council of Ephesus (431 AD) defined Theotokos because Mary gave birth to the Divine Person of Jesus Christ."},
    {"question": "What does the Catholic doctrine of Justification teach regarding Faith and Works?", "option_a": "Salvation is earned by human good works without grace", "option_b": "Faith alone saves, works are completely irrelevant", "option_c": "Justification is by God's unmerited grace through faith working in love (Gal 5:6, James 2:24)", "option_d": "Salvation depends strictly on self-righteous ritualism", "correct_option": "C", "explanation": "As defined by Trent, justification begins by unmerited grace; faith working through love (Gal 5:6) fruits in good works (James 2:24)."},
    {"question": "Why does the Catholic Bible contain 73 books while Protestant Bibles contain 66?", "option_a": "Catholics added 7 books at the Council of Trent", "option_b": "Protestant reformers removed the 7 Deuterocanonical books (Septuagint canon) used by the Apostles", "option_c": "The Pope wrote 7 extra books in the 15th century", "option_d": "It was a typographical printing error", "correct_option": "B", "explanation": "The early Church adopted the Greek Septuagint Old Testament containing 46 books. 16th-century Reformers dropped the 7 Deuterocanonical books."},
    {"question": "What is the relationship between the Church and Jesus Christ according to Ephesians 5:25-32?", "option_a": "The Church is an optional social club", "option_b": "The Church is the Bride of Christ and His Mystical Body", "option_c": "The Church is a purely human organizational construct", "option_d": "The Church replaces Jesus Christ", "correct_option": "B", "explanation": "St. Paul teaches in Ephesians 5 that Christ loved the Church and gave Himself up for her, making her His Bride and Body."},
    {"question": "What is the ultimate purpose of Catholic Apologetics?", "option_a": "To win intellectual debates and mock non-Catholics", "option_b": "To proclaim Christ, clarify truth in charity, remove obstacles to faith, and lead souls to Christ's Church", "option_c": "To promote secular political power", "option_d": "To force people against their will", "correct_option": "B", "explanation": "Apologetics (1 Peter 3:15) defends Catholic truth with gentleness, reverence, and charity to lead hearts to Jesus Christ."},
    {"question": "Why should someone investigating Christianity seriously consider the Catholic Church?", "option_a": "Because it was founded by 16th-century reformers", "option_b": "Because it possesses 2,000 years of unbroken historical continuity, biblical fullness, and sacramental life instituted by Christ", "option_c": "Because it changes its doctrines according to modern popular culture", "option_d": "Because it has no central authority or doctrine", "correct_option": "B", "explanation": "The Catholic Church offers the fullness of Christian truth, apostolic succession, the 7 Sacraments, and unbroken continuity from Christ."}
]

for exam_q in final_questions:
    cursor.execute("""
        INSERT INTO course_assessment_questions (course_id, question, option_a, option_b, option_c, option_d, correct_option, explanation)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """, (
        course_id, exam_q["question"], exam_q["option_a"], exam_q["option_b"], exam_q["option_c"], exam_q["option_d"],
        exam_q["correct_option"], exam_q["explanation"]
    ))

print("Seeded 30 Final Assessment Questions for Course!", flush=True)

cursor.close()
conn.close()

print("SUCCESS: Finished seeding all 10 masterclass lessons and assessment questions into Supabase PostgreSQL!", flush=True)
