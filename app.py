import streamlit as st
import urllib.parse

# වෙබ් අඩවියේ මාතෘකාව
st.title("🎨 AI රූප නිර්මාණකරු (AI Image Generator)")
st.write("ඔබට අවශ්‍ය රූපය ගැන විස්තරයක් (Prompt) ඉංග්‍රීසි බසින් පහතින් ඇතුලත් කරන්න.")

# පරිශීලකයාගෙන් Prompt එක ලබා ගැනීම
prompt = st.text_input("ඔබගේ Prompt එක (උදා: A futuristic city with flying cars, sunset):")

# Generate බොත්තම
if st.button("රූපය නිර්මාණය කරන්න (Generate Image)"):
    if prompt:
        # රූපය නිර්මාණය වන තුරු පෙන්වන පණිවිඩය
        with st.spinner("රූපය නිර්මාණය වෙමින් පවතී. කරුණාකර රැඳී සිටින්න..."):
            
            # Prompt එක අන්තර්ජාල ලින්ක් එකකට ගැලපෙන ලෙස වෙනස් කිරීම
            encoded_prompt = urllib.parse.quote(prompt)
            
            # Pollinations AI හරහා රූපය ලබා ගන්නා ලින්ක් එක
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
            
            # රූපය වෙබ් අඩවියේ පෙන්වීම
            st.image(image_url, caption=f"ඔබගේ Prompt එක: {prompt}")
            
    else:
        st.warning("කරුණාකර රූපය නිර්මාණය කිරීමට පෙර Prompt එකක් ඇතුලත් කරන්න!")
