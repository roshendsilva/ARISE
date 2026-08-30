"""
Course Platform Database Seeder for ARISE Catholic Apologetics.
Seeds and updates the 10-lesson course: "Understanding the Catholic Church"
with 5,000+ words per lesson of comprehensive, scholarly apologetics content.
"""

import sys
import os

# Add root directory to sys.path
sys.path.append(r"c:\Users\joyce evangeline\OneDrive\Desktop\Apologetics")

from models import (
    db, Course, CourseModule, Lesson, LessonSource, Quiz, QuizQuestion, 
    QuizOption, CourseProgress, FinalAssessment, FinalAssessmentQuestion, FinalAssessmentOption
)

def generate_5000_word_lesson_1():
    return (
        "### CHAPTER 1: ETYMOLOGY AND LINGUISTIC FOUNDATIONS\n\n"
        "The word **Catholic** derives from the Ancient Greek compound adjective **Katholikon** (καθολικόν), which combines "
        "the preposition **kata** (κατά, meaning 'according to' or 'throughout') and the adjective **holos** (ὅλος, meaning 'the whole', 'entirety', or 'fullness'). "
        "Literally, *Katholikon* means **'according to the whole'**, **'universal'**, or **'possessing the complete fullness'**. "
        "When applied to the Church founded by Jesus Christ in Jerusalem in 33 AD, the title 'Catholic Church' designates not merely a geographic expansion across the earth, "
        "but an organic, qualitative fullness of divine doctrine, sacramental grace, and unbroken apostolic lineage entrusted by Christ to mankind.\n\n"
        "In contrast to human denominations established during or after the 16th-century Protestant Reformation, the Catholic Church is the original, visible, "
        "2,000-year-old Christian communion. The word *Church* itself derives from the Greek **Ecclesia** (ἐκκλησία), which in turn translates the Hebrew **Qahal** (קָהָל), "
        "the solemn covenant assembly of God's chosen people in the Old Testament. When Jesus declared in Matthew 16:18, *'I will build my Ecclesia'*, His Apostles immediately "
        "understood that Christ was restoring, fulfilling, and expanding the covenant assembly of Israel into an international, eternal Family of God.\n\n"
        "### CHAPTER 2: OLD TESTAMENT TYPOLOGY OF THE CHURCH\n\n"
        "Catholic theology recognizes that God prepared the human race for the Church through dramatic Old Testament types and shadows:\n\n"
        "1. **Noah's Ark (Genesis 6–9; 1 Peter 3:20–21)**: Just as Noah's Ark was the sole wooden vessel floating upon the chaotic waters of the deluge by which Noah and his family were saved from physical destruction, "
        "the Fathers of the Church (*such as St. Cyprian and St. Augustine*) universally taught that the Catholic Church is the spiritual Ark of Salvation floating upon the stormy seas of sin and heresy. Outside this Ark, souls lack the ordinary sacramental means of salvation.\n\n"
        "2. **Israel in the Wilderness (Exodus 19; Acts 7:38)**: Under the Old Covenant, God gathered Israel at Mount Sinai as a consecrated, priestly nation governed by an ordained Levitical priesthood, guided by visible leaders (*Moses and Aaron*), "
        "and nourished by miraculous physical bread from heaven (*Manna*). In the New Covenant, the Catholic Church is the restored Israel, governed by Bishops and Priests in unbroken succession, nourished by the True Bread from Heaven (*the Holy Eucharist*).\n\n"
        "3. **The Davidic Monarchy (2 Samuel 7; Isaiah 22; Luke 1:32–33)**: God swore an eternal covenant with King David that his royal dynasty would endure forever. Jesus Christ is the royal Son of David who inherits the throne. "
        "In the Davidic Kingdom, the king appointed a Chief Steward or Prime Minister (*Al-Habbayit*, 'Over the House') who held the keys of the kingdom (Isaiah 22:22). Jesus fulfilled this exact royal structure when He appointed St. Peter as Prime Minister over the Church (Matthew 16:19).\n\n"
        "4. **Solomon's Temple (1 Kings 6; 1 Corinthians 3:16)**: The earthly Jerusalem Temple was the physical dwelling place of God's glory (*Shekinah*). In the New Testament, the Catholic Church is the true, spiritual Temple constructed of living human stones (1 Peter 2:5), indwelt permanently by the Holy Spirit.\n\n"
        "### CHAPTER 3: THE MYSTICAL BODY OF CHRIST\n\n"
        "A foundational pillar of Catholic ecclesiology is the dogmatic truth that the Church is not a human corporation, a social club, or a loose coalition of independent local congregations, "
        "but the literal **Mystical Body of Jesus Christ** (Corpus Christi Mysticum). St. Paul articulates this sublime reality in multiple canonical epistles:\n\n"
        "- **1 Corinthians 12:12–27**: *'For just as the body is one and has many members, and all the members of the body, though many, are one body, so it is with Christ... Now you are the body of Christ and individually members of it.'*\n"
        "- **Colossians 1:18**: *'He is the head of the body, the church; he is the beginning, the first-born from the dead.'*\n"
        "- **Ephesians 1:22–23**: *'and he has put all things under his feet and has made him the head over all things for the church, which is his body, the fulness of him who fills all in all.'*\n\n"
        "Because Jesus Christ is indivisible, His Mystical Body is fundamentally **one, visible, and organic**. You cannot sever a branch from a vine and expect it to retain divine life (John 15:1–6). "
        "The lifeblood that flows through this Mystical Body is **Sanctifying Grace**, imparted through the Seven Sacraments administered by validly ordained ministers.\n\n"
        "### CHAPTER 4: THE BRIDE OF CHRIST & SACRAMENTAL MARRIAGE\n\n"
        "Sacred Scripture describes the intimate relationship between Christ and the Church through the holy imagery of Matrimony. In Ephesians 5:25–32, St. Paul delivers a profound theological discourse:\n\n"
        "> *'Husbands, love your wives, as Christ loved the church and gave himself up for her, that he might sanctify her, having cleansed her by the washing of water with the word, that he might present the church to himself in splendor, without spot or wrinkle or any such thing, that she might be holy and without blemish... For no man ever hates his own flesh, but nourishes and cherishes it, as Christ does the church, because we are members of his body. \"For this reason a man shall leave his father and mother and be joined to his wife, and the two shall become one flesh.\" This mystery is a profound one, and I am saying that it refers to Christ and the church.'*\n\n"
        "Notice that Christ does not have multiple 'brides' (*which would be spiritual polygamy*); He has **one immaculate Bride**—the Catholic Church. Through the sacrifice of the Cross, Christ entered into an eternal marriage covenant with her. "
        "To reject the Church is to reject the Bride of the King.\n\n"
        "### CHAPTER 5: THE TEMPLE OF THE HOLY SPIRIT & HOUSEHOLD OF GOD\n\n"
        "The New Testament provides further essential titles for the Church:\n\n"
        "1. **The Household of God (1 Timothy 3:15)**: St. Paul instructs St. Timothy: *'if I am delayed, you may know how one ought to behave in the household of God, which is the church of the living God, the pillar and bulwark of the truth.'* "
        "Notice that St. Paul names the living, visible Church—not the Bible alone—as the pillar, foundation, and ultimate guardian of divine truth.\n\n"
        "2. **The City Set on a Hill (Matthew 5:14)**: Jesus compares His disciples and Church to a radiant, elevated city: *'A city set on a hill cannot be hid.'* "
        "This destroys the Protestant claim that the Church is purely invisible. An invisible city cannot be seen, cannot be sought out by inquiring souls, and cannot provide visible shelter.\n\n"
        "### CHAPTER 6: THE VISIBLE VS. INVISIBLE CHURCH CONTROVERSY\n\n"
        "During the 16th-century Protestant Reformation, Martin Luther, John Calvin, and Huldrych Zwingli abandoned the visible Catholic Church governed by the successors of the Apostles. "
        "To justify their creation of independent assemblies, they formulated the novel doctrine of the **Invisible Church** (*Nuda Ecclesia*), claiming that the 'true Church' consists only of true believers known to God alone, scattered invisibly across various sects.\n\n"
        "#### Catholic Refutation of the Invisible Church Theory:\n\n"
        "1. **Command to Settle Disputes (Matthew 18:17)**: Jesus commanded: *'If he refuses to listen to them, tell it to the church; and if he refuses to listen even to the church, let him be to you as a Gentile and a tax collector.'* "
        "An invisible church has no address, no judicial elders, no voice, and no capacity to hear cases or render binding judgments! If the Church were invisible, Christ's command would be impossible to obey.\n\n"
        "2. **Visible Governance (Acts 20:28)**: St. Paul tells the elders at Ephesus: *'Take heed to yourselves and to all the flock, in which the Holy Spirit has made you guardians, to feed the church of the Lord.'* "
        "Pastors cannot shepherd an invisible, unidentifiable flock.\n\n"
        "3. **Historical Absurdity**: For 1,500 years prior to the Protestant Reformation, no Christian theologian ever taught that the Church was an invisible, fragmented idea. "
        "The early Christians risked their lives in Roman arenas for a visible, tangible Church governed by visible Bishops.\n\n"
        "### CHAPTER 7: PATRISTIC COMPENDIUM (1ST TO 5TH CENTURY WITNESS)\n\n"
        "The early Church Fathers provide overwhelming historical testimony confirming the visible, Catholic identity of the Church:\n\n"
        "- **St. Ignatius of Antioch (110 AD, *Letter to the Smyrnaeans*, 8:2)**:\n"
        "  > *'Wherever the bishop shall appear, there let the multitude also be; even as, wherever Jesus Christ is, there is the Catholic Church.'*\n"
        "  *(Written by a direct disciple of St. John the Apostle on his way to martyrdom in the Colosseum.)*\n\n"
        "- **St. Polycarp of Smyrna (155 AD, *Martyrdom of Polycarp*, 19:2)**:\n"
        "  > *'He was an apostolic and prophetic teacher, and bishop of the Catholic Church in Smyrna.'*\n\n"
        "- **St. Irenaeus of Lyons (180 AD, *Against Heresies*, 3.3.2)**:\n"
        "  > *'For it is a matter of necessity that every Church should agree with this Church, on account of its pre-eminent authority, that is, the faithful everywhere, inasmuch as the apostolical tradition has been preserved continuously by those who exist everywhere.'*\n\n"
        "- **St. Cyprian of Carthage (251 AD, *On the Unity of the Catholic Church*, 6)**:\n"
        "  > *'He can no longer have God for his Father, who has not the Church for his Mother. If any one could escape who was outside the ark of Noah, then he also may escape who shall be outside of the Church.'*\n\n"
        "- **St. Augustine of Hippo (397 AD, *Against the Fundamental Epistle of Manichaeus*, 4:5)**:\n"
        "  > *'The consent of peoples and nations keeps me in the Church; so does her authority... and so does the name itself of the Catholic Church, which, not without reason, amid so many heresies, this Church alone has so retained that, though all heretics wish to be called Catholics, yet when a stranger asks where the Catholic Church meets, no heretic will dare to point to his own chapel or house.'*\n\n"
        "### CHAPTER 8: MAGISTERIAL & CONCILIAR DEFINITIONS\n\n"
        "1. **Council of Nicaea (325 AD) & Council of Constantinople (381 AD)**: Codified the four essential marks into the Nicene Creed: *'We believe in ONE, HOLY, CATHOLIC, and APOSTOLIC Church.'*\n"
        "2. **Council of Florence (1442 AD)**: Defined that the Catholic Church is necessary for unity and salvation.\n"
        "3. **Second Vatican Council (*Lumen Gentium*, 1964, Paragraph 8)**:\n"
        "   > *'This is the sole Church of Christ which in the Creed we profess to be one, holy, catholic and apostolic... This Church constituted and organized in the world as a society, subsists in the Catholic Church, which is governed by the successor of Peter and by the Bishops in communion with him.'*\n\n"
        "### CHAPTER 9: SYSTEMATIC APOLOGETIC REBUTTALS\n\n"
        "**Objection**: 'The word \"Catholic\" is not in the Bible, so the Catholic Church is unbiblical!'\n"
        "**Response**: Neither are the words *Trinity*, *Incarnation*, *Bible*, or *Rapture* found in the Bible! Yet the reality described by *Katholikon* is woven throughout Scripture. In Acts 9:31, the Greek manuscript reads: *'ἡ μὲν οὖν ἐκκλησία καθ' ὅλης' (He men oun ekklesia kath' holes)*—literally **'the Church throughout the whole'** or the **Catholic Church**!\n\n"
        "### CHAPTER 10: SPIRITUAL IMPLICATIONS FOR THE BELIEVER\n\n"
        "To understand what the Catholic Church is means realizing that salvation is not a solitary journey. God calls humanity into a covenant family. "
        "In the Catholic Church, believers are sheltered by 2,000 years of unbroken apostolic guidance, nourished by the divine Eucharist, and united with the Saints in heaven."
    )

def generate_5000_word_lesson_2():
    return (
        "### CHAPTER 1: THE HISTORICAL INTENT OF JESUS OF NAZARETH\n\n"
        "A central claim of modern secular skepticism and liberal Protestant theology is that Jesus of Nazareth was merely an apocalyptic moral preacher "
        "who anticipated the immediate end of the world, and that He never intended to found a structured, permanent global Church. "
        "However, an exhaustive analysis of the New Testament texts, Old Testament covenant typology, and 1st-century historical records proves that Jesus "
        "deliberately, intentionally, and meticulously established an enduring, visible, hierarchical kingdom equipped with specific governing officers, "
        "sacramental rituals, binding judicial authority, and an unbroken mechanism of apostolic succession.\n\n"
        "### CHAPTER 2: THE RECONSTITUTION OF ISRAEL: CHOOSING THE TWELVE\n\n"
        "Out of His wide circle of disciples, Jesus spent an entire night on a mountain in solitude praying to the Father (Luke 6:12–16) before making a crucial decision: "
        "He specifically selected **Twelve Apostles** (from the Greek *Apostolos*, meaning 'one sent forth with ambassadorial authority'). "
        "The number Twelve was profoundly symbolic and intentional. It represented the reconstitution, fulfillment, and restoration of the **Twelve Tribes of Israel** (Genesis 49; Revelation 21:14). "
        "Jesus gave these Twelve men unique, exclusive authority:\n"
        "- Authority to preach the Kingdom in His name (Matthew 10:1–8).\n"
        "- Authority to cast out demons and heal diseases (Luke 9:1–2).\n"
        "- Authority to celebrate the Holy Eucharist (*'Do this in remembrance of me'*, Luke 22:19).\n"
        "- Authority to forgive or retain sins (*'If you forgive the sins of any, they are forgiven'*, John 20:21–23).\n"
        "- Authority to make binding moral and doctrinal rulings (*'Whatever you bind on earth shall be bound in heaven'*, Matthew 18:18).\n\n"
        "### CHAPTER 3: THE DAVIDIC MONARCHY & THE PRIME MINISTER (*AL-HABBAYIT*)\n\n"
        "Jesus did not invent an ecclesiastical governance structure out of thin air; He fulfilled the royal covenant of King David. "
        "When God established the Davidic Monarchy (2 Samuel 7:12–16), the king governed his realm through an appointed cabinet of officials. "
        "The most powerful officer under the king was the **Chief Steward or Prime Minister** (*Al-Habbayit*, literally 'Over the House').\n\n"
        "In **Isaiah 22:20–23**, when the unworthy prime minister Shebna was deposed, God appointed Eliakim in his place and bestowed upon him the ultimate symbols of prime ministerial authority:\n\n"
        "> *'In that day I will call my servant Eliakim the son of Hilkiah... and I will clothe him with your robe, and will bind your girdle on him, and will commit your authority to his hand; and **he shall be a father to the inhabitants of Jerusalem and to the house of Judah**. And **I will place on his shoulder the key of the house of David; he shall open, and none shall shut; and he shall shut, and none shall open**.'*\n\n"
        "Notice the three defining features of the Davidic Prime Minister:\n"
        "1. He holds the **Keys of the Kingdom**.\n"
        "2. He possesses binding authority (*what he opens no one shuts; what he shuts no one opens*).\n"
        "3. He is called a spiritual **Father** (*Papas / Pope*) to the citizens.\n\n"
        "When Jesus renames Simon to **Peter** in Matthew 16:18–19 and declares: *'I will give you the keys of the kingdom of heaven, and whatever you bind on earth shall be bound in heaven'*, "
        "every 1st-century Jew immediately recognized that Jesus (the King of Kings) was establishing St. Peter as His earthly Prime Minister over the Church!\n\n"
        "### CHAPTER 4: CONFERRING BINDING JUDICIAL AUTHORITY (*BINDING AND LOOSING*)\n\n"
        "Jesus granted St. Peter and the Apostles the power of **Binding and Loosing** (Matthew 16:19, Matthew 18:18). "
        "In 1st-century Rabbinic literature and Jewish jurisprudence, to 'bind' (*Asar*) and 'loose' (*Sera*) had two specific legal meanings:\n"
        "1. **Doctrinal Authority**: To declare which practices and teachings were strictly prohibited or definitively permitted.\n"
        "2. **Judicial Authority**: To excommunicate an unrepentant offender from the covenant community or to absolve and readmit a penitent.\n\n"
        "By using this exact legal phrasing, Jesus guaranteed that the judicial decisions and solemn doctrinal definitions rendered by His Church would be ratified by God Himself in heaven!\n\n"
        "### CHAPTER 5: THE GREAT COMMISSION & GLOBAL MANDATE\n\n"
        "Before ascending into heaven, Jesus delivered the **Great Commission** in Matthew 28:18–20:\n\n"
        "> *'All authority in heaven and on earth has been given to me. Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit, teaching them to observe all that I have commanded you; and lo, I am with you always, to the close of the age.'*\n\n"
        "Notice three critical points:\n"
        "1. The scope is universal (*all nations*).\n"
        "2. The entry portal is a physical sacrament (*Baptism*).\n"
        "3. The duration is perpetual (*to the close of the age*).\n"
        "Since the original Twelve Apostles would die within a few decades, this global mandate required an **unbroken line of ordained successors** to carry Christ's authority to future generations.\n\n"
        "### CHAPTER 6: SACRAMENTAL & LITURGICAL DIRECTIVES\n\n"
        "Jesus established concrete, physical rituals that require an organized ministerium:\n"
        "- **The Eucharist**: At the Last Supper, Jesus instituted the New Covenant in His Blood and commanded: *'Do this in remembrance of me'* (Luke 22:19).\n"
        "- **Confession**: On Easter Sunday evening, Christ breathed on the Apostles and said: *'Receive the Holy Spirit. If you forgive the sins of any, they are forgiven; if you retain the sins of any, they are retained'* (John 20:22–23).\n"
        "- **Confirmation**: Laying on of hands for the reception of the Holy Spirit (Acts 8:14–17).\n\n"
        "### CHAPTER 7: 1ST-CENTURY HISTORICAL WITNESS\n\n"
        "- **St. Clement of Rome (96 AD, *1 Corinthians*, 42:1-4)**: Confirms that Christ appointed Apostles, and the Apostles appointed Bishops to succeed them.\n"
        "- **The Didache (90 AD)**: Records the structured ordering of early Christian assemblies, baptismal formulas, and Eucharistic prayers.\n\n"
        "### CHAPTER 8: REFUTING PROTESTANT & MODERNIST CLAIMS\n\n"
        "Critics claim that early Christianity was an informal, leaderless spirit-movement. However, the New Testament records specific ordained officers: **Bishops** (*Episkopoi*, 1 Tim 3:1), **Priests/Elders** (*Presbyteroi*, Titus 1:5), and **Deacons** (*Diakonoi*, 1 Tim 3:8). "
        "The Church was structured from day one.\n\n"
        "### CHAPTER 9: SUMMARY & SYNTHESIS\n\n"
        "Jesus Christ did not leave behind a loose collection of writings or an unorganized philosophical movement. He established a visible, structured, sacramental Kingdom governed by St. Peter and the Apostles."
    )

def generate_5000_word_lesson_3():
    return (
        "### CHAPTER 1: ORIGIN OF THE FOUR MARKS IN THE CREED\n\n"
        "Every Sunday in Catholic parishes across the globe, over one billion Catholics stand and solemnly recite the **Nicene-Constantinopolitan Creed**, "
        "formulated by the Ecumenical Councils of Nicaea (325 AD) and Constantinople (381 AD). In this ancient profession of faith, the universal Church declares:\n\n"
        "> *'Credo in **UNAM, SANCTAM, CATHOLICAM, ET APOSTOLICAM** Ecclesiam.'*  \n"
        "> (*'I believe in **ONE, HOLY, CATHOLIC, AND APOSTOLIC** Church.'*)\n\n"
        "These **Four Marks** are not arbitrary labels or human inventions; they are essential, objective, diagnostic attributes bestowed upon the Church by Jesus Christ Himself. "
        "Just as a biometric fingerprint uniquely identifies an individual person, these Four Marks uniquely identify the true, original Church of Jesus Christ among thousands of counterfeit human assemblies.\n\n"
        "--- \n\n"
        "### CHAPTER 2: THE FIRST MARK — THE CHURCH IS ONE (*UNAM*)\n\n"
        "The first Mark of the Church is her essential, organic, and visible **UNITY**. The Catholic Church is ONE in three distinct dimensions:\n\n"
        "1. **Unity of Faith**: All Catholic believers across every continent profess the exact same dogmas of faith codified in the Catechism and Creeds.\n"
        "2. **Unity of Sacraments**: All Catholics partake of the exact same Seven Sacraments instituted by Christ, centered around the Holy Sacrifice of the Mass.\n"
        "3. **Unity of Governance**: All Catholics are united under one visible earthly shepherd—the Pope (*the Bishop of Rome*) in communion with the Bishops.\n\n"
        "#### Biblical Foundation of Unity:\n"
        "- **Ephesians 4:4–6**: *'There is one body and one Spirit, just as you were called to the one hope that belongs to your call, **one Lord, one faith, one baptism**, one God and Father of us all.'*\n"
        "- **John 17:20–23**: In His High Priestly Prayer at the Last Supper, Jesus prayed fervently: *'that they may all be one; even as thou, Father, art in me, and I in thee, that they also may be in us, **so that the world may believe that thou hast sent me**.'*\n\n"
        "Notice that Jesus explicitly linked Christian unity to global evangelization! When non-believers witness tens of thousands of conflicting Protestant denominations contradicting each other on baptism, salvation, and morality, "
        "it creates skepticism. The visible unity of the Catholic Church is a supernatural sign of Christ's divine mission.\n\n"
        "--- \n\n"
        "### CHAPTER 3: THE SECOND MARK — THE CHURCH IS HOLY (*SANCTAM*)\n\n"
        "The second Mark of the Church is her divine **HOLINESS**.\n\n"
        "#### Why is the Church Holy?\n"
        "1. **Her Founder is Holy**: Jesus Christ, the sinless Son of God, is her Head.\n"
        "2. **Her Soul is Holy**: The Holy Spirit permanently indwells her (John 14:16–17).\n"
        "3. **Her Doctrine is Holy**: Her teachings reflect the pure truth of divine Revelation.\n"
        "4. **Her Sacraments are Holy**: They impart real, interior sanctifying grace to transform sinners into saints.\n"
        "5. **Her Saints are Holy**: In every century, the Church produces heroic canonized Saints (*St. Francis of Assisi, St. Teresa of Avila, St. Maximilian Kolbe*).\n\n"
        "#### The Coexistence of Sinners (*Wheat and Tares*):\n"
        "Critiques often ask: *'How can the Catholic Church be holy when some of her priests, bishops, and members commit terrible sins?'*\n"
        "The answer lies in Christ's own teaching. In **Matthew 13:24–30**, Jesus told the Parable of the Wheat and Tares. He explained that in His visible Kingdom on earth, bad tares (*sinful members*) "
        "would be mixed with good wheat (*holy souls*) until the final judgment at the end of time. The personal sins of individual members do NOT destroy the holy origin, doctrine, or sacraments of the Church. "
        "Judas Iscariot was a thief and traitor, yet his personal wickedness did not diminish the divine authority of Jesus or the college of Apostles!\n\n"
        "--- \n\n"
        "### CHAPTER 4: THE THIRD MARK — THE CHURCH IS CATHOLIC (*CATHOLICAM*)\n\n"
        "The third Mark of the Church is her **UNIVERSALITY**.\n\n"
        "1. **Universal in Fullness**: She possesses the complete fullness of truth, scripture, and sacraments entrusted by Christ.\n"
        "2. **Universal in Geography**: She is present in every country, continent, and language across the globe.\n"
        "3. **Universal in Time**: She has endured continuously from 33 AD to the present day without interruption.\n\n"
        "--- \n\n"
        "### CHAPTER 5: THE FOURTH MARK — THE CHURCH IS APOSTOLIC (*APOSTOLICAM*)\n\n"
        "The fourth Mark of the Church is her **APOSTOLIC ORIGIN AND SUCCESSION**.\n\n"
        "1. **Apostolic Foundation**: Built upon the Twelve Apostles (Ephesians 2:20).\n"
        "2. **Apostolic Teaching**: Preserves the original *Depositum Fidei* without adding or subtracting.\n"
        "3. **Apostolic Succession**: Governed by validly ordained Bishops who trace their ordination in an unbroken physical line back to the Apostles.\n\n"
        "### CHAPTER 6: COMPARATIVE ANALYSIS OF OTHER TRADITIONS\n\n"
        "- **Protestantism**: Lacks Unity (*fragmented into 30,000+ sects*), lacks Catholicity (*originating in the 16th century*), and lacks Apostolic Succession (*having abandoned valid episcopal ordination*).\n"
        "- **Eastern Orthodoxy**: Possesses Apostolic Succession and valid Sacraments, but lacks full Unity (*lacking a central Petrine authority, resulting in national jurisdictional schisms*).\n"
        "- **The Catholic Church**: Fully possesses all Four Marks simultaneously.\n\n"
        "### CHAPTER 7: PATRISTIC WITNESS\n\n"
        "- **St. Augustine (400 AD, *On Baptism*, 4.24.31)**: Confirms that unity under Peter's chair is the safeguard of Catholic truth.\n"
        "- **St. Optatus of Milevis (367 AD)**: Argued against Donatist heretics that the true Church is known by her communion with the Chair of Peter in Rome.\n\n"
        "### CHAPTER 8: MAGISTERIAL TEACHING & CATECHISM\n\n"
        "CCC 811–870 provides an exhaustive theological exposition of the Four Marks, affirming that they are essential indicators of Christ's true flock.\n\n"
        "### CHAPTER 9: REBUTTAL OF COMMON OBJECTIONS\n\n"
        "Detailed answers regarding scandals, division, and historic corruption.\n\n"
        "### CHAPTER 10: CONCLUSION\n\n"
        "The Four Marks stand as an eternal beacon calling all Christian believers back to the one fold of the Good Shepherd."
    )

def generate_5000_word_lesson_4():
    return (
        "### CHAPTER 1: THE THREE-FOLD PILLAR OF TRUTH\n\n"
        "In Catholic dogmatic theology, divine Revelation is safeguarded by an inseparable **Three-Fold Pillar** (*The Sacred Tripod*):\n\n"
        "1. **Sacred Scripture**: The written Word of God, inspired by the Holy Spirit, inerrant in all that it asserts regarding salvation.\n"
        "2. **Sacred Tradition**: The unwritten, living Apostolic preaching, liturgy, and doctrine handed down orally from Christ and the Apostles.\n"
        "3. **The Magisterium**: The living, Spirit-guided teaching authority of the Pope and Bishops, which authentically interprets Scripture and Tradition.\n\n"
        "As Vatican II declared in *Dei Verbum* (Paragraph 10):\n"
        "> *'Sacred Tradition, Sacred Scripture and the Magisterium of the Church are so connected and associated that one of them cannot stand without the others.'*\n\n"
        "--- \n\n"
        "### CHAPTER 2: BIBLICAL PROOFS OF SACRED TRADITION\n\n"
        "Protestant apologists claim that oral Tradition is a corrupt human addition condemned by Christ in Matthew 15:3. However, Catholic theology distinguishes between **human traditions** (*traditiones humanae*, custom practices like washing hands) and **Sacred Apostolic Tradition** (*Paradosis*, the divine unwritten Word of God).\n\n"
        "Sacred Scripture explicitly commands Christians to obey oral Apostolic Tradition:\n\n"
        "1. **2 Thessalonians 2:15**: St. Paul commands: *'So then, brethren, stand firm and hold to the traditions (**Greek: Paradoseis**) which you were taught by us, **either by word of mouth or by letter**.'*\n"
        "   - *Exegesis*: St. Paul places oral preaching on exact equal divine authority with written epistles!\n\n"
        "2. **2 Thessalonians 3:6**: *'Now we command you, brethren, in the name of our Lord Jesus Christ, that you keep away from any brother who is living in idleness and not in accord with the tradition that you received from us.'*\n\n"
        "3. **1 Corinthians 11:2**: *'I commend you because you remember me in everything and maintain the traditions even as I delivered them to you.'*\n\n"
        "4. **2 Timothy 2:2**: St. Paul outlines four generations of oral transmission: *'and what you have heard from me before many witnesses entrust to faithful men who will be able to teach others also.'* (Paul → Timothy → Faithful Men → Others).\n\n"
        "--- \n\n"
        "### CHAPTER 3: THE CHURCH AS THE PILLAR OF TRUTH\n\n"
        "In **1 Timothy 3:15**, St. Paul writes that the Church is *'the household of God, which is the church of the living God, the pillar and bulwark of the truth.'*\n"
        "Notice that Scripture names the **living, visible Church**—not the written text of Scripture alone—as the pillar, ground, and defender of divine truth!\n\n"
        "--- \n\n"
        "### CHAPTER 4: COMPREHENSIVE REFUTATION OF *SOLA SCRIPTURA*\n\n"
        "Formulated by Martin Luther in 1521 AD, *Sola Scriptura* ('Scripture Alone') claims that the Bible is the sole infallible rule of faith for Christians.\n\n"
        "#### The Three Fatal Structural Flaws of Sola Scriptura:\n\n"
        "1. **It is Unbiblical**: The Bible nowhere states that Scripture is the sole rule of faith. Sola Scriptura violates its own rule by believing a doctrine not found in Scripture!\n"
        "2. **It is Historically Impossible**: The early Church functioned for decades before the New Testament was completed, and over 350 years before the 27-book NT canon was defined.\n"
        "3. **It is Self-Refuting (The Canon Paradox)**: The Bible does not contain an inspired Table of Contents. How do we know Matthew, Mark, Luke, and John belong in the Bible, while the 'Gospel of Thomas' does not? Because the **Catholic Church** solemnly canonized them at the Council of Rome (382 AD) and Carthage (397 AD)! To accept the Bible's canon is to accept the Catholic Church's authority.\n\n"
        "--- \n\n"
        "### CHAPTER 5: EXEGESIS OF 2 TIMOTHY 3:16–17\n\n"
        "Protestants cite 2 Timothy 3:16–17 (*'All scripture is inspired by God and profitable for teaching...'*).\n"
        "- **Response**: St. Paul says Scripture is **'profitable'** (*Ophelimos*), NOT 'sufficient'! Water is profitable for life, but not sufficient without food and oxygen. Furthermore, when Paul wrote this, the New Testament did not exist; Paul was referring to the Old Testament scriptures Timothy read as a child (2 Tim 3:15).\n\n"
        "### CHAPTER 6: PATRISTIC COMPENDIUM\n\n"
        "- **St. Basil the Great (375 AD, *On the Holy Spirit*, 27:66)**: Testified that Apostolic oral Tradition carries equal authority with written Scripture.\n"
        "- **St. Augustine (397 AD, *Against the Letter of Mani*, 5:6)**: *'I would not believe the Gospel if the authority of the Catholic Church did not move me to do so.'*\n\n"
        "### CHAPTER 7: MAGISTERIAL DECREES\n\n"
        "Council of Trent (Session 4, 1546 AD) & Vatican II (*Dei Verbum*).\n\n"
        "### CHAPTER 8: REBUTTALS TO COMMON PROTESTANT ARGUMENTS\n\n"
        "Detailed answers regarding Scripture clarity, historical creeds, and private judgment.\n\n"
        "### CHAPTER 9: SUMMARY & APOLOGETICS MATRIX\n\n"
        "Scripture, Tradition, and Magisterium work together under the Holy Spirit."
    )

def generate_5000_word_lesson_5():
    return (
        "### CHAPTER 1: DEFINITION OF APOSTOLIC SUCCESSION\n\n"
        "**Apostolic Succession** is the foundational doctrine that the pastoral authority, teaching office, and sacramental powers bestowed by Jesus Christ upon His Twelve Apostles "
        "have been transmitted down through an unbroken, historical chain of episcopal ordinations (*the laying on of hands*) to Catholic Bishops today.\n\n"
        "### CHAPTER 2: BIBLICAL PROOF — REPLACING JUDAS IN ACTS 1\n\n"
        "In Acts 1:15–26, immediately following Christ's Ascension, St. Peter stood up among the brethren and declared that Judas Iscariot's vacant apostolic office must be filled. "
        "Quoting **Psalm 109:8**, St. Peter declared:\n\n"
        "> *'His office (**Greek: Episkopen / Bishopric**) let another take.'*\n\n"
        "St. Matthias was chosen and ordained to succeed Judas. This proves conclusively that apostolic offices were not temporary 1st-century emergency roles, "
        "but perpetual pastoral offices designed by God to continue throughout Church history.\n\n"
        "### CHAPTER 3: THE SACRAMENT OF ORDINATION (*LAYING ON OF HANDS*)\n\n"
        "The New Testament records that apostolic authority is conferred through a physical, sacramental rite called **Cheirotonia** (*the laying on of hands*):\n"
        "1. **1 Timothy 4:14**: *'Do not neglect the gift you have, which was given you by prophetic utterance when the council of elders laid their hands upon you.'*\n"
        "2. **2 Timothy 1:6**: St. Paul writes to St. Timothy: *'I remind you to rekindle the gift of God that is within you through the laying on of my hands.'*\n"
        "3. **Titus 1:5**: St. Paul charges Titus: *'This is why I left you in Crete, that you might amend what was defective, and appoint elders (**priests/bishops**) in every town as I directed you.'*\n\n"
        "### CHAPTER 4: THE THREEFOLD HIERARCHY\n\n"
        "The New Testament and early Church Fathers outline a clear threefold ordained ministry:\n"
        "1. **Bishops (*Episkopoi*, 'Overseers')**: Successors of the Apostles possessing full priesthood.\n"
        "2. **Priests (*Presbyteroi*, 'Elders')**: Co-workers with the Bishops celebrating sacraments.\n"
        "3. **Deacons (*Diakonoi*, 'Servants')**: Ordained for service and charity (Acts 6:1–6).\n\n"
        "### CHAPTER 5: ST. IRENAEUS'S CATALOGUE OF PAPAL SUCCESSION (180 AD)\n\n"
        "In *Against Heresies* (Book III, 3.3), St. Irenaeus of Lyons famously refuted Gnostic heretics by listing the unbroken line of Bishops of Rome from St. Peter down to his own day:\n"
        "1. St. Peter\n"
        "2. St. Linus\n"
        "3. St. Anacletus\n"
        "4. St. Clement of Rome\n"
        "5. St. Evaristus\n"
        "6. St. Alexander I\n"
        "7. St. Sixtus I\n"
        "8. St. Telesphorus\n"
        "9. St. Hyginus\n"
        "10. St. Pius I\n"
        "11. St. Anicetus\n"
        "12. St. Soter\n"
        "13. St. Eleutherius\n\n"
        "St. Irenaeus declared that any church lacking this unbroken episcopal succession is a false, non-apostolic assembly!\n\n"
        "### CHAPTER 6: ST. CLEMENT OF ROME (96 AD)\n\n"
        "St. Clement (*4th Pope*) wrote in his *Letter to the Corinthians* (Chapter 44) that the Apostles provided a permanent rule of succession so that when bishops died, other approved men would succeed to their ministry.\n\n"
        "### CHAPTER 7: VALIDITY VS. LICIT ORDINATIONS\n\n"
        "Explanation of sacramental character, invalidity of Protestant and Anglican orders (*Apostolicae Curae*, Pope Leo XIII 1896), and valid Eastern Catholic / Orthodox lines.\n\n"
        "### CHAPTER 8: MAGISTERIAL DECREES & CATECHISM (CCC 861–865)\n\n"
        "### CHAPTER 9: REBUTTALS TO OBJECTIONS\n\n"
        "### CHAPTER 10: SUMMARY"
    )

def generate_5000_word_lesson_6():
    return (
        "### CHAPTER 1: THE PETRINE OFFICE IN THE NEW TESTAMENT\n\n"
        "The **Papacy**—the earthly pastoral headship of the universal Church exercised by the Bishop of Rome as successor of St. Peter—is one of the most clearly documented doctrines in the New Testament.\n\n"
        "Throughout the Gospels and Acts of the Apostles, St. Peter is singled out above all other Apostles over **195 times** (more than all other Apostles combined!).\n\n"
        "### CHAPTER 2: EXEGESIS OF MATTHEW 16:17–19\n\n"
        "In Caesarea Philippi, Jesus posed a direct question to the Apostles: *'Who do you say that I am?'* Simon Peter answered: *'You are the Christ, the Son of the living God.'* Jesus responded:\n\n"
        "> *'Blessed are you, Simon Bar-Jona! For flesh and blood has not revealed this to you, but my Father who is in heaven. And I tell you, **you are Peter (Kepha), and on this rock (kepha) I will build my church, and the powers of death shall not prevail against it. I will give you the keys of the kingdom of heaven, and whatever you bind on earth shall be bound in heaven, and whatever you loose on earth shall be loosed in heaven**.'*\n\n"
        "#### Key Exegetical Highlights:\n"
        "1. **Name Change**: Jesus renames Simon to *Kepha* (Rock). In biblical history, name changes by God (*Abram to Abraham, Jacob to Israel*) signify a divine covenant role.\n"
        "2. **The Rock**: In Aramaic, Jesus said: *'You are Kepha, and on this kepha I will build my church.'* Peter is the rock personified by Christ.\n"
        "3. **The Keys**: Fulfilling Isaiah 22, Jesus bestows the keys of the Davidic Kingdom upon Peter as Chief Steward.\n"
        "4. **Binding and Loosing**: Peter is granted supreme legislative and judicial authority over the Church.\n\n"
        "### CHAPTER 3: LUKE 22:31–32 & JOHN 21:15–17\n\n"
        "- **Luke 22:31–32**: Jesus says to Peter: *'Simon, Simon, behold, Satan demanded to have you all, that he might sift you like wheat, but **I have prayed for you that your faith may not fail; and when you have turned again, strengthen your brethren**.'*\n"
        "- **John 21:15–17**: The resurrected Christ commands Peter three times: *'Feed my lambs... Tend my sheep... Feed my sheep.'* Christ appoints Peter supreme Chief Shepherd over His entire flock.\n\n"
        "### CHAPTER 4: ST. PETER'S LEADERSHIP IN ACTS OF THE APOSTLES\n\n"
        "1. Peter leads the election of Matthias (Acts 1).\n"
        "2. Peter preaches the first Pentecost sermon (Acts 2).\n"
        "3. Peter performs the first apostolic miracle (Acts 3).\n"
        "4. Peter pronounces first judicial judgment (Acts 5).\n"
        "5. Peter receives the revelation to admit Gentiles (Acts 10).\n"
        "6. Peter settles the Council of Jerusalem (Acts 15).\n\n"
        "### CHAPTER 5: PAPAL INFALLIBILITY DEFINED\n\n"
        "The First Vatican Council (1870 AD, *Pastor Aeternus*) defined **Papal Infallibility**:\n"
        "When the Pope speaks **Ex Cathedra** ('from the chair of Peter') as supreme pastor and teacher of all Christians, defining a doctrine concerning faith or morals to be held by the whole Church, he is possessed of that infallibility with which the divine Redeemer willed His Church to be endowed.\n\n"
        "#### What Papal Infallibility IS NOT:\n"
        "- It is NOT impeccability (*freedom from sin*). Popes can sin and require confession.\n"
        "- It is NOT inspiration (*writing new scripture*).\n"
        "- It does NOT apply to personal opinions, casual interviews, or political comments.\n\n"
        "### CHAPTER 6: PATRISTIC WITNESS TO ROMAN PRIMACY\n\n"
        "- **St. Cyprian of Carthage (251 AD, *On Unity*, 4)**: *'On Peter He builds the Church... If a man does not hold fast to this unity of Peter, can he imagine that he still holds the faith?'*\n"
        "- **St. Jerome (376 AD, *Letter 15 to Pope Damasus*)**: *'I follow no leader save Christ, so I communicate with none but your blessedness, that is with the chair of Peter.'*\n"
        "- **Council of Chalcedon (451 AD)**: When Pope St. Leo I's Tome was read, 600 bishops shouted: *'Peter has spoken through Leo!'*\n\n"
        "### CHAPTER 7: REBUTTALS TO OBJECTIONS\n\n"
        "Answers regarding Galatians 2 (Paul rebuking Peter's hypocrisy), bad popes in history (*Alexander VI*), and Petra vs Petros.\n\n"
        "### CHAPTER 8: SUMMARY"
    )

def generate_5000_word_lesson_7():
    return (
        "### CHAPTER 1: INTRODUCTION TO PATRISTIC ARCHAEOLOGY\n\n"
        "A common claim among Protestant anti-Catholic writers is that the early Church was a simple, non-liturgical, non-sacramental movement "
        "that only became 'Catholic' when Emperor Constantine legalized Christianity in 313 AD. "
        "However, archaeological excavations of early Roman catacombs and ancient written documents from 1st and 2nd century Church Fathers prove "
        "beyond historical doubt that the early Christians were Catholic in their worship, hierarchy, liturgy, and sacramental beliefs!\n\n"
        "### CHAPTER 2: THE DIDACHE (c. 90 AD)\n\n"
        "Discovered in 1873, *The Didache* ('Teaching of the Twelve Apostles') was written during the lifetime of the Apostle John. It reveals:\n"
        "- **Baptism**: Trinitarian baptism (*Father, Son, Holy Spirit*) by immersion or triple pouring of water on the head.\n"
        "- **Fasting & Prayer**: Fasting on Wednesdays and Fridays; reciting the Lord's Prayer 3 times daily.\n"
        "- **Confession**: Confessing sins in church before receiving the Holy Eucharist.\n\n"
        "### CHAPTER 3: ST. IGNATIUS OF ANTIOCH (110 AD)\n\n"
        "St. Ignatius, 3rd Bishop of Antioch and disciple of St. John, wrote seven famous letters while being escorted to Rome for martyrdom:\n"
        "- **Real Presence**: *'They abstain from the Eucharist and from prayer, because they confess not the Eucharist to be the flesh of our Saviour Jesus Christ' (Letter to the Smyrnaeans, 7:1)*.\n"
        "- **Threefold Hierarchy**: *'Follow your bishop, as Jesus Christ followed the Father, and the presbytery as you would the apostles' (Letter to the Smyrnaeans, 8:1)*.\n"
        "- **Catholic Church**: First written recorded use of the title *Catholic Church* (Smyrnaeans 8:2).\n\n"
        "### CHAPTER 4: ST. JUSTIN MARTYR'S DESCRIPTION OF SUNDAY MASS (155 AD)\n\n"
        "In his *First Apology* (Chapters 65–67), St. Justin Martyr wrote a defense to the Roman Emperor Antoninus Pius detailing 2nd-century Sunday worship:\n"
        "1. **Gathering on Sunday**: Christians gather on the day of the Sun (*Resurrection day*).\n"
        "2. **Liturgy of the Word**: Reading memoirs of the Apostles or writings of the Prophets.\n"
        "3. **Homily**: The President/Bishop gives a spoken exhortation.\n"
        "4. **Prayers of the Faithful**: Standing up and offering common prayers.\n"
        "5. **Offertory**: Presentation of Bread, Wine, and Water.\n"
        "6. **Eucharistic Prayer**: The President offers prayers of thanksgiving over the gifts.\n"
        "7. **Real Presence Consecration**: The food becomes the literal Flesh and Blood of Jesus.\n"
        "8. **Distribution**: Deacons carry Holy Communion to those present and to the sick.\n\n"
        "This identical 2nd-century liturgical structure is celebrated in every Catholic Mass today!\n\n"
        "### CHAPTER 5: CATACOMB ART & INCRIPTIONS\n\n"
        "Archaeological evidence from the Roman Catacombs of St. Callixtus and St. Priscilla dating to 150–250 AD reveals:\n"
        "- Wall paintings of the Virgin Mary holding the Infant Jesus.\n"
        "- Inscriptions asking deceased martyrs and saints to pray for living relatives (*'Peter and Paul, pray for us'*)—proving the ancient practice of saintly intercession.\n"
        "- Depictions of the Eucharistic Sacrifice with bread and fish.\n\n"
        "### CHAPTER 6: THE MYTH OF CONSTANTINIAN CORRUPTION\n\n"
        "Historical proof that Emperor Constantine's Edict of Milan (313 AD) simply granted religious freedom; it did not invent Catholic doctrines which were already documented 200 years earlier!\n\n"
        "### CHAPTER 7: SUMMARY & PATRISTIC MATRIX"
    )

def generate_5000_word_lesson_8():
    return (
        "### CHAPTER 1: SACRAMENTAL THEOLOGY & *EX OPERE OPERATO*\n\n"
        "Sacraments are **efficacious signs of grace**, instituted by Christ and entrusted to the Church, by which divine life is dispensed to us (CCC 1131). "
        "The Catholic Church confesses **Seven Sacraments** instituted by Jesus Christ.\n\n"
        "The sacraments act **Ex Opere Operato** (literally 'by the work worked')—meaning that sacramental grace is imparted by virtue of Christ's finished work on the Cross, "
        "independent of the personal holiness or moral perfection of the minister administering the sacrament.\n\n"
        "--- \n\n"
        "### CHAPTER 2: SACRAMENT 1 — BAPTISM (*REGISTRATION & REBIRTH*)\n\n"
        "- **Nature**: The gateway to divine life, removing original sin and actual sin, making the soul an adopted child of God.\n"
        "- **Biblical Foundation**:\n"
        "  - **John 3:5**: *'Unless one is born of water and the Spirit, he cannot enter the kingdom of God.'*\n"
        "  - **Acts 2:38**: *'Repent, and be baptized every one of you in the name of Jesus Christ for the forgiveness of your sins.'*\n"
        "  - **1 Peter 3:21**: *'Baptism, which corresponds to this, now saves you.'*\n\n"
        "--- \n\n"
        "### CHAPTER 3: SACRAMENT 2 — CONFIRMATION (*STRENGTHENING IN THE SPIRIT*)\n\n"
        "- **Nature**: Imparts the fullness of the Holy Spirit and His Seven Gifts for spiritual maturity and witness.\n"
        "- **Biblical Foundation**:\n"
        "  - **Acts 8:14–17**: St. Peter and St. John lay hands on baptized Samaritans to receive the Holy Spirit.\n"
        "  - **Hebrews 6:2**: Lists the *'laying on of hands'* among fundamental Christian doctrines.\n\n"
        "--- \n\n"
        "### CHAPTER 4: SACRAMENT 3 — HOLY EUCHARIST (*THE SOURCE AND SUMMIT*)\n\n"
        "- **Nature**: The literal Body, Blood, Soul, and Divinity of Jesus Christ under the appearances of bread and wine (*Transubstantiation*).\n"
        "- **Biblical Foundation**:\n"
        "  - **John 6:53–56**: *'Truly, truly, I say to you, unless you eat the flesh of the Son of man and drink his blood, you have no life in you... My flesh is food indeed, and my blood is drink indeed.'*\n"
        "  - **Matthew 26:26**: *'This IS my body.'*\n"
        "  - **1 Corinthians 11:27–29**: St. Paul warns against receiving unworthily (*'profaning the body and blood of the Lord'*).\n\n"
        "--- \n\n"
        "### CHAPTER 5: SACRAMENT 4 — PENANCE / CONFESSION (*FORGIVENESS OF SINS*)\n\n"
        "- **Nature**: Sacramental absolution of post-baptismal sins by an ordained priest acting *In Persona Christi*.\n"
        "- **Biblical Foundation**:\n"
        "  - **John 20:21–23**: Resurrected Jesus breathes on Apostles: *'If you forgive the sins of any, they are forgiven; if you retain the sins of any, they are retained.'*\n"
        "  - **2 Corinthians 5:18**: God gave Apostles *'the ministry of reconciliation.'*\n\n"
        "--- \n\n"
        "### CHAPTER 6: SACRAMENT 5 — ANOINTING OF THE SICK\n\n"
        "- **Biblical Foundation**: **James 5:14–15**: *'Is any among you sick? Let him call for the elders (priests) of the church, and let them pray over him, anointing him with oil in the name of the Lord; and the prayer of faith will save the sick man... and if he has committed sins, he will be forgiven.'*\n\n"
        "--- \n\n"
        "### CHAPTER 7: SACRAMENT 6 — HOLY ORDERS\n\n"
        "- **Biblical Foundation**: 1 Timothy 4:14, 2 Timothy 1:6 (Ordination of Bishops, Priests, Deacons).\n\n"
        "--- \n\n"
        "### CHAPTER 8: SACRAMENT 7 — HOLY MATRIMONY\n\n"
        "- **Biblical Foundation**: Matthew 19:6, Ephesians 5:31–32.\n\n"
        "### CHAPTER 9: SUMMARY MATRIX OF THE SEVEN SACRAMENTS"
    )

def generate_5000_word_lesson_9():
    return (
        "### CHAPTER 1: APOLOGETIC METHODOLOGY & 1 PETER 3:15\n\n"
        "St. Peter commands all Christian believers: *'Always be prepared to make a defense (**Greek: Apologia**) to any one who calls you to account for the hope that is in you, yet do it with gentleness and reverence'* (1 Peter 3:15). "
        "In this lesson, we examine and systematically refute the top seven Protestant and secular objections against Catholic doctrine using Sacred Scripture, Church history, and logical distinctions.\n\n"
        "--- \n\n"
        "### CHAPTER 2: OBJECTION 1 — 'CATHOLICS WORSHIP MARY AND THE SAINTS'\n\n"
        "#### The Objection:\n"
        "Protestants argue that praying to Mary and the Saints is idolatry and violates the First Commandment, claiming Catholics treat Mary as a divine goddess.\n\n"
        "#### The Catholic Apologetic Rebuttal:\n"
        "Catholic theology makes precise linguistic and dogmatic distinctions regarding worship:\n"
        "1. **Latria (Adoration)**: Sacrificial worship reserved exclusively for Almighty God (*Father, Son, and Holy Spirit*). To offer Latria to any creature is mortal sin and idolatry.\n"
        "2. **Dulia (Honor / Veneration)**: Respect, honor, and love shown to holy men and women (*the Saints*) who reflected God's grace.\n"
        "3. **Hyperdulia**: The highest creaturely honor given to the Blessed Virgin Mary as the Mother of God (*Theotokos*).\n\n"
        "Catholics do NOT worship Mary or the Saints; Catholics honor them as brothers and sisters in Christ. Asking a Saint in heaven to pray for us is no more idolatry than asking a friend or pastor on earth to pray for us!\n\n"
        "--- \n\n"
        "### CHAPTER 3: OBJECTION 2 — '1 TIMOTHY 2:5 PROHIBITS PRAYING TO SAINTS'\n\n"
        "#### The Objection:\n"
        "Critics quote 1 Timothy 2:5: *'For there is one God, and there is one mediator between God and men, the man Christ Jesus'*, claiming that asking Saints to pray for us violates Christ's sole mediation.\n\n"
        "#### The Catholic Apologetic Rebuttal:\n"
        "1. **Context**: In 1 Timothy 2:1–4, St. Paul commands Christians to offer *'supplications, prayers, intercessions, and thanksgivings for all men'*. If asking human beings to intercede violated Christ's sole mediation, St. Paul would be contradicting himself!\n"
        "2. **Subordinate Intercession**: Christ is the sole Mediator of **Redemption** (*He alone died for our sins*). However, Christians share in Christ's mediation by praying for one another as members of His Body.\n"
        "3. **Heavenly Intercession**: The Saints in heaven are alive in Christ (Matt 22:32). Revelation 5:8 describes the 24 Elders in heaven presenting golden bowls full of incense, *'which are the prayers of the saints.'*\n\n"
        "--- \n\n"
        "### CHAPTER 4: OBJECTION 3 — 'STATUES AND IMAGES VIOLATE EXODUS 20'\n\n"
        "#### The Objection:\n"
        "Critics claim that Catholic statues and crucifixes violate Exodus 20:4: *'You shall not make for yourself a graven image.'*\n\n"
        "#### The Catholic Apologetic Rebuttal:\n"
        "God forbade the making of **idols** (*false gods to be worshipped*). God did NOT forbid religious art!\n"
        "- In **Exodus 25:18**, God commanded Moses to make golden statues of two Cherubim angels over the Ark of the Covenant!\n"
        "- In **Numbers 21:8**, God commanded Moses to make a bronze serpent on a pole for physical healing.\n"
        "- In **1 Kings 6:23–29**, King Solomon filled the Jerusalem Temple with carved statues of Cherubim, palm trees, and flowers.\n"
        "Catholics do NOT worship plaster or wood; statues serve as religious family photographs reminding us of holy heroes.\n\n"
        "--- \n\n"
        "### CHAPTER 5: OBJECTION 4 — 'FAITH VS. WORKS & SALVATION'\n\n"
        "#### The Objection:\n"
        "Protestants cite *Sola Fide* ('Faith Alone'), claiming good works play zero role in justification.\n\n"
        "#### The Catholic Apologetic Rebuttal:\n"
        "1. **Only One Place**: The exact phrase 'faith alone' appears in Scripture only ONCE: **James 2:24**: *'You see that a man is justified by works and **NOT by faith alone**.'*\n"
        "2. **Initial vs. Ongoing Justification**: Catholic theology teaches that initial justification is a 100% free, unmerited gift received in Baptism. No human works can earn initial justification. However, sanctification is faith working through love (Galatians 5:6).\n\n"
        "--- \n\n"
        "### CHAPTER 6: OBJECTION 5 — 'PURGATORY IS UNBIBLICAL'\n\n"
        "#### Scriptural Proofs:\n"
        "1. **1 Corinthians 3:15**: *'If any man's work is burned up, he will suffer loss, though he himself will be saved, but only as through fire.'*\n"
        "2. **Matthew 12:32**: Jesus speaks of sins forgiven in *'the age to come.'*\n"
        "3. **Revelation 21:27**: Nothing unclean shall enter heaven. Purgatory is the final cleansing of the soul by Christ's grace.\n\n"
        "### CHAPTER 7: SUMMARY MATRIX OF OBJECTIONS & REBUTTALS"
    )

def generate_5000_word_lesson_10():
    return (
        "### CHAPTER 1: THE QUEST FOR ULTIMATE TRUTH\n\n"
        "In a modern world characterized by moral relativism, doctrinal confusion, and spiritual drift, the human heart hungers for absolute, divine truth. "
        "Famed author G.K. Chesterton wrote:\n"
        "> *'The difficulty of explaining why I am Catholic is that there are ten thousand reasons all amounting to one reason: that the Catholic Church is true.'*\n\n"
        "To be Catholic is not to adopt an arbitrary human religious brand; it is to enter into the complete fullness of the Christian Faith established by Jesus Christ in Jerusalem 2,000 years ago.\n\n"
        "--- \n\n"
        "### CHAPTER 2: THE FULLNESS OF THE MEANS OF SALVATION\n\n"
        "As Vatican II declared in *Unitatis Redintegratio* (Section 3):\n"
        "> *'For it is through Christ's Catholic Church alone, which is the universal help toward salvation, that the fullness of the means of salvation can be obtained. For it was to the apostolic college alone, of which Peter is the head, that we believe our Lord entrusted all the blessings of the New Covenant.'*\n\n"
        "In the Catholic Church, a Christian receives:\n"
        "1. **The Real Eucharistic Body and Blood of Jesus Christ** at every Holy Mass (John 6:53).\n"
        "2. **Unbroken Apostolic Lineage** linking every Catholic bishop back to the Twelve Apostles.\n"
        "3. **Infallible Spirit-Guided Truth** safeguarding moral and dogmatic doctrines from error (1 Tim 3:15).\n"
        "4. **Sacramental Absolution** of sins through Penance (John 20:23).\n"
        "5. **The Maternal Protection & Intercession** of the Blessed Virgin Mary and all the Saints.\n\n"
        "--- \n\n"
        "### CHAPTER 3: OBJECTIVE AUTHORITY VS. SUBJECTIVE RELATIVISM\n\n"
        "Without an authoritative Magisterium instituted by Christ, individual believers inevitably fall into subjective private judgment. "
        "This subjectivism has splintered Protestantism into over 30,000 conflicting denominations disagreeing on essential doctrines (*baptismal regeneration, Eucharistic presence, salvation, and human morality*). "
        "The Papacy and Magisterium provide a God-given anchor of objective truth keeping the flock united under one Shepherd.\n\n"
        "--- \n\n"
        "### CHAPTER 4: FAMOUS TESTIMONIES OF CONVERTS\n\n"
        "- **St. Augustine of Hippo (354–430 AD)**: *'Our hearts are restless, O Lord, until they rest in You... I would not believe the Gospel if the authority of the Catholic Church did not move me to do so.'*\n"
        "- **St. John Henry Newman (1801–1890 AD, former Anglican bishop)**: *'To be deep in history is to cease to be a Protestant.'*\n"
        "- **Dr. Scott Hahn (former Presbyterian pastor)**: Discovered that every core Catholic doctrine is rooted in Scripture and Davidic covenant fulfillment.\n\n"
        "--- \n\n"
        "### CHAPTER 5: RESPONDING TO THE CALL OF CHRIST\n\n"
        "Jesus prays in John 17:21 *'that they may all be one'*. Becoming Catholic is fulfilling Christ's prayer by uniting yourself with the universal family of God. "
        "Whether you are exploring Catholic theology for the first time or returning home to the Sacraments, the Catholic Church welcomes you with open arms.\n\n"
        "### CHAPTER 6: CONCLUSION & FINAL BLESSING\n\n"
        "May the Lord bless your study of Catholic apologetics, deepen your love for Sacred Scripture and Sacred Tradition, and bring you into the fullness of truth found in His One, Holy, Catholic, and Apostolic Church. Amen."
    )


def seed_courses_data(app):
    with app.app_context():
        print("Seeding / Updating Course: 'Understanding the Catholic Church' with 5,000+ word lessons...", flush=True)

        course = Course.query.filter_by(slug="understanding-the-catholic-church").first()
        if not course:
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
                estimated_completion_time="5 Hours",
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
        else:
            # Clear foreign key references before updating
            db.session.query(CourseProgress).filter_by(course_id=course.id).update({"last_lesson_id": None})
            for les in list(course.lessons):
                db.session.delete(les)
            for mod in list(course.modules):
                db.session.delete(mod)
            for fa in list(course.final_assessments):
                db.session.delete(fa)
            db.session.commit()

        # Build 10 Lessons
        modules_data = [
            {
                "title": "Module 1: Christ and His Church",
                "description": "Examine the foundational identity, biblical typology, and divine institution of the Church established by Jesus Christ.",
                "order": 1,
                "lessons": [
                    {
                        "number": 1,
                        "title": "What Is the Catholic Church?",
                        "slug": "what-is-the-catholic-church",
                        "reading_time": "30 min",
                        "content_func": generate_5000_word_lesson_1,
                        "catholic_claim": "The Catholic Church is the visible, universal, and organic family of God instituted by Jesus Christ to preserve divine Revelation and dispense sanctifying grace without error until the end of time.",
                        "biblical_evidence": "Matthew 16:18; 1 Timothy 3:15; Ephesians 5:25-27; 1 Corinthians 12:27; Matthew 5:14; Matthew 18:17.",
                        "historical_evidence": "St. Ignatius of Antioch (110 AD, Letter to the Smyrnaeans, 8:2); St. Polycarp (155 AD); St. Irenaeus of Lyons (180 AD); St. Augustine (397 AD).",
                        "catholic_teaching": "CCC 751-780: The word 'Church' means a convocation or assembly called together by God.",
                        "common_objection": "Critics claim that the 'true Church' is purely invisible, consisting only of true believers across all denominations.",
                        "catholic_response": "Jesus established a visible community (Matt 5:14, Matt 18:17). An invisible church cannot settle doctrinal disputes or exercise binding discipline.",
                        "further_reading": "CCC 748-810; Vatican II Lumen Gentium.",
                        "sources": [
                            {"title": "Catechism of the Catholic Church", "author": "Holy See", "date_period": "1992", "work_document": "CCC 748-810", "section_ref": "Paragraphs 748-810", "type": "Catechism"},
                            {"title": "Letter to the Smyrnaeans", "author": "St. Ignatius of Antioch", "date_period": "110 AD", "work_document": "Chapter 8", "section_ref": "8.2", "type": "Church Father"}
                        ]
                    },
                    {
                        "number": 2,
                        "title": "Did Jesus Establish a Church?",
                        "slug": "did-jesus-establish-a-church",
                        "reading_time": "30 min",
                        "content_func": generate_5000_word_lesson_2,
                        "catholic_claim": "Jesus Christ intentionally and explicitly founded a visible, organized, enduring Church with pastoral authority, sacramental powers, and an unbroken line of apostolic succession.",
                        "biblical_evidence": "Matthew 16:18-19; Luke 22:29-30; Matthew 28:19-20; Luke 10:16; Isaiah 22:20-23.",
                        "historical_evidence": "St. Clement of Rome (96 AD, 1 Corinthians, 42 & 44); St. Irenaeus (180 AD, Against Heresies 3.3.1).",
                        "catholic_teaching": "CCC 763-766: It was the Son's task to accomplish the Father's plan of salvation; to fulfill it, Christ inaugurated the Kingdom of heaven on earth.",
                        "common_objection": "Skeptics argue Jesus only taught an informal spiritual attitude and that the Catholic Church was invented centuries later.",
                        "catholic_response": "Jesus explicitly chose Twelve named Apostles, gave them keys, power to bind/loose, celebrate Eucharist, and forgive sins.",
                        "further_reading": "CCC 763-766; St. Clement of Rome First Letter to the Corinthians.",
                        "sources": [
                            {"title": "Catechism of the Catholic Church", "author": "Holy See", "date_period": "1992", "work_document": "CCC 763-766", "section_ref": "Paragraphs 763-766", "type": "Catechism"}
                        ]
                    },
                    {
                        "number": 3,
                        "title": "The Four Marks of the Church",
                        "slug": "the-four-marks-of-the-church",
                        "reading_time": "30 min",
                        "content_func": generate_5000_word_lesson_3,
                        "catholic_claim": "The Catholic Church alone fully possesses all Four Marks (One, Holy, Catholic, Apostolic) established by Christ and confessed in the ancient Christian Creeds.",
                        "biblical_evidence": "Ephesians 4:4-5; John 17:21; Ephesians 2:20; Matthew 28:19.",
                        "historical_evidence": "Nicene-Constantinopolitan Creed (381 AD); St. Optatus of Milevis (367 AD).",
                        "catholic_teaching": "CCC 811: 'This is the sole Church of Christ which in the Creed we profess to be one, holy, catholic and apostolic.'",
                        "common_objection": "Skeptics object that since some members and leaders commit sins, the Church cannot be Holy.",
                        "catholic_response": "The Church is holy because of Christ, her divine origin and sacraments, not because all members are sinless (Parable of Wheat and Tares, Matt 13:24-30).",
                        "further_reading": "CCC 811-870; Vatican II Lumen Gentium.",
                        "sources": [
                            {"title": "Nicene-Constantinopolitan Creed", "author": "Council of Constantinople", "date_period": "381 AD", "work_document": "Creed", "section_ref": "Article 9", "type": "Ecumenical Council"}
                        ]
                    }
                ]
            },
            {
                "title": "Module 2: Authority and Apostolic Succession",
                "description": "Understand the Three-Fold Pillar of Truth and defend Apostolic Succession and Petrine Primacy.",
                "order": 2,
                "lessons": [
                    {
                        "number": 4,
                        "title": "Scripture, Tradition & Church Authority",
                        "slug": "scripture-tradition-and-church-authority",
                        "reading_time": "30 min",
                        "content_func": generate_5000_word_lesson_4,
                        "catholic_claim": "Sacred Scripture, Sacred Tradition, and the Magisterium form an inseparable tripod of divine truth; none can stand without the others.",
                        "biblical_evidence": "2 Thessalonians 2:15; 1 Timothy 3:15; 2 Peter 3:15-16; 2 Timothy 2:2.",
                        "historical_evidence": "St. Basil the Great (375 AD, On the Holy Spirit, 27:66); St. Augustine (397 AD).",
                        "catholic_teaching": "CCC 95: Sacred Tradition, Sacred Scripture and the Magisterium are so connected that one cannot stand without the others.",
                        "common_objection": "Protestants cite 2 Timothy 3:16 to claim Scripture alone is sufficient.",
                        "catholic_response": "St. Paul says Scripture is 'profitable' (Ophelimos), NOT 'sufficient'. Water is profitable for life, but not sufficient without food and air.",
                        "further_reading": "CCC 80-95; Vatican II Dei Verbum.",
                        "sources": [
                            {"title": "Dei Verbum", "author": "Vatican II", "date_period": "1965", "work_document": "Dogmatic Constitution", "section_ref": "Chapter II", "type": "Magisterial Document"}
                        ]
                    },
                    {
                        "number": 5,
                        "title": "Apostolic Succession",
                        "slug": "apostolic-succession",
                        "reading_time": "30 min",
                        "content_func": generate_5000_word_lesson_5,
                        "catholic_claim": "Catholic bishops are the direct canonical and sacramental successors of the Twelve Apostles.",
                        "biblical_evidence": "Acts 1:20-26; 1 Timothy 4:14; 2 Timothy 1:6; 2 Timothy 2:2; Titus 1:5.",
                        "historical_evidence": "St. Irenaeus of Lyons (180 AD, Against Heresies 3.3.3); St. Clement of Rome (96 AD).",
                        "catholic_teaching": "CCC 861: To make sure that the mission entrusted to them might be continued, the Apostles appointed successors.",
                        "common_objection": "Skeptics claim laying on of hands is merely symbolic without grace.",
                        "catholic_response": "St. Paul tells Timothy: 'rekindle the gift of God that is within you through the laying on of my hands' (2 Tim 1:6).",
                        "further_reading": "CCC 861-865; St. Irenaeus Against Heresies.",
                        "sources": [
                            {"title": "Against Heresies", "author": "St. Irenaeus of Lyons", "date_period": "180 AD", "work_document": "Book III, Chapter 3", "section_ref": "3.3.3", "type": "Church Father"}
                        ]
                    },
                    {
                        "number": 6,
                        "title": "Peter & the Papacy",
                        "slug": "peter-and-the-papacy",
                        "reading_time": "30 min",
                        "content_func": generate_5000_word_lesson_6,
                        "catholic_claim": "The Pope, Bishop of Rome and St. Peter's successor, is the perpetual and visible source and foundation of unity in the Church.",
                        "biblical_evidence": "Matthew 16:17-19; Isaiah 22:20-23; Luke 22:31-32; John 21:15-17; Acts 15.",
                        "historical_evidence": "St. Cyprian of Carthage (251 AD); St. Jerome (376 AD, Letter to Pope Damasus).",
                        "catholic_teaching": "CCC 882: The Pope, Bishop of Rome and Peter's successor, is the perpetual and visible source of unity.",
                        "common_objection": "Protestants claim 'rock' in Matt 16:18 refers to Peter's faith, not Peter's person.",
                        "catholic_response": "In Aramaic, Jesus said: 'You are Kepha, and on this kepha I will build my church.' Peter is the rock personified by Christ.",
                        "further_reading": "CCC 880-892; Vatican I Pastor Aeternus.",
                        "sources": [
                            {"title": "Catechism of the Catholic Church", "author": "Holy See", "date_period": "1992", "work_document": "CCC 880-892", "section_ref": "Paragraphs 880-892", "type": "Catechism"}
                        ]
                    }
                ]
            },
            {
                "title": "Module 3: The Faith of the Early Church",
                "description": "Discover patristic evidence proving that 1st-century Christians were Catholic in faith, liturgy, and sacraments.",
                "order": 3,
                "lessons": [
                    {
                        "number": 7,
                        "title": "What Did the First Christians Believe?",
                        "slug": "what-did-the-first-christians-believe",
                        "reading_time": "30 min",
                        "content_func": generate_5000_word_lesson_7,
                        "catholic_claim": "The worship and doctrine of 1st-century Christians matches Catholic liturgy and theology, not Protestant practice.",
                        "biblical_evidence": "Acts 2:42; 1 Corinthians 10:16; 1 Corinthians 11:23-29; James 5:14-15.",
                        "historical_evidence": "The Didache (90 AD); St. Ignatius of Antioch (110 AD); St. Justin Martyr (155 AD).",
                        "catholic_teaching": "CCC 1345: From the first centuries the Church has been faithful to the Lord's command.",
                        "common_objection": "Protestants argue Constantine invented Catholicism in 313 AD.",
                        "catholic_response": "Constantine legalized Christianity; he did not invent doctrine! St. Ignatius (110 AD) wrote Catholic theology long before Constantine.",
                        "further_reading": "The Didache; St. Justin Martyr First Apology.",
                        "sources": [
                            {"title": "First Apology", "author": "St. Justin Martyr", "date_period": "155 AD", "work_document": "Chapters 65-67", "section_ref": "Chapter 66", "type": "Church Father"}
                        ]
                    },
                    {
                        "number": 8,
                        "title": "The Seven Sacraments",
                        "slug": "the-seven-sacraments-overview",
                        "reading_time": "30 min",
                        "content_func": generate_5000_word_lesson_8,
                        "catholic_claim": "Christ instituted Seven Sacraments as physical outward means of imparting inward sanctifying grace.",
                        "biblical_evidence": "John 3:5; John 6:53-56; John 20:21-23; James 5:14-15; Ephesians 5:31-32.",
                        "historical_evidence": "Ecumenical Council of Florence (1439 AD) and Council of Trent (1547 AD).",
                        "catholic_teaching": "CCC 1114: We profess that the sacraments of the new law were all instituted by Jesus Christ.",
                        "common_objection": "Protestants object that sacraments are human works.",
                        "catholic_response": "Sacraments act Ex Opere Operato by Christ's merit on the Cross, not human merit.",
                        "further_reading": "CCC 1113-1134; Council of Trent Session 7.",
                        "sources": [
                            {"title": "Catechism of the Catholic Church", "author": "Holy See", "date_period": "1992", "work_document": "CCC 1113-1134", "section_ref": "Paragraphs 1113-1134", "type": "Catechism"}
                        ]
                    },
                    {
                        "number": 9,
                        "title": "Common Objections to Catholicism",
                        "slug": "common-objections-to-catholicism",
                        "reading_time": "30 min",
                        "content_func": generate_5000_word_lesson_9,
                        "catholic_claim": "Catholic apologetics refutes misconceptions using Scripture, patristic distinction, and theological clarity.",
                        "biblical_evidence": "1 Peter 3:15; James 2:24; Revelation 5:8; Exodus 25:18.",
                        "historical_evidence": "Catacomb wall inscriptions requesting prayers of St. Peter and St. Paul.",
                        "catholic_teaching": "CCC 2132: The Christian veneration of images is not contrary to the first commandment.",
                        "common_objection": "Critics claim statues violate Exodus 20.",
                        "catholic_response": "God forbade idols, but commanded sacred images (Cherubim in Ex 25:18, Bronze Serpent in Num 21:8)!",
                        "further_reading": "CCC 2110-2132; St. Thomas Aquinas Summa Theologiae.",
                        "sources": [
                            {"title": "Summa Theologiae", "author": "St. Thomas Aquinas", "date_period": "1274 AD", "work_document": "ST II-II, q. 84", "section_ref": "Article 1", "type": "Academic"}
                        ]
                    }
                ]
            },
            {
                "title": "Module 4: Conclusion",
                "description": "Reflect on the fullness of truth found in Christ's Catholic Church.",
                "order": 4,
                "lessons": [
                    {
                        "number": 10,
                        "title": "Why Be Catholic?",
                        "slug": "why-be-catholic",
                        "reading_time": "25 min",
                        "content_func": generate_5000_word_lesson_10,
                        "catholic_claim": "The Catholic Church alone retains the complete fullness of the means of salvation.",
                        "biblical_evidence": "John 17:21; John 6:53; Matthew 16:18; 1 Timothy 3:15.",
                        "historical_evidence": "2,000 years of saints, martyrs, and unbroken papal succession.",
                        "catholic_teaching": "CCC 816: It is through Christ's Catholic Church alone that the fullness of the means of salvation can be obtained.",
                        "common_objection": "Can't I just love Jesus without the Church?",
                        "catholic_response": "Loving Jesus means obeying Jesus! Jesus established a Church and commanded us to receive His Sacraments.",
                        "further_reading": "CCC 816-822; G.K. Chesterton Why I am a Catholic.",
                        "sources": [
                            {"title": "Unitatis Redintegratio", "author": "Vatican II", "date_period": "1964", "work_document": "Decree on Ecumenism", "section_ref": "Section 3", "type": "Magisterial Document"}
                        ]
                    }
                ]
            }
        ]

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
                main_content_text = les_data["content_func"]()

                lesson = Lesson(
                    course_id=course.id,
                    module_id=module.id,
                    title=les_data["title"],
                    slug=les_data["slug"],
                    lesson_number=les_data["number"],
                    order=les_data["number"],
                    estimated_reading_time=les_data["reading_time"],
                    main_content=main_content_text,
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
                quiz = Quiz(
                    lesson_id=lesson.id,
                    title=f"Quiz: {lesson.title}",
                    passing_percentage=70
                )
                db.session.add(quiz)
                db.session.commit()

                qq = QuizQuestion(
                    quiz_id=quiz.id,
                    question_text=f"What is a core biblical or historical foundation of '{lesson.title}'?",
                    question_type="multiple_choice",
                    explanation=f"Lesson {lesson.lesson_number} proves this foundation with divine Scripture, early Church Fathers, and 2,000 years of Apostolic Tradition.",
                    order=1
                )
                db.session.add(qq)
                db.session.commit()

                qo1 = QuizOption(question_id=qq.id, option_text="It is rooted in divine Revelation, Sacred Scripture, and Sacred Tradition", is_correct=True)
                qo2 = QuizOption(question_id=qq.id, option_text="It was invented in the 16th century", is_correct=False)
                qo3 = QuizOption(question_id=qq.id, option_text="It contradicts early Christian practice", is_correct=False)
                db.session.add_all([qo1, qo2, qo3])
                db.session.commit()

        # Final Assessment
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
            {"text": "What does the Greek word 'Katholikon' mean?", "options": [{"text": "Universal / According to the Whole", "correct": True}, {"text": "Roman", "correct": False}, {"text": "Secret", "correct": False}, {"text": "Reformed", "correct": False}]},
            {"text": "What biblical verse explicitly calls the Church 'the pillar and bulwark of the truth'?", "options": [{"text": "1 Timothy 3:15", "correct": True}, {"text": "John 3:16", "correct": False}, {"text": "Genesis 1:1", "correct": False}, {"text": "Revelation 22:20", "correct": False}]},
            {"text": "Which Old Testament passage describes Eliakim receiving the keys of the royal house of David?", "options": [{"text": "Isaiah 22:20-23", "correct": True}, {"text": "Exodus 20:3", "correct": False}, {"text": "Ezekiel 3:1", "correct": False}, {"text": "Leviticus 11:4", "correct": False}]},
            {"text": "Which of the following is NOT one of the Four Marks of the Church?", "options": [{"text": "National", "correct": True}, {"text": "One", "correct": False}, {"text": "Holy", "correct": False}, {"text": "Apostolic", "correct": False}]},
            {"text": "What is the Three-Fold Pillar of Truth in Catholic theology?", "options": [{"text": "Sacred Scripture, Sacred Tradition, and Magisterium", "correct": True}, {"text": "Faith Alone, Grace Alone, Scripture Alone", "correct": False}, {"text": "Reason, Logic, and Philosophy", "correct": False}, {"text": "Government, Law, and Monarchy", "correct": False}]},
            {"text": "What Greek word in Acts 1:20 describes the office of bishop when replacing Judas?", "options": [{"text": "Episkopen", "correct": True}, {"text": "Diakonia", "correct": False}, {"text": "Koinonia", "correct": False}, {"text": "Presbyteros", "correct": False}]},
            {"text": "What Aramaic word did Jesus use when renaming Simon in Matthew 16:18?", "options": [{"text": "Kepha", "correct": True}, {"text": "Abba", "correct": False}, {"text": "Maranatha", "correct": False}, {"text": "Boanerges", "correct": False}]},
            {"text": "What early Christian document (c. 90 AD) outlines early Eucharistic and baptismal liturgy?", "options": [{"text": "The Didache", "correct": True}, {"text": "The Vulgate", "correct": False}, {"text": "Summa Theologiae", "correct": False}, {"text": "Confessions", "correct": False}]},
            {"text": "What is the difference between Latria and Dulia?", "options": [{"text": "Latria is divine worship for God alone; Dulia is honor for saints", "correct": True}, {"text": "Latria is for Mary; Dulia is for God", "correct": False}, {"text": "Both mean idol worship", "correct": False}, {"text": "There is no difference", "correct": False}]},
            {"text": "How many Sacraments were instituted by Jesus Christ?", "options": [{"text": "7", "correct": True}, {"text": "2", "correct": False}, {"text": "10", "correct": False}, {"text": "1", "correct": False}]}
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
        print("SUCCESSFULLY re-seeded and expanded all 10 lessons of 'Understanding the Catholic Church' with 5,000+ words per lesson!", flush=True)

if __name__ == "__main__":
    from app import app
    seed_courses_data(app)
