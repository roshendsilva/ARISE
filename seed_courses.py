import os
import sys

# Add root directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import db, Course, Lesson, Quiz, QuizQuestion

# 10 Lesson Configurations for Course 1: Understanding the Catholic Church
course_1_lessons = [
    {
        "lesson_number": 1,
        "title": "What Is the Catholic Church?",
        "slug": "what-is-the-catholic-church",
        "objectives": "- Define the theological essence of the Church as the Mystical Body of Christ and Sacrament of Salvation.\n- Analyze the Greek term Ekklesia in Old Testament and New Testament ecclesiology.\n- Distinguish between the visible historical communion and her invisible spiritual reality.\n- Understand the organic relationship between Christ the Head and the Church as His Bride.",
        "reading_time": "40 mins"
    },
    {
        "lesson_number": 2,
        "title": "Did Jesus Christ Establish a Church?",
        "slug": "did-jesus-christ-establish-a-church",
        "objectives": "- Examine the Gospel evidence in Matthew 16:18 and Matthew 18:17 for Christ's founding of a visible Church.\n- Refute the modern myth that Jesus proclaimed the Kingdom while later centuries invented the Church.\n- Analyze the appointment, training, and commission of the Twelve Apostles as a visible governing college.\n- Evaluate Patristic testimony confirming Christ's direct establishment of the Catholic Church.",
        "reading_time": "45 mins"
    },
    {
        "lesson_number": 3,
        "title": "The Four Marks of the Church: One, Holy, Catholic and Apostolic",
        "slug": "the-four-marks-of-the-church",
        "objectives": "- Deconstruct the Nicene-Constantinopolitan Creed's four essential marks of the true Church.\n- Demonstrate how the Catholic Church alone historically possesses unity, holiness, catholicity, and apostolicity.\n- Address Protestant counter-claims regarding invisible unity and denominational fragmentation.\n- Explore the Patristic roots of the term 'Catholic' from St. Ignatius of Antioch (110 AD) onward.",
        "reading_time": "45 mins"
    },
    {
        "lesson_number": 4,
        "title": "Sacred Scripture, Sacred Tradition and the Authority of the Church",
        "slug": "sacred-scripture-sacred-tradition-and-church-authority",
        "objectives": "- Examine the Catholic 'Three-Legged Stool' of divine Revelation: Scripture, Tradition, and the Magisterium.\n- Provide a robust biblical and historical critique of the Protestant doctrine of Sola Scriptura.\n- Trace how the Canon of Sacred Scripture was solemnly defined and guarded by the Catholic Church.\n- Clarify the proper relationship between the written Word of God and the living Apostolic Tradition.",
        "reading_time": "50 mins"
    },
    {
        "lesson_number": 5,
        "title": "Apostolic Succession and the Continuity of the Church",
        "slug": "apostolic-succession-and-the-continuity-of-the-church",
        "objectives": "- Trace the biblical paradigm of ordained succession through the laying on of hands (Episcope).\n- Examine 1st and 2nd-century Patristic records (Clement of Rome, Irenaeus, Tertullian) verifying Episcopal succession.\n- Demonstrate how unbroken succession safeguards dogmatic truth and sacramental validity against heresy.\n- Refute theories of early apostasy or medieval corruption of Church authority.",
        "reading_time": "45 mins"
    },
    {
        "lesson_number": 6,
        "title": "Saint Peter, the Keys and the Papacy",
        "slug": "saint-peter-the-keys-and-the-papacy",
        "objectives": "- Analyze Matthew 16:18-19 in light of Isaiah 22:22 and the Davidic Royal Prime Minister (Al Habbayit).\n- Examine Peter's unique primacy across the New Testament (Petrine texts, leadership in Acts, Jerusalem Council).\n- Trace the early Roman Primacy from St. Clement (96 AD) and St. Ignatius to the Councils of Ephesus and Chalcedon.\n- Clarify Papal Infallibility as defined by Vatican I, refuting common anti-papal objections.",
        "reading_time": "50 mins"
    },
    {
        "lesson_number": 7,
        "title": "The Early Church: What Did the First Christians Believe?",
        "slug": "the-early-church-what-did-the-first-christians-believe",
        "objectives": "- Explore the liturgical, sacramental, and doctrinal life of 1st-3rd century Christians through primary documents.\n- Demonstrate that early Christian worship centered on the Real Presence in the Eucharist, baptismal regeneration, and episcopal structure.\n- Examine primary texts from the Didache, Justin Martyr, Irenaeus, and Hippolytus of Rome.\n- Refute myths claiming Constantine invented Catholic doctrines in 325 AD at Nicaea.",
        "reading_time": "45 mins"
    },
    {
        "lesson_number": 8,
        "title": "The Seven Sacraments and the Life of the Church",
        "slug": "the-seven-sacraments-and-the-life-of-the-church",
        "objectives": "- Define the sacramental economy as physical channels of Christ's sanctifying grace instituted by Him.\n- Categorize the Seven Sacraments into Initiation, Healing, and Service/Communion.\n- Defend the biblical and patristic necessity of sacraments against purely symbolic ordinance theories.\n- Explain how the sacraments sanctify every stage of human life from birth to death.",
        "reading_time": "45 mins"
    },
    {
        "lesson_number": 9,
        "title": "Common Objections to Catholicism and Catholic Responses",
        "slug": "common-objections-to-catholicism-and-catholic-responses",
        "objectives": "- Formulate charitable, biblically grounded responses to major Protestant, Orthodox, and secular objections.\n- Clarify Marian dogmas, intercession of saints, and veneration (Dulia) vs. worship (Latria).\n- Explain Catholic soteriology: Faith, Works, Grace, and Justification vs. Sola Fide.\n- Provide clear answers regarding Purgatory, Indulgences, and Priestly Celibacy.",
        "reading_time": "50 mins"
    },
    {
        "lesson_number": 10,
        "title": "Why Be Catholic? — Bringing the Evidence Together",
        "slug": "why-be-catholic-bringing-the-evidence-together",
        "objectives": "- Synthesize the cumulative biblical, historical, theological, and philosophical arguments for Catholicism.\n- Recognize the fullness of truth, grace, and sacraments preserved in the Catholic Church.\n- Understand the personal call to holiness, conversion, and active communion with Christ's Church.\n- Formulate a personal action plan for continuing apologetics study and faithful Catholic living.",
        "reading_time": "45 mins"
    }
]

def generate_lesson_content(title):
    intro_p = f"""The question of the Church lies at the absolute heart of divine Revelation and human history. In contemporary discussions surrounding religion, Christianity is frequently reduced to a subjective, individualized philosophy of life—a set of moral principles or personal spiritual feelings detached from any visible, authoritative institution. However, when we turn to the pages of Sacred Scripture, the witness of the early Church Fathers, and the two-thousand-year trajectory of historical Christianity, we discover a radically different reality. Jesus Christ did not merely impart a doctrine or leave behind a collection of inspired texts; He founded a visible, organized, sacramental society—the Catholic Church—and promised that the gates of hell would never prevail against it. This lesson provides an exhaustive, scholarly investigation into *{title}*, examining its profound biblical roots, patristic testimony, dogmatic definitions, and apologetic defense against historical and modern objections."""
    
    headings = [
        f"1. Theological Foundations and Biblical Precedents of {title}",
        f"2. The Historical Witness of the Early Church Fathers on {title}",
        f"3. Dogmatic Definitions and Magisterial Teaching on {title}",
        f"4. Addressing Protestant, Orthodox, and Secular Objections Regarding {title}",
        f"5. Philosophical and Practical Implications for the Christian Life",
        f"6. Synthesis and Defense of the Catholic Doctrine of {title}"
    ]
    
    body_text = ""
    for h in headings:
        body_text += f"\n\n## {h}\n\n"
        p1 = f"To understand the depth of Catholic teaching regarding {title.lower()}, one must first analyze the divine economy of salvation as revealed throughout Sacred Scripture. God has always dealt with humanity not as isolated individuals, but as a covenantal people. In the Old Testament, the Lord called Abraham, established the nation of Israel, gave them a priesthood, a sanctuary, a moral law, and a visible sacrificial liturgy. When the fullness of time had come (Galatians 4:4), the Eternal Son of God took on human flesh, not to dismantle the covenantal structure of God's interaction with mankind, but to elevate and fulfill it. The Greek word *Ekklesia*—used throughout the Septuagint to denote the assembly of the Lord's covenant people in the wilderness—was explicitly chosen by Jesus Christ to describe the new covenantal community He established upon Saint Peter (Matthew 16:18). This demonstrates an organic, divine continuity between the Israel of the Old Covenant and the Catholic Church of the New Covenant."
        p2 = f"Furthermore, Sacred Scripture reveals that the Church is not a mere human association or political entity, but the Mystical Body of Jesus Christ. As Saint Paul repeatedly emphasizes in his epistles (1 Corinthians 12:12-27, Ephesians 1:22-23, Colossians 1:18), Christ is the Head of the Church, and baptized believers are individual members of His Body. This profound reality means that the Church possesses both a visible, historical structure and an invisible, divine soul. Just as Jesus Christ is true God and true Man—possessing both a visible human nature and an invisible divine nature in one Divine Person—so too the Church, as the extension of the Incarnation in time and space, possesses a visible hierarchical structure (bishops, priests, deacons, sacraments, canon law) animated by the invisible, indwelling presence of the Holy Spirit. To attempt to separate the 'spiritual' Church from the 'institutional' Church is to commit a form of ecclesiological Nestorianism, dividing what God has joined together."
        p3 = f"The historical record of the early post-apostolic Church confirms that the first Christians possessed an unmistakably Catholic understanding of {title.lower()}. Saint Ignatius of Antioch, writing in 110 AD on his way to martyrdom in Rome, gives us the earliest surviving written record of the term 'Catholic Church' (*He Katholike Ekklesia*) in his *Letter to the Smyrnaeans*: 'Wherever the bishop shall appear, there let the multitude also be; even as, wherever Jesus Christ is, there is the Catholic Church.' For Ignatius and his contemporaries, catholicity was not an abstract ideal, but a tangible historical reality characterized by communion with the validly ordained bishop, adherence to the apostolic rule of faith, and celebration of the true Eucharist. Likewise, Saint Irenaeus of Lyons (c. 180 AD), in his monumental treatise *Against Heresies*, argued that truth is found exclusively in the Catholic Church because she alone preserves the unbroken succession of bishops from the Apostles."
        p4 = f"When evaluating opposing arguments, Catholic apologetics demonstrates that alternative models of the Church fail both biblical and historical scrutiny. The Protestant Reformation of the sixteenth century introduced the novel concept of an 'invisible church' composed of all true believers across fragmented denominational lines. However, this concept is entirely absent from the New Testament and the writings of the Church Fathers. A purely invisible church cannot resolve doctrinal disputes (Matthew 18:17), cannot serve as the 'pillar and bulwark of the truth' (1 Timothy 3:15), and cannot manifest the visible unity for which Christ prayed on the night before He died: 'That they may all be one... so that the world may believe that thou hast sent me' (John 17:21). The visible unity of the Catholic Church—governed by the successors of the Apostles under the Petrine primacy of the Bishop of Rome—stands as an enduring miracle and an inescapable witness to the divine origin of Christianity."
        p5 = f"In conclusion, the Catholic doctrine of {title.lower()} offers the only coherent synthesis of biblical prophecy, apostolic practice, patristic testimony, and historical continuity. By remaining in full communion with the Catholic Church, the faithful are not merely joining an earthly organization; they are entering into living communion with the Triune God, receiving the authentic, uncorrupted Gospel of Jesus Christ, and partaking in the very sacraments that communicate sanctifying grace unto eternal life. As Saint Augustine famously declared in the fourth century: 'I would not believe in the Gospel if the authority of the Catholic Church did not move me to do so' (*Against the Epistolam Manichaei*). The Church remains today what she has always been for two thousand years: the ark of salvation, the city set on a mountain, and the Bride of Christ."
        body_text += f"{p1}\n\n{p2}\n\n{p3}\n\n{p4}\n\n{p5}\n"

    return intro_p + body_text

takeaways_sample = """- **Divine Institution**: Jesus Christ explicitly founded a visible, organized covenantal Church (*Ekklesia*) upon the Apostles, appointing Saint Peter as the chief steward (*Matthew 16:18-19*).
- **The Mystical Body of Christ**: The Church is the organic extension of the Incarnation, possessing both a visible hierarchical structure and an invisible divine life (*1 Corinthians 12:12-27*).
- **Patristic Witness**: From the 1st century onward (St. Clement of Rome, St. Ignatius of Antioch, St. Irenaeus), early Christians identified the true Church by her episcopal succession, Eucharistic realism, and Roman primacy.
- **Refutation of Objections**: The Protestant theory of an 'invisible church' contradicts Scripture (*1 Timothy 3:15*) and historical reality, whereas the Catholic Church preserves unbroken continuity for 2,000 years.
- **Salvific Role**: The Catholic Church is the Universal Sacrament of Salvation, conveying Christ's truth and sanctifying grace through the Sacraments."""

scripture_sample = """1. **Matthew 16:18-19**: *"And I tell you, you are Peter, and on this rock I will build my church, and the powers of death shall not prevail against it. I will give you the keys of the kingdom of heaven..."*
2. **1 Timothy 3:15**: *"...the household of God, which is the church of the living God, the pillar and bulwark of the truth."*
3. **Ephesians 1:22-23**: *"And he has put all things under his feet and has made him the head over all things for the church, which is his body, the fullness of him who fills all in all."*
4. **John 17:21**: *"That they may all be one; even as thou, Father, art in me, and I in thee, that they also may be in us, so that the world may believe that thou hast sent me."*
5. **Acts 2:42**: *"And they devoted themselves to the apostles' teaching and fellowship, to the breaking of bread and the prayers."*"""

sources_sample = """1. **Catechism of the Catholic Church**: Paragraphs 748-870 (*The Church in God's Plan, The Four Marks, The Hierarchical Constitution*).
2. **Vatican Council II**: Dogmatic Constitution on the Church (*Lumen Gentium*), 1964.
3. **St. Ignatius of Antioch**: *Letter to the Smyrnaeans* & *Letter to the Trallians*, c. 110 AD.
4. **St. Irenaeus of Lyons**: *Against Heresies* (*Adversus Haereses*), Book III, c. 180 AD.
5. **St. Cyprian of Carthage**: *On the Unity of the Catholic Church* (*De Ecclesiae Catholicae Unitate*), 251 AD.
6. **Heinrich Denzinger**: *Enchiridion Symbolorum* (Compendium of Creeds, Definitions, and Declarations on Matters of Faith and Morals)."""

quiz_questions_sample = [
    {
        "question": "According to Catholic ecclesiology and New Testament scripture, what is the primary nature of the Church established by Christ?",
        "options": {"A": "A purely invisible spiritual fellowship of all believers", "B": "The Mystical Body of Christ and visible Sacrament of Salvation", "C": "A human political association created in 325 AD", "D": "A temporary collection of independent congregations"},
        "correct": "B",
        "explanation": "The Catholic Church is both the visible hierarchical assembly established by Christ upon the Apostles and the invisible Mystical Body of Christ animated by the Holy Spirit (CCC 771-773, 1 Cor 12:12-27)."
    },
    {
        "question": "What does the Greek word Ekklesia mean in the Septuagint Old Testament and New Testament contexts?",
        "options": {"A": "A private philosophical club", "B": "The solemn assembly of God's covenant people called out by the Lord", "C": "A secret political organization", "D": "A non-binding voluntary society"},
        "correct": "B",
        "explanation": "Ekklesia means the assembly of the Lord's covenant people. Christ chose this word in Matthew 16:18 to show that His Church is the fulfillment of Israel's covenantal assembly."
    },
    {
        "question": "Who was the first Church Father to use the written term 'Catholic Church' (He Katholike Ekklesia) in 110 AD?",
        "options": {"A": "St. Augustine of Hippo", "B": "St. Ignatius of Antioch", "C": "St. Jerome", "D": "St. Thomas Aquinas"},
        "correct": "B",
        "explanation": "St. Ignatius of Antioch wrote in his Letter to the Smyrnaeans (c. 110 AD): 'Wherever the bishop shall appear, there let the multitude also be; even as, wherever Jesus Christ is, there is the Catholic Church.'"
    },
    {
        "question": "How does 1 Timothy 3:15 describe the Church of the living God?",
        "options": {"A": "As a secondary human organization", "B": "As the pillar and bulwark of the truth", "C": "As an invisible collection of varying opinions", "D": "As an obsolete Old Testament structure"},
        "correct": "B",
        "explanation": "1 Timothy 3:15 explicitly calls the Church 'the household of God, which is the church of the living God, the pillar and bulwark of the truth.'"
    },
    {
        "question": "Why does the Protestant concept of a purely 'invisible church' fail biblical and historical scrutiny?",
        "options": {"A": "Because Scripture commands believers to bring disputes to a visible Church (Matt 18:17) and maintain visible unity (John 17:21)", "B": "Because the Apostles never taught any doctrines", "C": "Because the early Church Fathers did not write books", "D": "Because invisible entities are easy to manage"},
        "correct": "A",
        "explanation": "A purely invisible church cannot judge disputes (Matt 18:17), possess visible apostolic succession, or demonstrate the visible oneness prayed for by Christ in John 17:21."
    }
]

def seed_courses():
    try:
        print("Starting Reusable Arise Course Platform Seeding...", flush=True)

        course = Course.query.filter_by(slug="understanding-the-catholic-church").first()
        if not course:
            course = Course(
                title="Understanding the Catholic Church",
                slug="understanding-the-catholic-church",
                description="A comprehensive, 10-lesson masterclass exploring the divine origin, biblical foundation, historical development, four marks, apostolic authority, sacramental life, and apologetic defense of the Catholic Church.",
                short_description="Master the biblical, historical, and theological foundation of the Catholic Church across 10 in-depth scholarly lessons.",
                thumbnail="images/logo.jpg",
                instructor="Roshen D'silva",
                category="Catholic Ecclesiology & Formation",
                difficulty="Intermediate to Advanced",
                estimated_duration="12 Hours",
                published=True
            )
            db.session.add(course)
            db.session.commit()
            print(f"Created Course: '{course.title}' (ID: {course.id})", flush=True)

        for l_cfg in course_1_lessons:
            lesson = Lesson.query.filter_by(course_id=course.id, slug=l_cfg["slug"]).first()
            if not lesson:
                content_text = generate_lesson_content(l_cfg["title"])
                lesson = Lesson(
                    course_id=course.id,
                    title=l_cfg["title"],
                    slug=l_cfg["slug"],
                    lesson_number=l_cfg["lesson_number"],
                    introduction=f"An in-depth investigation into {l_cfg['title']}.",
                    content=content_text,
                    learning_objectives=l_cfg["objectives"],
                    key_takeaways=takeaways_sample,
                    scripture_references=scripture_sample,
                    sources=sources_sample,
                    estimated_reading_time=l_cfg["reading_time"],
                    published=True
                )
                db.session.add(lesson)
                db.session.commit()
                print(f"  + Added Lesson #{lesson.lesson_number}: '{lesson.title}'", flush=True)

            # Seed Quiz & QuizQuestions
            quiz = Quiz.query.filter_by(lesson_id=lesson.id).first()
            if not quiz:
                quiz = Quiz(
                    lesson_id=lesson.id,
                    title=f"Quiz: {lesson.title}",
                    passing_score=70
                )
                db.session.add(quiz)
                db.session.commit()

                for q_item in quiz_questions_sample:
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
    except Exception as e:
        print(f"Course Seeding Exception Notice: {e}", flush=True)
