import streamlit as st
from spellchecker import SpellChecker

def spell_check(text):
    spell = SpellChecker()

    # Memecah teks menjadi kata-kata
    words = text.split()

    # Mendapatkan kata-kata yang salah eja
    misspelled = spell.unknown(words)

    # Menggantikan kata-kata yang salah eja dengan koreksi
    corrected_text = ' '.join(spell.correction(word) if word in misspelled else word for word in words)

    return corrected_text

def main():
    st.title("Spell and Grammarly Check")

    # Mendapatkan teks dari pengguna
    user_input = st.text_area("Enter your text here:")

    # Pengecekan ejaan saat tombol ditekan
    if st.button("Check Spelling"):
        # Melakukan pengecekan ejaan
        corrected_text = spell_check(user_input)

        # Menampilkan hasil
        st.subheader("Corrected Text:")
        st.write(corrected_text)

if __name__ == "__main__":
    main()


