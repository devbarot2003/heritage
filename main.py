import streamlit as st
import tensorflow as tf
import numpy as np
from streamlit_option_menu import option_menu
from keras.layers import TFSMLayer

inference_layer = TFSMLayer('C:/Users/khushi/OneDrive/Desktop/Project2/model3', call_endpoint='serving_default')

# Create a Keras model with the inference-only layer
model = tf.keras.Sequential([inference_layer])



header_css = """
<style>
h1 {
    font-size: 36px !important;
}
h2 {
    font-size: 24px !important;
}
h3 {
    font-size: 18px !important;
}
</style>
"""
st.markdown(header_css, unsafe_allow_html=True)

# Tensorflow Model Prediction
def model_prediction(test_image):
    try:
        # model_path ='C:/Users/khushi/OneDrive/Desktop/Project2/model3'
        # model = tf.keras.models.load_model(model_path)
        image = tf.keras.preprocessing.image.load_img(test_image,target_size=(175,175))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr]) #convert single image to batch
        print("Input array shape:", input_arr.shape)
        predictions = model.predict(input_arr)
        print(type(predictions))
        print("Predictions:", predictions)
        print(type(predictions))

        prediction_array = list(predictions.values())[0]
        print(prediction_array)
        converted_list = [int(element) for sublist in prediction_array for element in sublist]  
        print(converted_list) 
        return np.argmax(converted_list) #return index of max element
    except Exception as e:
        st.error(f"Error during model prediction: {str(e)}")
        return None

#Sidebar
selected = option_menu(
            menu_title=None,  # required
            options=["Home", "About", "AI Engine"],  # required
            icons=["house", "book", "gear"],  # optional
            #menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#ffffff"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )

#Main Page
if(selected=="Home"):
    #st.header("HERITAGE SITE RECOGNITION SYSTEM")
    image_path = "image.jpg"
    st.image(image_path,use_column_width=True)
    st.markdown("""
    Welcome to the Heritage Site Recognition System! 🌿🔍
            
    Embark on a journey through time and culture with HeritageSpotter, your gateway to discovering and learning about the world's diverse heritage sites. From ancient wonders to modern marvels, HeritageSpotter brings the past to life through cutting-edge recognition technology.
    
    Our mission is to help in identifying heritage sites efficiently. Upload an image of a monument, and our system will analyze it and will predict it and will provide you with a short historical description. Together, let's explore your heritage sites!

    Capture, Recognize, Learn

    Using state-of-the-art image recognition algorithms, HeritageSpotter instantly identifies heritage sites from your uploaded photos. Simply snap a picture, upload it to the app, and let HeritageSpotter do the rest. With each recognition, delve deeper into the history, significance, and cultural importance of the identified site.

    Preserve Cultural Heritage

    Join us in our mission to preserve and celebrate the world's cultural heritage. By promoting awareness and appreciation of heritage sites, HeritageSpotter aims to foster a global community dedicated to safeguarding our shared legacy for future generations.
                
    ### How It Works
    1. **Upload Image:** Go to the **Heritage Site Recognition** page and upload an image of a monument.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify monuments.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate monuments classification.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.
                
    Whether you're a seasoned traveler, a history enthusiast, or simply curious about the world around you, HeritageSpotter invites you to embark on an enriching exploration of heritage and history. Start your journey now and unlock the secrets of the past with HeritageSpotter.

    ### Get Started
    Click on the **Heritage Site Recognition** page in the sidebar to upload an image and experience the power of our Heritage Site Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    Get Started Today

    """)

#About Project
elif(selected=="About"):
    st.header("About")
    st.markdown("""
                Our Mission

                At HeritageSpotter, we are passionate about preserving and celebrating the rich tapestry of cultural heritage that spans the globe. Our mission is to leverage cutting-edge technology to promote awareness, appreciation, and conservation of heritage sites worldwide.

                What We Do

                Through our innovative heritage site recognition system, HeritageSpotter empowers users to explore, discover, and learn about heritage sites with ease. By harnessing the power of image recognition technology, we make it simple for users to identify and delve deeper into the stories behind these cultural treasures.

                
                Why Heritage Matters

                Cultural heritage represents the collective memory of humanity, reflecting our shared history, values, and identity. From ancient monuments and archaeological sites to traditional practices and intangible cultural heritage, these treasures enrich our lives, inspire creativity, and foster a sense of belonging and connection to our past.

                Our Commitment

                At HeritageSpotter, we are committed to promoting responsible tourism, sustainable development, and the preservation of cultural diversity. By raising awareness of the importance of heritage conservation and fostering a deeper understanding of our global heritage, we aim to contribute to a more inclusive, tolerant, and culturally enriched world.

                Join Us

                Join us on our journey to celebrate and safeguard the world's cultural heritage. Whether you're a traveler, educator, heritage enthusiast, or simply curious about the world around you, HeritageSpotter invites you to embark on an inspiring exploration of heritage and history.

                Contact Us

                Have questions, feedback, or suggestions? We'd love to hear from you! Feel free to reach out to us at contact@heritagespotter.com and connect with us on social media @HeritageSpotter.

                Thank You

                Thank you for supporting HeritageSpotter and joining us in our mission to preserve and celebrate the world's cultural heritage. Together, we can make a difference and ensure that these treasures endure for generations to come.



                """)

#Prediction Page
elif(selected=="AI Engine"):
    st.header("Heritage Site Recognition System")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        #st.snow()
        try:
            
            st.write("Our Prediction")
            result_index = model_prediction(test_image)
            
            #Reading Labels
            class_name = ['Fatehpur Sikri','Golden Temple','Jagannath Temple','Qutub Minar','Rani Ki Vav','Sanchi Stupa','Taj Mahal']
            
            class_details = {
            "Fatehpur Sikri":"Fatehpur Sikri, a historical city near Agra, India, was established in the 16th century by Mughal Emperor Akbar. Known for its splendid red sandstone architecture, the city served as the Mughal capital from 1571 to 1585. Notable structures include the Jama Masjid, Buland Darwaza, and various palaces like the Panch Mahal. Fatehpur Sikri holds significance for its historical and cultural heritage, showcasing a blend of Persian and Indian architectural styles. Despite being abandoned due to water scarcity, it remains a UNESCO World Heritage Site, attracting visitors with its architectural grandeur and tales of Mughal history.",
            "Golden Temple":"The Golden Temple, or Sri Harmandir Sahib, stands as a testament to Sikhism's rich history and values. Founded by Guru Ram Das and constructed by Guru Arjan Dev in the 16th century, it symbolizes Sikh sovereignty and inclusivity. The temple, located in Amritsar, Punjab, houses the Guru Granth Sahib and features the Akal Takht, the temporal seat of Sikh authority. Despite facing challenges and the tragic event of Operation Blue Star in 1984, the Sikh community's resilience has ensured the temple's restoration. Known for its spiritual significance, the Golden Temple embodies principles of equality, selfless service through its langar, and serves as a global symbol of peace and harmony.",
            "Jagannath Temple": "The Jagannath Temple, located in Puri, Odisha, is a revered Hindu temple dedicated to Lord Jagannath, an incarnation of Lord Vishnu. Built in the 12th century, the temple is famous for its annual Rath Yatra, where massive chariots carry deities through the streets. The temple complex also includes the iconic Singhadwara or Lion Gate and the sacred kitchen, where daily meals are prepared for devotees in the largest kitchen in the world. The Jagannath Temple stands as a significant pilgrimage site, embodying a rich blend of religious devotion, cultural traditions, and architectural splendor.",
            "Qutub Minar": "The Qutub Minar, located in Delhi, India, is an iconic historical monument and UNESCO World Heritage Site. Built in the early 13th century by Qutb-ud-din Aibak, the founder of the Delhi Sultanate, the minar stands as the world's tallest brick minaret. Its five distinctive stories showcase intricate Islamic architecture and calligraphy. The Qutub Minar complex also includes other significant structures like the Quwwat-ul-Islam Mosque and the Iron Pillar. This architectural marvel is a testament to India's rich cultural and historical heritage, attracting visitors with its soaring height and historical significance.",
            "Rani Ki Vav": "Rani ki Vav, located in Patan, Gujarat, is a UNESCO World Heritage Site and an exquisite stepwell dating back to the 11th century. Commissioned by Queen Udayamati in memory of her husband King Bhimdev I, the stepwell is a marvel of intricate design and artistic expression. Its seven levels descend to a subterranean well, adorned with over a thousand sculptures, showcasing exceptional craftsmanship. Rani ki Vav stands as a testament to the significance of water conservation and the rich cultural heritage of ancient India, drawing visitors with its breathtaking architecture and historical importance.",
            "Sanchi Stupa": "The Sanchi Stupa, nestled in the heart of Madhya Pradesh, India, is an ancient Buddhist monument of great historical and spiritual significance. Built by Emperor Ashoka in the 3rd century BCE, the stupa is a symbol of Buddhism's spread and acceptance in India. Surrounded by a serene landscape, the dome-shaped structure houses relics of Lord Buddha. Its intricately carved toranas (gateways) depict scenes from Buddha's life. The Sanchi Stupa, a UNESCO World Heritage Site, stands as a timeless testament to India's Buddhist heritage, attracting visitors with its peaceful ambiance and architectural beauty.",
            "Taj Mahal": "The Taj Mahal, situated in Agra, India, is a globally renowned masterpiece of Mughal architecture and an enduring symbol of love. Commissioned by Emperor Shah Jahan in memory of his beloved wife Mumtaz Mahal, the ivory-white marble mausoleum stands as a pinnacle of beauty and craftsmanship. Completed in the 17th century, the Taj Mahal's intricate details, including its iconic dome and minarets, reflect the epitome of Mughal art. This UNESCO World Heritage Site draws millions of visitors annually, mesmerizing them with its romantic history and timeless elegance."
            }
            class_links = {
            "Fatehpur Sikri": "https://en.wikipedia.org/wiki/Fatehpur_Sikri",
            "Golden Temple": "https://en.wikipedia.org/wiki/Golden_Temple",
            "Jagannath Temple": "https://en.wikipedia.org/wiki/Jagannath_Temple,_Puri",
            "Qutub Minar": "https://en.wikipedia.org/wiki/Qutb_Minar",
            "Rani Ki Vav": "https://en.wikipedia.org/wiki/Rani_ki_Vav",
            "Sanchi Stupa": "https://en.wikipedia.org/wiki/Sanchi",
            "Taj Mahal": "https://en.wikipedia.org/wiki/Taj_Mahal"
            
            }
            def custom_success(message):
                st.markdown(
                    f"""
                    <div style='
                        background-color: #FFFFFF; 
                        color: black;
                        padding: 10px;
                        border-radius: 5px;
                        text-align: left;
                        margin-bottom: 10px;
                        '>{message}</div>
                    """,
                    unsafe_allow_html=True,
                )
            print("Predicted_index",result_index)
            predicted_site = class_name[result_index]
            print("Predicted site:", predicted_site)
            description = class_details.get(predicted_site, "Description not available")
            link = class_links.get(predicted_site,"No information available") 
            custom_success("Model predicts it's a {}.".format(predicted_site))
            custom_success("Let me provide you a short description on {}".format(predicted_site))
            custom_success("{}.".format(description))
            custom_success("For more information click on the link given below 👇.")
            st.success("{}".format(link))

        except Exception as e:
            
             st.error("An error occurred during prediction: {}".format(str(e)))
             st.error("Please ensure that the input image is valid and try again.")
             # Print additional debugging information
             print("Error during prediction:", str(e))
             print("Input image:", test_image)