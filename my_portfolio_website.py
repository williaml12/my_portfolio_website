import streamlit as st

from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
# model = genai.GenerativeModel('gemini-1.5-flash')
model = genai.GenerativeModel("gemini-2.5-flash")

st.markdown("<a id='top'></a>", unsafe_allow_html=True)


with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'AI Assistant', 'Projects', 'Contact'],
        icons=['person-bounding-box', 'info-square-fill', 'grid-fill', 'chat-text-fill'],
        orientation='horizontal'
    )





if selected == 'About':
    # st.markdown("<a id='top'></a>", unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Hi :wave:,")
            st.title("I am William Lu")
            st.write("A motivated biomedical engineering graduate with a versatile skill set and a strong passion for "
                     "research in computational applied aerodynamics and finite element analysis. Experienced in "
                     "product "
                     "design, CAD modeling, assembly, and QA testing, with a proven background in computer vision, "
                     "machine learning object detection, and data analysis. Seeking opportunities to contribute to "
                     "cutting-edge research in fluid mechanics, aerodynamics, and aerospace technology."
                    )
            # st.write("Get in touch by emailing me at luwei2359@gmail.com")
            if st.button("Get In Touch"):
                st.write("luwei2359@gmail.com")
            # st.link_button("Get In Touch", "https://mail.google.com/mail/u/0/#inbox?compose=CllgCJqTfmBCsDqXWvzGZxHNMSxcZJlvxmjkcDcFbNNmwLSnzLpbdzCBtbnxhDDshWtvDkJHblq")
            # st.link_button("Get In Touch", "https://luwei2359@gmail.com")
            
        with col2:
            st.title(" ")
            st.img = st.image("my images/ChatGPT Image 2.png")

        # st.title(" ")
                        
        st.write('---')
        # st.title(" ")

        # st.write(" ")
        
        st.title("🧠My Skills")

        col3, col4 = st.columns(2)
        with col3:
            # st.slider("Programming", 0, 100, 85)
            # st.slider("3D Printing", 0, 100, 85)
            # st.slider("Problem Solving", 0, 100, 90)
            # st.slider("Mathematical Modeling", 0, 100, 80)

            # Define the skills and their levels

            skills = {
                "Computer Vision": 80,
                "Programming": 85,
                "Chinese Mandarin": 97,
                "Problem Solving": 90,
                "Arduino": 85,
            }

            # Function to create a skill bar
            def create_skill_bar(skill, level):
                return f"""
                <div style="width: 100%; background-color: #e1e1e1; height: 30px; border-radius: 15px; position: relative; margin-top: 10px; margin-bottom: 10px;">
                    <div style="width: {level}%; background-color: #4CAF50; height: 100%; border-radius: 15px;"></div>
                    <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); color: white; font-weight: bold; line-height: 30px;">
                        <span>{level}%</span>
                    </div>
                    <div style="position: absolute; top: 0; left: 10px; color: black; font-weight: bold; line-height: 30px;">
                        <span>{skill}</span>
                    </div>
                </div>
                """


            for skill, level in skills.items():
                st.markdown(create_skill_bar(skill, level), unsafe_allow_html=True)

        with col4:
            # st.slider("Finite Element Analysis (FEA)", 0, 100, 75)
            # st.slider("Computer Vision", 0, 100, 75)
            # st.slider("Simulations", 0, 100, 80)
            # st.slider("CAD modeling", 0, 100, 75)

            skills = {
                "FEA": 80,
                "3D Printing": 80,
                "Prototyping": 75,
                "CFD": 80,
                "CAD modeling": 75,
            }

            # Function to create a skill bar
            def create_skill_bar(skill, level):
                return f"""
                            <div style="width: 100%; background-color: #e1e1e1; height: 30px; border-radius: 15px; position: relative; margin-top: 10px; margin-bottom: 10px;">
                                <div style="width: {level}%; background-color: #4CAF50; height: 100%; border-radius: 15px;"></div>
                                <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); color: white; font-weight: bold; line-height: 30px;">
                                    <span>{level}%</span>
                                </div>
                                <div style="position: absolute; top: 0; left: 10px; color: black; font-weight: bold; line-height: 30px;">
                                    <span>{skill}</span>
                                </div>
                            </div>
                            """


            for skill, level in skills.items():
                st.markdown(create_skill_bar(skill, level), unsafe_allow_html=True)

        st.write('---')

        st.title("Education")
        col5, col6 = st.columns([8, 1])
        with col5:
            st.write("""
            - __Ira A. Fulton Schools of Engineering at Arizona State University__
                - Bachelor's degree in Engineering, Biomedical Engineering
            """)
        with col6:
            st.write("__May 2017__")

        st.write('---')
        st.title("Experience")
        # col1, col2 = st.columns([4, 1])
        # with col1:
        st.write("""
            - __IMAV LLC –__ Mechanical Design Engineer & CFD Analyst 
            - __Intelligent Embedded Systems Laboratory (IeSL), ASU -__ Undergraduate Research Assistant in Mechanical
             Engineering
            - __Arizona Biomedical Collaborative, University of Arizona College of Medicine –__ Product Design Engineer 
            Intern
            - __Neural Control of Movement Lab, ASU –__ Undergraduate Research Assistant 
            """)

        # with col2:
        # st.write("__05/2017 - 04/2020__")
        # st.write("__02/2016 - 03/2017__")
        # st.write("__05/2016 - 08/2016__")

        st.write('---')
        
        # st.title("My Hobbies & Interests")
        # col7, col8, col9, col10 = st.columns(4)
        # with col7:
        #     st.image("my images/Gym.jpg")
        #     st.write("## Gym")

        # with col8:
        #     st.image("my images/Reading.jpg")
        #     st.write("## Reading")

        # with col9:
        #     st.image("my images/Hiking.jpg")
        #     st.write("## Hiking")

        # with col10:
        #     st.image("my images/Puzzle.jpg")
        #     st.write("## Puzzles")
        

        st.title("My Hobbies & Interests")
        col7, col8, col9, col10 = st.columns(4)
        
        with col7:
            st.image("my images/Gym.jpg")
            st.markdown("<h2 style='text-align: center;'>Gym</h2>", unsafe_allow_html=True)
        
        with col8:
            st.image("my images/Reading.jpg")
            st.markdown("<h2 style='text-align: center;'>Reading</h2>", unsafe_allow_html=True)
        
        with col9:
            st.image("my images/Hiking.jpg")
            st.markdown("<h2 style='text-align: center;'>Hiking</h2>", unsafe_allow_html=True)
        
        with col10:
            st.image("my images/Puzzle.jpg")
            st.markdown("<h2 style='text-align: center;'>Puzzles</h2>", unsafe_allow_html=True)


        st.write('---')

        st.title("Socials")


        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        lottie_socials = load_lottieurl("https://lottie.host/bb225ecd-f3c1-47b7-a6a3-006190fb71a3/IrL428Gc1O.json")

        col13, col14 = st.columns(2)
        with col13:
            ######################################################################################################
            # Include Font Awesome CSS
            st.markdown("""
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
                """, unsafe_allow_html=True)

            # HTML for contact icons with vertical layout
            contact_icons_html = """
                <div style="display: flex; flex-direction: column; align-items: left; margin-top: 40px;">
                    <a href="https://www.linkedin.com/in/william-lu-47693b145/" target="_blank" style="text-decoration: none; color: black; margin-bottom: 35px;">
                         <i class="fab fa-linkedin" style="font-size: 36px; color: black;"></i> <span style="color: black; font-size: 35px;">LinkedIn</span>
                    </a>
                    <a href="https://github.com/williaml12" target="_blank" style="text-decoration: none; color: black; margin-bottom: 35px;">
                        <i class="fab fa-github" style="font-size: 36px; color: black;"></i> <span style="color: black; font-size: 35px;">GitHub</span>
                    </a>
                    <a href="https://www.hackster.io/wlu1" target="_blank" style="text-decoration: none; color: black; margin-bottom: 25px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/Hackster.io_logo.svg" style="width: 36px; height: 36px; filter: invert(100%); vertical-align: middle;"/> <span style="color: black; font-size: 35px;">Hackster.io</span>
                    </a>
                </div>
                        """

            # Display the contact icons
            st.markdown(contact_icons_html, unsafe_allow_html=True)
            #################################################################################################
        with col14:
            st_lottie(lottie_socials, height=300)

        # Back to Top button
        st.markdown("""
        <style>
            .stButton > button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 10px;
                font-size: 18px;
            }
        </style>
    """, unsafe_allow_html=True)

        if st.button("⬆️ Back to top"):
            st.markdown("<meta http-equiv='refresh' content='0; url=#top'>", unsafe_allow_html=True)

        # # --- BACK TO TOP BUTTON (NO JS) ---
        # st.markdown(
        #     """
        #     <style>
        #     /* Floating fixed-position button */
        #     .back-to-top {
        #         position: fixed;
        #         bottom: 40px;
        #         right: 40px;
        #         background-color: #4CAF50;
        #         color: white;
        #         padding: 12px 20px;
        #         border-radius: 10px;
        #         text-decoration: none;
        #         font-size: 18px;
        #         font-weight: bold;
        #         box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        #         z-index: 9999;
        #     }
        #     .back-to-top:hover {
        #         background-color: #45a049;
        #     }
        #     </style>
        
        #     <a href="#top" class="back-to-top">⬆</a>
        #     """,
        #     unsafe_allow_html=True
        # )

        # if st.button("⬆ Back to top"):
        #     st.markdown("<meta http-equiv='refresh' content='0; #top'>", unsafe_allow_html=True)


        # --- Back to Top Button ---
        st.markdown("""
        <div style='position: fixed; bottom: 40px; right: 40px;'>
            <form action="#top">
                <button style="
                    background-color:#4CAF50;
                    color:white;
                    padding:12px 20px;
                    border:none;
                    border-radius:10px;
                    font-size:18px;
                    cursor:pointer;
                ">⬆ Back to Top</button>
            </form>
        </div>
        """, unsafe_allow_html=True)



if selected == 'AI Assistant':
    with st.container():

        persona = """
                You are William's AI bot. You help people answer questions about your self (i.e William)
                Answer as if you are responding . Dont answer in second or third person.
                If you don't know they answer you simply say "That's a secret"
                Here is more info about William: 
                
                ## About William: 
                William is a motivated student at NYU Tandon Bridge Program with experience 
                in product design and development, CAD modeling, assembling, QA testing, computer vision, 
                machine learning object detection, data analysis, and seeking opportunities in medical imaging, 
                medical tech., Computer Vision, IoT solutions, Robotics, and AI. 

                ## Career Goal:
                William's career goal is to emerging in AI and biotechnologies to drive meaningful innovation and create solutions that positively impact on society.
                
                ## EDUCATION: 
                - I'm currently a student at the NYU Tandon Bridge Program. 
                - You can find that information in the "Education" section of the "About" tab of my AI portfolio 
                website.

                    
                ## Work Experience:
                - You can find that information in the "Experience" section of the "About" tab of my AI portfolio 
                website.

                    
                ## SKILLS: 
                    
                Software: MatLab, LabVIEW, SolidWorks, ANSYS(CFD), PSpice, ImageJ, MS Word, Excel, PowerPoint, 
                Project, Arduino IDE, and Visual Studio
                Hardware: Arduino, Particle Photon, Sony Spresense, ESP32, ESP8266, and Raspberry Pi 
                Programming Languages: C++, C, Python, Java, and MatLab 
                Languages: Chinese (Native), and Spanish (Elementary Proficiency, basic, entry-level) 
                Others: Good verbal and written communication skills, 3D printing, assembling, troubleshooting, 
                validation and documentation, FEA and failure analysis, and technical writing
                You can also find that information in the "My Skills" section of the "About" tab of my AI 
                portfolio website.
                    
                    
                ## Interests and Hobbies:
                I enjoy most of my time listening to music, watching YouTube videos, WeChat and TikTok short videos, 
                and reading journal articles or magazines in the fields of physics, engineering, medicine, and biology 
                to gain insight for research. You can also find that information in the "My Hobbies & Interests" section
                of the "About" tab of my AI portfolio website.

                
                ## Projects:
                You can find information about my projects in a few places:
                - William's Github:https://github.com/williaml12
                - Hackster.io: https://www.hackster.io/wlu1
                - Go to "Projects" tab of my AI portfolio website
                - You can find links to those websites in the "Socials" section of the "About" tab of my AI portfolio 
                  website.
                
                ## Contact:
                You can reach me at luwei2359@gmail.com. You can also find me on LinkedIn at 
                https://www.linkedin.com/in/william-lu-47693b145/. Or you can contact me through the "Contact" tab of
                my AI portfolio website.

                
                ## Availability:
                William is actively seeking new opportunities and is ready to start immediately.
                """


        
        # st.title("William's AI Bot")

        # title_row = st.container(
        #     horizontal=True,
        #     vertical_alignment="bottom",
        # )

        # with title_row:
        #     st.title(
        #         # ":material/cognition_2: Streamlit AI assistant", anchor=False, width="stretch"
        #         "Streamlit AI assistant",
        #         anchor=False,
        #         width="stretch",
        #     )

        # # # --- Create title row with restart button ---
        # title_row = st.container()

        # with title_row:
        #     # Define function to clear conversation
        #     def clear_conversation():
        #         st.session_state.conversation = []
        
        #     st.button(
        #         "Restart",
        #         icon=":material/refresh:",
        #         on_click=clear_conversation,
        #     )

        # --- CSS for aligning restart button with title ---
        st.markdown("""
        <style>
        .align-right {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            height: 100%;
            padding-top: 25px; 
        }
        </style>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([10, 2])

        with col1:
            st.title("William's AI Bot")
        
        with col2:
            st.markdown('<div class="align-right">', unsafe_allow_html=True)

            def clear_conversation():
                st.session_state.conversation = []
                # st.session_state.messages = []
                st.session_state.initial_question = None
                st.session_state.selected_suggestion = None

            # if st.session_state.conversation:   # Show ONLY after first message
            #     st.markdown('<div class="align-right">', unsafe_allow_html=True)
            #     # st.button("🔄 Restart", on_click=clear_conversation)
            #     # st.markdown('</div>', unsafe_allow_html=True)

            # ✅ Show restart button ONLY if there is at least one message
            if "conversation" in st.session_state and len(st.session_state.conversation) > 0:
            # if len(st.session_state.conversation) > 0:
                st.button(
                    "Restart",
                    icon=":material/refresh:",
                    on_click=clear_conversation,
                )
            
            st.markdown('</div>', unsafe_allow_html=True)

        
        # Initialize session state for conversation history if not already done
        if 'conversation' not in st.session_state:
            st.session_state.conversation = []

        # Define the URLs for your custom icons
        user_icon_url = "https://cdn-icons-png.flaticon.com/128/1057/1057240.png"
        bot_icon_url = "https://cdn-icons-png.flaticon.com/128/8943/8943377.png"

        # CSS to style the user input background
        st.markdown(
            """
            <style>
            .user-message {
                background-color: #fafafa;  /* Even lighter gray color */
                padding: 5px;
                border-radius: 5px;
            }
            .bot-message {
                background-color: #ffffff;  /* White background for bot messages */
                padding: 5px;
                border-radius: 5px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Create a placeholder for conversation history
        placeholder = st.empty()

        # Display the conversation history with icons
        with placeholder.container():
            for chat in st.session_state.conversation:
                col1, col2 = st.columns([1, 18])
                # col1, col2 = st.columns([0.7, 10])
                # col1, col2 = st.columns([0.8, 12])
                with col1:
                    st.image(user_icon_url, width=30)
                with col2:
                    st.markdown(f'<div class="user-message">{chat["user"]}</div>', unsafe_allow_html=True)
                col1, col2 = st.columns([1, 18])
                # col1, col2 = st.columns([0.7, 10])
                # col1, col2 = st.columns([0.8, 12])
                with col1:
                    st.image(bot_icon_url, width=30)
                with col2:
                    st.markdown(f'<div class="bot-message">{chat["AI bot"]}</div>', unsafe_allow_html=True)
    
        # Create a form for input and button
        # with st.form(key='question_form'):
        #     user_question = st.text_input("Ask anything about me", placeholder="Enter a prompt here")
        #     submit_button = st.form_submit_button(label='ASK ME', use_container_width=True)

        with st.form(key='question_form', clear_on_submit=True):  # ✅ this auto-clears input
            user_question = st.text_input("Ask anything about me", placeholder="Enter a prompt here")
            submit_button = st.form_submit_button(label='ASK ME', use_container_width=True)


        # When submitted, do something and then clear input
        # if submit_button:
        #     st.write(f"You asked: {st.session_state.user_question}")
        #     clear_input()

        # Handle form submission
        if submit_button:
            
            if user_question:
                prompt = persona + "Here is the question that the user asked: " + user_question
                try:
                    response = model.generate_content(prompt)
                    # Append user question and AI response to conversation history
                    st.session_state.conversation.append({"user": user_question, "AI bot": response.text})

                    # ⭐ Force UI refresh so Restart button appears right after first message
                    if len(st.session_state.conversation) == 1:
                        st.rerun()

                    # Update the placeholder with the new conversation
                    placeholder.empty()  # Clear the previous content
                    with placeholder.container():
                        for chat in st.session_state.conversation:
                            col1, col2 = st.columns([1, 22])
                            with col1:
                                st.image(user_icon_url, width=50)
                            with col2:
                                st.markdown(f'<div class="user-message">{chat["user"]}</div>', unsafe_allow_html=True)
                            col1, col2 = st.columns([1, 22])
                            with col1:
                                st.image(bot_icon_url, width=50)
                            with col2:
                                st.markdown(f'<div class="bot-message">{chat["AI bot"]}</div>', unsafe_allow_html=True)

                    # 🔹 Clear the input after submission
                    # st.session_state.user_input = ""
                    # 🔹 Clear the input box after successful submission
                    # clear_input()
                    
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("Please enter a question before clicking ASK ME.")




        

        # st.title("William's AI Bot")
        
        # # 🔹 Define clear_input() function
        # def clear_input():
        #     st.session_state.user_question = ""  # This will now work safely
        
        # # Initialize conversation history
        # if "conversation" not in st.session_state:
        #     st.session_state.conversation = []
        
        # # Icons
        # user_icon_url = "https://cdn-icons-png.flaticon.com/128/1057/1057240.png"
        # bot_icon_url = "https://cdn-icons-png.flaticon.com/128/8943/8943377.png"
        
        # # CSS styling
        # st.markdown("""
        # <style>
        # .user-message {
        #     background-color: #fafafa;
        #     padding: 10px;
        #     border-radius: 5px;
        # }
        # .bot-message {
        #     background-color: #ffffff;
        #     padding: 10px;
        #     border-radius: 5px;
        # }
        # </style>
        # """, unsafe_allow_html=True)
        
        # # Conversation placeholder
        # placeholder = st.empty()
        
        # # Display existing conversation
        # with placeholder.container():
        #     for chat in st.session_state.conversation:
        #         col1, col2 = st.columns([1, 20])
        #         with col1:
        #             st.image(user_icon_url, width=30)
        #         with col2:
        #             st.markdown(f'<div class="user-message">{chat["user"]}</div>', unsafe_allow_html=True)
        #         col1, col2 = st.columns([1, 20])
        #         with col1:
        #             st.image(bot_icon_url, width=30)
        #         with col2:
        #             st.markdown(f'<div class="bot-message">{chat["AI bot"]}</div>', unsafe_allow_html=True)
        
        # # 🔹 Create a form with a text input bound to session_state
        # with st.form(key="question_form", clear_on_submit=True):  # ✅ Auto-clears input
        #     user_question = st.text_input(
        #         "Ask anything about me",
        #         placeholder="Enter a prompt here",
        #         key="user_question"
        #     )
        #     submit_button = st.form_submit_button(label="ASK ME", use_container_width=True)
        
        # # Handle submission
        # if submit_button:
        #     if user_question.strip():  # ✅ Avoid empty input
        #         # Your model prompt
        #         persona = "You are William's AI bot. Respond naturally. "
        #         prompt = persona + "Here is the question the user asked: " + user_question
        
        #         try:
        #             # Replace this with your actual model call
        #             response_text = f"This is a simulated response to: '{user_question}'"
        
        #             # Append to chat history
        #             st.session_state.conversation.append({
        #                 "user": user_question,
        #                 "AI bot": response_text
        #             })
        
        #             # Rerun to refresh chat
        #             # st.experimental_rerun()
        #             st.rerun()
        
        #         except Exception as e:
        #             st.error(f"An error occurred: {e}")
        #     else:
        #         st.warning("Please enter a question before clicking ASK ME.")

        
if selected == 'Projects':
    with st.container():
        st.header("My Projects")
        
        # col11, col12 = st.columns([8, 3])
        # with col11:
        #     st.write("""
        #     - __iSense: Smart Home Security System__
        #     - __IoT Product Design for Medical Device and Health Care__
        #         - Participated in a team of three to design a wearable device that can monitor sunlight intensity and
        #         send reminders to users for minimum and maximum exposure to UV sunlight
        #         - Researched existing products on the market to establish benchmarks
        #         - Presented final design report in front of entire class and judge panel composed by other teams and
        #         professors""")
        #
        # with col12:
        #     st.write("__July 2022__")
        #     st.write("__Jan 2017 - May 2017__")

        # CSS styles for themed projects
        # st.markdown("""
        #     <style>
        #     .project-container {
        #         margin-top: 20px;
        #         padding: 20px;
        #         border-radius: 10px;
        #     }
        #     .project-1 { background-color: #ffdddd; }
        #     .project-2 { background-color: #ddffdd; }
        #     .project-3 { background-color: #ddddff; }
        #     .project-4 { background-color: #ffffdd; }
        #     .project-5 { background-color: #ddffff; }
        #     .project-6 { background-color: #ff6347; }
        #     .project-title {
        #         font-size: 24px;
        #         font-weight: bold;
        #     }
        #     .project-description {
        #         font-size: 18px;
        #         margin-top: 10px;
        #     }
        #     .project-technologies {
        #         font-size: 16px;
        #         margin-top: 10px;
        #     }
        #     .project-link {
        #         font-size: 16px;
        #         margin-top: 10px;
        #     }
        #     </style>
        #     """, unsafe_allow_html=True)

        # # Project 1
        # with st.expander("Project 1: iSense: Smart Home Security System"):
        #     st.markdown("""
        #     <div class="project-container project-1">
        #         <div class="project-title">iSense: Smart Home Security System</div>
        #         <img src="https://hackster.imgix.net/uploads/attachments/1473651/_T0QQDArozA.blob?auto=compress"
        #                      "%2Cformat&w=900&h=675&fit=min" alt="iSense: Smart Home Security System" style="width:100%">
        #         <div class="project-description">
        #             <strong>Description</strong>: Make IoT-based Smart Home Security system to monitor daily home 
        #             activity and control all the home appliances with Blynk app & Switches.
        #         </div>
        #         <div class="project-technologies">
        #             <strong>Technologies Used</strong>: Sony Spresense boards (main & extension), PIR Motion Sensor , 
        #             Ultrasonic Sensor, NodeMCU ESP8266 Breakout Board, Arduino IDE, Blynk, etc.
        #         </div>
        #         <div class="project-link">
        #             <strong>Repository</strong>: <a href="https://www.hackster.io/wlu1/isense-smart-home-security-system-ee9156#things">Hackster.io</a>
        #         </div>
        #         <div class="project-video">
        #             <video width="320" height="240" controls>
        #                 <source src="https://www.youtube.com/shorts/2l1Yx57YpeE" type="video/mp4">
        #             </video>
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # # Project 2
        # with st.expander("Project 2: Smart Temperature Monitoring System"):
        #     st.markdown("""
        #     <div class="project-container project-2">
        #         <div class="project-title">Smart Temperature Monitoring System</div>
        #         <img src="https://hackster.imgix.net/uploads/attachments/1630153/_aOOTsKkUrv.blob?auto=compress%2Cformat&w=900&h=675&fit=min" alt="Smart Temperature Monitoring System" style="width:100%">
        #         <div class="project-description">
        #             <strong>Description</strong>: Monitor your room temperature from your mobile devices.
        #         </div>
        #         <div class="project-technologies">
        #             <strong>Technologies Used</strong>: Infineon CY8CPROTO-062-4343W,  Infineon ModusToolbox™ Software,  EFR Connect BLE Mobile App
        #         </div>
        #         <div class="project-link">
        #             <strong>Repository</strong>: <a href="https://www.hackster.io/wlu1/smart-temperature-monitoring-system-529da8">Hackster.io</a>
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # # Project 3
        # with st.expander("Project 3: Vehicle-Edge-Application"):
        #     st.markdown("""
        #     <div class="project-container project-3">
        #         <div class="project-title">Vehicle-Edge-Application</div>
        #         <img src="https://github.com/williaml12/Vehicle-Edge-Application/raw/master/Capture_vehicle.PNG" alt="Vehicle-Edge-Application" style="width:100%">
        #         <div class="project-description">
        #             <strong>Description</strong>: The vehicle counter application will demonstrate how to create a smart video IoT solution using Intel® hardware and software tools. The app will detect people, vehicle in a designated area, providing the number of frame, average duration of vehicle in frame, and total count.
        #         </div>
        #         <div class="project-technologies">
        #             <strong>Technologies Used</strong>: Intel® Distribution of OpenVINO™ toolkit 2019 R3 release, Node v6.17.1, Npm v3.10.10, CMake, MQTT Mosca server
        #         </div>
        #         <div class="project-link">
        #             <strong>Repository</strong>: <a href="https://github.com/williaml12/Vehicle-Edge-Application">GitHub</a>
        #         </div>
        #         <div class="project-chart">
        #             <!-- Place your chart code here -->
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # # Project 4
        # with st.expander("Project 4: People Counter App at the Edge"):
        #     st.markdown("""
        #     <div class="project-container project-4">
        #         <div class="project-title">People Counter App at the Edge</div>
        #         <img src="https://github.com/williaml12/People-Counter-App-at-the-Edge/raw/master/images/people-counter-image.png" alt="People Counter App at the Edge" style="width:100%">
        #         <div class="project-description">
        #             <strong>Description</strong>: The people counter application will demonstrate how to create a smart video IoT solution using Intel® hardware and software tools. The app will detect people in a designated area, providing the number of people in the frame, average duration of people in frame, and total count.
        #         </div>
        #         <div class="project-technologies">
        #             <strong>Technologies Used</strong>: Intel® Distribution of OpenVINO™ toolkit 2019 R3 release, Node v6.17.1, Npm v3.10.10, CMake, MQTT Mosca server
        #         </div>
        #         <div class="project-link">
        #             <strong>Repository</strong>: <a href="https://github.com/williaml12/People-Counter-App-at-the-Edge">GitHub</a>
        #         </div>
        #         <div class="project-video">
        #             <video width="320" height="240" controls>
        #                 <source src="https://www.youtube.com/watch?v=dQw4w9WgXcQ" type="video/mp4">
        #             </video>
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # # Add more projects as needed
        # with st.expander("Project 5: Door-Security-System"):
        #     st.markdown("""
        #     <div class="project-container project-5">
        #         <div class="project-title">Door-Security-System</div>
        #         <img src="https://th.bing.com/th/id/OIP.TMupY92oAYCkcQr8MzzzOwHaHa?rs=1&pid=ImgDetMain" alt="Door-Security-System" style="width:100%">
        #         <div class="project-description">
        #             <strong>Description</strong>: Contribute to design and develop on home security system. Users will get alert when they appoach to the door that set with sensor for detection.
        #         </div>
        #         <div class="project-technologies">
        #             <strong>Technologies Used</strong>: Arduino Nano, Ultrasonic sensor, Arduino IDE, Blynk, Arduino Web Editor
        #         </div>
        #         <div class="project-link">
        #             <strong>Repository</strong>: <a href="https://github.com/williaml12/Door-Security-System">GitHub</a>
        #         </div>
        #         <div class="project-chart">
        #             <!-- Place your chart code here -->
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)

        # with st.expander("Project 6: “OcuTrack”: Personal Eye Tracking Profile (Eye Tracking)"):
        #     st.markdown("""
        #     <div class="project-container project-6">
        #         <div class="project-title">“OcuTrack”: Personal Eye Tracking Profile (Eye Tracking)</div>
        #         <img src="https://th.bing.com/th/id/R.87c2a5fc313737ea30509569edce7396?rik=MFt1m%2b0ppv50tg&pid=ImgRaw&r=0" alt="“OcuTrack”: Personal Eye Tracking Profile (Eye Tracking)" style="width:100%">
        #         <div class="project-description">
        #             <strong>Description</strong>: BME Senior Capstone Design Project
        #         </div>
        #         <div class="project-technologies">
        #             <strong>Technologies Used</strong>: Python, OpenCV, Raspberry Pi 
        #         </div>
        #         <div class="project-link">
        #             <strong>Repository</strong>: <a href="https://github.com/williaml12/-OcuTrack-Personal-Eye-Tracking-Profile-Eye-Tracking-">GitHub</a>
        #         </div>
        #         <div class="project-chart">
        #             <!-- Place your chart code here -->
        #         </div>
        #     </div>
        #     """, unsafe_allow_html=True)


        # Sample project data
        projects = [
            {
                "title": "AI Portfolio Website",
                # "image_url": "https://blog.streamlit.io/content/images/size/w2000/2023/06/Announcement--7-.svg",
                "image_url": "https://media.istockphoto.com/id/2169349687/photo/generative-ai-tool-ai-prompt-image-generator-technology-prompt-engineering-or-ai-image.jpg?s=612x612&w=0&k=20&c=Li5_E8QIMwsyhKBc_6gVEOqEBpaWW-nPk24U6kGBUTE=",
                "repo_url": "https://github.com/williaml12/AI_Portfolio_Website"
            },
            {
                "title": "iSense: Smart Home Security System",
                "image_url": "https://hackster.imgix.net/uploads/attachments/1473651/_T0QQDArozA.blob?auto=compress",
                "repo_url": "https://www.hackster.io/wlu1/isense-smart-home-security-system-ee9156#things"
            },
            {
                "title": "Smart Temperature Monitoring System",
                "image_url": "https://hackster.imgix.net/uploads/attachments/1630153/_aOOTsKkUrv.blob?auto=compress%2Cformat&w=900&h=675&fit=min",
                "repo_url": "https://www.hackster.io/wlu1/smart-temperature-monitoring-system-529da8"
            },
            {
                "title": "People Counter App at the Edge",
                "image_url": "https://github.com/williaml12/People-Counter-App-at-the-Edge/raw/master/images/people-counter-image.png",
                "repo_url": "https://github.com/williaml12/People-Counter-App-at-the-Edge"
            },
            {
                "title": "Vehicle-Edge-Application",
                "image_url": "https://github.com/williaml12/Vehicle-Edge-Application/raw/master/Capture_vehicle.PNG",
                "repo_url": "https://github.com/williaml12/Vehicle-Edge-Application"
            },
            {
                "title": "Door-Security-System",
                "image_url": "https://th.bing.com/th/id/OIP.TMupY92oAYCkcQr8MzzzOwHaHa?rs=1&pid=ImgDetMain",
                "repo_url": "https://github.com/williaml12/Door-Security-System"
            },
            {
                "title": "“OcuTrack”: Personal Eye Tracking Profile",
                # "image_url": "https://th.bing.com/th/id/R.87c2a5fc313737ea30509569edce7396?rik=MFt1m%2b0ppv50tg&pid=ImgRaw&r=0",
                "image_url": "https://media.istockphoto.com/id/1285201659/video/biometric-retina-recognition.avif?s=640x640&k=20&c=qBuTPJhZYwR_3BUQIZHBTgnodwNpyBCakG-Py8uzEVI=",
                "repo_url": "https://github.com/williaml12/-OcuTrack-Personal-Eye-Tracking-Profile-Eye-Tracking-"
            }
        ]
        
        # Custom CSS styles
        st.markdown("""
            <style>
            .project-card {
                background-color: #000000
                border-radius: 15px;
                padding: 20px;
                margin: 10px;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                transition: 0.3s;
                text-align: center;
            }
            .project-card:hover {
                box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
            }
            .project-title {
                font-size: 16px;
                font-weight: bold;
                margin-top: 10px;
            }
            .project-button {
                background-color: #FFD966;
                border: none;
                color: white;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin-top: 10px;
                padding: 10px 24px;
                border-radius: 5px;
                cursor: pointer;
                transition: 0.3s;
            }
            .project-button:hover {
                background-color: #E06666;
            }
            </style>
            """, unsafe_allow_html=True)
        
        # Function to display a project card
        def display_project(project):
            st.markdown(f"""
            <div class="project-card">
                <img src="{project['image_url']}" alt="{project['title']}" style="width:100%">
                <div class="project-title">{project['title']}</div>
                <a href="{project['repo_url']}" class="project-button">View Project</a>
            </div>
            """, unsafe_allow_html=True)
        
        # Display projects in a grid
        num_columns = 2  # Number of columns in the grid
        columns = st.columns(num_columns)
        
        for i, project in enumerate(projects):
            with columns[i % num_columns]:
                display_project(project)
        
        # Add more projects and adjust the layout as needed
        


if selected == "Contact":
    with st.container():

        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        # Apply local CSS styles from the "style.css" file
        local_css("style/style.css")

        lottie_contact = load_lottieurl("https://lottie.host/6c502d7d-9573-4d15-8063-b93dd8aef2af/MhPNlv4ZJ5.json")

        contact_form = """
        <form action="https://formsubmit.co/alphagalaga@gmail.com" method="POST">
          <input type="hidden" name="_captcha" value="false">
          <input type="text" name="name" placeholder = "Your name" required>
          <input type="email" name="email" placeholder = "Your email" required>
          <textarea name = "message" placeholder = "Your message" required></textarea>
          <button type="submit">Send</button>
        </form>
        """
        left_col, right_col = st.columns((2, 1))
        with left_col:
            st.subheader("🖆 Contact Me")
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            st_lottie(lottie_contact, height=300)


# Footer
st.markdown("""
<div class="footer">
    ©️ 2024 William Lu. All rights reserved.
</div>
""", unsafe_allow_html=True)

