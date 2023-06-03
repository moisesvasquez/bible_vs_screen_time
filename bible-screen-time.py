import streamlit as st
import pandas as pd

# Define the Bible books and their word counts and chapter counts
bible_books = {
    "Genesis": {"word_count": 38278, "chapter_count": 50},
    "Exodus": {"word_count": 32392, "chapter_count": 40},
    "Leviticus": {"word_count": 24889, "chapter_count": 27},
    "Numbers": {"word_count": 32701, "chapter_count": 36},
    "Deuteronomy": {"word_count": 28311, "chapter_count": 34},
    "Joshua": {"word_count": 18939, "chapter_count": 24},
    "Judges": {"word_count": 18474, "chapter_count": 21},
    "Ruth": {"word_count": 2307, "chapter_count": 4},
    "1 Samuel": {"word_count": 25346, "chapter_count": 31},
    "2 Samuel": {"word_count": 24769, "chapter_count": 24},
    "1 Kings": {"word_count": 24566, "chapter_count": 22},
    "2 Kings": {"word_count": 23736, "chapter_count": 25},
    "1 Chronicles": {"word_count": 20493, "chapter_count": 29},
    "2 Chronicles": {"word_count": 26325, "chapter_count": 36},
    "Ezra": {"word_count": 10155, "chapter_count": 10},
    "Nehemiah": {"word_count": 16935, "chapter_count": 13},
    "Esther": {"word_count": 9818, "chapter_count": 10},
    "Job": {"word_count": 18046, "chapter_count": 42},
    "Psalms": {"word_count": 43023, "chapter_count": 150},
    "Proverbs": {"word_count": 15071, "chapter_count": 31},
    "Ecclesiastes": {"word_count": 5776, "chapter_count": 12},
    "Song of Solomon": {"word_count": 2126, "chapter_count": 8},
    "Isaiah": {"word_count": 37060, "chapter_count": 66},
    "Jeremiah": {"word_count": 43104, "chapter_count": 52},
    "Lamentations": {"word_count": 3235, "chapter_count": 5},
    "Ezekiel": {"word_count": 39336, "chapter_count": 48},
    "Daniel": {"word_count": 18301, "chapter_count": 12},
    "Hosea": {"word_count": 5583, "chapter_count": 14},
    "Joel": {"word_count": 2030, "chapter_count": 3},
    "Amos": {"word_count": 4421, "chapter_count": 9},
    "Obadiah": {"word_count": 669, "chapter_count": 1},
    "Jonah": {"word_count": 1466, "chapter_count": 4},
    "Micah": {"word_count": 4418, "chapter_count": 7},
    "Nahum": {"word_count": 2043, "chapter_count": 3},
    "Habakkuk": {"word_count": 2219, "chapter_count": 3},
    "Zephaniah": {"word_count": 2317, "chapter_count": 3},
    "Haggai": {"word_count": 1571, "chapter_count": 2},
    "Zechariah": {"word_count": 8336, "chapter_count": 14},
    "Malachi": {"word_count": 1878, "chapter_count": 4},
    "Matthew": {"word_count": 18623, "chapter_count": 28},
    "Mark": {"word_count": 11560, "chapter_count": 16},
    "Luke": {"word_count": 19745, "chapter_count": 24},
    "John": {"word_count": 15489, "chapter_count": 21},
    "Acts": {"word_count": 24541, "chapter_count": 28},
    "Romans": {"word_count": 9427, "chapter_count": 16},
    "1 Corinthians": {"word_count": 11699, "chapter_count": 16},
    "2 Corinthians": {"word_count": 8374, "chapter_count": 13},
    "Galatians": {"word_count": 3565, "chapter_count": 6},
    "Ephesians": {"word_count": 3089, "chapter_count": 6},
    "Philippians": {"word_count": 2909, "chapter_count": 4},
    "Colossians": {"word_count": 2733, "chapter_count": 4},
    "1 Thessalonians": {"word_count": 2466, "chapter_count": 5},
    "2 Thessalonians": {"word_count": 1623, "chapter_count": 3},
    "1 Timothy": {"word_count": 3261, "chapter_count": 6},
    "2 Timothy": {"word_count": 2505, "chapter_count": 4},
    "Titus": {"word_count": 1315, "chapter_count": 3},
    "Philemon": {"word_count": 430, "chapter_count": 1},
    "Hebrews": {"word_count": 12495, "chapter_count": 13},
    "James": {"word_count": 2445, "chapter_count": 5},
    "1 Peter": {"word_count": 2558, "chapter_count": 5},
    "2 Peter": {"word_count": 1523, "chapter_count": 3},
    "1 John": {"word_count": 2500, "chapter_count": 5},
    "2 John": {"word_count": 298, "chapter_count": 1},
    "3 John": {"word_count": 294, "chapter_count": 1},
    "Jude": {"word_count": 608, "chapter_count": 1},
    "Revelation": {"word_count": 11952, "chapter_count": 22}
}


def calculate_reading_progress(reading_speed, screen_time, starting_book):
    # Convert screen time to minutes
    screen_time_minutes = sum(x * int(t) for x, t in zip([60, 1, 1/60], screen_time.split(':')))
    
    # Calculate the number of words the user could have read
    words_read = reading_speed * screen_time_minutes
    
    # Calculate the reading progress
    progress = []
    
    for book, info in bible_books.items():
        if book == starting_book:
            words_read_book = min(info["word_count"], words_read)
            chapters_read_book = round((words_read_book / info["word_count"]) * info["chapter_count"])
            
            if words_read_book > 0:
                completion_percentage = (words_read_book / info["word_count"]) * 100
                progress.append({
                    "Book": book,
                    "Words Read": words_read_book,
                    "Completion (%)": round(completion_percentage, 2),
                    "Chapters Read": chapters_read_book
                })
        
        elif sum(p["Words Read"] for p in progress) > 0:
            words_read_book = min(info["word_count"], words_read - sum(p["Words Read"] for p in progress))
            chapters_read_book = round((words_read_book / info["word_count"]) * info["chapter_count"])
            
            if words_read_book > 0:
                completion_percentage = (words_read_book / info["word_count"]) * 100
                progress.append({
                    "Book": book,
                    "Words Read": words_read_book,
                    "Completion (%)": round(completion_percentage, 2),
                    "Chapters Read": chapters_read_book
                })
    
    return progress

# Streamlit app layout
st.title("Bible vs Screen Time Calculator")

st.subheader('Fill the form below to find out how much of The Bible you could have read in the time you spent on your phone (or other activities).')
st.markdown('An average reading speed is about 250 WPM, if you want a more accurate words per minute score you can use this website: [SwiftRead](https://swiftread.com/reading-speed-test)')

reading_speed = st.number_input("Reading Speed (words per minute)", min_value=1, value=250)
screen_time = st.text_input("Screen Time", value="01:30:00")
starting_book = st.selectbox("Starting Book", list(bible_books.keys()))

# Calculate progress on button click
if st.button("Calculate"):
    progress = calculate_reading_progress(reading_speed, screen_time, starting_book)
    
    # Create a DataFrame from the progress list
    df = pd.DataFrame(progress)
    df = df[["Book", "Words Read", "Completion (%)", "Chapters Read"]]
    df.set_index("Book", inplace=True)
    
    st.subheader("Reading Progress")
    st.dataframe(df)

# Add a footer with a link
# footer = 'Developed by [moisesvasquez.io](https://moisesvasquez.io/) using ChatGPT'
# Custom footer HTML and CSS
footer_html = """
<div style="position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0E1117; padding: 10px; text-align: center; font-size: 10px;">
    <style>
        .footer-link {
            color: #262730;
            font-size: 12px;
            text-decoration: none;
            margin-right: 5px;
        }
    </style>
    <span>Developed by <a href="https://moisesvasquez.io/" target="_blank" class="footer-link">moisesvasquez.io</a> using ChatGPT</span>
</div>
"""

# Display the custom footer
st.markdown(footer_html, unsafe_allow_html=True)