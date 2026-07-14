import streamlit as st
import urllib.parse
import random

# වෙබ් අඩවියේ මාතෘකාව
st.title("🎨 Midjourney Style - AI Image Generator")
st.write("ඔබට අවශ්‍ය රූපය ගැන විස්තරයක් (Prompt) ඉංග්‍රීසි බසින් පහතින් ඇතුලත් කරන්න. (උදා: A cute golden retriever playing in a magical forest)")

# පරිශීලකයාගෙන් Prompt එක ලබා ගැනීම
prompt = st.text_input("ඔබගේ Prompt එක:")

# Generate බොත්තම
if st.button("රූපය නිර්මාණය කරන්න (Generate)"):
    if prompt:
        with st.spinner("Midjourney මට්ටමේ උසස් රූපයක් නිර්මාණය වෙමින් පවතී. කරුණාකර රැඳී සිටින්න..."):
            
            # Midjourney Quality එක ලබා ගැනීමට විශේෂ වචන (Magic Keywords) ස්වයංක්‍රීයව එකතු කිරීම
            magic_keywords = "masterpiece, ultra-realistic, highly detailed, 8k resolution, cinematic lighting, photorealistic, Midjourney style, beautiful coloring"
            enhanced_prompt = f"{prompt}, {magic_keywords}"
            
            # Prompt එක අන්තර්ජාල ලින්ක් එකකට ගැලපෙන ලෙස වෙනස් කිරීම
            encoded_prompt = urllib.parse.quote(enhanced_prompt)
            
            # හැමවිටම අලුත් රූපයක් ලබා ගැනීමට අහඹු අංකයක් (Seed) යෙදීම
            random_seed = random.randint(1, 100000)
            
            # HD තත්ත්වයෙන් (1280x720) රූපය ලබා ගන්නා ලින්ක් එක
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1280&height=720&seed={random_seed}&nologo=true"
            
            # රූපය වෙබ් අඩවියේ පෙන්වීම
            st.image(image_url, caption=f"ඔබගේ මුල් Prompt එක: {prompt}")
            st.success("සාර්ථකව නිර්මාණය කරන ලදී!")
            
    else:
        st.warning("කරුණාකර රූපය නිර්මාණය කිරීමට පෙර Prompt එකක් ඇතුලත් කරන්න!")
