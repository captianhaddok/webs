import streamlit as st
import urllib.parse
import random
import requests

# වෙබ් අඩවියේ පිටුවට අදාළ මූලික සැකසුම් (මෙය කේතයේ මුලින්ම තිබිය යුතුය)
st.set_page_config(page_title="Pro AI Image Gen", page_icon="✨", layout="wide")

# --- පැති මෙනුව (Sidebar) නිර්මාණය කිරීම ---
with st.sidebar:
    st.header("⚙️ රූපයේ සැකසුම් (Settings)")
    st.write("ඔබගේ රූපය තවත් අලංකාර කරගැනීමට මේවා වෙනස් කරන්න.")
    
    # 1. රූපයේ විලාසය තේරීම (Dropdown Menu)
    style = st.selectbox(
        "🎨 රූපයේ විලාසය (Image Style):",
        ["Photorealistic (සැබෑ ඡායාරූපයක්)", "Anime (ඇනිමේෂන්)", "3D Render (ත්‍රිමාණ)", "Digital Art (ඩිජිටල් චිත්‍රයක්)", "Watercolor (දියසායම්)"]
    )
    
    # 2. රූපයේ හැඩය තේරීම (Radio Buttons)
    shape = st.radio(
        "📐 රූපයේ හැඩය (Aspect Ratio):",
        ["Landscape (16:9 - පළලින් වැඩි)", "Portrait (9:16 - දිගින් වැඩි)", "Square (1:1 - සමචතුරස්‍ර)"]
    )

# --- ප්‍රධාන තිරය (Main Screen) ---
st.title("✨ Pro AI Image Generator")
st.markdown("---") # තිරස් රේඛාවක් (Horizontal line) එකතු කිරීම

# පරිශීලකයාගෙන් Prompt එක ලබා ගැනීම
prompt = st.text_input("ඔබට අවශ්‍ය රූපය මෙතන විස්තර කරන්න (ඉංග්‍රීසියෙන්):", "A futuristic cyberpunk city with flying cars")

# Generate බොත්තම වඩාත් විශාලව ලබා දීම
if st.button("🚀 රූපය නිර්මාණය කරන්න", use_container_width=True):
    if prompt:
        with st.spinner("සුපිරි රූපයක් නිර්මාණය වෙමින් පවතී. කරුණාකර රැඳී සිටින්න... ⏳"):
            
            # තෝරාගත් විලාසයට (Style) අනුව Magic Keywords වෙනස් කිරීම
            if "Photorealistic" in style:
                magic_words = "masterpiece, ultra-realistic, 8k resolution, cinematic lighting, highly detailed, photograph"
            elif "Anime" in style:
                magic_words = "anime style, Studio Ghibli, highly detailed, beautiful colors, masterpiece, 2d art"
            elif "3D Render" in style:
                magic_words = "3D render, octane render, unreal engine 5, highly detailed, vibrant, volumetric lighting"
            elif "Digital Art" in style:
                magic_words = "digital concept art, trending on artstation, masterpiece, vibrant colors, fantasy"
            else:
                magic_words = "watercolor painting, artistic, beautiful brush strokes, masterpiece, elegant"
            
            # තෝරාගත් හැඩයට අනුව රූපයේ දිග පළල (Width/Height) තීරණය කිරීම
            if "Square" in shape:
                w, h = 1024, 1024
            elif "Landscape" in shape:
                w, h = 1280, 720
            else:
                w, h = 720, 1280

            # අවසන් Prompt එක සහ අහඹු අංකය සකස් කිරීම
            final_prompt = f"{prompt}, {magic_words}"
            encoded_prompt = urllib.parse.quote(final_prompt)
            random_seed = random.randint(1, 9999999)
            
            # Pollinations AI වෙතින් රූපය ලබා ගන්නා සම්පූර්ණ ලින්ක් එක
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model=flux&seed={random_seed}&width={w}&height={h}&nologo=true"
            
            # රූපය වෙබ් අඩවියේ පෙන්වීම
            st.image(image_url, caption=f"Style: {style} | Prompt: {prompt}", use_container_width=True)
            
            # සාර්ථක වූ බව පෙන්වීමට බැලුන් යැවීමේ ඇනිමේෂන් එකක් (Balloons animation)
            st.success("සාර්ථකව නිර්මාණය කරන ලදී! 🎉")
            st.balloons() 
            
            # --- රූපය Download කරගැනීමේ බොත්තම (Download Button) ---
            try:
                # අන්තර්ජාලයෙන් රූපය Download කිරීම සඳහා
                response = requests.get(image_url)
                if response.status_code == 200:
                    st.download_button(
                        label="💾 රූපය ඔබගේ උපාංගයට Download කරගන්න",
                        data=response.content,
                        file_name=f"AI_Image_{random_seed}.jpg",
                        mime="image/jpeg",
                        use_container_width=True
                    )
            except Exception as e:
                st.warning("Download බොත්තම සකස් කිරීමේදී දෝෂයක් ඇතිවිය.")

    else:
        st.error("කරුණාකර රූපය නිර්මාණය කිරීමට පෙර Prompt එකක් ඇතුලත් කරන්න!")
