import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.set_page_config(page_title="Password Generator", page_icon="🔐")
    st.title("🔐 Password Generator")

    length = st.slider("Select Password Length", min_value=6, max_value=64, value=12)
    use_uppercase = st.checkbox("Include Uppercase Letters")
    use_numbers = st.checkbox("Include Numbers")
    use_special = st.checkbox("Include Special Characters")

    if st.button("Generate Password"):
        if length > 0:
            password = generate_password(length, use_uppercase, use_numbers, use_special)
            st.success(f"Your generated password: {password}")
        else:
            st.warning("Please select a valid password length.")


if __name__ == "__main__":
    main()
