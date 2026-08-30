"""
Course Platform Database Seeder for ARISE Catholic Apologetics.
Seeds the initial 10-lesson demo course: "Understanding the Catholic Church"
with full modules, lessons, apologetics sections, sources, quizzes, and final assessment.
"""

import sys
import os

# Add root directory to sys.path
sys.path.append(r"c:\Users\joyce evangeline\OneDrive\Desktop\Apologetics")

from models import (
    db, Course, CourseModule, Lesson, LessonSource, Quiz, QuizQuestion, 
    QuizOption, FinalAssessment, FinalAssessmentQuestion, FinalAssessmentOption
)

def seed_courses_data(app):
    with app.app_context():
        # Check if course already exists
        existing_course = Course.query.filter_by(slug="understanding-the-catholic-church").first()
        if existing_course:
            print("Course 'Understanding the Catholic Church' already exists in database.", flush=True)
            return

        print("Seeding Course: 'Understanding the Catholic Church' into database...", flush=True)

        course = Course(
            title="Understanding the Catholic Church",
            slug="understanding-the-catholic-church",
            short_description="Learn the biblical, historical, and theological foundations of the Catholic Church and discover Catholic answers to common objections.",
            full_description=(
                "This foundational course guides you step-by-step through the biblical, patristic, and theological "
                "pillars of the Catholic Church. Discover why Jesus Christ established a visible, hierarchical Church, "
                "examine the Four Marks of the Church, understand the dynamic interplay of Scripture, Tradition, and Magisterium, "
                "and equip yourself with clear, charitable apologetic answers to common objections."
            ),
            thumbnail_icon="bi-bank",
            image_url="/static/images/course_catholic_church.jpg",
            instructor_name="Roshen D'silva & ARISE Theological Faculty",
            difficulty="Beginner",
            category_name="Catholic Apologetics",
            estimated_completion_time="3 Hours",
            learning_objectives=(
                "Explain why Jesus Christ established a visible, organized Church on St. Peter and the Apostles.\n"
                "Master the Four Marks of the Church: One, Holy, Catholic, and Apostolic.\n"
                "Understand how Scripture, Sacred Tradition, and the Magisterium form an inseparable tripod of divine truth.\n"
                "Defend Apostolic Succession and Petrine Authority using Scripture and early Church Fathers.\n"
                "Discover what the 1st and 2nd century Christians believed regarding liturgy, sacraments, and authority.\n"
                "Articulate clear, persuasive Catholic answers to popular Protestant and secular objections."
            ),
            status="Published",
            is_featured=True
        )
        db.session.add(course)
        db.session.commit()

        # ==============================================================================
        # MODULES & LESSONS DATA
        # ==============================================================================
        modules_data = [
            {
                "title": "Module 1: Christ and His Church",
                "description": "Examine the foundational identity of the Church established by Jesus Christ in the New Testament.",
                "order": 1,
                "lessons": [
                    {
                        "number": 1,
                        "title": "What Is the Catholic Church?",
                        "slug": "what-is-the-catholic-church",
                        "reading_time": "12 min",
                        "main_content": (
                            "### Introduction to Ecclesiology\n\n"
                            "The word **Catholic** comes from the Greek *Katholikon*, meaning *'universal'* or *'according to the whole'*. "
                            "The Catholic Church is not merely one denomination among thousands; it is the original, visible, 2,000-year-old "
                            "Christian community founded directly by Jesus Christ in 33 AD.\n\n"
                            "### The Mystical Body of Christ\n\n"
                            "Scripture reveals that the Church is not a human institution or a loose alliance of independent believers, "
                            "but the living **Mystical Body of Christ** (1 Cor 12:27, Eph 1:22-23). Christ is the Head, and baptized believers "
                            "are His living members. Because Christ is indivisible, His Church is fundamentally one and undivided."
                        ),
                        "catholic_claim": "The Catholic Church is the visible, universal family of God established by Jesus Christ to preserve divine revelation without error.",
                        "biblical_evidence": (
                            "### Key Biblical Passages\n\n"
                            "1. **Matthew 16:18**: *'And I tell you, you are Peter, and on this rock I will build my church, and the powers of death shall not prevail against it.'*\n"
                            "2. **1 Timothy 3:15**: *'the household of God, which is the church of the living God, the pillar and bulwark of the truth.'*\n"
                            "3. **Ephesians 5:25**: *'Christ loved the church and gave himself up for her.'*"
                        ),
                        "historical_evidence": (
                            "### The Witness of St. Ignatius of Antioch (110 AD)\n\n"
                            "> *'Wherever the bishop shall appear, there let the multitude also be; even as, wherever Jesus Christ is, there is the Catholic Church.'*  \n"
                            "— **Letter to the Smyrnaeans**, Chapter 8"
                        ),
                        "catholic_teaching": "CCC 751: The word 'Church' (Latin *ecclesia*, from the Greek *ek-kalein*, to 'call out of') means a convocation or assembly.",
                        "common_objection": "Critics claim that the 'true Church' is purely invisible, consisting of all true believers across all denominations.",
                        "catholic_response": (
                            "While all baptized Christians share an imperfect communion with the Church, Jesus established a **visible** community. "
                            "He compared the Church to a city set on a hill (Matt 5:14) and commanded believers to submit disputes to the visible Church (Matt 18:17). "
                            "An invisible church cannot settle doctrinal disputes or exercise binding discipline!"
                        ),
                        "further_reading": "Catechism of the Catholic Church (CCC 748–810); Vatican II Dogmatic Constitution *Lumen Gentium*.",
                        "sources": [
                            {"title": "Catechism of the Catholic Church", "author": "Holy See", "date_period": "1992", "work_document": "CCC 748-810", "section_ref": "Paragraphs 748-810", "type": "Catechism"},
                            {"title": "Letter to the Smyrnaeans", "author": "St. Ignatius of Antioch", "date_period": "110 AD", "work_document": "Chapter 8", "section_ref": "8.2", "type": "Church Father"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "What does the Greek word 'Katholikon' (Catholic) mean?",
                                    "type": "multiple_choice",
                                    "explanation": "'Katholikon' comes from Greek roots meaning 'universal' or 'according to the whole'.",
                                    "options": [
                                        {"text": "Roman", "correct": False},
                                        {"text": "Universal or According to the Whole", "correct": True},
                                        {"text": "Medieval", "correct": False},
                                        {"text": "Western", "correct": False}
                                    ]
                                },
                                {
                                    "text": "What does 1 Timothy 3:15 explicitly call the Church?",
                                    "type": "multiple_choice",
                                    "explanation": "St. Paul explicitly terms the living Church 'the pillar and bulwark of the truth'.",
                                    "options": [
                                        {"text": "A human tradition", "correct": False},
                                        {"text": "The pillar and bulwark of the truth", "correct": True},
                                        {"text": "An invisible suggestion", "correct": False},
                                        {"text": "A fallen institution", "correct": False}
                                    ]
                                },
                                {
                                    "text": "Who was the first Church Father to write the exact phrase 'Catholic Church' in 110 AD?",
                                    "type": "multiple_choice",
                                    "explanation": "St. Ignatius of Antioch wrote 'wherever Jesus Christ is, there is the Catholic Church' in his Letter to the Smyrnaeans (110 AD).",
                                    "options": [
                                        {"text": "St. Augustine", "correct": False},
                                        {"text": "St. Ignatius of Antioch", "correct": True},
                                        {"text": "St. Jerome", "correct": False},
                                        {"text": "Martin Luther", "correct": False}
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "number": 2,
                        "title": "Did Jesus Establish a Church?",
                        "slug": "did-jesus-establish-a-church",
                        "reading_time": "10 min",
                        "main_content": (
                            "### The Intentional Foundation of Jesus\n\n"
                            "Some modern skeptics argue that Jesus was a simple apocalyptic preacher who never intended to found a structured religion. "
                            "However, the Gospels record that Jesus deliberately chose Twelve Apostles, gave them specific authority, ordained sacraments, "
                            "and solemnly promised: *'I will build my Church'* (Matt 16:18).\n\n"
                            "### The Kingdom and the Prime Minister\n\n"
                            "In establishing His Kingdom, Jesus fulfilled the Davidic Monarchy of the Old Testament. In the Kingdom of David, the king appointed "
                            "a chief minister who held the 'keys of the house of David' (Isaiah 22:22). Jesus conferred these exact keys upon Simon Peter."
                        ),
                        "catholic_claim": "Jesus Christ intentionally founded a visible, organized, enduring Church with pastoral authority.",
                        "biblical_evidence": (
                            "1. **Matthew 16:18–19**: Jesus promises to build His Church on Peter and gives him the keys of the kingdom.\n"
                            "2. **Luke 22:29–30**: Jesus confers royal covenant kingdom authority upon the Apostles.\n"
                            "3. **Matthew 28:19–20**: Jesus commissions the Church to make disciples of all nations until the end of time."
                        ),
                        "historical_evidence": "St. Clement of Rome (96 AD) records that the Apostles appointed bishops and deacons to succeed them by divine mandate.",
                        "catholic_teaching": "CCC 763: It was the Son's task to accomplish the Father's plan of salvation; to fulfill it, Christ inaugurated the Kingdom of heaven on earth.",
                        "common_objection": "Protestants object that Jesus only taught personal faith in Himself, not allegiance to an ecclesiastical institution.",
                        "catholic_response": "Belief in Jesus is inseparable from receiving the Church He sent! Jesus said: 'He who hears you hears me, and he who rejects you rejects me' (Luke 10:16).",
                        "further_reading": "CCC 763-766; St. Irenaeus *Against Heresies* Book III.",
                        "sources": [
                            {"title": "Catechism of the Catholic Church", "author": "Holy See", "date_period": "1992", "work_document": "CCC 763-766", "section_ref": "Paragraphs 763-766", "type": "Catechism"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "What Old Testament passage in Isaiah background-checks the conferral of the 'keys of the kingdom' in Matthew 16:19?",
                                    "type": "multiple_choice",
                                    "explanation": "Isaiah 22:22 details Eliakim receiving the keys of the house of David as prime minister.",
                                    "options": [
                                        {"text": "Genesis 1:1", "correct": False},
                                        {"text": "Isaiah 22:22", "correct": True},
                                        {"text": "Psalm 23:1", "correct": False},
                                        {"text": "Malachi 4:5", "correct": False}
                                    ]
                                },
                                {
                                    "text": "True or False: Jesus told His Apostles 'He who hears you hears me'.",
                                    "type": "true_false",
                                    "explanation": "Luke 10:16 explicitly connects hearing the Apostles with hearing Christ Himself.",
                                    "options": [
                                        {"text": "True", "correct": True},
                                        {"text": "False", "correct": False}
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "number": 3,
                        "title": "The Four Marks of the Church",
                        "slug": "the-four-marks-of-the-church",
                        "reading_time": "11 min",
                        "main_content": (
                            "### Identifying the True Church\n\n"
                            "Every Sunday Catholics recite the Nicene Creed (381 AD), professing belief in **Four Marks** of the Church: "
                            "**One, Holy, Catholic, and Apostolic**. These four attributes are essential signs by which the true Church of Christ "
                            "can be distinguished from all counterfeit human organizations.\n\n"
                            "### 1. ONE (*Unam*)\n"
                            "The Church is ONE in faith, sacraments, and governance. St. Paul writes: *'One body and one Spirit, one Lord, one faith, one baptism'* (Eph 4:4-5).\n\n"
                            "### 2. HOLY (*Sanctam*)\n"
                            "The Church is HOLY because her founder Jesus Christ is holy, her doctrine is holy, and her sacraments impart holiness.\n\n"
                            "### 3. CATHOLIC (*Catholicam*)\n"
                            "The Church is CATHOLIC because she possesses the fullness of truth and is sent to all nations across all times.\n\n"
                            "### 4. APOSTOLIC (*Apostolicam*)\n"
                            "The Church is APOSTOLIC because she is built on the foundation of the Apostles (Eph 2:20) through unbroken succession."
                        ),
                        "catholic_claim": "Only the Catholic Church fully possesses all four Marks established in the ancient Christian Creeds.",
                        "biblical_evidence": "Ephesians 4:4-5; John 17:21; Ephesians 2:20; Matthew 28:19.",
                        "historical_evidence": "The Council of Constantinople (381 AD) codified these four marks into the universal Nicene-Constantinopolitan Creed.",
                        "catholic_teaching": "CCC 811: 'This is the sole Church of Christ which in the Creed we profess to be one, holy, catholic and apostolic.'",
                        "common_objection": "Skeptics object that since members of the Catholic Church have sinned, the Church cannot be Holy.",
                        "catholic_response": "The Church is holy because of Christ, her divine origin and sacraments, not because all her earthly members are free from sin! The Church is a hospital for sinners.",
                        "further_reading": "CCC 811-870.",
                        "sources": [
                            {"title": "Nicene-Constantinopolitan Creed", "author": "Council of Constantinople", "date_period": "381 AD", "work_document": "Creed", "section_ref": "Article 9", "type": "Ecumenical Council"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "Which of the following is NOT one of the Four Marks of the Church?",
                                    "type": "multiple_choice",
                                    "explanation": "The Four Marks are One, Holy, Catholic, and Apostolic. 'National' is not a mark.",
                                    "options": [
                                        {"text": "One", "correct": False},
                                        {"text": "Holy", "correct": False},
                                        {"text": "National", "correct": True},
                                        {"text": "Apostolic", "correct": False}
                                    ]
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Module 2: Authority and Apostolic Succession",
                "description": "Understand the Three-Fold Pillar of Truth: Scripture, Tradition, and Magisterium.",
                "order": 2,
                "lessons": [
                    {
                        "number": 4,
                        "title": "Scripture, Tradition & Church Authority",
                        "slug": "scripture-tradition-and-church-authority",
                        "reading_time": "15 min",
                        "main_content": (
                            "### The Three-Fold Pillar of Truth\n\n"
                            "A three-legged stool stands firm on any surface, but remove one leg and it instantly collapses! "
                            "In Catholic theology, God's divine Revelation is protected by a **Three-Fold Pillar**:\n\n"
                            "1. **Sacred Scripture**: The written Word of God inspired by the Holy Spirit.\n"
                            "2. **Sacred Tradition**: The unwritten oral preaching and worship handed down by the Apostles.\n"
                            "3. **The Magisterium**: The living teaching authority of the Pope and Bishops.\n\n"
                            "### Refuting Sola Scriptura\n\n"
                            "Protestants rely on *Sola Scriptura* ('Scripture Alone'), claiming the Bible is the sole rule of faith. "
                            "However, Scripture nowhere teaches Sola Scriptura! St. Paul explicitly commands: *'Stand firm and hold to the traditions "
                            "which you were taught by us, either by word of mouth or by letter'* (2 Thess 2:15)."
                        ),
                        "catholic_claim": "Scripture, Tradition, and Magisterium work together under the Holy Spirit so that none can stand without the others.",
                        "biblical_evidence": "2 Thessalonians 2:15; 1 Timothy 3:15; 2 Peter 3:15-16.",
                        "historical_evidence": "St. Basil the Great (375 AD) testified that Apostolic oral tradition carries equal authority with written Scripture.",
                        "catholic_teaching": "CCC 95: Sacred Tradition, Sacred Scripture and the Magisterium are so connected that one cannot stand without the others.",
                        "common_objection": "Protestants cite 2 Timothy 3:16 ('All scripture is inspired...') to claim Scripture alone is sufficient.",
                        "catholic_response": "St. Paul says Scripture is 'profitable', NOT 'sufficient'! Water is profitable for life, but not sufficient without food and air.",
                        "further_reading": "Vatican II Dogmatic Constitution *Dei Verbum*.",
                        "sources": [
                            {"title": "Dei Verbum", "author": "Vatican II", "date_period": "1965", "work_document": "Dogmatic Constitution", "section_ref": "Chapter II", "type": "Magisterial Document"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "According to 2 Thessalonians 2:15, how did St. Paul command Christians to receive tradition?",
                                    "type": "multiple_choice",
                                    "explanation": "St. Paul explicitly mentions 'either by word of mouth OR by letter'.",
                                    "options": [
                                        {"text": "Only in written letters", "correct": False},
                                        {"text": "Either by word of mouth or by letter", "correct": True},
                                        {"text": "Only through private dreams", "correct": False},
                                        {"text": "Reject all tradition", "correct": False}
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "number": 5,
                        "title": "Apostolic Succession",
                        "slug": "apostolic-succession",
                        "reading_time": "12 min",
                        "main_content": (
                            "### Unbroken Lineage of Faith\n\n"
                            "Apostolic Succession is the doctrine that the spiritual authority given by Jesus Christ to the Twelve Apostles "
                            "has been handed down in an unbroken chain to Catholic bishops through the laying on of hands (ordination).\n\n"
                            "### Replacing Judas\n\n"
                            "When Judas died, the Apostles did not let his office vanish. In Acts 1:20, St. Peter quotes Psalm 109:8: "
                            "*'His office (Greek: Episkopen / Bishopric) let another take.'* Matthias was ordained to succeed Judas, demonstrating "
                            "that apostolic offices were designed to continue perpetually."
                        ),
                        "catholic_claim": "Catholic bishops are the direct canonical successors of the Apostles.",
                        "biblical_evidence": "Acts 1:20; 1 Timothy 4:14; 2 Timothy 2:2; Titus 1:5.",
                        "historical_evidence": "St. Irenaeus of Lyons (180 AD) listed the unbroken sequence of 12 Popes from St. Peter down to Pope Eleutherius of his own day.",
                        "catholic_teaching": "CCC 861: 'To make sure that the mission entrusted to them might be continued, the Apostles appointed successors.'",
                        "common_objection": "Skeptics claim that laying on of hands is merely a symbolic ritual without spiritual grace.",
                        "catholic_response": "St. Paul tells Timothy: 'rekindle the gift of God that is within you through the laying on of my hands' (2 Tim 1:6). Ordination imparts real sacramental grace!",
                        "further_reading": "CCC 861-865.",
                        "sources": [
                            {"title": "Against Heresies", "author": "St. Irenaeus of Lyons", "date_period": "180 AD", "work_document": "Book III, Chapter 3", "section_ref": "3.3.3", "type": "Church Father"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "What Greek word is used in Acts 1:20 when replacing Judas's office?",
                                    "type": "multiple_choice",
                                    "explanation": "Acts 1:20 uses 'Episkopen', meaning office of bishop / overseer.",
                                    "options": [
                                        {"text": "Episkopen (Bishopric)", "correct": True},
                                        {"text": "Diakonia", "correct": False},
                                        {"text": "Synagoga", "correct": False},
                                        {"text": "Kerygma", "correct": False}
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "number": 6,
                        "title": "Peter & the Papacy",
                        "slug": "peter-and-the-papacy",
                        "reading_time": "14 min",
                        "main_content": (
                            "### The Petrine Office\n\n"
                            "The Papacy is the earthly headship of the Catholic Church exercised by the Bishop of Rome as successor of St. Peter. "
                            "Jesus singles out Simon Peter above all other Apostles:\n\n"
                            "1. **Name Change**: Jesus renames Simon to *Petros* ('Rock', Matt 16:18).\n"
                            "2. **The Keys**: Jesus gives Peter the *'keys of the kingdom of heaven'* (Matt 16:19).\n"
                            "3. **Chief Shepherd**: Jesus commands Peter: *'Feed my lambs... Tend my sheep'* (John 21:15-17)."
                        ),
                        "catholic_claim": "The Pope is the earthly Vicar of Christ and supreme pastor of the universal Church.",
                        "biblical_evidence": "Matthew 16:18-19; Luke 22:31-32; John 21:15-17.",
                        "historical_evidence": "St. Cyprian of Carthage (251 AD) declared: 'On Peter He builds the Church, and to him He gives the command to feed the sheep.'",
                        "catholic_teaching": "CCC 882: The Pope, Bishop of Rome and Peter's successor, is the perpetual and visible source and foundation of unity.",
                        "common_objection": "Protestants claim that 'rock' in Matt 16:18 refers to Peter's faith, not Peter's person.",
                        "catholic_response": "Jesus spoke Aramaic (*Kepha*). He said: 'You are Kepha, and on this kepha I will build my church.' Peter is the rock personified by Christ!",
                        "further_reading": "CCC 880-892.",
                        "sources": [
                            {"title": "Catechism of the Catholic Church", "author": "Holy See", "date_period": "1992", "work_document": "CCC 880-892", "section_ref": "Paragraphs 880-892", "type": "Catechism"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "What Aramaic word did Jesus use for both Simon's new name and the rock in Matthew 16:18?",
                                    "type": "multiple_choice",
                                    "explanation": "In Aramaic, Jesus used the word 'Kepha' for both.",
                                    "options": [
                                        {"text": "Kepha", "correct": True},
                                        {"text": "Shalom", "correct": False},
                                        {"text": "Rabboni", "correct": False},
                                        {"text": "Hosanna", "correct": False}
                                    ]
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Module 3: The Faith of the Early Church",
                "description": "Discover patristic evidence proving that 1st-century Christians were Catholic in faith, liturgy, and practice.",
                "order": 3,
                "lessons": [
                    {
                        "number": 7,
                        "title": "What Did the First Christians Believe?",
                        "slug": "what-did-the-first-christians-believe",
                        "reading_time": "13 min",
                        "main_content": (
                            "### Uncovering Patristic Archaeology\n\n"
                            "Many Christians assume that early Christianity was a simple non-denominational movement that only became Catholic "
                            "in the 4th century under Emperor Constantine. However, ancient historical documents like the *Didache* (90 AD) and St. Justin Martyr's "
                            "*First Apology* (155 AD) prove that 1st and 2nd century Christians celebrated the Mass, confessed sins to priests, prayed for the dead, "
                            "and believed in the Real Presence of Christ in the Eucharist!"
                        ),
                        "catholic_claim": "The doctrine and worship of 1st-century Christians matches Catholic teaching, not Protestant theology.",
                        "biblical_evidence": "Acts 2:42; 1 Corinthians 10:16; James 5:14-15.",
                        "historical_evidence": "St. Justin Martyr (155 AD) describes Sunday Mass with liturgical readings, consecration of Eucharist, and distribution by deacons.",
                        "catholic_teaching": "CCC 1345: The liturgy of the Eucharist has retained its essential structure from the earliest centuries down to our day.",
                        "common_objection": "Protestants argue that Constantine invented Catholicism in 313 AD.",
                        "catholic_response": "Constantine legalized Christianity (Edict of Milan); he did not invent doctrine! The Church Fathers wrote explicitly Catholic theology centuries before Constantine was born.",
                        "further_reading": "The Didache; St. Justin Martyr's *First Apology*.",
                        "sources": [
                            {"title": "First Apology", "author": "St. Justin Martyr", "date_period": "155 AD", "work_document": "Chapters 65-67", "section_ref": "Chapter 66", "type": "Church Father"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "What early Christian document written c. 90 AD outlines 1st-century liturgical practices?",
                                    "type": "multiple_choice",
                                    "explanation": "The Didache (Teaching of the Twelve Apostles, c. 90 AD) records early liturgical and moral instructions.",
                                    "options": [
                                        {"text": "The Didache", "correct": True},
                                        {"text": "The Koran", "correct": False},
                                        {"text": "The Book of Mormon", "correct": False},
                                        {"text": "The Magna Carta", "correct": False}
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "number": 8,
                        "title": "The Seven Sacraments",
                        "slug": "the-seven-sacraments-overview",
                        "reading_time": "14 min",
                        "main_content": (
                            "### Channels of Sanctifying Grace\n\n"
                            "Sacraments are **efficacious signs of grace**, instituted by Christ and entrusted to the Church, by which divine life "
                            "is dispensed to us (CCC 1131). The Catholic Church celebrates **Seven Sacraments**:\n\n"
                            "1. **Baptism**: Rebirth by water and Spirit (John 3:5).\n"
                            "2. **Confirmation**: Sealing with the Holy Spirit (Acts 8:17).\n"
                            "3. **Holy Eucharist**: Real Body and Blood of Christ (John 6:53-56).\n"
                            "4. **Penance / Confession**: Forgiveness of sins (John 20:23).\n"
                            "5. **Anointing of the Sick**: Healing and forgiveness (James 5:14).\n"
                            "6. **Holy Orders**: Ordained priesthood (1 Tim 4:14).\n"
                            "7. **Holy Matrimony**: Sacramental union of man and woman (Eph 5:31-32)."
                        ),
                        "catholic_claim": "Christ instituted Seven Sacraments as physical, outward means of imparting inward grace.",
                        "biblical_evidence": "John 3:5; John 6:53; John 20:23; James 5:14; Ephesians 5:31.",
                        "historical_evidence": "The Council of Florence (1439 AD) and Council of Trent (1547 AD) dogmatically defined all seven sacraments against medieval heresies.",
                        "catholic_teaching": "CCC 1114: 'Adhering to the teaching of the Holy Scriptures, to the apostolic Traditions, and to the consensus of the Fathers, we profess that the sacraments of the new law were all instituted by Jesus Christ our Lord.'",
                        "common_objection": "Protestants object that sacraments are works-based righteousness.",
                        "catholic_response": "Sacraments act *ex opere operato* ('by the work worked') by Christ's merit on the Cross, not by human merit!",
                        "further_reading": "CCC 1113–1134.",
                        "sources": [
                            {"title": "Catechism of the Catholic Church", "author": "Holy See", "date_period": "1992", "work_document": "CCC 1113-1134", "section_ref": "Paragraphs 1113-1134", "type": "Catechism"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "How many Sacraments did Jesus Christ institute in the Catholic Church?",
                                    "type": "multiple_choice",
                                    "explanation": "The Catholic Church dogmatically confesses Seven Sacraments.",
                                    "options": [
                                        {"text": "2", "correct": False},
                                        {"text": "5", "correct": False},
                                        {"text": "7", "correct": True},
                                        {"text": "12", "correct": False}
                                    ]
                                }
                            ]
                        }
                    },
                    {
                        "number": 9,
                        "title": "Common Objections to Catholicism",
                        "slug": "common-objections-to-catholicism",
                        "reading_time": "15 min",
                        "main_content": (
                            "### Answering Objections with Charity & Clarity\n\n"
                            "St. Peter commands: *'Always be prepared to make a defense to any one who calls you to account for the hope that is in you, yet do it with gentleness and reverence'* (1 Peter 3:15).\n\n"
                            "### Objection 1: 'Catholics Worship Mary and Saints!'\n"
                            "**Catholic Response**: False! Catholic theology distinguishes between **Latria** (adoration/worship reserved for Almighty God alone) and **Dulia** (honor/veneration given to holy saints). Mary receives **Hyperdulia** (highest creaturely honor) as the Mother of God, but NEVER divine worship!\n\n"
                            "### Objection 2: 'Catholics Believe Works Save Them!'\n"
                            "**Catholic Response**: False! Initial justification is a 100% free, unmerited gift received in Baptism. Good works performed in grace are fruits of faith working through love (Gal 5:6, James 2:24)."
                        ),
                        "catholic_claim": "Catholic apologetics refutes misunderstandings with Scripture, patristic sources, and clear distinctions.",
                        "biblical_evidence": "1 Peter 3:15; James 2:24; Galatians 5:6; Revelation 5:8.",
                        "historical_evidence": "2nd-century catacomb wall inscriptions request intercession from St. Peter and St. Paul.",
                        "catholic_teaching": "CCC 2132: The Christian veneration of images is not contrary to the first commandment which proscribes idols.",
                        "common_objection": "Critics claim 1 Timothy 2:5 prohibits asking saints in heaven to pray for us.",
                        "catholic_response": "1 Tim 2:5 states Christ is sole Mediator of redemption. Asking saints in heaven to intercede is no more a violation than asking a friend on earth to pray for you!",
                        "further_reading": "CCC 2110-2132; St. Thomas Aquinas *Summa Theologiae*.",
                        "sources": [
                            {"title": "Summa Theologiae", "author": "St. Thomas Aquinas", "date_period": "1274 AD", "work_document": "ST II-II, q. 84", "section_ref": "Article 1", "type": "Academic"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "What theological term is used for adoration and worship reserved for God alone?",
                                    "type": "multiple_choice",
                                    "explanation": "Latria is adoration reserved exclusively for Almighty God.",
                                    "options": [
                                        {"text": "Latria", "correct": True},
                                        {"text": "Dulia", "correct": False},
                                        {"text": "Hyperdulia", "correct": False},
                                        {"text": "Koinonia", "correct": False}
                                    ]
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "title": "Module 4: Conclusion",
                "description": "Reflect on the fullness of truth found in Christ's Church.",
                "order": 4,
                "lessons": [
                    {
                        "number": 10,
                        "title": "Why Be Catholic?",
                        "slug": "why-be-catholic",
                        "reading_time": "10 min",
                        "main_content": (
                            "### The Fullness of Truth and Grace\n\n"
                            "Famed Catholic author G.K. Chesterton famously wrote: *'The difficulty of explaining why I am Catholic is that there are ten thousand reasons all amounting to one reason: that the Catholic Church is true.'*\n\n"
                            "To be Catholic is to enter into the fullness of Christian faith instituted by Jesus Christ. In the Catholic Church, you receive:\n\n"
                            "- **The Real Eucharistic Body of Christ** at every Mass.\n"
                            "- **The Unbroken Apostolic Succession** tracing back to St. Peter.\n"
                            "- **The Infallible Guidance of the Holy Spirit** protecting truth from confusion.\n"
                            "- **The Loving Intercession of Mary and All Saints**."
                        ),
                        "catholic_claim": "The Catholic Church alone retains the complete fullness of the means of salvation entrusted by Christ.",
                        "biblical_evidence": "John 17:21; John 6:53; Matthew 16:18; 1 Timothy 3:15.",
                        "historical_evidence": "2,000 years of martyrs, saints, doctors, and unbroken papal succession.",
                        "catholic_teaching": "CCC 816: 'The decree on Ecumenism of the Second Vatican Council explains: For it is through Christ's Catholic Church alone, which is the universal help toward salvation, that the fullness of the means of salvation can be obtained.'",
                        "common_objection": "Some ask: 'Can't I just read my Bible at home and love Jesus without joining the Catholic Church?'",
                        "catholic_response": "Loving Jesus means obeying Jesus! Jesus established a Church, gave us the Sacraments, and commanded us to eat His Flesh. You cannot love the King while rejecting His Kingdom.",
                        "further_reading": "CCC 816-822; G.K. Chesterton *Why I am a Catholic*.",
                        "sources": [
                            {"title": "Unitatis Redintegratio", "author": "Vatican II", "date_period": "1964", "work_document": "Decree on Ecumenism", "section_ref": "Section 3", "type": "Magisterial Document"}
                        ],
                        "quiz": {
                            "questions": [
                                {
                                    "text": "True or False: According to Catholic teaching, the Catholic Church possesses the complete fullness of the means of salvation.",
                                    "type": "true_false",
                                    "explanation": "Catholic doctrine confesses that the Catholic Church retains the complete fullness of means of salvation entrusted by Christ.",
                                    "options": [
                                        {"text": "True", "correct": True},
                                        {"text": "False", "correct": False}
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        ]

        lesson_count = 0
        for mod_data in modules_data:
            module = CourseModule(
                course_id=course.id,
                title=mod_data["title"],
                description=mod_data["description"],
                order=mod_data["order"]
            )
            db.session.add(module)
            db.session.commit()

            for les_data in mod_data["lessons"]:
                lesson_count += 1
                lesson = Lesson(
                    course_id=course.id,
                    module_id=module.id,
                    title=les_data["title"],
                    slug=les_data["slug"],
                    lesson_number=les_data["number"],
                    order=les_data["number"],
                    estimated_reading_time=les_data["reading_time"],
                    main_content=les_data["main_content"],
                    catholic_claim=les_data.get("catholic_claim"),
                    biblical_evidence=les_data.get("biblical_evidence"),
                    historical_evidence=les_data.get("historical_evidence"),
                    catholic_teaching=les_data.get("catholic_teaching"),
                    common_objection=les_data.get("common_objection"),
                    catholic_response=les_data.get("catholic_response"),
                    further_reading=les_data.get("further_reading"),
                    status="Published"
                )
                db.session.add(lesson)
                db.session.commit()

                # Add Lesson Sources
                for s in les_data.get("sources", []):
                    ls = LessonSource(
                        lesson_id=lesson.id,
                        title=s["title"],
                        author=s["author"],
                        date_period=s["date_period"],
                        work_document=s["work_document"],
                        section_ref=s["section_ref"],
                        source_type=s["type"]
                    )
                    db.session.add(ls)

                # Add Quiz & Questions
                if "quiz" in les_data:
                    quiz = Quiz(
                        lesson_id=lesson.id,
                        title=f"Quiz: {lesson.title}",
                        passing_percentage=70
                    )
                    db.session.add(quiz)
                    db.session.commit()

                    q_order = 0
                    for q_data in les_data["quiz"]["questions"]:
                        q_order += 1
                        qq = QuizQuestion(
                            quiz_id=quiz.id,
                            question_text=q_data["text"],
                            question_type=q_data["type"],
                            explanation=q_data.get("explanation"),
                            order=q_order
                        )
                        db.session.add(qq)
                        db.session.commit()

                        for opt in q_data["options"]:
                            qo = QuizOption(
                                question_id=qq.id,
                                option_text=opt["text"],
                                is_correct=opt["correct"]
                            )
                            db.session.add(qo)

                db.session.commit()

        # ==============================================================================
        # FINAL ASSESSMENT DATA
        # ==============================================================================
        final_assessment = FinalAssessment(
            course_id=course.id,
            title="Understanding the Catholic Church — Final Comprehensive Assessment",
            description="Test your mastery across all 10 lessons. Score 70% or higher to earn your official Certificate of Completion.",
            passing_percentage=70,
            total_questions=10
        )
        db.session.add(final_assessment)
        db.session.commit()

        assessment_questions = [
            {
                "text": "What does the Greek word 'Katholikon' mean?",
                "options": [
                    {"text": "Universal / According to the Whole", "correct": True},
                    {"text": "Roman", "correct": False},
                    {"text": "Secret", "correct": False},
                    {"text": "Reformed", "correct": False}
                ]
            },
            {
                "text": "What biblical verse explicitly calls the Church 'the pillar and bulwark of the truth'?",
                "options": [
                    {"text": "1 Timothy 3:15", "correct": True},
                    {"text": "John 3:16", "correct": False},
                    {"text": "Genesis 1:1", "correct": False},
                    {"text": "Revelation 22:20", "correct": False}
                ]
            },
            {
                "text": "Which Old Testament passage describes Eliakim receiving the keys of the royal house of David?",
                "options": [
                    {"text": "Isaiah 22:22", "correct": True},
                    {"text": "Exodus 20:3", "correct": False},
                    {"text": "Ezekiel 3:1", "correct": False},
                    {"text": "Leviticus 11:4", "correct": False}
                ]
            },
            {
                "text": "Which of the following is NOT one of the Four Marks of the Church?",
                "options": [
                    {"text": "National", "correct": True},
                    {"text": "One", "correct": False},
                    {"text": "Holy", "correct": False},
                    {"text": "Apostolic", "correct": False}
                ]
            },
            {
                "text": "What is the Three-Fold Pillar of Truth in Catholic theology?",
                "options": [
                    {"text": "Sacred Scripture, Sacred Tradition, and Magisterium", "correct": True},
                    {"text": "Faith Alone, Grace Alone, Scripture Alone", "correct": False},
                    {"text": "Reason, Logic, and Philosophy", "correct": False},
                    {"text": "Government, Law, and Monarchy", "correct": False}
                ]
            },
            {
                "text": "What Greek word in Acts 1:20 describes the office of bishop when replacing Judas?",
                "options": [
                    {"text": "Episkopen", "correct": True},
                    {"text": "Diakonia", "correct": False},
                    {"text": "Koinonia", "correct": False},
                    {"text": "Presbyteros", "correct": False}
                ]
            },
            {
                "text": "What Aramaic word did Jesus use when renaming Simon in Matthew 16:18?",
                "options": [
                    {"text": "Kepha", "correct": True},
                    {"text": "Abba", "correct": False},
                    {"text": "Maranatha", "correct": False},
                    {"text": "Boanerges", "correct": False}
                ]
            },
            {
                "text": "What early Christian document (c. 90 AD) outlines early Eucharistic and baptismal liturgy?",
                "options": [
                    {"text": "The Didache", "correct": True},
                    {"text": "The Vulgate", "correct": False},
                    {"text": "Summa Theologiae", "correct": False},
                    {"text": "Confessions", "correct": False}
                ]
            },
            {
                "text": "What is the difference between Latria and Dulia?",
                "options": [
                    {"text": "Latria is divine worship for God alone; Dulia is honor for saints", "correct": True},
                    {"text": "Latria is for Mary; Dulia is for God", "correct": False},
                    {"text": "Both mean idol worship", "correct": False},
                    {"text": "There is no difference", "correct": False}
                ]
            },
            {
                "text": "How many Sacraments were instituted by Jesus Christ?",
                "options": [
                    {"text": "7", "correct": True},
                    {"text": "2", "correct": False},
                    {"text": "10", "correct": False},
                    {"text": "1", "correct": False}
                ]
            }
        ]

        fq_order = 0
        for fq_data in assessment_questions:
            fq_order += 1
            fq = FinalAssessmentQuestion(
                assessment_id=final_assessment.id,
                question_text=fq_data["text"],
                question_type="multiple_choice",
                order=fq_order
            )
            db.session.add(fq)
            db.session.commit()

            for opt in fq_data["options"]:
                fo = FinalAssessmentOption(
                    question_id=fq.id,
                    option_text=opt["text"],
                    is_correct=opt["correct"]
                )
                db.session.add(fo)
        
        db.session.commit()
        print("SUCCESSFULLY seeded 10-lesson demo course 'Understanding the Catholic Church'!", flush=True)

if __name__ == "__main__":
    from app import app
    seed_courses_data(app)
